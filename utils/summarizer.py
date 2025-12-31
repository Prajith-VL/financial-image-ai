from transformers import pipeline

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def generate_summary(text):
    if len(text) < 50:
        return "Not enough data to summarize."

    summary = summarizer(
        text,
        max_length=150,
        min_length=50,
        do_sample=False
    )
    return summary[0]["summary_text"]
