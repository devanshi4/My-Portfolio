import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_lottie import st_lottie
import requests

# ======================
# 1. CONFIGURATION
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

# --- ASSETS (UPDATED TO WOMAN) ---
# 1. Hero Animation: Woman Analyst with Dark Hair working on laptop
lottie_coding = load_lottieurl("https://lottie.host/6a5ff966-2244-448d-b08e-59174dfb2049/23E4C3bT36.json")
# Alternate if above fails: "https://assets5.lottiefiles.com/packages/lf20_3rwasyjy.json"

# 2. Profile Avatar: Woman Waving
lottie_profile = load_lottieurl("https://lottie.host/020059c3-cd6d-4956-b072-f112c2288330/509Wb8dY6u.json")

# 3. Project Animations
lottie_sql = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_5njp3vgg.json")
lottie_churn = load_lottieurl("https://assets7.lottiefiles.com/packages/lf20_hs5pkq.json")

# --- CSS STYLING (REMOVED DARK SIDEBAR TO FIX BUTTONS) ---
st.markdown("""
<style>
    /* Make badges look like pills */
    .badge {
        background-color: #ff4b4b;
        color: white;
        padding: 4px 8px;
        border-radius: 4px;
        font-size: 12px;
        margin-right: 5px;
    }
    /* Fix button width to ensure uniformity */
    div.stButton > button {
        width: 100%;
    }
</style>
""", unsafe_allow_html=True)

# ======================
# 2. SIDEBAR
# ======================
with st.sidebar:
    # Profile Animation
    st_lottie(lottie_profile, height=180, key="profile_anim")
    
    st.markdown("<h1 style='text-align: center;'>Devanshi Pandya</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: gray;'>📍 NYC, New York</p>", unsafe_allow_html=True)
    st.markdown("---")
    
    st.write("CONTACT & RESUME")
    
    # 1. Resume Button
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

    # 2. Social Buttons
    st.link_button("LinkedIn Profile", "https://linkedin.com/in/YOUR_LINKEDIN")
    st.link_button("GitHub Profile", "https://github.com/devanshi4")

    # --- SKILLS ---
    st.markdown("---")
    st.write("**Core Skills**")
    st.caption("Python & SQL")
    st.progress(95)
    st.caption("Machine Learning")
    st.progress(85)
    st.caption("Generative AI")
    st.progress(80)

# ======================
# 3. HERO SECTION
# ======================
col1, col2 = st.columns([2, 1])

with col1:
    st.title("Hi, I'm Devanshi! 👋")
    st.markdown("### 🚀 Data Scientist | GenAI Builder | Analyst")
    st.write("""
    I transform messy data into **strategic decisions** and **intelligent tools**. 
    Currently optimizing network operations at **Cloudify (Verizon)**, I specialize in replacing manual workflows 
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
    # This is the Woman Analyst Animation
    st_lottie(lottie_coding, height=250, key="hero_anim")

st.markdown("---")

# ======================
# 4. CAREER JOURNEY (Timeline)
# ======================
st.header("📅 My Career Journey")

# Data with Tooltip Descriptions
data = [
    dict(Task="Cloudify (Verizon)", Start='2024-08-01', Finish='2025-12-31', Resource='Current', 
         Description="AI Integration, Cycle-Time Models, SQL Pipelines"),
    dict(Task="Brillio", Start='2023-09-01', Finish='2024-07-31', Resource='Past', 
         Description="Predictive Models (20-30% lift), ETL Automation"),
    dict(Task="Master's at USC", Start='2021-08-01', Finish='2023-05-30', Resource='Education', 
         Description="M.S. Electrical & Computer Engineering"),
    dict(Task="USC Auxiliary", Start='2022-02-01', Finish='2023-05-01', Resource='Past', 
         Description="Dashboarding (40% faster), Supply Chain Analytics"),
    dict(Task="Verizon Internship", Start='2022-05-01', Finish='2022-08-30', Resource='Internship', 
         Description="Churn Prediction (18% lift), A/B Testing, Clustering"),
]

df = pd.DataFrame(data)

# Gantt Chart
fig = px.timeline(df, x_start="Start", x_end="Finish", y="Task", color="Resource", 
                  title="Professional Timeline (Hover bars for details)", height=350, 
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
        st_lottie(lottie_sql, height=150, key="sql_anim")
        st.markdown("**Tech:** LangChain, OpenAI, PostgreSQL")
        st.write("A GenAI tool that lets non-technical users query databases in plain English.")
        st.link_button("View Code", "https://github.com/devanshi4/sql-ai-assistant", use_container_width=True)

with col_p2:
    with st.container(border=True):
        st.subheader("📉 Churn Predictor")
        st_lottie(lottie_churn, height=150, key="churn_anim")
        st.markdown("**Tech:** XGBoost, SHAP, Streamlit")
        st.write("An ML dashboard predicting customer risk with 79% accuracy & Explainable AI.")
        st.link_button("View Code", "https://github.com/devanshi4/Churn-Prediction", use_container_width=True)

# ======================
# 6. DETAILED EXPERIENCE (Tabs)
# ======================
st.markdown("---")
st.header("📝 Detailed Experience")

tab1, tab2, tab3, tab4 = st.tabs(["Cloudify (Verizon)", "Brillio", "USC Auxiliary", "Verizon Intern"])

with tab1:
    st.subheader("Data Analyst | Cloudify Technologies (Contracted to Verizon)")
    st.caption("August 2024 - Present | Remote, USA")
    st.markdown("""
    - **AI Modernization:** Replaced a static 450-line SQL script with an **AI-assisted Python pipeline**, using GenAI to parse complex JSON logs.
    - **Operational Efficiency:** Analyzed workflow logs to build cycle-time models, identifying bottlenecks that reduced troubleshooting time by **~40%**.
    - **Data Engineering:** Developed SQL pipelines to validate network deployment metrics across thousands of sites (Accuracy +55%).
    - **Dashboarding:** Designed the team's central reporting suite (**Tableau, Looker**) to provide real-time visibility into KPI performance for leadership.
    """)

with tab2:
    st.subheader("Data Analyst | Brillio")
    st.caption("September 2023 - July 2024 | Tampa, FL")
    st.markdown("""
    - **Predictive Analytics:** Developed Time Series and Regression models in Python and R to forecast marketing trends, achieving a **20-30% improvement** in forecast accuracy.
    - **ETL Automation:** Engineered automated pipelines using SQL and Python, reducing data processing latency by **~40%** to ensure timely executive reporting.
    - **Customer Retention:** Designed customer segmentation and churn prediction models using **TensorFlow and Scikit-learn**, enabling targeted retention strategies for high-risk segments (performance boost ~15%).
    """)

with tab3:
    st.subheader("Business Data Analyst | USC Auxiliary Services")
    st.caption("February 2022 - May 2023 | Los Angeles, CA")
    st.markdown("""
    - **Dashboard Development:** Transformed manual, paper-based tracking into dynamic **Power BI and Excel dashboards**, reducing reporting turnaround time by **~40%**.
    - **Process Optimization:** Streamlined the end-to-end order-to-payment workflow by coordinating with cross-functional teams, resolving data discrepancies in receipt and payment tracking.
    - **Supply Chain Analytics:** Managed large-scale vendor data to optimize inventory levels across multiple locations, ensuring timely deliveries and minimizing stock variances.
    """)

with tab4:
    st.subheader("Data Analyst Intern | Verizon")
    st.caption("May 2022 - August 2022 | Remote")
    st.markdown("""
    - **Predictive Modeling:** Enhanced customer churn prediction models, improving accuracy by **18%** to support targeted retention campaigns and reduce attrition.
    - **Customer Segmentation:** Applied unsupervised learning techniques (**K-means, DBSCAN**) to cluster user bases, creating actionable segments for personalized marketing.
    - **A/B Testing:** Designed and executed statistical experiments (A/B tests) to evaluate the impact of new product features and service changes on user engagement.
    - **Strategic Communication:** Translated complex clustering and churn findings into actionable insights for non-technical stakeholders.
    """)

# ======================
# 7. CONTACT
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