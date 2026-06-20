import streamlit as st
import google.generativeai as genai

st.set_page_config(
    page_title="AI Career Assistant",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
.main {
    padding-top: 1rem;
}

.stChatMessage {
    border-radius: 15px;
    padding: 10px;
}

h1 {
    color: #4CAF50;
}

.stButton > button {
    width: 100%;
}
</style>
""", unsafe_allow_html=True)

api_key = st.secrets["GEMINI_API_KEY"]

genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-2.5-flash")

st.title("🤖 AI Career Assistant")

st.markdown("""
### Your Personal AI Career Coach

Get instant help with:

- 📄 Resume Reviews
- 🎯 Interview Preparation
- 🗺️ Learning Roadmaps
- 💼 Career Guidance

Ask a question below to get started.
""")

st.sidebar.title("🤖 AI Career Assistant")

st.sidebar.markdown("""
Welcome!

This AI assistant helps you with:

✅ Resume Review

✅ Interview Preparation

✅ Skill Roadmaps

✅ Career Guidance
""")

tool = st.sidebar.selectbox(
    "Choose a Tool",
    [
        "General Chat",
        "Resume Review",
        "Interview Questions",
        "Skill Roadmap"
    ]
)

st.sidebar.divider()

if st.sidebar.button("🗑️ Clear Chat"):
    st.session_state.messages = []
    st.rerun()

st.info(f"Current Mode: {tool}")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("AI Model", "Gemini")

with col2:
    st.metric("Tools", "4")

with col3:
    st.metric("Status", "Online")

with st.expander("💡 Example Prompts"):

    st.markdown("""
    **Resume Review**
    - Review my resume for a Data Analyst role

    **Interview Questions**
    - Generate Python interview questions

    **Skill Roadmap**
    - Create a roadmap to become a Data Scientist

    **Career Guidance**
    - What skills are needed for AI Engineering?
    """)

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

st.divider()

st.markdown("""
---
Built using Streamlit and Google Gemini

Developer: Amal Babu
""")
