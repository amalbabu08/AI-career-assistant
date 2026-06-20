import streamlit as st
import google.generativeai as genai

st.set_page_config(
    page_title="AI Career Assistant",
    page_icon="🤖",
    layout="wide"
)

api_key = st.secrets["GEMINI_API_KEY"]

genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-2.5-flash")

st.title("🤖 AI Career Assistant")

st.sidebar.header("Tools")

tool = st.sidebar.selectbox(
    "Choose Tool",
    [
        "General Chat",
        "Resume Review",
        "Interview Questions",
        "Skill Roadmap"
    ]
)

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

prompt = st.chat_input("Ask me anything...")

if prompt:

    if tool == "Resume Review":
        final_prompt = f"""
        Review the following resume content and suggest improvements:

        {prompt}
        """

    elif tool == "Interview Questions":
        final_prompt = f"""
        Generate interview questions and answers for:

        {prompt}
        """

    elif tool == "Skill Roadmap":
        final_prompt = f"""
        Create a learning roadmap for:

        {prompt}
        """

    else:
        final_prompt = prompt

    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.spinner("Thinking..."):
        response = model.generate_content(final_prompt)
        answer = response.text

    st.session_state.messages.append(
        {"role": "assistant", "content": answer}
    )

    with st.chat_message("assistant"):
        st.markdown(answer)

if st.sidebar.button("Clear Chat"):
    st.session_state.messages = []
    st.rerun()