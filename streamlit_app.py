st.title("Generador de bibliografía estilo APA")

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