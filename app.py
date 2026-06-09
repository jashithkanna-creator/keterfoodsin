import streamlit as st
import time

# Set page configuration to make it wide and match modern layouts
st.set_page_config(page_title="Keterfoods", layout="wide")

# Initialize session state for page routing and slideshow tracking
if "page" not in st.session_state:
    st.session_state.page = "home"
if "slide_index" not in st.session_state:
    st.session_state.slide_index = 0

# Custom CSS styling to give it a clean, premium off-white look
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
</style>
""", unsafe_allow_html=True)


# =========================================================
# 1. HOME PAGE FUNCTION
# =========================================================
def show_homepage():
    # List of your 5 exact local files from your Replit sidebar directory
    slides = [
        "static/images/keter-hero.png",
        "static/images/dried-vegetables.jpeg",
        "static/images/dehydrated-fruits.jpeg",
        "static/images/product-spice.png",
        "static/images/tamarind-powder.jpeg"
    ]

    # Render-safe native Streamlit slider engine
    current_slide = slides[st.session_state.slide_index]
    st.image(current_slide, use_container_width=True)

    # About Us Section
    st.header("About us")
    st.subheader("The Keterfoods Philosophy: A Foundation of Excellence")
    st.write("""In the competitive landscape of artisanal food production, the success of a brand is measured not merely by its reach, but by the integrity of its core pillars. Keterfoods stands as a beacon of quality, anchoring its methodologies in rigorous safety frameworks and sustainable practices. We believe that true culinary value stems from clean processing, direct transparent relationships with our farmers, and an unyielding commitment to delivering absolute freshness to consumers.""")

    # Automated slider trigger (changes slide image safely every 5 seconds)
    time.sleep(5)
    st.session_state.slide_index = (st.session_state.slide_index + 1) % len(slides)
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
