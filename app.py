

Devanshi_Pandya_Resume.pdf

import streamlit as st
from PIL import Image

# ======================
# PAGE CONFIG
# ======================
st.set_page_config(page_title="Devanshi Pandya | Data Scientist", page_icon="👩‍💻", layout="wide")

# ======================
# SIDEBAR
# ======================
with st.sidebar:
    try:
        # Replace with your actual image file
        image = Image.open("profile_pic.png")
        st.image(image, width=250)
    except:
        st.write("*(Add a profile_pic.png to your folder)*")
    
    st.markdown("### Devanshi Pandya")
    st.write("📍 NYC, New York")
    st.write("📧 devanshipandya44@gmail.com")
    
    # Download Resume Button
    with open("Devanshi_Pandya_Resume.pdf", "rb") as pdf_file:
        PDFbyte = pdf_file.read()
    
    st.download_button(
        label="📄 Download Resume",
        data=PDFbyte,
        file_name="Devanshi_Resume.pdf",
        mime="application/octet-stream",
    )
    
    st.markdown("---")
    st.write("**Skills:** Python, SQL, Machine Learning, GenAI, Tableau")

# ======================
# MAIN PAGE - HERO SECTION
# ======================
st.title("Hi, I'm Devanshi! 👋")
st.subheader("Data Scientist | GenAI Enthusiast | Problem Solver")

st.markdown("""
I bridge the gap between **raw data** and **strategic decisions**. 
With a background in Electrical Engineering (USC) and expertise in **Machine Learning**, 
I build tools that predict what happens next and explain *why*.
""")

st.markdown("---")

# ======================
# PROJECTS SECTION
# ======================
st.header("💻 Interactive Projects")
st.write("Don't just take my word for it—**play with the tools I built:**")

col1, col2 = st.columns(2)

# --- PROJECT 1 ---
with col1:
    st.info("🤖 **AI-Powered SQL Assistant**")
    st.write("A GenAI tool that lets you talk to your database in plain English.")
    st.markdown("**Tech:** LangChain, OpenAI, PostgreSQL")
    
    # Link to your deployed Streamlit app (We will get this URL later)
    if st.button("Launch SQL Assistant 🚀"):
        st.markdown("[Click here to open App](https://github.com/devanshi4/sql-ai-assistant)", unsafe_allow_html=True)
    
    with st.expander("See Key Features"):
        st.write("- Translates Natural Language to SQL")
        st.write("- Handles Multi-table Joins")
        st.write("- Auto-corrects SQL errors")

# --- PROJECT 2 ---
with col2:
    st.success("📉 **Customer Churn Predictor**")
    st.write("An ML dashboard that predicts customer risk with 79% accuracy.")
    st.markdown("**Tech:** XGBoost, SHAP, Streamlit")
    
    # Link to your deployed Streamlit app (We will get this URL later)
    if st.button("Launch Churn Predictor 🔮"):
        st.markdown("[Click here to open App](https://github.com/devanshi4/Churn-Prediction)", unsafe_allow_html=True)

    with st.expander("See Key Features"):
        st.write("- Interactive Risk Calculator")
        st.write("- Explainable AI (SHAP Plots)")
        st.write("- Real-time scenario planning")

st.markdown("---")

# ======================
# EXPERIENCE TIMELINE
# ======================
st.header("📚 Experience & Education")

st.markdown("##### 💼 **Data Analyst | Cloudify (Verizon)**")
st.caption("July 2024 - Present")
st.write("Building AI-assisted pipelines to automate error detection in network logs.")

st.markdown("##### 💼 **Data Analyst | Brillio**")
st.caption("Sept 2023 - June 2024")
st.write("Developed predictive models for marketing trends and customer retention.")

st.markdown("##### 🎓 **M.S. Electrical Engineering | USC**")
st.caption("Class of 2023")

# ======================
# CONTACT FORM (Simple)
# ======================
st.markdown("---")
st.header("📬 Get In Touch")

contact_form = """
<form action="https://formsubmit.co/devanshipandya44@gmail.com" method="POST">
     <input type="text" name="name" placeholder="Your Name" required>
     <input type="email" name="email" placeholder="Your Email" required>
     <textarea name="message" placeholder="Your Message here"></textarea>
     <button type="submit">Send</button>
</form>
"""
st.markdown(contact_form, unsafe_allow_html=True)