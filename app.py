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
# 1. Profile: Woman Analyst with dark hair working on data
lottie_profile = load_lottieurl("https://assets4.lottiefiles.com/packages/lf20_3rwasyjy.json")
# 2. Hero: Coding/Data
lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")
# 3. Project: SQL (Robot/AI)
lottie_ai = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_5njp3vgg.json")
# 4. Project: Churn (Moving Graph/Analytics)
lottie_graph = load_lottieurl("https://assets7.lottiefiles.com/packages/lf20_hs5pkq.json")

# Custom CSS for styling
st.markdown("""
<style>
    .main { background-color: #f5f7fa; }
    h1, h2, h3 { color: #2b303b; }
    /* Style for the badge pills */
    .badge {
        background-color: #ff4b4b;
        color: white;
        padding: 4px 8px;
        border-radius: 4px;
        font-size: 12px;
        margin-right: 5px;
    }
</style>
""", unsafe_allow_html=True)

# ======================
# 2. SIDEBAR
# ======================
with st.sidebar:
    # Use the Lottie Animation for the profile picture (Woman Analyst)
    st_lottie(lottie_profile, height=200, key="profile")

    st.markdown("<h1 style='text-align: center;'>Devanshi Pandya</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: gray;'>📍 Los Angeles, CA</p>", unsafe_allow_html=True)
    
    st.markdown("---")
    
    # --- UNIFIED BUTTON SECTION ---
    # We use columns to make the buttons look uniform
    st.write("**Resume & Socials**")
    
    # 1. Download Resume Button
    try:
        with open("Devanshi_Pandya_Resume.pdf", "rb") as pdf_file:
            st.download_button(
                label="📄 Download Resume",
                data=pdf_file,
                file_name="Devanshi_Pandya_Resume.pdf",
                mime="application/pdf",
                use_container_width=True
            )
    except:
        st.warning("Resume file missing in folder")

    # 2. Social Links (Side by Side)
    col_s1, col_s2 = st.columns(2)
    with col_s1:
        st.link_button("LinkedIn", "https://linkedin.com/in/YOUR_LINKEDIN", use_container_width=True)
    with col_s2:
        st.link_button("GitHub", "https://github.com/devanshi4", use_container_width=True)

    # --- SKILLS ---
    st.markdown("---")
    st.markdown("### Core Skills")
    
    st.write("Python & SQL")
    st.progress(95)
    
    st.write("Machine Learning (XGBoost/Scikit)")
    st.progress(85)
    
    st.write("Generative AI (LangChain)")
    st.progress(80)
    
    st.write("Predictive Modeling")
    st.progress(90)
    
    st.write("Tableau & Power BI")
    st.progress(85)

# ======================
# 3. HERO SECTION
# ======================
col1, col2 = st.columns([2, 1])

with col1:
    st.title("Hi, I'm Devanshi! 👋")
    st.markdown("### 🚀 Data Scientist | GenAI Builder | Analyst")
    st.write("""
    I transform complex workflow logs into **strategic decisions** and **intelligent tools**. 
    Currently optimizing network operations at **Cloudify (Verizon)**, I specialize in modernizing legacy SQL 
    processes into **automated Python & AI-driven solutions**.
    """)
    
    # Tech Stack Badges
    st.markdown("""
    <span class="badge">Python</span>
    <span class="badge">Generative AI</span>
    <span class="badge">SQL</span>
    <span class="badge">A/B Testing</span>
    <span class="badge">Time Series</span>
    <span class="badge">Tableau</span>
    """, unsafe_allow_html=True)

with col2:
    st_lottie(lottie_coding, height=250, key="hero_anim")

st.markdown("---")

# ======================
# 4. INTERACTIVE CAREER TIMELINE (UPDATED)
# ======================
st.header("📅 My Career Journey")

# Timeline Data (Updated with correct dates & Descriptions for Hover)
data = [
    dict(Task="Cloudify (Verizon)", Start='2024-08-01', Finish='2025-12-31', Resource='Current Role', 
         Description="AI Integration, Network Analytics, Cycle-Time Models"),
    
    dict(Task="Brillio", Start='2023-09-01', Finish='2024-07-31', Resource='Experience', 
         Description="Predictive Analytics, ETL Automation, Churn Modeling"),
    
    dict(Task="Master's at USC", Start='2021-08-01', Finish='2023-05-30', Resource='Education', 
         Description="M.S. Electrical & Computer Engineering"),
    
    dict(Task="USC Auxiliary Services", Start='2022-02-01', Finish='2023-05-01', Resource='Experience', 
         Description="Dashboarding, Supply Chain Analytics"),
    
    dict(Task="Verizon Internship", Start='2022-05-01', Finish='2022-08-30', Resource='Internship', 
         Description="Churn Prediction, A/B Testing, Clustering"),
]

df = pd.DataFrame(data)

# Gantt Chart
fig = px.timeline(df, x_start="Start", x_end="Finish", y="Task", color="Resource", 
                  title="Professional Timeline (Hover for details)", height=350,
                  hover_data=["Description"], # This makes the description pop up!
                  color_discrete_map={'Current Role': '#ff4b4b', 'Experience': '#2d2d2d', 'Internship': '#ffa500', 'Education': '#1f77b4'})

fig.update_yaxes(autorange="reversed")
st.plotly_chart(fig, use_container_width=True)

# ======================
# 5. PROJECT SHOWCASE (Updated Animations)
# ======================
st.header("💻 What I've Built")

col_p1, col_p2 = st.columns(2)

# Project 1
with col_p1:
    with st.container(border=True):
        st.subheader("🤖 AI SQL Assistant")
        st_lottie(lottie_ai, height=150, key="ai_anim")
        st.markdown("**Tech:** LangChain, OpenAI, PostgreSQL")
        st.markdown("A GenAI tool that lets non-technical users query databases in plain English.")
        st.link_button("View Code", "https://github.com/devanshi4/sql-ai-assistant", use_container_width=True)

# Project 2
with col_p2:
    with st.container(border=True):
        st.subheader("📉 Churn Predictor")
        st_lottie(lottie_graph, height=150, key="graph_anim") # NEW ANIMATION HERE
        st.markdown("**Tech:** XGBoost, SHAP, Streamlit")
        st.markdown("An ML dashboard predicting customer risk with 79% accuracy & Explainable AI.")
        st.link_button("View Code", "https://github.com/devanshi4/Churn-Prediction", use_container_width=True)

# ======================
# 6. DETAILED EXPERIENCE (4 TABS)
# ======================
st.markdown("---")
st.header("📝 Detailed Experience")

tab1, tab2, tab3, tab4 = st.tabs(["Cloudify (Verizon)", "Brillio", "USC Auxiliary", "Verizon Intern"])

with tab1:
    st.subheader("Data Analyst | Cloudify (Contracted to Verizon)")
    st.caption("August 2024 - Present | Los Angeles, CA")
    st.markdown("""
    My role sits at the intersection of **Data Engineering** and **Analytics**, modernizing legacy SQL processes into automated Python & AI-driven solutions.
    
    - 🚀 **AI Integration:** Led a modernization initiative to replace static, maintenance-heavy SQL scripts (450+ lines) with an **AI-assisted Python pipeline**, using GenAI to dynamically parse complex JSON event streams.
    - 📊 **Operational Intelligence:** Analyzed workflow logs to build cycle-time models, identifying bottlenecks that reduced troubleshooting time by **~40%**.
    - 🛠 **Data Engineering:** Developed SQL pipelines to validate network deployment metrics across thousands of sites, improving version tracking accuracy by **~55%**.
    - 📈 **Dashboarding:** Designed the team's central reporting suite (**Tableau, Looker**) to provide real-time visibility into KPI performance.
    """)

with tab2:
    st.subheader("Data Analyst | Brillio")
    st.caption("Sept 2023 - July 2024 | Tampa, FL")
    st.markdown("""
    Partnered with cross-functional teams to move the organization from descriptive reporting to **predictive modeling**.
    
    - 🔮 **Predictive Analytics:** Developed Time Series and Regression models in Python/R to forecast marketing trends (**20-30% accuracy lift**).
    - ⚙️ **ETL Automation:** Engineered automated pipelines (SQL/Python), reducing data processing latency by **~40%**.
    - 📉 **Customer Retention:** Designed customer segmentation and churn prediction models using **TensorFlow/Scikit-learn** (Performance boost ~15%).
    """)

with tab3:
    st.subheader("Business Data Analyst | USC Auxiliary Services")
    st.caption("Feb 2022 - May 2023 | Los Angeles, CA")
    st.markdown("""
    Oversaw inventory analytics for the university's high-volume dining operations, digitizing manual workflows.
    
    - 📊 **Dashboard Development:** Transformed manual tracking into dynamic **Power BI/Excel dashboards**, reducing reporting time by **~40%**.
    - 🔄 **Process Optimization:** Streamlined order-to-payment workflows, resolving data discrepancies in receipt tracking.
    - 📦 **Supply Chain Analytics:** Managed large-scale vendor data to optimize inventory levels and minimize stock variances.
    """)

with tab4:
    st.subheader("Data Analyst Intern | Verizon")
    st.caption("May 2022 - Aug 2022 | Remote")
    st.markdown("""
    Leveraged Machine Learning to drive customer retention strategies and optimize marketing effectiveness.
    
    - 📉 **Predictive Modeling:** Enhanced customer churn prediction models, improving accuracy by **18%** to support targeted retention.
    - 🎯 **Customer Segmentation:** Applied unsupervised learning (**K-means, DBSCAN**) to cluster user bases for personalized marketing.
    - 🧪 **A/B Testing:** Designed statistical experiments to evaluate new product features on user engagement.
    - 🐍 **Data Pipelines:** Utilized Python and SQL for end-to-end data extraction and cleaning.
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