import streamlit as st
import folium
from streamlit_folium import st_folium
from PIL import Image
import numpy as np
import random

st.set_page_config(page_title="Coral Bleaching Detection", layout="wide")

st.title("🌊 Coral Bleaching Early Detection & Awareness")

# SECTION 1: Upload & Analyze Image
st.header("📸 Coral Image Analysis (Demo AI)")
uploaded_file = st.file_uploader("Upload a coral reef image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)
    st.write("✅ Processing image...")
    
    # Dummy bleaching detection logic (simulating AI)
    bleaching_probability = round(random.uniform(0.2, 0.9), 2)
    if bleaching_probability > 0.6:
        st.error(f"⚠️ High likelihood of bleaching detected! Probability: {bleaching_probability}")
    else:
        st.success(f"✅ Healthy coral detected. Probability of bleaching: {bleaching_probability}")

# SECTION 2: Interactive Coral Bleaching Map
st.header("🗺️ Global Coral Bleaching Map")

# Create a folium map with dummy data
m = folium.Map(location=[0, 160], zoom_start=2)
bleaching_locations = [
    {"location": [14.6, 145.8], "severity": "High", "region": "Micronesia"},
    {"location": [-18.3, 147.7], "severity": "Moderate", "region": "Great Barrier Reef"},
    {"location": [5.3, -72.4], "severity": "Low", "region": "Caribbean"},
]

for loc in bleaching_locations:
    folium.Marker(
        location=loc["location"],
        popup=f"{loc['region']} - Severity: {loc['severity']}",
        icon=folium.Icon(color="red" if loc["severity"] == "High" else "orange")
    ).add_to(m)

st_folium(m, width=700, height=500)

# SECTION 3: Informative Section
st.header("📚 What Are Corals and Why Are They Bleaching?")

st.subheader("🌱 What Are Corals?")
st.markdown("""
Corals are marine invertebrates that build large reef structures using calcium carbonate. These reefs are home to **25% of all marine life**.
They live in symbiosis with **zooxanthellae algae**, which give corals their vibrant color and help them photosynthesize.

However, these algae are extremely sensitive to temperature, pH changes, and pollutants.
""")

st.subheader("🔥 Why Does Coral Bleaching Happen?")
st.markdown("""
When water gets **too warm** or polluted, corals **expel their algae**, turning white — a process called **bleaching**.
If stressful conditions persist, corals die from lack of nutrients.

**Main causes**:
- Ocean warming due to **climate change**
- **Overfishing** and reef damage
- Ocean acidification
- Coastal pollution from oil, plastic, or sewage
""")

st.subheader("✅ How Can We Prevent It?")
st.markdown("""
- **Reduce carbon emissions**: Support renewable energy and climate policies
- **Ban harmful fishing practices** like trawling and cyanide fishing
- Create **Marine Protected Areas** (MPAs)
- Promote **coral-friendly tourism** and sunscreen
- Fund AI-based **reef monitoring programs** like this one!
""")

# Footer
# --- Credits
st.markdown('<div class="section"><div class="big-font">👨‍💻 Credits</div></div>', unsafe_allow_html=True)
st.markdown("""
- **Student:** Srijan Trivedi
- **Roll Number:** 32
- **Grade:** Class 10th G
- **Project:** AI HHW 2025  
- **Tech Used:** Python, Streamlit, NOAA Coral Data, Computer Vision
""")
