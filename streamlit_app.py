import openai
import streamlit as st
import os

# Autenticación de OpenAI (oculta la clave en una variable de entorno)
openai.api_key = os.environ.get("OPENAI_API_KEY")


st.title("Generador de bibliografía estilo APA")
st.caption("Es preciso verificar todas las referencias")
tema = st.text_input("Introduce el tema de la bibliografía:", "")

if st.button("Generar"):
  bibliography = []

  for i in range(25):
    model_engine = "text-davinci-003"
    prompt = f"Generar item de bibliografía estilo APA sobre {tema}"
    completions = openai.Completion.create(
      engine=model_engine,
      prompt=prompt,
      max_tokens=1024,
      n=1,
      stop=None,
      temperature=0.7,
    )
    bibliography_item = completions.choices[0].text
    bibliography.append(bibliography_item)

  bibliography_str = "\n".join(bibliography)
  st.markdown(f"- {bibliography_str}")
