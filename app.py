from flask import Flask, render_template, request
import google.generativeai as genai
from dotenv import load_dotenv
import os
from datetime import date
import re

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

app = Flask(__name__)

def bold_headings(text):
    # Replace only full-line headings enclosed in **
    return re.sub(r"^\*\*(.+?)\*\*$", r"<strong>\1</strong>", text, flags=re.MULTILINE)

@app.route('/', methods=['GET', 'POST'])
def index():
    resume = ""
    cover_letter = ""
    show_output = False

    states = ["Andhra Pradesh", "Karnataka", "Maharashtra", "Tamil Nadu", "Delhi", "Other"]
    education_opts = [
        "12th Class", "Diploma", "BTech - Computer Science", "BTech - Electrical", "MTech - AI", "MCA"
    ]
    experience_opts = ["Fresher", "1 Year", "2 Years", "3-5 Years", "5+ Years"]

    today = date.today().strftime("%B %d, %Y")

    if request.method == 'POST':
        name         = request.form['name']
        contact      = request.form['contact']
        state        = request.form['state']
        address      = request.form['address']
        education    = request.form['education']
        university   = request.form.get('university', '')
        grad_year    = request.form.get('grad_year', '')
        experience   = request.form['experience']
        job_role     = request.form['job_role']
        certifications = request.form['certifications']
        achievements = request.form['achievements']
        company      = request.form['company']

        prompt = f"""
Generate a resume and cover letter in plain text format. Use this structure with bolded headings using **:

**Resume**

**{name}**  
{contact} | {address}, {state}

**Professional Summary**

Highly motivated and results-oriented {job_role} with {experience} of experience. Strong academic background in {education}. Skilled in tools such as {certifications}. Proven ability to manage, clean, and analyze large datasets to extract actionable insights and support decision-making. Seeking a challenging role at {company} to contribute to innovative projects.

**Achievements**

* {achievements}

**Certifications & Skills**

* {certifications}

**Education**

* {education}, {university}, Expected Graduation: {grad_year}

**Experience**

* [Company Name], [Job Title], [Dates of Employment]  
    * [Describe responsibilities and accomplishments using action verbs.]

**Cover Letter**

{name}  
{address}  
{contact}  

{today}  

Hiring Manager  
{company}  

Dear Hiring Manager,

I am writing to express my keen interest in the {job_role} position at {company}. My name is {name} and I live at {address}, {state}.

I am a highly motivated and results-oriented individual currently pursuing {education} at {university}, with an expected graduation year of {grad_year}. My academic background, along with {experience} of experience, has equipped me with strong expertise in {certifications}. My achievements include: {achievements}.

I am confident that my skills and experience align perfectly with the requirements of this role and I am eager to contribute my abilities to {company}’s innovative environment.

Thank you for your time and consideration. I look forward to hearing from you soon.

Sincerely,  
{name}  
{contact}  
{address}, {state}
"""

        try:
            model = genai.GenerativeModel('gemini-1.5-flash')
            response = model.generate_content(prompt)
            text = response.text.strip()

            if "**Cover Letter**" in text:
                parts = text.split("**Cover Letter**")
                resume = bold_headings(parts[0].strip())
                cover_letter = bold_headings("**Cover Letter**\n\n" + parts[1].strip())
            else:
                resume = bold_headings(text)
                cover_letter = ""

            show_output = True
        except Exception as e:
            resume = f"Error: {e}"
            show_output = True

    return render_template(
        'index.html',
        states=states,
        education_opts=education_opts,
        experience_opts=experience_opts,
        resume=resume,
        cover_letter=cover_letter,
        show_output=show_output
    )

if __name__ == '__main__':
    app.run(debug=True)
