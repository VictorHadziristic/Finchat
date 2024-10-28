import os
import json

from langchain_community.document_loaders import PyPDFLoader
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage

from TenK_extraction_model import TenKForm


def extract_from_pdf(pdf_path: str, data_model, form_type: str, max_retries: int = 5):
    try:
        loader = PyPDFLoader(pdf_path)
        pages = loader.load_and_split()
        text = " ".join(list(map(lambda page: page.page_content, pages)))
        llm = ChatOpenAI(model="gpt-4o-mini", temperature=0, api_key=os.getenv("OPEN_AI_API_KEY"))
        structured_llm = llm.with_structured_output(data_model)

        messages = [
            SystemMessage(
                content=[{"type": "text", "text": f"You are a data extractor for {form_type} PDF files."}]
            ),
            HumanMessage(
                content=[{"type": "text", "text": text}]
            )
        ]

        # Attempt to invoke the structured LLM with retries
        for attempt in range(max_retries):
            try:
                return structured_llm.invoke(messages)
            except Exception as invoke_error:
                print(f"Attempt {attempt + 1} failed: {str(invoke_error)}")
                if attempt + 1 == max_retries:  # Last attempt
                    raise  # Raise if max retries exceeded
    except Exception as e:
        print(f"Error Parsing PDF: {str(e)}")

print(extract_from_pdf("dev-takehome-filing.pdf", TenKForm, "10-K").json())