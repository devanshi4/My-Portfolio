import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_lottie import st_lottie
import requests

# ======================
# 1. CONFIGURATION
# ======================
st.set_page_config(page_title="Devanshi Pandya | Portfolio", page_icon="⚡", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# --- ASSETS ---
lottie_profile = load_lottieurl("https://assets4.lottiefiles.com/packages/lf20_3rwasyjy.json") # Woman Analyst
lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")  # Hero Animation
lottie_sql = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_5njp3vgg.json")    # SQL Robot
lottie_churn = load_lottieurl("https://assets7.lottiefiles.com/packages/lf20_hs5pkq.json")    # Moving Graph

# --- CSS STYLING ---
st.markdown("""
<style>
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
    # Profile Animation
    st_lottie(lottie_profile, height=200, key="profile")
    
    st.markdown("<h1 style='text-align: center;'>Devanshi Pandya</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: gray;'>📍 Los Angeles, CA</p>", unsafe_allow_html=True)
    st.markdown("---")
    
    # --- UNIFIED BUTTONS ---
    st.write("CONTACT & RESUME")
    
    # Resume Button
    try:
        with open("Devanshi_Pandya_Resume.pdf", "rb") as pdf_file:
            st.download_button(
                label="📄 Download Resume",
                data=pdf_file,
                file_name="Devanshi_Pandya_Resume.pdf",
                mime="application/pdf",
                use_container_width=True  # This makes it full width
            )
    except:
        st.warning("Resume file missing")

    # Social Buttons (Stacked to look consistent)
    st.link_button("LinkedIn Profile", "https://linkedin.com/in/YOUR_LINKEDIN", use_container_width=True)
    st.link_button("GitHub Profile", "https://github.com/devanshi4", use_container_width=True)

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
    I transform complex workflow logs into **strategic decisions** and **intelligent tools**. 
    Currently optimizing network operations at **Cloudify (Verizon)**, I specialize in modernizing legacy SQL 
    processes into **automated Python & AI-driven solutions**.
    """)
    st.markdown("""
    <span class="badge">Python</span>
    <span class="badge">Generative AI</span>
    <span class="badge">SQL</span>
    <span class="badge">Tableau</span>
    <span class="badge">A/B Testing</span>
    """, unsafe_allow_html=True)

with col2:
    st_lottie(lottie_coding, height=250, key="hero")

st.markdown("---")

# ======================
# 4. CAREER JOURNEY (Timeline)
# ======================
st.header("📅 My Career Journey")

# Updated Data with Internship
data = [
    dict(Task="Cloudify (Verizon)", Start='2024-08-01', Finish='2025-12-31', Resource='Current', Description="AI Integration & Network Analytics"),
    dict(Task="Brillio", Start='2023-09-01', Finish='2024-07-31', Resource='Past', Description="Predictive Analytics & ETL Automation"),
    dict(Task="Master's at USC", Start='2021-08-01', Finish='2023-05-30', Resource='Education', Description="M.S. Electrical & Computer Engineering"),
    dict(Task="USC Auxiliary", Start='2022-02-01', Finish='2023-05-01', Resource='Past', Description="Dashboarding & Supply Chain Analytics"),
    dict(Task="Verizon Internship", Start='2022-05-01', Finish='2022-08-30', Resource='Internship', Description="Churn Prediction & A/B Testing"),
]

df = pd.DataFrame(data)

fig = px.timeline(df, x_start="Start", x_end="Finish", y="Task", color="Resource", 
                  title="Professional Timeline (Hover for details)", height=350, hover_data=["Description"],
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
        st.link_button