# AI Career Assistant

## Overview

AI Career Assistant is a Generative AI-powered web application built using Streamlit and Google Gemini. The application helps users with resume improvement, interview preparation, skill development roadmaps, and general career guidance through an interactive chat interface.

## Features

* AI-powered career guidance
* Resume review and improvement suggestions
* Interview question and answer generation
* Personalized skill roadmap creation
* Interactive chat interface
* Chat history management
* Built with Google Gemini AI and Streamlit

## Technologies Used

* Python
* Streamlit
* Google Gemini API
* Generative AI

## Project Structure

```text
AI-Career-Assistant/
│
├── app.py
├── requirements.txt
└── README.md
```

## Installation

### Clone the Repository

```bash
git clone https://github.com/your-username/AI-Career-Assistant.git
cd AI-Career-Assistant
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

## Configure Gemini API Key

Create a `.streamlit/secrets.toml` file and add:

```toml
GEMINI_API_KEY="YOUR_API_KEY"
```

Alternatively, when deploying on Streamlit Community Cloud, add the API key under:

**App Settings → Secrets**

```toml
GEMINI_API_KEY="YOUR_API_KEY"
```

## Run the Application

```bash
streamlit run app.py
```

## Usage

1. Launch the application.
2. Select a tool from the sidebar:

   * General Chat
   * Resume Review
   * Interview Questions
   * Skill Roadmap
3. Enter your query.
4. Receive AI-generated responses and recommendations.

## Example Use Cases

### Resume Review

* Improve resume content
* Get professional suggestions
* Identify missing skills

### Interview Preparation

* Generate interview questions
* Practice answers
* Prepare for technical and HR interviews

### Skill Roadmap

* Create learning plans
* Explore career paths
* Build technology-specific roadmaps

## Deployment

This application can be deployed easily using Streamlit Community Cloud.

Steps:

1. Push the project to GitHub.
2. Sign in to Streamlit Community Cloud.
3. Create a new application.
4. Select the repository and branch.
5. Set `app.py` as the main file.
6. Add the Gemini API key in Secrets.
7. Deploy the application.

## Future Enhancements

* PDF Resume Upload and Analysis
* Voice-Based Career Assistant
* Job Recommendation System
* Career Progress Tracking
* Multi-Language Support
* Conversation Export Feature

## Author

Amal Babu

Computer Science and Engineering Graduate

Interested in Data Science, Machine Learning, Generative AI, and Cloud Technologies.

## License

This project is intended for educational and portfolio purposes.
