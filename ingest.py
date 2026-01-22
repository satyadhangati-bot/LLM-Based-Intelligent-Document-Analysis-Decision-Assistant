import os

def load_documents(path):
    docs = []
    for file in os.listdir(path):
        if file.endswith(".txt"):
            with open(os.path.join(path, file), "r", encoding="utf-8") as f:
                docs.append(f.read())
    return docs
