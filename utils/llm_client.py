from __future__ import annotations
import os
from typing import Optional
from dotenv import load_dotenv
from groq import Groq
from config.model_config import load_config

load_dotenv()


class GroqClient:
    def __init__(self, api_key: Optional[str] = None, config_path: Optional[str] = None):
        self.app_config = load_config(config_path)
        self.model_cfg = self.app_config.model

        self.api_key = api_key or os.getenv("GROQ_API_KEY")
        if not self.api_key:
            raise ValueError("GROQ_API_KEY not found.")

        # Initialize Groq client
        self.client = Groq(api_key=self.api_key)

    def ask(self, prompt: str) -> str:
        response = self.client.chat.completions.create(
            model=self.model_cfg.name,
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=self.model_cfg.temperature,
            top_p=self.model_cfg.top_p,
            max_tokens=self.model_cfg.max_tokens
        )

        if not response or not response.choices:
            return "No response generated. Please try again."

        return response.choices[0].message.content
