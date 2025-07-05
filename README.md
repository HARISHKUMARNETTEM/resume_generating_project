🧠 AI Resume Generator (using Gemini API)
An AI-powered resume and cover letter generator developed using Flask and Google’s Gemini API. This web application helps users instantly generate a job-ready resume and a personalized cover letter based on their profile, experience, and target role using Generative AI.

🚀 Features
✍️ Instantly generates professional resumes and cover letters using user inputs

🧠 Powered by Google Gemini 1.5 Flash (google-generativeai)

🖥️ Clean UI built using Flask, HTML, and CSS

📥 Form inputs include: Name, Education, Experience, Job Role, Skills, Certifications, Achievements

🔒 API key securely handled using .env (not pushed to GitHub)

🎯 Outputs formatted with bold headings using Markdown-style formatting via regex

🛠️ Tech Stack
Backend: Python, Flask

Frontend: HTML5, CSS3

AI Integration: Google Gemini 1.5 Flash API

Environment Management: python-dotenv

📂 Project Structure
bash
Copy code
resume_writer_project/
├── app.py                 # Flask backend
├── requirements.txt       # Project dependencies
├── .gitignore             # Files to be ignored by Git
├── .env                   # Stores API key (keep secret)
│
├── templates/
│   └── index.html         # Form-based user interface
│
└── static/
    └── style.css          # Frontend styling
🔧 Setup Instructions
1. Clone the repository
bash
Copy code
git clone https://github.com/your-username/resume-writer-project.git
cd resume-writer-project
2. Install dependencies
bash
Copy code
pip install -r requirements.txt
3. Configure the Gemini API key
Create a .env file in the root directory and add:

env
Copy code
GEMINI_API_KEY=your_api_key_here
⚠️ Note: The .env file is excluded from version control via .gitignore.

4. Start the application
bash
Copy code
python app.py
Then, open your browser and go to http://127.0.0.1:5000/

✅ Sample Workflow
Fill in your name, contact details, education, skills, experience, and target job role.

Click the Generate button.

The app displays a personalized resume and a formal cover letter generated using Gemini AI.

🧪 Testing Strategy
This project was tested to ensure a smooth user experience, coherent output, and system reliability. The following types of testing were performed:

• Input Handling: Checked compatibility with various user profiles (freshers, experienced, long/short inputs).
• Content Accuracy: Ensured generated content reflects the input data and is relevant to the chosen role.
• Form Validation: Required fields trigger validation warnings when left empty.
• Formatting: Resume and cover letter follow professional standards using bold headings and structured content.
• Edge Case Testing: Used unexpected values (e.g., empty skills, fake tools) to ensure system stability.

🔮 Future Enhancements
Export as PDF
Add a feature to download resume and cover letter in PDF format.

Multiple Resume Layouts
Offer different formatting templates for user selection.

User Login & Profile Saving
Allow users to log in and save their resume data for future editing.

Smart Suggestions
Recommend certifications, job roles, or skill keywords during form filling.

Multilingual Resume Output
Support multiple languages for broader usability.

AI-powered Job Recommendations
Suggest jobs based on the skills and roles selected by the user.

👨‍💻 Author
HARISH KUMAR NETTEM
B.Tech Student | AIML Specialization
Email: harish.23bce7749@vitapstudent.ac.in
College: VELLORE INSTITUTE OF TECHNOLOGY, AMARAVATI

📄 License
This project is for academic and educational use only. All generated content should be reviewed before professional use.

