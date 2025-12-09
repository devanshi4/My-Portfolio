import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_lottie import st_lottie
import requests
from PIL import Image

# ======================
# 1. CONFIG & SETTINGS
# ======================
st.set_page_config(
    page_title="Devanshi Pandya | Portfolio",
    page_icon="⚡",
    layout="wide"
)

# Function to load Lottie Animations
def load_lottieurl(url):
    try:
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()
    except:
        return None

# --- LOAD ASSETS (Working Links) ---
# 1. Hero: Woman Analyst (Dark hair, Laptop)
lottie_hero = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_qp1q7mct.json")
# Alternative Hero if above fails: "https://assets5.lottiefiles.com/packages/lf20_3rwasyjy.json"

# 2. SQL Project: Robot
lottie_sql = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_5njp3vgg.json")

# 3. Churn Project: Moving Graph
lottie_churn = load_lottieurl("https://assets3.lottiefiles.com/packages/lf20_qp1q7mct.json")

# Custom CSS for clean buttons and badges
st.markdown("""
<style>
    .main { background-color: #f5f7fa; }
    .badge {
        background-color: #ff4b4b;
        color: white;
        padding: 4px 8px;
        border-radius: 4px;
        font-size: 12px;
        margin-right: 5px;
    }
    div.stButton > button { width: 100%; }
</style>
""", unsafe_allow_html=True)

# ======================
# 2. SIDEBAR
# ======================
with st.sidebar:
    # Profile Pic
    try:
        image = Image.open("profile_pic.png")
        st.image(image, width=220)
    except:
        st.header("👩‍💻")

    st.markdown("<h1>Devanshi Pandya</h1>", unsafe_allow_html=True)
    st.markdown("<p style='color: gray;'>📍 NYC, New York</p>", unsafe_allow_html=True)
    
    st.markdown("---")
    st.write("**RESUME & SOCIALS**")
    
    # Resume Button
    try:
        with open("Devanshi_Pandya_Resume.pdf", "rb") as pdf_file:
            st.download_button(
                label="📄 Download Resume",
                data=pdf_file,
                file_name="Devanshi_Pandya_Resume.pdf",
                mime="application/pdf"
            )
    except:
        st.warning("Resume file missing")

    st.link_button("LinkedIn", "https://linkedin.com/in/YOUR_LINKEDIN")
    st.link_button("GitHub", "https://github.com/devanshi4")

    # Skills
    st.markdown("---")
    st.write("**Core Skills**")
    st.caption("Python & SQL")
    st.progress(95)
    st.caption("Machine Learning")
    st.progress(80)
    st.caption("Generative AI")
    st.progress(75)

# ======================
# 3. HERO SECTION
# ======================
col1, col2 = st.columns([2, 1])

with col1:
    st.title("Hi, I'm Devanshi! 👋")
    st.markdown("### 🚀 Data Scientist | GenAI Builder | Analyst")
    st.write("""
    I transform messy data into **strategic decisions** and **intelligent tools**. 
    Currently optimizing network operations at **Verizon**, I specialize in replacing manual workflows 
    with **AI-driven pipelines** and **predictive models**.
    """)
    st.markdown("""
    <span class="badge">Python</span>
    <span class="badge">Generative AI</span>
    <span class="badge">SQL</span>
    <span class="badge">Tableau</span>
    <span class="badge">A/B Testing</span>
    """, unsafe_allow_html=True)

with col2:
    # Hero Animation
    if lottie_hero:
        st_lottie(lottie_hero, height=250, key="hero_anim")

st.markdown("---")

# ======================
# 4. CAREER JOURNEY
# ======================
st.header("📅 My Career Journey")

data = [
    dict(Task="Cloudify (Verizon)", Start='2024-08-01', Finish='2025-12-31', Resource='Current', 
         Description="AI Integration, SQL Pipelines"),
    dict(Task="Brillio", Start='2023-09-01', Finish='2024-07-31', Resource='Past', 
         Description="Predictive Models, ETL Automation"),
    dict(Task="Verizon Internship", Start='2022-05-01', Finish='2022-08-30', Resource='Internship', 
         Description="Churn Prediction (18% lift), A/B Testing"),
    dict(Task="USC Auxiliary", Start='2022-02-01', Finish='2023-05-01', Resource='Past', 
         Description="Dashboarding, Supply Chain Analytics"),
    dict(Task="Master's at USC", Start='2021-08-01', Finish='2023-05-30', Resource='Education', 
         Description="M.S. Electrical & Computer Engineering"),
]
df = pd.DataFrame(data)

fig = px.timeline(df, x_start="Start", x_end="Finish", y="Task", color="Resource", 
                  title="Professional Timeline (Hover for details)", height=350,
                  hover_data=["Description"],
                  color_discrete_map={'Current': '#ff4b4b', 'Past': '#2d2d2d', 'Internship': '#ffa500', 'Education': '#1f77b4'})
fig.update_yaxes(autorange="reversed")
st.plotly_chart(fig, use_container_width=True)

# ======================
# 5. PROJECTS
# ======================
st.header("💻 What I've Built")
col_p1, col_p2 = st.columns(2)

with col_p1:
    with st.container(border=True):
        st.subheader("🤖 AI SQL Assistant")
        if lottie_sql:
            st_lottie(lottie_sql, height=150, key="sql_anim")
        st.markdown("**Tech:** LangChain, OpenAI, PostgreSQL")
        st.write("A GenAI tool that lets non-technical users query databases in plain English.")
        st.link_button("View Code", "https://github.com/devanshi4/sql-ai-assistant")

with col_p2:
    with st.container(border=True):
        st.subheader("📉 Churn Predictor")
        if lottie_churn:
            st_lottie(lottie_churn, height=150, key="churn_anim")
        st.markdown("**Tech:** XGBoost, SHAP, Streamlit")
        st.write("An ML dashboard predicting customer risk with 79% accuracy & Explainable AI.")
        st.link_button("View Code", "https://github.com/devanshi4/Churn-Prediction")

# ======================
# 6. DETAILED EXPERIENCE
# ======================
st.markdown("---")
st.header("📝 Detailed Experience")

tab1, tab2, tab3, tab4 = st.tabs(["Verizon (Current)", "Brillio", "Verizon Internship", "USC"])

with tab1:
    st.subheader("Data Analyst | Cloudify Technologies (Contracted to Verizon)")
    st.caption("August 2024 - Present")
    st.markdown("""
    - **AI Modernization:** Replaced a static 450-line SQL script with an **AI-assisted Python pipeline**, using GenAI to parse complex JSON logs.
    - **Operational Efficiency:** Analyzed orchestration logs to build cycle-time models, reducing troubleshooting time by **~40%**.
    - **Data Engineering:** Developed SQL pipelines to validate network deployment metrics across thousands of sites (Accuracy +55%).
    """)

with tab2:
    st.subheader("Data Analyst | Brillio")
    st.caption("September 2023 - July 2024")
    st.markdown("""
    - **Predictive Modeling:** Built Time Series & Regression models in Python/R, improving forecast accuracy by **20-30%**.
    - **ETL Automation:** Engineered automated pipelines (SQL/Python), reducing latency by **~40%**.
    - **Churn Analysis:** Developed customer segmentation models using TensorFlow/Scikit-learn (Performance +15%).
    """)

with tab3:
    st.subheader("Data Analyst Intern | Verizon")
    st.caption("May 2022 - August 2022")
    st.markdown("""
    - **Predictive Modeling:** Enhanced customer churn prediction models, improving accuracy by **18%** to support targeted retention campaigns.
    - **Customer Segmentation:** Applied unsupervised learning techniques (**K-means, DBSCAN**) to cluster user bases.
    - **A/B Testing:** Designed and executed statistical experiments (A/B tests) to evaluate the impact of new product features.
    - **Strategic Insights:** Translated complex clustering and churn findings into actionable insights for non-technical stakeholders.
    """)

with tab4:
    st.subheader("Business Data Analyst | USC Auxiliary Services")
    st.caption("February 2022 - May 2023")
    st.markdown("""
    - **Dashboarding:** Built interactive Power BI/Excel dashboards that reduced manual reporting time by **~40%**.
    - **Supply Chain:** Optimized inventory tracking for high-volume dining operations.
    """)

# ======================
# 7. CONTACT
# ======================
st.markdown("---")
st.header("📬 Let's Connect")
contact_form = """
<form action="https://formsubmit.co/devanshipandya44@gmail.com" method="POST">
     <input type="text" name="name" placeholder="Your Name" required style="width: 100%; padding: 10px; border-radius: 5px; border: 1px solid #ccc; margin-bottom:10px;">
     <input type="email" name="email" placeholder="Your Email" required style="width: 100%; padding: 10px; border-radius: 5px; border: 1px solid #ccc; margin-bottom:10px;">
     <textarea name="message" placeholder="Your Message" required style="width: 100%; padding: 10px; border-radius: 5px; border: 1px solid #ccc; margin-bottom:10px;"></textarea>
     <button type="submit" style="background-color: #ff4b4b; color: white; padding: 10px 20px; border: none; border-radius: 5px; cursor: pointer;">Send Message</button>
</form>
"""
st.markdown(contact_form, unsafe_allow_html=True)