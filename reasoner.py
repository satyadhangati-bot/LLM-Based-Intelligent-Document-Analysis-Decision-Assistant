from transformers import pipeline

llm = pipeline("text-generation", model="google/flan-t5-large")

def generate_answer(context, question):
    prompt = f"""
    Context:
    {context}

    Question:
    {question}

    Answer:
    """
    return llm(prompt, max_length=300)[0]["generated_text"]
