# This file is generated by the BAML compiler.
# Do not edit this file directly.
# Instead, edit the BAML files and recompile.

# ruff: noqa: E501,F401
# flake8: noqa: E501,F401
# pylint: disable=unused-import,line-too-long
# fmt: off

from .clients.client_gpt35 import GPT35
from .clients.client_gpt35_yes_no import GPT35_YES_NO
from .clients.client_gpt4 import GPT4
from .clients.client_gptinstruct import GPTInstruct
from .clients.client_main import Main
from .functions.fx_classifyintent import BAMLClassifyIntent
from .functions.fx_extractmeetingrequestinfo import BAMLExtractMeetingRequestInfo
from .functions.fx_extractmeetingrequestinfopartial import BAMLExtractMeetingRequestInfoPartial
from .functions.fx_generateuserchatprompts import BAMLGenerateUserChatPrompts
from .functions.fx_getnextquestion import BAMLGetNextQuestion
from .functions.fx_thingy import BAMLThingy
from baml_core.otel import add_message_transformer_hook, flush_trace_logs
from baml_core.services import LogSchema
from baml_core.services.api_types import LogSchema
from baml_lib import DeserializerException, baml_init
from typing import Callable, List, Optional


class BAMLClient:
    ClassifyIntent = BAMLClassifyIntent
    ExtractMeetingRequestInfo = BAMLExtractMeetingRequestInfo
    ExtractMeetingRequestInfoPartial = BAMLExtractMeetingRequestInfoPartial
    GenerateUserChatPrompts = BAMLGenerateUserChatPrompts
    GetNextQuestion = BAMLGetNextQuestion
    Thingy = BAMLThingy
    GPT35 = GPT35
    GPT35_YES_NO = GPT35_YES_NO
    GPT4 = GPT4
    GPTInstruct = GPTInstruct
    Main = Main

    def __init__(self):
        baml_init()

    def configure(
        self,
        project_id: Optional[str] = None,
        secret_key: Optional[str] = None,
        base_url: Optional[str] = None,
        enable_cache: Optional[bool] = None,
        stage: Optional[str] = None,
    ):
        return baml_init(
            project_id=project_id,
            secret_key=secret_key,
            base_url=base_url,
            enable_cache=enable_cache,
            stage=stage,
        )

    def add_before_send_message_hook(self, hook: Callable[[LogSchema], None]):
        add_message_transformer_hook(hook)

    def flush(self):
        flush_trace_logs()


baml = BAMLClient()
