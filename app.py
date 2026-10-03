import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Ahir-AI", layout="centered")
st.title("🤖 Ahir-AI Studio")

api_key = st.sidebar.text_input("Gemini API Key:", type="password")

if not api_key:
    st.info("ડાબી બાજુ API Key નાખો.")
    st.stop()

genai.configure(api_key=api_key)

# કયા મોડેલ અવેલેબલ છે તે ચેક કરો
try:
    available_models = [
        m.name for m in genai.list_models() 
        if 'generateContent' in m.supported_generation_methods
    ]
    st.sidebar.write("તમારા ખાતામાં ઉપલબ્ધ મોડેલ:")
    selected_model = st.sidebar.selectbox("મોડેલ પસંદ કરો", available_models)
except Exception as e:
    st.sidebar.error(f"કી ચેક કરવામાં એરર: {e}")
    selected_model = None

user_prompt = st.text_area("તમારો પ્રશ્ન પૂછો:")
if st.button("મોકલો"):
    if user_prompt and selected_model:
        with st.spinner("જવાબ વિચારી રહ્યો છું..."):
            try:
                model = genai.GenerativeModel(selected_model)
                res = model.generate_content(user_prompt)
                st.markdown(res.text)
            except Exception as e:
                st.error(f"એરર: {e}")
    elif not selected_model:
        st.error("કોઈ મોડેલ મળ્યું નથી. API Key સાચી નથી અથવા પૂરતી પરવાનગી નથી.")
