import streamlit as st
from streamlit_autorefresh import st_autorefresh

# 1. Force the layout to use the entire width of your iPad screen
st.set_page_config(layout="wide")

# 2. Add custom CSS to style the background and cards
st.markdown("""
<style>
.stApp {
    background-color: #FDFBF7;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
    max-width: 95% !important;
}
</style>
""", unsafe_allow_html=True)

# Hero Images
hero_images = [
    "static/images/keter-hero.png",
    "static/images/product-spice.png",
    "static/images/dehydrated-fruits.jpeg"
]

# Auto refresh every 10 seconds
count = st_autorefresh(interval=10000, key="refresh")

# Change image on each refresh
hero_index = count % len(hero_images)

# Display current image
st.image(hero_images[hero_index], use_container_width=True)

# --- Rest of your page starts here ---
st.header("About us")

st.subheader("The Keterfoods Philosophy: A Foundation of Excellence")
st.write("""
In the competitive landscape of artisanal food production, the success of a brand is measured not merely by its reach, but by the integrity of its core pillars. Keterfoods stands as a testament to the belief that high-quality, processed food products can be both accessible and reliable. By harmonizing rigorous quality standards with a vision for sustainable growth, Keterfoods is redefining what it means to be a trusted provider in the modern food market.
""")

st.subheader("Quality and Reliability")
st.write("""The dehydration process is often misunderstood as a simple reduction of moisture, but for Keterfoods, it is a delicate science of preservation. By utilizing advanced, low-temperature dehydration methods, the company ensures that the essential vitamins, enzymes, and vibrant colors of the raw ingredients are retained. This commitment to quality transforms "dried goods" from mere pantry staples into premium, nutrient-dense foods. Every product that leaves the Keterfoods facility undergoes rigorous testing to ensure that it meets the highest standards of purity, offering a superior alternative to highly processed or chemically preserved snacks.""")

st.subheader("Affordability")
st.write("""
Often, the term "premium" in food production implies an exclusive price point, but Keterfoods challenges this paradigm. Affordability is not a concession to quality; rather, it is a deliberate strategic goal. By optimizing production workflows—such as the digital transformation of inventory and supply chain management—Keterfoods reduces operational waste and streamlines overhead costs. These efficiencies allow the company to offer superior products at a price point that remains accessible to a broader demographic.
""")

st.subheader("Vision for the future")
st.write("""
The vision for Keterfoods extends far beyond current product lines. It is centered on the integration of technology and artisanal craftsmanship. The company looks toward a future where data-driven insights—ranging from real-time climate monitoring in production facilities to AI-powered stock forecasting—further enhance the efficiency and sustainability of their operations.

Ultimately, Keterfoods is not just selling food; it is building a system that values the consumer's well-being. By maintaining a balance between the precision of technology and the care of traditional methods, the company aims to become a standard-bearer for how modern food enterprises should operate: with quality at the forefront, reliability in every package, and affordability at the core of its mission.
""")
