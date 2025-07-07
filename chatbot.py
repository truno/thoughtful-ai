import json
from pydantic import BaseModel
from typing import Annotated
from typing_extensions import TypedDict
import os

from langchain.chat_models import init_chat_model
from langchain_core.tools import tool, BaseTool, ToolException

class QATool(BaseModel):
    name: str = "qa_tool"
    description: str = "A tool to answer questions based on prepared questions and answers."
    prepared_questions: list[(str, str)] = []

    def __init__(self, prepared_questions: list, **kwargs):
        super().__init__(**kwargs)
        self.prepared_questions = prepared_questions

    def _run(self, question: str, llm) -> str:
        try:
            # Basic string match, can be improved with more sophisticated matching
            for prepared in self.prepared_questions:
                if question.lower() in prepared["question"].lower():
                    return prepared["answer"]
                
            # Ask the LLM if no match is found
            prompt_template = f"You are a friendly customer support agent. Answer the following question: {question}"

            results = llm.invoke(prompt_template, {"question": question})
            return results.content
        except ToolException:
            # Re-raise tool exceptions
            raise
        except Exception as e:
            return f"error: {e}"

    def invoke(self, question: str, llm) -> str:
        # Custom invoke method to pass the `llm` argument to `_run`
        return self._run(question, llm)
    
    async def _arun(self, question: str, llm) -> str:
        raise NotImplementedError("This tool does not support async execution.")  
