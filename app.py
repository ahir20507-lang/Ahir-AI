import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Ahir-AI", layout="centered")
st.title("🤖 Ahir-AI Studio")

api_key = st.sidebar.text_input("Gemini API Key:", type="password")

if not api_key:
    st.info("ડાબી બાજુ API Key નાખો.")
    st.stop()

genai.configure(api_key=api_key)

user_prompt = st.text_area("તમારો પ્રશ્ન પૂછો:")
if st.button("મોકલો"):
    if user_prompt:
        with st.spinner("જવાબ વિચારી રહ્યો છું..."):
            try:
                model = genai.GenerativeModel("models/gemini-3.8-flash")
                res = model.generate_content(user_prompt)
                st.markdown(res.text)
            except Exception as e:
                st.error(f"એરર: {e}")
