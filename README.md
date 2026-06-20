# 🤖 AI Career Assistant

An AI-powered career guidance application built using **Streamlit** and **Google Gemini AI**. This assistant helps users improve resumes, prepare for interviews, generate personalized learning roadmaps, and receive career guidance through an interactive chat interface.

## 🚀 Live Demo

Add your deployed Streamlit URL here:

```text
https://your-app-name.streamlit.app
```

## 📌 Features

### 💬 General Chat

Ask career-related questions and receive AI-powered responses.

### 📄 Resume Review

Get suggestions to improve resume content, structure, and presentation.

### 🎯 Interview Preparation

Generate interview questions and sample answers for various roles and technologies.

### 🗺️ Skill Roadmap

Receive personalized learning roadmaps for careers such as:

* Data Science
* Data Analytics
* Machine Learning
* AI Engineering
* Python Development

### 📊 Interactive Dashboard

* Current mode indicator
* AI model status
* Example prompts
* Professional sidebar navigation
* Responsive Streamlit interface

### 🗑️ Chat Management

Clear chat history instantly with a single click.

---

## 🛠️ Technologies Used

* Python
* Streamlit
* Google Gemini API
* Generative AI

---

## 📂 Project Structure

```text
AI-Career-Assistant/
│
├── app.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### Clone the Repository

```bash
git clone https://github.com/your-username/AI-Career-Assistant.git
cd AI-Career-Assistant
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Configure Gemini API Key

### Local Development

Create a `.streamlit/secrets.toml` file:

```toml
GEMINI_API_KEY="YOUR_API_KEY"
```

### Streamlit Community Cloud

1. Open your deployed app dashboard.
2. Navigate to **App Settings → Secrets**.
3. Add:

```toml
GEMINI_API_KEY="YOUR_API_KEY"
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

The application will open automatically in your browser.

---

## 💡 Example Prompts

### Resume Review

```text
Review my resume for a Data Analyst position.
```

### Interview Questions

```text
Generate Python interview questions with answers.
```

### Skill Roadmap

```text
Create a roadmap to become a Data Scientist.
```

### Career Guidance

```text
What skills are required for an AI Engineer role?
```

---

## 🌐 Deployment

This application is deployed using **Streamlit Community Cloud**.

Deployment Steps:

1. Create a GitHub repository.
2. Upload `app.py` and `requirements.txt`.
3. Connect GitHub with Streamlit Community Cloud.
4. Add the Gemini API key in Secrets.
5. Deploy the application.
6. Share the public URL.

---

## 🔮 Future Enhancements

* PDF Resume Upload and Analysis
* ATS Resume Score Checker
* Voice-Based AI Career Assistant
* Job Recommendation System
* Resume Download Feature
* Multi-Language Support
* Career Progress Tracker

---

## 👨‍💻 Author

**Amal B**

Computer Science and Engineering Graduate

Interested in:

* Data Science
* Data Analytics
* Machine Learning
* Generative AI
* Cloud Computing

---

## 📜 License

This project is intended for educational, learning, and portfolio purposes.
