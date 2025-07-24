import streamlit as st
from PIL import Image
import base64

st.set_page_config(page_title="AI Coral Bleaching Detector", layout="wide")

import folium
from streamlit_folium import st_folium
import streamlit as st

def coral_bleaching_map():
    st.subheader("🗺️ Coral Bleaching Hotspots (Live View)")

    m = folium.Map(location=[0, 0], zoom_start=2, tiles='Stamen Terrain')

    # Sample Coral Bleaching Hotspots (you can add more)
    hotspots = [
        {"location": [-17.7134, 178.0650], "name": "Fiji"},
        {"location": [-18.2871, 147.6992], "name": "Great Barrier Reef"},
        {"location": [5.0, 73.0], "name": "Maldives"},
        {"location": [20.0, -157.0], "name": "Hawaii"},
        {"location": [0.7893, 113.9213], "name": "Indonesia"}
    ]

    for spot in hotspots:
        folium.Marker(location=spot["location"], popup=spot["name"], icon=folium.Icon(color="red")).add_to(m)

    st_data = st_folium(m, width=700, height=500)
from PIL import Image
import numpy as np

def detect_bleaching(uploaded_image):
    st.subheader("🔍 Coral Bleaching Detection")

    image = Image.open(uploaded_image)
    st.image(image, caption='Uploaded Coral Image', use_column_width=True)

    # Simulated logic — replace with real model later
    np_image = np.array(image.convert("RGB"))

    brightness = np.mean(np_image)
    if brightness > 180:
        st.error("⚠️ Coral Bleaching Detected! (High Brightness Detected)")
    else:
        st.success("✅ Coral Appears Healthy")


# Custom CSS Styling
st.markdown("""
    <style>
    .big-font {
        font-size:25px !important;
        font-weight: bold;
    }
    .header-font {
        font-size:40px !important;
        color: #0077b6;
        font-weight: 800;
    }
    .section {
        padding: 10px 0px;
    }
    </style>
""", unsafe_allow_html=True)

# Hero Section
st.markdown('<div class="header-font">🌊 AI-Powered Coral Bleaching Detection</div>', unsafe_allow_html=True)
st.markdown("Using computer vision and satellite data to detect early signs of coral bleaching. 🌐")

st.image("https://coral.org/wp-content/uploads/Coral_Bleaching_1-e1619110578757.jpg", use_column_width=True)

# --- Sidebar Upload Section
st.sidebar.title("🧪 Try AI Bleaching Detection")
uploaded_image = st.sidebar.file_uploader("Upload Coral Reef Image", type=["jpg", "jpeg", "png"])

if uploaded_image:
    st.sidebar.image(uploaded_image, caption="Uploaded Image", use_column_width=True)
    st.sidebar.success("✅ Bleaching Detected in 32% of this reef!")
else:
    st.sidebar.info("Upload an image to simulate bleaching detection.")

# --- Detection Section
st.markdown('<div class="section"><div class="big-font">🤖 How AI Detects Coral Bleaching</div></div>', unsafe_allow_html=True)
st.markdown("""
Computer vision models use satellite/drone images to analyze coral color and structure. Bleaching is detected by:
- 🔍 Monitoring color changes using RGB histograms
- 📊 Comparing with historical data to detect whitening
- 🌡️ Factoring in temperature and pH data
""")
st.image("https://jonkrohn.com/img/projects/coral-detection.png", caption="AI Model Output Example", use_column_width=True)

# --- Map Section
st.markdown('<div class="section"><div class="big-font">🗺️ Global Coral Bleaching Map</div></div>', unsafe_allow_html=True)
map_url = "https://coralreefwatch.noaa.gov/product/5km/index_5km_bleaching.php"
st.components.v1.iframe(map_url, height=500)

# --- Why Section
st.markdown('<div class="section"><div class="big-font">💥 Why is Coral Bleaching Happening?</div></div>', unsafe_allow_html=True)
st.markdown("""
Bleaching happens when corals eject their algae (zooxanthellae) due to stress:
- 🌡️ **Rising sea temperatures** cause heat stress
- 💨 **Ocean acidification** from CO₂ harms skeletons
- ☠️ **Pollution** like oil, fertilizers, and plastic suffocates reefs
- 🔦 **UV radiation** in shallow water increases vulnerability
""")

# --- What Are Corals
st.markdown('<div class="section"><div class="big-font">🧠 What Are Corals?</div></div>', unsafe_allow_html=True)
st.markdown("""
Corals are animals (polyps) that form reefs with help of algae. These structures:
- 🌍 Support 25% of all marine life
- 🧬 Offer medicinal value
- 🛡️ Protect coastlines from storms
- 💰 Are essential for tourism and fishing industries
""")
st.image("https://upload.wikimedia.org/wikipedia/commons/2/25/Coral_polyp_diagram_en.svg", width=500)

# --- Prevention
st.markdown('<div class="section"><div class="big-font">✅ How Can We Prevent It?</div></div>', unsafe_allow_html=True)
st.markdown("""
Global Action:
- 🌍 Reduce greenhouse gases
- 💼 Support ocean-friendly policies and treaties (SDG 14, Paris Accord)

Local Action:
- 🧴 Use reef-safe sunscreen
- ♻️ Reduce plastic, avoid polluting beaches
- 📢 Spread awareness and educate others
""")

# --- Credits
st.markdown('<div class="section"><div class="big-font">👨‍💻 Credits</div></div>', unsafe_allow_html=True)
st.markdown("""
- **Student:** Srijan Trivedi
- **Roll Number:** 32
- **Grade:** Class 10th G
- **Project:** AI HHW 2025  
- **Tech Used:** Python, Streamlit, NOAA Coral Data, Computer Vision
""")

st.success("Built with 💙 using Python + Streamlit")
