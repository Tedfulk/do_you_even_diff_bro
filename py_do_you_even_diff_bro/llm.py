"""
This module contains the functions that interact with the OpenAI API.
"""

import os
import sys
from typing import Any, Dict

import openai

openai.api_key = os.getenv("OPENAI_API_KEY")


def safe_get(data: Dict[str, Any], dot_chained_keys: str) -> Any:
    """
    {'a': {'b': [{'c': 1}]}}
    safe_get(data, 'a.b.0.c') -> 1
    """
    try:
        for key in dot_chained_keys.split("."):
            data = data[int(key)] if isinstance(data, list) else data[key]
    except (KeyError, TypeError, IndexError):
        return None
    return data


def response_parser(response: Dict[str, Any]) -> str:
    return safe_get(response, "choices.0.message.content")


def gpt_prompt(prompt: str, model: str = "gpt-4") -> str:
    if not openai.api_key:
        sys.exit(
            """
ERROR: OpenAI API key not found. Please export your key to OPENAI_API_KEY
Example bash command:
    export OPENAI_API_KEY=<your openai apikey>
            """
        )

    response = openai.ChatCompletion.create(
        model=model,
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
    )

    return response_parser(response)
