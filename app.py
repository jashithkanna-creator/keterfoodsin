import streamlit as st

st.set_page_config(layout="wide")

# --- 1. PERFECTED LAYOUT & CAROUSEL ANIMATION ---
st.markdown("""
<style>
/* Style the navigation buttons to look like a modern navbar block */
div.stButton > button:first-child {
    background-color: #ffffff;
    color: #2c3e50;
    border: 1px solid #e0e0e0;
    padding: 10px 24px;
    font-weight: 600;
    border-radius: 8px;
    box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    transition: all 0.3s ease;
}
div.stButton > button:first-child:hover {
    border-color: #2ecc71;
    color: #2ecc71;
    background-color: #fafffa;
}
.stApp {
    background-color: #FDFBF7;
}
/* Safe padding to completely prevent top-clipping on iPad/mobile browsers */
.block-container {
    padding-top: 4.5rem !important;
    padding-bottom: 2rem;
    max-width: 95% !important;
}

/* Browser-side CSS Slideshow Frame - 0% Server CPU overhead, No subpage glitches */
.render-slideshow-container {
    position: relative;
    width: 100%;
    height: 400px;
    overflow: hidden;
    border-radius: 12px;
    margin-bottom: 30px;
    box-shadow: 0 4px 15px rgba(0,0,0,0.06);
    background-color: #eaeaea;
}
.render-slide {
    position: absolute;
    width: 100%;
    height: 100%;
    background-size: cover;
    background-position: center;
    opacity: 0;
    animation: renderCarouselKeyframes 20s infinite ease-in-out;
}
/* Individual delay timings for a seamless 4-second crossfade loop */
.rs-1 { background-image: url('app/static/images/keter-hero.png'); animation-delay: 0s; }
.rs-2 { background-image: url('app/static/images/dried-vegetables.jpeg'); animation-delay: 4s; }
.rs-3 { background-image: url('app/static/images/dehydrated-fruits.jpeg'); animation-delay: 8s; }
.rs-4 { background-image: url('app/static/images/product-spice.png'); animation-delay: 12s; }
.rs-5 { background-image: url('app/static/images/tamarind-powder.jpeg'); animation-delay: 16s; }

@keyframes renderCarouselKeyframes {
    0% { opacity: 0; }
    4% { opacity: 1; }
    20% { opacity: 1; }
    24% { opacity: 0; }
    100% { opacity: 0; }
}
</style>
""", unsafe_allow_html=True)

# --- 2. INITIALIZE NAVIGATION STATE ---
if "page" not in st.session_state:
    st.session_state.page = "home"


# --- 3. DEFINE THE PAGES ---

def show_homepage():
    # Injecting the pure CSS carousel. It handles cycling natively in the browser window
    st.markdown("""
    <div class="render-slideshow-container">
        <div class="render-slide rs-1"></div>
        <div class="render-slide rs-2"></div>
        <div class="render-slide rs-3"></div>
        <div class="render-slide rs-4"></div>
        <div class="render-slide rs-5"></div>
    </div>
    """, unsafe_allow_html=True)

    # About Us Section
    st.header("About us")
    st.subheader("The Keterfoods Philosophy: A Foundation of Excellence")
    st.write("""In the competitive landscape of artisanal food production, the success of a brand is measured not merely by its reach, but by the integrity of its core pillars. Keterfoods stands as a testament to the belief that high quality, processed food products can be both accessible and reliable. By harmonizing rigorous quality standards with a vision for sustainable growth, Keterfoods is redefining what it means to be a trusted provider in the modern food market.""")

    st.subheader("Quality and Reliability")
    st.write("""The dehydration process is often misunderstood as a simple reduction of moisture, but for Keterfoods, it is a delicate science of preservation. By utilizing advanced, low-temperature dehydration methods, the company ensures that the essential vitamins, enzymes, and vibrant colors of the raw ingredients are retained. This commitment to quality transforms "dried goods" from mere pantry staples into premium, nutrient dense foods. Every product that leaves the Keterfoods facility undergoes rigorous testing to ensure that it meets the highest standards of purity, offering a superior alternative to highly processed or chemically preserved snacks.""")

    st.subheader("Affordability")
    st.write("""Often, the term "premium" in food production implies an exclusive price point, but Keterfoods challenges this paradigm. Affordability is not a concession to quality; rather, it is a deliberate strategic goal. By optimizing production workflows such as the digital transformation of inventory and supply chain management Keterfoods reduces operational waste and streamlines overhead costs. These efficiencies allow the company to offer superior products at a price point that remains accessible to a broader demographic.""")

    st.subheader("Vision for the future")
    st.write("""The vision for Keterfoods extends far beyond current product lines. It is centered on the integration of technology and artisanal craftsmanship. The company looks toward a future where data driven insights ranging from real time climate monitoring in production facilities to AI powered stock forecasting further enhance the efficiency and sustainability of their operations.
    Ultimately, Keterfoods is not just selling food; it is building a system that values the consumer's well-being. By maintaining a balance between the precision of technology and the care of traditional methods, the company aims to become a standard bearer for how modern food enterprises should operate: with quality at the forefront, reliability in every package, and affordability at the core of its mission.""")

    # Products Category Grid
    st.write("<br>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center;'>OUR <span style='color: #2ecc71;'>PRODUCTS</span></h2>", unsafe_allow_html=True)
    st.write("---")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        with st.container(border=True):
            st.markdown("<h4 style='text-align: center;'>DEHYDRATED VEGETABLES</h4>", unsafe_allow_html=True)
            st.write("Premium vegetables keeping natural nutrients completely intact.")
            if st.button("View Products", key="veg_btn"):
                st.session_state.page = "vegetables"
                st.rerun()

    with col2:
        with st.container(border=True):
            st.markdown("<h4 style='text-align: center;'>DEHYDRATED FRUITS</h4>", unsafe_allow_html=True)
            st.write("Naturally sweet dehydrated fruits without any added chemical preservatives.")
            if st.button("View Products", key="fruit_btn"):
                st.session_state.page = "fruits"
                st.rerun()

    with col3:
        with st.container(border=True):
            st.markdown("<h4 style='text-align: center;'>SPICES & POWDERS</h4>", unsafe_allow_html=True)
            st.write("Finely processed aromatic dehydrated whole spices and herbal blends.")
            if st.button("View Products", key="spices_btn"):
                st.session_state.page = "spices"
                st.rerun()

    with col4:
        with st.container(border=True):
            st.markdown("<h4 style='text-align: center;'>PICKLES,CHAPATHI & POORI</h4>", unsafe_allow_html=True)
            st.write("chapatis and pooris made from whole wheat flour")
            if st.button("View Products", key="OTHER_btn"):
                st.session_state.page = "OTHER"
                st.rerun()


def show_vegetables_page():
    nav_col, title_col = st.columns([1, 4])
    with nav_col:
        if st.button("🏠 Home", key="back_veg"):
            st.session_state.page = "home"
            st.rerun()
    with title_col:
        st.markdown("<h2 style='margin:0; padding:0;'>🧅 Dehydrated Vegetables</h2>", unsafe_allow_html=True)
    st.write("---")
    st.write("Premium selections coming soon.")


def show_fruits_page():
    nav_col, title_col = st.columns([1, 4])
    with nav_col:
        if st.button("🏠 Home", key="back_fruit"):
            st.session_state.page = "home"
            st.rerun()
    with title_col:
        st.markdown("<h2 style='margin:0; padding:0;'>🍓 Dehydrated Fruits</h2>", unsafe_allow_html=True)
    st.write("---")
    st.write("Premium selections coming soon.")


def show_spices_page():
    nav_col, title_col = st.columns([1, 4])
    with nav_col:
        if st.button("🏠 Home", key="back_spices"):
            st.session_state.page = "home"
            st.rerun()
    with title_col:
        st.markdown("<h2 style='margin:0; padding:0;'>🌶️ Spices & Powders</h2>", unsafe_allow_html=True)
    st.write("---")
    st.write("Premium selections coming soon.")


def show_other_page():
    nav_col, title_col = st.columns([1, 4])
    with nav_col:
        if st.button("🏠 Home", key="back_other"):
            st.session_state.page = "home"
            st.rerun()
    with title_col:
        st.markdown("<h2 style='margin:0; padding:0;'>🥞 Pickles, Chapathi & Poori</h2>", unsafe_allow_html=True)
    st.write("---")
    st.write("Premium selections coming soon.")


# --- 4. CLEAN PAGE ROUTER CONTROL ---
if st.session_state.page == "home":
    show_homepage()
elif st.session_state.page == "vegetables":
    show_vegetables_page()
elif st.session_state.page == "fruits":
    show_fruits_page()
elif st.session_state.page == "spices":
    show_spices_page()
elif st.session_state.page == "OTHER":
    show_other_page()
