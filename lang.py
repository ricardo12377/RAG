from langchain_ollama import ChatOllama
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory

txt_path = "./context/history.txt"

loader = TextLoader(txt_path)
docs = loader.load()

text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
documents = text_splitter.split_documents(docs)

embeddings = OllamaEmbeddings(model="mistral")

vectordb = Chroma.from_documents(documents, embedding=embeddings, persist_directory="./db")
vectordb.persist()

llm = ChatOllama(model="mistral")

memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

qa_chain = ConversationalRetrievalChain.from_llm(
    llm=llm,
    retriever=vectordb.as_retriever(),
    memory=memory,
)

print("Digite 'sair' para encerrar.\n")

while True:
    query = input("Você: ")
    if query.lower() in ["sair", "exit", "quit"]:
        break

    result = qa_chain.invoke({"question": query})
    print(f"IA: {result['answer']}")
