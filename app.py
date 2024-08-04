import streamlit as st
from langchain.llms.openai import OpenAI
from dotenv import load_dotenv
import os

#Carregar variáveis de ambiente do arquivo .env
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
def summarize_article(article_text):
    llm = OpenAI(api_key=api_key)
    prompt = f"Por favor, forneça um resumo conciso do seguinte artigo:\n\n{article_text}"
    summary = llm(prompt)
    return summary

# Configurando a interface do Streamlit
st.title("Sumarizador de Artigos")
st.write("Insira o texto do artigo abaixo e obtenha um resumo conciso.")

article_text = st.text_area("Texto do Artigo", height=300)

if st.button("Resumir"):
    if article_text:
        summary = summarize_article(article_text)
        st.write("**Resumo:**")
        st.write(summary)
    else:
        st.write("Por favor, insira o texto do artigo.") 