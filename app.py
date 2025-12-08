import streamlit as st
from PIL import Image

# ======================
# 1. VISUAL CONFIGURATION
# ======================
st.set_page_config(
    page_title="Devanshi Pandya | Data Scientist",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for "Badges" and cleaner text
st.markdown("""
    <style>
    .small-font { font-size:14px !important; }
    .badge {
        background-color: #2d2d2d;
        color: white;
        padding: 4px 8px;
        border-radius: 4px;
        font-size: 12px;
        margin-right: 5px;
    }
    </style>
""", unsafe_allow_html=True)

# ======================
# 2. SIDEBAR (Profile & Resume)
# ======================
with st.sidebar:
    # Try to load profile pic, fallback to emoji if missing
    try:
        image = Image.open("profile_pic.png")
        st.image(image, width=200)
    except FileNotFoundError:
        st.header("👩‍💻") 

    st.title("Devanshi Pandya")
    st.markdown("📍 **NYC, New York**")
    st.markdown("📧 **devanshipandya44@gmail.com**")
    
    # Social Links as Buttons
    st.markdown("---")
    col_a, col_b = st.columns(2)
    with col_a:
        st.link_button("LinkedIn", "https://www.linkedin.com/in/devanshi4/")
    with col_b:
        st.link_button("GitHub", "https://github.com/devanshi4")

    # Resume Download
    st.markdown("---")
    try:
        with open("Devanshi_Pandya_Resume.pdf", "rb") as pdf_file:
            st.download_button(
                label="📄 Download Resume",
                data=pdf_file,
                file_name="Devanshi_Pandya_Resume.pdf",
                mime="application/pdf"
            )
    except FileNotFoundError:
        st.warning("⚠️ Resume file not found in folder")

# ======================
# 3. HERO SECTION (Intro)
# ======================
st.title("Hi, I'm Devanshi! 👋")
st.markdown("### 🔍 Data Analyst | Data Scientist | GenAI Builder")
st.markdown("""
I bridge the gap between **raw data** and **strategic decisions**. 
Currently optimizing network operations at **Verizon**, I specialize in replacing manual workflows with **AI-driven pipelines** and **predictive models**.
""")

# Tech Stack Badges (Visual Upgrade)
st.write("---")
st.markdown("**MY TECH STACK:**")
st.markdown("""
<span class="badge">Python</span>
<span class="badge">Generative AI</span>
<span class="badge">LangChain</span>
<span class="badge">SQL</span>
<span class="badge">Machine Learning</span>
<span class="badge">Tableau</span>
<span class="badge">Streamlit</span>
""", unsafe_allow_html=True)
st.write("") # Spacer

# ======================
# 4. KEY PROJECTS (Interactive Cards)
# ======================
st.header("💻 Key Projects")

col1, col2 = st.columns(2)

# --- Project 1: SQL AI Assistant ---
with col1:
    with st.container(border=True):
        st.subheader("🤖 AI SQL Assistant")
        st.markdown("**Stack:** LangChain, OpenAI, PostgreSQL")
        st.markdown("""
        *Built a GenAI tool that lets non-technical users query databases in plain English.*
        - **Impact:** Reduced ad-hoc data retrieval time by ~80%.
        - **Tech:** Implemented schema-aware prompt engineering for multi-table joins.
        """)
        # Link to the repo or live app
        st.link_button("View Code & Demo", "https://github.com/devanshi4/sql-ai-assistant")

# --- Project 2: Churn Prediction ---
with col2:
    with st.container(border=True):
        st.subheader("📉 Churn Predictor")
        st.markdown("**Stack:** XGBoost, SHAP, Streamlit")
        st.markdown("""
        *Engineered an ML dashboard to identify at-risk customers with 79% accuracy.*
        - **Impact:** Used Explainable AI (SHAP) to visualize key risk drivers.
        - **Tech:** Interactive dashboard for real-time scenario planning.
        """)
        # Link to the repo or live app
        st.link_button("View Code & Demo", "https://github.com/devanshi4/Churn-Prediction")

# ======================
# 5. EXPERIENCE (Content Upgrade)
# ======================
st.header("📚 Professional Experience")

# --- JOB 1: VERIZON ---
with st.container(border=True):
    st.markdown("#### **Data Analyst | Cloudify Technologies (Verizon)**")
    st.markdown("Start: *July 2024 - Present*")
    st.markdown("""
    - **AI Modernization:** Replaced a static 450-line SQL script with an **AI-assisted Python pipeline**, using GenAI to parse complex JSON logs.
    - **Operational Efficiency:** Analyzed orchestration logs to build cycle-time models, reducing troubleshooting time by **~40%**.
    - **Data Engineering:** Developed SQL pipelines to validate network deployment metrics across thousands of sites (Accuracy +55%).
    """)

# --- JOB 2: BRILLIO ---
with st.container(border=True):
    st.markdown("#### **Data Analyst | Brillio**")
    st.markdown("Start: *Sept 2023 - June 2024*")
    st.markdown("""
    - **Predictive Modeling:** Built Time Series & Regression models in Python/R, improving forecast accuracy by **20-30%**.
    - **ETL Automation:** Engineered automated pipelines (SQL/Python), reducing latency by **~40%**.
    - **Churn Analysis:** Developed customer segmentation models using TensorFlow/Scikit-learn (Performance +15%).
    """)

# --- JOB 3: USC ---
with st.container(border=True):
    st.markdown("#### **Business Data Analyst | USC Auxiliary Services**")
    st.markdown("Start: *Feb 2022 - May 2023*")
    st.markdown("""
    - **Dashboarding:** Built interactive Power BI/Excel dashboards that reduced manual reporting time by **~40%** and improved vendor tracking clarity.
    """)

# ======================
# 6. EDUCATION & CONTACT
# ======================
st.header("🎓 Education")
st.markdown("**M.S. Electrical & Computer Engineering** | University of Southern California (2023)")
st.markdown("**B.Tech. Electrical & Communication Engineering** | Gujarat Technological University (2021)")

st.write("---")
st.header("📬 Get in Touch")
st.write("Ready to build scalable AI solutions? Let's connect!")

contact_form = """
<form action="https://formsubmit.co/devanshipandya44@gmail.com" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your Name" required style="width: 100%; padding: 8px; margin-bottom: 10px; border: 1px solid #ccc; border-radius: 4px;">
     <input type="email" name="email" placeholder="Your Email" required style="width: 100%; padding: 8px; margin-bottom: 10px; border: 1px solid #ccc; border-radius: 4px;">
     <textarea name="message" placeholder="Your Message" required style="width: 100%; padding: 8px; margin-bottom: 10px; border: 1px solid #ccc; border-radius: 4px;"></textarea>
     <button type="submit" style="background-color: #4CAF50; color: white; padding: 10px 20px; border: none; border-radius: 4px; cursor: pointer;">Send Message</button>
</form>
"""
st.markdown(contact_form, unsafe_allow_html=True)