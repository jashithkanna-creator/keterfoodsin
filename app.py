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
if slide_index is not in st.session_state:
   st.session_state.slide_index=0
slides=[
    "static/image/dehydrated-food.jpeg",
    "static/images/tamarind-powder.jpeg"
    "static/images/dried-vegetables.jpeg"
]
# 2. Create the Manual Slider UI
slider_container = st.container(border=True)
with slider_container:
    current_slide = slides[st.session_state.slide_index]

    # Display the current banner image & text
    st.image(current_slide["image"], use_container_width=True)
    st.markdown(f"<h3 style='text-align: center;'>{current_slide['title']}</h3>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: center; color: gray;'>{current_slide['desc']}</p>", unsafe_allow_html=True)

    # Left and Right manual buttons centered below the image
    prev_col, space, next_col = st.columns([1, 4, 1])

    with prev_col:
        if st.button("⬅️ Prev"):
            st.session_state.slide_index = (st.session_state.slide_index - 1) % len(slides)
            st.rerun()

    with next_col:
        if st.button("Next ➡️"):
            st.session_state.slide_index = (st.session_state.slide_index + 1) % len(slides)
            st.rerun()

st.write("<br>", unsafe_allow_html=True)

# 3. Your 3-Button Product Grid Layout (Matches image_109.png)
st.markdown("<h2 style='text-align: center;'>OUR <span style='color: #2ecc71;'>PRODUCTS</span></h2>", unsafe_allow_html=True)
st.write("---")

col1, col2, col3 = st.columns(3)

with col1:
    with st.container(border=True):
        st.markdown("<h4 style='text-align: center;'>DEHYDRATED VEGETABLES</h4>", unsafe_allow_html=True)
        st.write("Premium vegetables keeping natural nutrients completely intact.")
        if st.button("View Products", key="veg_btn"):
            st.session_state.page = "vegetables"

with col2:
    with st.container(border=True):
        st.markdown("<h4 style='text-align: center;'>DEHYDRATED FRUITS</h4>", unsafe_allow_html=True)
        st.write("Naturally sweet dehydrated fruits without any added chemical preservatives.")
        if st.button("View Products", key="fruit_btn"):
            st.session_state.page = "fruits"

with col3:
    with st.container(border=True):
        st.markdown("<h4 style='text-align: center;'>SPICES & POWDERS</h4>", unsafe_allow_html=True)
        st.write("Finely processed aromatic dehydrated whole spices and herbal blends.")
        if st.button("View Products", key="spices_btn"):
            st.session_state.page = "spices"



  
