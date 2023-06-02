from llama_index import GPTVectorStoreIndex, SimpleDirectoryReader
from langchain.chat_models import ChatOpenAI


import os

os.environ["OPENAI_API_KEY"] = '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'


documents = SimpleDirectoryReader('/documentation').load_data()
index = GPTVectorStoreIndex.from_documents(documents)

llm=ChatOpenAI(temperature=0.5, model_name="gpt-3.5-turbo", max_tokens=2048)
