# This file is generated by the BAML compiler.
# Do not edit this file directly.
# Instead, edit the BAML files and recompile.

# ruff: noqa: E501,F401
# flake8: noqa: E501,F401
# pylint: disable=unused-import,line-too-long
# fmt: off

from baml_core.provider_manager import LLMManager
from os import environ


GPTInstruct = LLMManager.add_llm(
    name="GPTInstruct",
    provider="baml-openai-completion",
    retry_policy=None,
    redactions=["api_key"],
    options=dict(
        model="gpt-3.5-instruct",
        api_key=environ['OPENAI_API_KEY'],
    ),
)
