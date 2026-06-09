
import streamlit as st

# Set page configuration to make it wide and match modern layouts
st.set_page_config(page_title="Keterfoods", layout="wide")

# Initialize session state for page routing if it doesn't exist
if "page" not in st.session_state:
    st.session_state.page = "home"

# Custom CSS styling (includes your off-white look and the slideshow animations)
st.markdown("""
<style>
    .main { background-color: #FDFBF7; color: #2c3e50; }
    h1 { font-size: 2.5rem; margin-bottom: 0.5rem; }
    h2 { font-size: 1.75rem; margin-top: 1.5rem; margin-bottom: 1rem; }
    h4 { font-size: 1.1rem; font-weight: 600; text-align: center; margin: 0; }
    p { margin-bottom: 1.5rem; color: #34495e; }

    /* Border Container Boxes for Categories */
    .category-box {
        background-color: #ffffff;
        border: 1px solid #e0e0e0;
        border-radius: 8px;
        padding: 20px;
        height: 100%;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
    }

    /* CSS Slideshow Container */
    .slideshow-container {
        position: relative;
        width: 100%;
        height: 400px;
        overflow: hidden;
        border-radius: 8px;
        margin-bottom: 20px;
    }

    .slideshow-container img {
        position: absolute;
        width: 100%;
        height: 100%;
        object-fit: cover;
        opacity: 0;
        animation: slideFade 25s infinite;
    }

    /* Animation timings for the 5 banner images (5 seconds per image) */
    .slideshow-container img:nth-child(1) { animation-delay: 0s; }
    .slideshow-container img:nth-child(2) { animation-delay: 5s; }
    .slideshow-container img:nth-child(3) { animation-delay: 10s; }
    .slideshow-container img:nth-child(4) { animation-delay: 15s; }
    .slideshow-container img:nth-child(5) { animation-delay: 20s; }

    @keyframes slideFade {
        0% { opacity: 0; }
        4% { opacity: 1; }
        20% { opacity: 1; }
        24% { opacity: 0; }
        100% { opacity: 0; }
    }
</style>
""", unsafe_allow_html=True)


# =========================================================
# 1. HOME PAGE FUNCTION
# =========================================================
def show_homepage():
    # Integrated HTML Slideshow containing all 5 of your project images
    st.markdown("""
    <div class="slideshow-container">
        <img src="app/static/images/keter-hero.png">
        <img src="app/static/images/dried-vegetables.jpeg">
        <img src="app/static/images/dehydrated-fruits.jpeg">
        <img src="app/static/images/product-spice.png">
        <img src="app/static/images/tamarind-powder.jpeg">
    </div>
    """, unsafe_allow_html=True)

    # About Us Section
    st.header("About us")
    st.subheader("The Keterfoods Philosophy: A Foundation of Excellence")
    st.write("""In the competitive landscape of artisanal food production, the success of a brand is measured not merely by its reach, but by the integrity of its core pillars. Keterfoods stands as a beacon of quality, anchoring its methodologies in rigorous safety frameworks and sustainable practices. We believe that true culinary value stems from clean processing, direct transparent relationships with our farmers, and an unyielding commitment to delivering absolute freshness to consumers.""")

    st.markdown("<br><h2 style='text-align: center;'>OUR <span style='color: #2ecc71;'>PRODUCTS</span></h2>", unsafe_allow_html=True)

    # The 4-Column Category Grid
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown("<div class='category-box'><h4>VEGETABLES</h4><p style='font-size:14px;'>Naturally grown, expertly sliced, and dehydrated vegetables keeping core nutrients preserved.</p></div>", unsafe_allow_html=True)
        if st.button("View Products", key="btn_veg", use_container_width=True):
            st.session_state.page = "vegetables"
            st.rerun()

    with col2:
        st.markdown("<div class='category-box'><h4>FRUITS</h4><p style='font-size:14px;'>Sweet and tangy premium dehydrated fruit slices perfect for healthy snacking and baking.</p></div>", unsafe_allow_html=True)
        if st.button("View Products", key="btn_fruit", use_container_width=True):
            st.session_state.page = "fruits"
            st.rerun()

    with col3:
        st.markdown("<div class='category-box'><h4>SPICES & POWDERS</h4><p style='font-size:14px;'>Finely processed aromatic dehydrated whole spices and herbal blends.</p></div>", unsafe_allow_html=True)
        if st.button("View Products", key="btn_spices", use_container_width=True):
            st.session_state.page = "spices"
            st.rerun()

    with col4:
        st.markdown("<div class='category-box'><h4>PICKLES & OTHER</h4><p style='font-size:14px;'>Chapatis and pooris made from whole wheat flour alongside delicious traditional items.</p></div>", unsafe_allow_html=True)
        if st.button("View Products", key="btn_other", use_container_width=True):
            st.session_state.page = "other"
            st.rerun()


# =========================================================
# 2. SUB-PAGE FUNCTIONS
# =========================================================
def show_vegetables_page():
    if st.button("🏠 Home", key="back_veg"):
        st.session_state.page = "home"
        st.rerun()
    st.markdown("## 🧅 Dehydrated Vegetables")
    st.write("Vegetables catalog details coming soon.")

def show_fruits_page():
    if st.button("🏠 Home", key="back_fruit"):
        st.session_state.page = "home"
        st.rerun()
    st.markdown("## 🍓 Dehydrated Fruits")
    st.write("Fruit catalog details coming soon.")

def show_spices_page():
    if st.button("🏠 Home", key="back_spices"):
        st.session_state.page = "home"
        st.rerun()
    st.markdown("## 🌶️ Spices & Powders")
    st.write("Spices catalog details coming soon.")

def show_other_page():
    if st.button("🏠 Home", key="back_other"):
        st.session_state.page = "home"
        st.rerun()
    st.markdown("## 🥞 Pickles, Chapathi & Poori")
    st.write("Pickles and bakery inventory coming soon.")


# =========================================================
# 3. ROUTING ROUTER SYSTEM
# =========================================================
if st.session_state.page == "home":
    show_homepage()
elif st.session_state.page == "vegetables":
    show_vegetables_page()
elif st.session_state.page == "fruits":
    show_fruits_page()
elif st.session_state.page == "spices":
    show_spices_page()
elif st.session_state.page == "other":
    show_other_page()
