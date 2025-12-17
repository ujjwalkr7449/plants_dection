import streamlit as st
from backend import analyze_image, analyze_farming_data
from PIL import Image

st.set_page_config(page_title="🌾 Krishi AI Mitra", page_icon="🌱", layout="wide")

st.markdown("## 🌾 Krishi AI Mitra (कृषि AI मित्र)")
st.markdown("फसल की फोटो डालें और बीमारी, इलाज और दवा की जानकारी पाएं")

organic_only = st.toggle("🌿 Organic solutions only")

if "messages" not in st.session_state:
    st.session_state.messages = []

uploaded = st.file_uploader("📸 फसल की फोटो अपलोड करें", type=["jpg","png","jpeg"])

if uploaded:
    img = Image.open(uploaded)
    st.image(img, use_container_width=True)

    if st.button("🔍 Analyze Crop"):
        with st.spinner("AI फसल का विश्लेषण कर रहा है..."):
            img_bytes = uploaded.getvalue()
            vision_text = analyze_image(img_bytes)
            result = analyze_farming_data(vision_text)
            st.session_state.messages.append(result)

for msg in st.session_state.messages:
    with st.chat_message("assistant"):
        st.markdown(f"### 🌱 Crop: {msg['crop']}")
        st.markdown(f"### 🦠 Disease: {msg['disease']}")
        st.write(msg["disease_description"])

        st.markdown("**💊 Treatment:**")
        st.write(msg["treatment"])

        if not organic_only:
            st.markdown("**🇮🇳 Indian Medicines:**")
            st.write(msg["indian_medicines"])

        st.markdown("**🌿 Organic Solution:**")
        st.write(msg["organic_solution"])

        st.markdown("**🌦️ Weather Advice:**")
        st.write(msg["weather_advice"])
