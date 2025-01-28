
import streamlit as st
from PIL import Image

# Configure the Streamlit app
st.set_page_config(
    page_title="Md Anique Zzama - Portfolio",
    page_icon="💻",
    layout="wide"
)

# Sidebar Navigation
st.sidebar.title("Navigation")
menu = ["Home", "About Me", "Projects", "Skills", "Contact"]
choice = st.sidebar.radio("Go to:", menu)

# Home Section
if choice == "Home":
    st.title("Welcome to My Portfolio! 👋")
   # st.image("https://via.placeholder.com/1200x400?text=Welcome+to+My+Portfolio", caption="Achieving success through innovation.")
    st.write("""
    Hi, I'm **Md Anique Zzama**, a passionate **Data Scientist** and **Machine Learning Engineer**.
    Explore my portfolio to learn about my journey, skills, and achievements.
    """)

# About Me Section
elif choice == "About Me":
    st.header("About Me 🧑‍🔬")
    st.write("""
    I’m **Md Anique Zzama**, a dedicated Data Scientist with over 6 months of experience in data analytics, machine learning, 
    and generative AI. I recently graduated with a degree in **Computer Science and Engineering**, and I have completed multiple impactful projects.
    """)
    st.subheader("Highlights")
    st.write("""
    - **Machine Learning & Deep Learning** expertise.
    - **Generative AI** and **LLM** research experience.
    - Proficient in **Python**, **SQL**, **PySpark**, **Tableau**, and **Git/GitHub**.
    - Strong understanding of **Big Data tools** and **MLOps workflows**.
    """)

# Projects Section
elif choice == "Projects":
    st.header("My Projects 🔧")
    projects = {
        "1. Heart Disease Prediction": "A machine learning project predicting heart disease probability using patient data.",
        "2. House Price Prediction": "Accurately predicted house prices based on various features using regression techniques.",
        "3. Customer Churn Analysis": "Analyzed and visualized customer churn data to enhance retention strategies.",
        "4. Bitcoin Price Analysis": "Explored and modeled Bitcoin price trends using time-series analysis.",
        "5. Glaucoma Detection": "Applied deep learning techniques to detect glaucoma in fundus imaging datasets.",
        "6. E-Commerce Review Analysis": "Analyzed BlinkIt vs Zepto vs JioMart reviews for consumer insights.",
        "7. Social Media Dataset Analysis": "Worked on Kaggle's Social Media and Entertainment Dataset for data insights.",
        "8. MNIST Handwritten Recognition": "Developed a CNN model for recognizing handwritten digits.",
        "9. U.S. Election Data Prediction": "Analyzed and predicted trends in U.S. election data.",
    }

    for title, description in projects.items():
        st.subheader(title)
        st.write(description)
        st.markdown("https://github.com/mdaniq45")  # Replace # with GitHub URLs
        st.write("---")

# Skills Section
elif choice == "Skills":
    st.header("My Skills 📚")
    skills = {
        "Programming Languages": ["Python", "SQL","C"],
        "Data Visualization Tools": ["Tableau", "Power BI", "Matplotlib", "Seaborn"],
        "Machine Learning Frameworks": ["Scikit-learn", "TensorFlow", "PyTorch"],
        "Big Data Tools": ["PySpark", "Hadoop Ecosystem"],
        "Other Expertise": ["Git/GitHub", "MLOps", "LangChain", "Streamlit","GEN-AI",],
    }

    for category, skillset in skills.items():
        st.subheader(category)
        st.write(", ".join(skillset))

# Contact Section
elif choice == "Contact":
    st.header("Contact Me 📧")
    st.write("Feel free to reach out for collaborations or opportunities.")
    st.write("---")
    st.write("- **Email**: [mdaniq45@gmail.com](mailto:mdaniq45@gmail.com)")  # Replace with your email
    st.write("- **LinkedIn**: [https://www.linkedin.com/in/mdaniq45/](https://www.linkedin.com/in/anique)")  # Replace with your LinkedIn URL
    st.write("- **GitHub**: [https://github.com/mdaniq45](https://github.com/anique)")  # Replace with your GitHub URL
    st.write("- **Portfolio**: [aniqueportfolio.com](#)")  # Replace with your portfolio URL
    st.write("---")
   # st.write("Developed with ❤️ using Streamlit.")

# Footer
st.sidebar.write("---")
#st.sidebar.write("© 2025 Md Anique Zzama - All Rights Reserved.")
