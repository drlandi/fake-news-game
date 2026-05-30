import streamlit as st
import random

st.title("🗳️ Fake News Game")

questions = [
    ("O voto é obrigatório para quem tem 16 anos.", "FAKE", "É facultativo entre 16 e 17."),
    ("É proibido levar o celular ligado para a cabine de votação.", "FATO", "Configura crime eleitoral."),
    ("Se mais de 50% votarem nulo, a eleição é cancelada.", "FAKE", "Votos nulos são descartados."),
    ("O Prefeito é quem cria as leis da cidade.", "FAKE", "Quem cria leis é o Vereador."),
    ("Posso votar usando apenas o app e-Título no celular.", "FATO", "Com foto cadastrada é válido."),
    ("O Vereador pode enviar verba para o laboratório da escola.", "FATO", "Via emendas parlamentares.")
]

if "q" not in st.session_state:
    st.session_state.q = random.choice(questions)
    st.session_state.score = 0
    st.session_state.answered = False

q, answer, explanation = st.session_state.q

st.subheader(q)

if not st.session_state.answered:
    col1, col2 = st.columns(2)
    if col1.button("FATO"):
        st.session_state.answered = True
        if answer == "FATO":
            st.session_state.score += 1
    if col2.button("FAKE"):
        st.session_state.answered = True
        if answer == "FAKE":
            st.session_state.score += 1

if st.session_state.answered:
    if answer == "FATO":
        st.success("Resposta correta: FATO")
    else:
        st.error("Resposta correta: FAKE")

    st.write(explanation)

    if st.button("Próxima pergunta"):
        st.session_state.q = random.choice(questions)
        st.session_state.answered = False

st.write("Pontuação:", st.session_state.score)
