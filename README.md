# 🧠 AI Resume Generator (using Gemini API)

An intelligent resume and cover letter generator built using Flask and Google’s Gemini API. This web application allows users to enter their details and instantly generate a professional resume along with a formal cover letter using Generative AI.

---

## 🚀 Features

- ✍️ Automatically generates resumes and cover letters based on user input  
- 🧠 Uses Google Gemini 1.5 Flash (via `google-generativeai`)  
- 🖥️ Clean user interface built with Flask, HTML, and CSS  
- 💡 Custom input fields: Name, Education, Experience, Job Role, Skills, Certifications  
- 🔒 Secure environment variable handling using `.env`  

---

## 🛠️ Tech Stack

- **Backend**: Python, Flask  
- **Frontend**: HTML5, CSS3  
- **AI Integration**: Google Gemini 1.5 Flash  
- **Environment Management**: python-dotenv  

---

## 📂 Project Structure

```text
resume_writer_project/
├── app.py                  # Main Flask application
├── requirements.txt        # Python dependencies
├── .gitignore              # Ignored files and folders
├── .env                    # Contains Gemini API key (not tracked)
│
├── templates/
│   └── index.html          # Web UI
│
└── static/
    └── style.css           # Styling for the app
```

---

## 🔧 Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/your-username/resume-writer-project.git
cd resume-writer-project
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Add your Gemini API key

Create a `.env` file in the project root and add:

```env
GEMINI_API_KEY=your_api_key_here
```

### 4. Run the application

```bash
python app.py
```

Visit `http://127.0.0.1:5000/` in your browser to use the app.

---

## ✅ Sample Use Flow

1. Enter your name, education, experience, job role, skills, and certifications.  
2. Click **Generate Resume**.  
3. The app displays a personalized resume and cover letter using AI.  

---

## 🧪 Testing Strategy

The system was tested across a variety of use cases to ensure its reliability, coherence, and user-friendliness. Both manual and functional testing methods were used to verify the following:

- **Input Handling:**  
  Ensuring the system accurately handles different combinations of user inputs (e.g., fresher vs experienced, empty or minimal fields, long skill lists).

- **Content Relevance:**  
  Verifying that the generated resume and cover letter align well with the provided job role, education, and certifications.

- **Form Validation:**  
  Checking that required fields are properly validated and appropriate error handling is triggered when data is missing.

- **User Experience:**  
  Assessing the clarity of the form layout, responsiveness of the interface, and readability of the generated output.

- **Edge Case Testing:**  
  Testing with unusual or unexpected input values (e.g., made-up skills, overly generic job roles) to evaluate the robustness of the AI-generated content.

---

## 🔮 Future Enhancements

1. **PDF Export Support**  
   Add a feature that lets users download their resume and cover letter as PDF.

2. **Profile Saving and Editing**  
   Allow users to create an account and save their profile data for future edits.

3. **Template Customization**  
   Let users select different resume themes and layouts.

4. **AI Feedback Loop**  
   Introduce a feedback mechanism to rate and improve the output over time.

5. **Multilingual Support**  
   Generate resumes in multiple languages using multilingual models.

6. **Job Suggestions**  
   Integrate a job recommendation feature based on entered skills and role.

---

## 👨‍💻 Author

**HARISH KUMAR NETTEM**  
B.Tech Student | AIML Specialization  
Email: harish.23bce7749@vitapstudent.ac.in  
College: VELLORE INSTITUTE OF TECHNOLOGY, AMARAVATI

---

## 📄 License

This project is intended for educational and non-commercial use only.
