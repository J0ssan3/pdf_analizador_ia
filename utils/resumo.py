from transformers import pipeline

def gerar_resumo(texto):
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    partes = [texto[i:i+1000] for i in range(0, len(texto), 1000)]
    resumo_final = ""

    for parte in partes:
        resumo = summarizer(parte, max_length=130, min_length=30, do_sample=False)[0]['summary_text']
        resumo_final += resumo + "\n"

    return resumo_final
