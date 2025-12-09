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
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# --- LOAD ASSETS ---
# 1. Hero Animation: CHANGED TO WOMAN ANALYST
lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_3rwasyjy.json")

# 2. SQL Project Animation
lottie_data = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_5njp3vgg.json")

# Custom CSS for a cleaner look
st.markdown("""
<style>
    .main {
        background-color: #f5f7fa; 
    }
    [data-testid="stSidebar"] {
        background-color: #2b303b;
        color: white;
    }
    h1, h2, h3 {
        color: #2b303b;
    }
    .metric-card {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
    }
</style>
""", unsafe_allow_html=True)

# ======================
# 2. SIDEBAR (Dark Themed)
# ======================
with st.sidebar:
    try:
        image = Image.open("profile_pic.png")
        st.image(image, width=220)
    except:
        st.header("👩‍💻")

    st.markdown("<h1 style='color: white;'>Devanshi Pandya</h1>", unsafe_allow_html=True)
    st.markdown("<p style='color: #dcdcdc;'>📍 NYC, New York</p>", unsafe_allow_html=True)
    
    # Resume Download Button
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

    st.markdown("---")
    st.markdown("<h3 style='color: white;'>Connect</h3>", unsafe_allow_html=True)
    st.link_button("LinkedIn", "https://linkedin.com/in/YOUR_LINKEDIN")
    st.link_button("GitHub", "https://github.com/devanshi4")

    # Skill Meters
    st.markdown("---")
    st.markdown("<h3 style='color: white;'>Core Skills</h3>", unsafe_allow_html=True)
    st.write("Python & SQL")
    st.progress(90)
    st.write("Machine Learning")
    st.progress(80)
    st.write("Generative AI")
    st.progress(75)
    st.write("Data Visualization")
    st.progress(85)

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
    st.info("**Current Focus:** Leveraging LLMs (LangChain) to automate SQL queries & building Explainable AI models.")

with col2:
    # This key ensures the animation reloads correctly
    st_lottie(lottie_coding, height=250, key="woman_analyst")

st.markdown("---")

# ======================
# 4. INTERACTIVE CAREER TIMELINE
# ======================
st.header("📅 My Career Journey")

# Creating the Timeline Data
data = [
    dict(Task="Master's at USC", Start='2021-08-01', Finish='2023-05-30', Resource='Education'),
    dict(Task="USC Auxiliary Services", Start='2022-02-01', Finish='2023-05-01', Resource='Work'),
    dict(Task="Brillio", Start='2023-09-01', Finish='2024-06-30', Resource='Work'),
    dict(Task="Cloudify (Verizon)", Start='2024-07-01', Finish='2025-12-31', Resource='Work') # Ongoing
]
df = pd.DataFrame(data)

# Creating the Gantt Chart using Plotly
fig = px.timeline(df, x_start="Start", x_end="Finish", y="Task", color="Resource", 
                  title="Experience Timeline", height=300,
                  color_discrete_map={'Work': '#ff4b4b', 'Education': '#1f77b4'})

fig.update_yaxes(autorange="reversed") # Verify visual alignment
st.plotly_chart(fig, use_container_width=True)

# ======================
# 5. PROJECT SHOWCASE (Interactive Cards)
# ======================
st.header("💻 What I've Built")
st.write("Click the links to explore the code or demo.")

col_p1, col_p2 = st.columns(2)

with col_p1:
    with st.container():
        st.subheader("🤖 AI SQL Assistant")
        st_lottie(lottie_data, height=150, key="data")
        st.markdown("**Tech:** LangChain, OpenAI, PostgreSQL")
        st.markdown("A GenAI tool that lets non-technical users query databases in plain English.")
        st.link_button("View Code", "https://github.com/devanshi4/sql-ai-assistant")

with col_p2:
    with st.container():
        st.subheader("📉 Churn Predictor")
        st.markdown("**Tech:** XGBoost, SHAP, Streamlit")
        st.markdown("An ML dashboard predicting customer risk with 79% accuracy & Explainable AI.")
        st.link_button("View Code", "https://github.com/devanshi4/Churn-Prediction")

# ======================
# 6. DETAILED EXPERIENCE
# ======================
st.markdown("---")
st.header("📝 Detailed Experience")

tab1, tab2, tab3 = st.tabs(["Verizon (Current)", "Brillio", "USC"])

with tab1:
    st.subheader("Data Analyst | Cloudify Technologies (Contracted to Verizon)")
    st.markdown("""
    - **AI Modernization:** Replaced a static 450-line SQL script with an **AI-assisted Python pipeline**, using GenAI to parse complex JSON logs.
    - **Operational Efficiency:** Analyzed orchestration logs to build cycle-time models, reducing troubleshooting time by **~40%**.
    - **Data Engineering:** Developed SQL pipelines to validate network deployment metrics across thousands of sites (Accuracy +55%).
    """)

with tab2:
    st.subheader("Data Analyst | Brillio")
    st.markdown("""
    - **Predictive Modeling:** Built Time Series & Regression models in Python/R, improving forecast accuracy by **20-30%**.
    - **ETL Automation:** Engineered automated pipelines (SQL/Python), reducing latency by **~40%**.
    - **Churn Analysis:** Developed customer segmentation models using TensorFlow/Scikit-learn (Performance +15%).
    """)

with tab3:
    st.subheader("Business Data Analyst | USC Auxiliary Services")
    st.markdown("""
    - **Dashboarding:** Built interactive Power BI/Excel dashboards that reduced manual reporting time by **~40%**.
    - **Supply Chain:** Optimized inventory tracking for high-volume dining operations.
    """)

# ======================
# 7. CONTACT FORM
# ======================
st.markdown("---")
st.header("📬 Let's Connect")

contact_form = """
<form action="https://formsubmit.co/devanshipandya44@gmail.com" method="POST">
     <input type="text" name="name" placeholder="Your Name" required style="width: 100%; padding: 10px; margin-bottom: 10px; border-radius: 5px; border: 1px solid #ccc;">
     <input type="email" name="email" placeholder="Your Email" required style="width: 100%; padding: 10px; margin-bottom: 10px; border-radius: 5px; border: 1px solid #ccc;">
     <textarea name="message" placeholder="Your Message" required style="width: 100%; padding: 10px; margin-bottom: 10px; border-radius: 5px; border: 1px solid #ccc;"></textarea>
     <button type="submit" style="background-color: #ff4b4b; color: white; padding: 10px 20px; border: none; border-radius: 5px; cursor: pointer;">Send Message</button>
</form>
"""
st.markdown(contact_form, unsafe_allow_html=True)