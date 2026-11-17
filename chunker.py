from langchain_text_splitters import RecursiveCharacterTextSplitter
from crudfiles import get_company_content

text = get_company_content(4)

text_splitter = RecursiveCharacterTextSplitter(chunk_size=300,
                                              chunk_overlap=50)

chunks = text_splitter.split_text(text)

#for i, chunk in enumerate(chunks):
    #print(f"\n====== Chunk {i+1} ======\n")
    #print(chunk)