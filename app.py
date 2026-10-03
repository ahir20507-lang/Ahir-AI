import streamlit as st
import google.generativeai as genai
from PIL import Image

st.set_page_config(page_title="Ahir-AI", layout="centered")

st.title("🤖 Ahir-AI Studio")
st.write("ચેટિંગ અને ફોટો એનાલિસિસ ટૂલ")

# Sidebar for API Key
api_key = st.sidebar.text_input("Gemini API Key દાખલ કરો:", type="password")

if not api_key:
    st.info("ડાબી બાજુના મેનુમાં તમારી Gemini API Key નાખો.")
    st.stop()

# Configure API
genai.configure(api_key=api_key)

tab1, tab2 = st.tabs(["💬 Chat", "🖼️ Image Analysis"])

with tab1:
    st.subheader("AI સાથે વાતચીત કરો")
    user_prompt = st.text_area("તમારો પ્રશ્ન પૂછો:", key="chat_input")
    if st.button("મોકલો", key="send_chat"):
        if user_prompt:
            with st.spinner("જવાબ વિચારી રહ્યો છું..."):
                try:
                    model = genai.GenerativeModel("models/gemini-3.8-flash")
                    response = model.generate_content(user_prompt)
                    st.markdown(response.text)
                except Exception as e:
                    st.error(f"એરર: {e}")
        else:
            st.warning("કંઈક લખો.")

with tab2:
    st.subheader("ફોટો મોકલીને સવાલ પૂછો")
    uploaded_file = st.file_uploader("ફોટો અપલોડ કરો", type=["jpg", "jpeg", "png"])
    img_prompt = st.text_input("આ ફોટો વિશે શું પૂછવું છે?", value="આ ફોટામાં શું છે તે સમજાવો.")
    
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="અપલોડ કરેલ ફોટો", use_container_width=True)
        
        if st.button("એનાલિસિસ કરો"):
            with st.spinner("ફોટો જોઈ રહ્યો છું..."):
                try:
                    model = genai.GenerativeModel("models/gemini-3.8-flash")
                    response = model.generate_content([img_prompt, image])
                    st.markdown(response.text)
                except Exception as e:
                    st.error(f"એરર: {e}")
