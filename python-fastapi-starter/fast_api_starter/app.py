from fastapi import FastAPI
import os
from baml_client import b
from baml_client.types import Message, Role
from fastapi.responses import StreamingResponse
from .cytoscape2neo4j import upload_cytoscape_to_neo4j
import asyncio
import requests
import html2text
import json

from dotenv import load_dotenv

load_dotenv()

app = FastAPI()


@app.post("/url")
async def extract_url_content(urls: list[str]):

    h = html2text.HTML2Text()
    h.ignore_links = False

    markdown_contents = []
    for url in urls:
        try:
            response = requests.get(url)
            response.raise_for_status()
            html_content = response.text
            markdown_content = h.handle(html_content)
            markdown_contents.append(markdown_content)
        except Exception as e:
            markdown_contents.append(f"Error processing {url}: {str(e)}")

    combined_markdown = "\n\n".join(markdown_contents)

    json_output = b.GenerateGraph(combined_markdown)
    json_str = str(json_output.model_dump_json())
    json_dict = json.loads(json_str)

    finished = upload_cytoscape_to_neo4j(json_dict)
    return {"finished": finished}


@app.get("/")
async def extract_resume():
    resume = """
    John Doe
    1234 Elm Street 
    Springfield, IL 62701
    (123) 456-7890

    Objective: To obtain a position as a software engineer.

    Education:
    Bachelor of Science in Computer Science
    University of Illinois at Urbana-Champaign
    May 2020 - May 2024

    Experience:
    Software Engineer Intern
    Google
    May 2022 - August 2022
    - Worked on the Google Search team
    - Developed new features for the search engine
    - Wrote code in Python and C++

    Software Engineer Intern
    Facebook
    May 2021 - August 2021
    - Worked on the Facebook Messenger team
    - Developed new features for the messenger app
    - Wrote code in Python and Java
    """

    async def stream_resume(resume):
        stream = b.stream.ExtractResume(resume)
        for chunk in stream:
            print(f"Got chunk: {chunk}")
            yield (str(chunk.model_dump_json()) + "\n")
            await asyncio.sleep(
                0
            )  # from https://github.com/encode/starlette/discussions/1776#discussioncomment-3207518

    return StreamingResponse(stream_resume(resume), media_type="text/event-stream")
