import os
import json
from langchain_community.document_loaders import PyPDFLoader
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_core.messages import HumanMessage, SystemMessage

pdf_path = "dev-takehome-filing.pdf"

def create_vector_store(pdf_path: str):
    print("Building Vector Store...")
    loader = PyPDFLoader(pdf_path)
    pages = loader.load_and_split()
    vector_store = InMemoryVectorStore.from_documents(pages, OpenAIEmbeddings(model="text-embedding-3-large", api_key=os.getenv("OPEN_AI_API_KEY")))
    print("Finished!")
    return vector_store

def search_vector_store(vector_store, question: str):
    try:
        docs = vector_store.similarity_search(question, k=3)
        
        # Gather the content from the retrieved documents
        context = "\n\n".join([f"Page {doc.metadata['page']}: {doc.page_content}" for doc in docs])
        
        chat_model = ChatOpenAI(api_key=os.getenv("OPEN_AI_API_KEY"), model="gpt-4o")

        messages = [
            SystemMessage(content="You are a helpful assistant who provides detailed answers based on provided document context."),
            HumanMessage(content=f"Context:\n{context}\n\nQuestion: {question}")
        ]
        
        response = chat_model.invoke(messages)
        print("Answer:", response.content)
        
    except Exception as e:
        print(f"Error Parsing PDF: {str(e)}")

vector_store = create_vector_store(pdf_path)

while True:
    user_input = input(f"Ask a question about {pdf_path}: ")
    if user_input.lower() == 'exit':
        print("Ending conversation. Goodbye!")
        break

    search_vector_store(vector_store, user_input)
