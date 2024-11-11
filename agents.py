from transformers import pipeline
# from outline.text import call

summarizer = pipeline("summarization", model="facebook/bart-base")  # Use a smaller summarization model
qa_model = pipeline("question-answering", model="distilbert-base-uncased-distilled-squad")
generator = pipeline("text-generation", model="distilgpt2")  # Use a lightweight text-generation model

def summarize_text(text):
    summary = summarizer(text, max_length=150, min_length=30, do_sample=False)
    return summary[0]['summary_text']

def question_answering(context, question):
    result = qa_model(question=question, context=context)
    return result['answer']

def generate_future_directions(summary):
    prompt = f"Based on the summary, suggest future research directions:\n{summary}"
    directions = generator(prompt, max_length=100, num_return_sequences=1)
    return directions[0]['generated_text']

