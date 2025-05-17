import streamlit as st
from transformers import pipeline


st.set_page_config(
        page_title="Chitti",
        page_icon="🤖",
        menu_items={
            'About': "# This is a Streamlit Question Answer Bot. This is an *extremely* cool application!"
        }
    )

question_answerer = pipeline("question-answering", model="distilbert/distilbert-base-cased-distilled-squad")

st.title("I`m a Quick Learner 😉")

context = st.text_area("Explain me something...", height=500)
qn_ask =  st.button("Question???")

if context.strip() or qn_ask:
    question = st.text_input("Now ask me 😎")
    ask_answer =  st.button("Tell the answer")
    
    if  question.strip() or ask_answer:
        with st.spinner("Let me think..."):
            answer = question_answerer(question=question, context=context)
            st.write(answer["answer"])