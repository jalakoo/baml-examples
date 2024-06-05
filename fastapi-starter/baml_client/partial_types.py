###############################################################################
#
#  Welcome to Baml! To use this generated code, please run the following:
#
#  $ pip install baml
#
###############################################################################

# This file was generated by BAML: please do not edit it. Instead, edit the
# BAML files and re-generate this code.
#
# ruff: noqa: E501,F401
# flake8: noqa: E501,F401
# pylint: disable=unused-import,line-too-long
# fmt: off
import baml_py
from enum import Enum
from pydantic import BaseModel
from typing import List, Optional, Union

from . import types

###############################################################################
#
#  These types are used for streaming, for when an instance of a type
#  is still being built up and any of its fields is not yet fully available.
#
###############################################################################


class BookAnalysis(BaseModel):
    bookNames: List[Optional[str]]
    popularityOverTime: List["PopularityOverTime"]

class CharacterDescription(BaseModel):
    name: Optional[str] = None
    clothingItems: List[Optional[str]]
    hairColor: Optional[str] = None
    smellDescription: Optional[str] = None
    spells: List["Spells"]

class DynamicOutput(BaseModel):

class Education(BaseModel):
    school: Optional[str] = None
    degree: Optional[str] = None
    year: Optional[int] = None

class Message(BaseModel):
    role: Optional[types.Role] = None
    content: Optional[str] = None

class PopularityOverTime(BaseModel):
    bookName: Optional[str] = None
    scores: List["Score"]

class Ranking(BaseModel):
    bookName: Optional[str] = None
    score: Optional[int] = None

class Resume(BaseModel):
    name: Optional[str] = None
    education: List["Education"]
    skills: List[Optional[str]]

class Score(BaseModel):
    year: Optional[int] = None
    score: Optional[int] = None

class Spells(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None

class WordCount(BaseModel):
    bookName: Optional[str] = None
    count: Optional[int] = None
