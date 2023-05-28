from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Jeevitha M"
PAGE_ICON = ":wave:"
NAME = "Jeevitha M"
DESCRIPTION = """
Student|Machine Learning and DevOps Enthusiast
"""
EMAIL = "jeevithamurugan.2512@gmail.com"
SOCIAL_MEDIA = {
       "LinkedIn": "https://www.linkedin.com/in/jeevitha-m-357979223/",
       "GitHub": "https://github.com/JEEVITHA2512",
}
PROJECTS = {
    "🏆 Resume Selector - Naive Bayes Classifier",
    "🏆 Diabetic Retinopathy using Artificial Intelligence - CNN ",
    "🏆 Fitness Data Analysis"
    "🏆 Heart Disease Prediction",
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qulifications")
st.write(
    """
- ✔️ 12th Equivalent Grade - St.John's Sr Sec School [2006-2020]
- ✔️ BTech : Artificial Intelligence and Data Science  - St.Joseph's College of Engineering [2021-2025]
- ✔️ Developer Intern - Tactlabs [December 2021- October 2022]
    - Skills gained : Machine Learning, Data Science , Feature Engineering , Python mentoring session 
- ✔️ Python development Intern - CodeClause [April 2023 - May 2023]
    - Skills gained : Potential coding and problem solving ability
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Programming: Python (Scikit-learn, Pandas), SQL, VBA
- 📊 Data Visulization: PowerBi, MS Excel, Plotly
- 📚 Modeling: Logistic regression, linear regression, decition trees
- 🗄️ Databases: Postgres, MongoDB, MySQL
"""
)


# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🚧", "**Developer Intern  | Tactlabs**")
st.write("12/2021 - 10/2022")
st.write(
    """
- ► Worked on Streamlit and Django projects
- ► Led a team of 4 analysts to brainstorm potential marketing and sales improvements
- ► Mentored python sessions for abroad students and got paid for my remarkable performance

"""
)

# --- JOB 2
st.write('\n')
st.write("🚧", "**Python Development Intern | CodeClause **")
st.write("04/2023 - 05/2023")
st.write(
    """
- ► Worked on projects like Random password Generator and Scientific Calculator design
- ► Worked on golden projects ike Library Management System through Django and speed typing test
"""
)

# --- JOB 3
st.write('\n')
st.write("🚧", "**Data Analyst Trainee | MedTourEasy **")
st.write("04/2023 - 05/2023")
st.write(
    """
- ► Undertook training of different modules and did work on various industry level projects
"""
) 


# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write(
    """
        1. Resume Selector using Naive Bayes Classifier
        2. Kyphosis Classification using Machine Learning
        3. EMI Due Automation - UIPath RPA
        4. Heart Disease Prediction
        5. Fitness Data Analysis
    """
)

    