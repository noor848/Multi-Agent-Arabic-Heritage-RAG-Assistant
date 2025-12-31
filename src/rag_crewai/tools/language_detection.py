from crewai.tools import BaseTool
from typing import Type, Any
from pydantic import BaseModel, Field
from transformers import pipeline
import torch


class LanguageDetectionInput(BaseModel):
    """Input schema for language detection."""
    text: str = Field(..., description="The text to detect the language of")


class LanguageDetectionTool(BaseTool):
    name: str = "Language Detector"
    description: str = "Detects the language of a given text. Returns language code (en/ar) or 'other' for unsupported languages"
    args_schema: Type[BaseModel] = LanguageDetectionInput

    classifier: Any = Field(default=None, exclude=True)

    def __init__(self):
        super().__init__()
        # Automatically detect device: use GPU if available, otherwise CPU
        device = 0 if torch.cuda.is_available() else -1
        self.classifier = pipeline(
            "text-classification",
            model="papluca/xlm-roberta-base-language-detection",
            device=device
        )

    def _run(self, text: str) -> str:
        """Execute the language detection."""
        result = self.classifier(text)[0]
        lang_code = result['label']

        if lang_code == 'ar':
            return "ar"
        elif lang_code == 'en':
            return "en"
        else:
            return "en"  # default
