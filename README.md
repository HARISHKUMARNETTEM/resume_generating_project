# 📄 AI-Powered Resume & Cover Letter Builder (Gemini API + Flask)

This project is a smart web application that assists users in generating professional resumes and cover letters using Google’s Gemini 1.5 Flash model. Designed with Flask and a simple frontend interface, it takes basic user inputs and outputs personalized content tailored for job applications.

---

## 🚀 Key Highlights

- 🤖 AI-based generation of resumes and cover letters using Gemini 1.5 Flash  
- 🌐 Developed with Python (Flask) for backend and HTML/CSS for frontend  
- 📌 Inputs include: Name, Education, Graduation Year, Experience Level, Job Role, Certifications, Skills, Achievements  
- 🔐 API keys are stored securely using `.env` environment files  
- 🎨 Outputs are structured using formatting techniques for better readability

---

## 🛠️ Technologies Used

- **Backend:** Flask (Python)  
- **Frontend:** HTML5, CSS3  
- **AI Integration:** Gemini 1.5 Flash via `google-generativeai`  
- **Config Management:** `python-dotenv` for environment variables

---

## 📁 Folder Layout

```text
resume_writer_project/
├── app.py                # Main application logic
├── .env                  # API key storage (excluded from GitHub)
├── .gitignore            # Ignored files list
├── requirements.txt      # Python libraries required
│
├── templates/
│   └── index.html        # HTML form UI
│
└── static/
    └── style.css         # Custom styles
```

---

## 🧑‍💻 How to Run the App

### 1. Clone the repo

```bash
git clone https://github.com/your-username/resume_writer_project.git
cd resume_writer_project
```

### 2. Install required packages

```bash
pip install -r requirements.txt
```

### 3. Add your Gemini API key

Create a `.env` file with the following line:

```env
GEMINI_API_KEY=your_actual_api_key
```

### 4. Start the Flask server

```bash
python app.py
```

Now open your browser and navigate to:  
`http://127.0.0.1:5000/`

---

## 📋 Workflow Summary

1. Users fill in a form with their personal and professional information.  
2. The backend sends this data to Gemini 1.5 Flash to generate custom content.  
3. A clean and copyable resume and cover letter is shown instantly.

---

## ✅ Testing Overview

To ensure a functional and smooth experience, the following tests were performed:

- **Form Inputs:** Handled multiple edge cases like fresher profiles, long skill sets, and missing data  
- **Output Quality:** Ensured AI responses reflected relevant job role, experience, and skills  
- **Validation:** Required fields were enforced; proper warnings shown for empty or invalid entries  
- **Layout Testing:** Verified consistency across browsers and devices  
- **Resilience:** Managed random or incorrect data without crashing

---

## 📊 Observations from Testing

- **Accuracy:** The AI-generated text was contextually accurate and professionally formatted  
- **Speed:** Average generation time remained under 3 seconds  
- **Stability:** The app did not crash even during repeated or incorrect usage

---

## 🔮 Planned Improvements

1. **PDF Resume Export**  
   Allow users to download the output as a PDF document.

2. **Multiple Resume Layouts**  
   Offer modern, minimal, and classic resume templates.

3. **User Authentication**  
   Add login/signup so users can save their resumes.

4. **Interactive Suggestions**  
   Recommend job roles or skills based on AI insight.

5. **Language Options**  
   Support resume generation in other languages.

6. **Integration with Job Portals**  
   Connect to LinkedIn or Naukri to autofill details.

---

## 👨‍🎓 Author

**Harish Kumar Nettem**  
B.Tech CSE | AIML Specialization  
📧 harish.23bce7749@vitapstudent.ac.in  
🏫 Vellore Institute of Technology, Amaravati

---

## 📄 License

This project is open for academic use only. Please review AI-generated resumes before submitting to companies.

