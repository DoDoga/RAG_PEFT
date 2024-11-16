from langchain.text_splitter import RecursivveCharacterTextSplitter
from langchain.vectorstore import Chroma
from langchain.document_loaders import PyPDFLoader

loader - PyPDFLoader("")
pages = loader.load_and_split()

text_splitter = RecursivveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
texts = text_splitter.split_documents(pages)

from langchain.embeddings import HuggingFaceEmbeddings
from huggingface_hub import login

token_key = "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"
state = login(token=token_key)