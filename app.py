import streamlit as st
from langchain.llms.openai import OpenAI
from dotenv import load_dotenv
import os

# Carregar variáveis de ambiente
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# Verificar se a variável de ambiente foi carregada corretamente
if not api_key:
    st.error("API_KEY não encontrada. Verifique o arquivo .env.")
    st.stop()

def summarize_article(article_text):
    # Inicializar o modelo OpenAI
    llm = OpenAI(api_key=api_key)
    
    # Verifique se o método `__call__` está disponível para a classe OpenAI
    try:
        prompt = f"Por favor, forneça um resumo conciso do seguinte artigo:\n\n{article_text}"
        summary = llm(prompt)  # Certifique-se de que esse é o método correto para obter o resumo
    except Exception as e:
        st.error(f"Erro ao gerar o resumo: {str(e)}")
        return None
    
    return summary

# Configurando a interface do Streamlit
st.title("Sumarizador de Artigos")
st.write("Insira o texto do artigo abaixo e obtenha um resumo conciso.")

article_text = st.text_area("Texto do Artigo", height=300)

if st.button("Resumir"):
    if article_text:
        summary = summarize_article(article_text)
        if summary:
            st.write("**Resumo:**")
            st.write(summary)
    else:
        st.write("Por favor, insira o texto do artigo.")