import streamlit as st

# Set page configuration to make it wide and match modern layouts
st.set_page_config(page_title="Keterfoods", layout="wide")

# Initialize session state for page routing if it doesn't exist
if "page" not in st.session_state:
    st.session_state.page = "home"

# Custom CSS styling to make things look pristine
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
def show_home_page():
    st.title("Keterfoods")
    st.markdown("<p style='font-size: 1.1rem; color: #7f8c8d; margin-top: -15px;'>Quality at forefront, reliability in every package, and affordability at core</p>", unsafe_allow_html=True)
    st.markdown("---")

    st.markdown("## About Keterfoods")
    st.write("At Keterfoods, the core philosophy revolves around delivering premium-quality food products while maintaining complete operational transparency and consumer trust. Established with a commitment to culinary excellence, the company bridges the gap between traditional food processing values and modern distribution efficiency. By strictly adhering to stringent quality control protocols, Keterfoods ensures that every item packed retains its organic integrity, rich flavor profiles, and essential nutritional values.")

    st.markdown("## Reliability")
    st.write("Reliability is the cornerstone of Keterfoods' operations. From sourcing raw ingredients directly from trusted agricultural networks to executing precision-controlled manufacturing processes, every step is optimized for consistency. The brand prides itself on an uninterrupted supply chain capable of meeting diverse market demands without compromising on product safety. This unwavering dedication ensures that retail partners and household consumers alike receive packages that conform to the highest safety and distribution standards every single time.")

    st.markdown("## Affordability")
    st.write("Often, the term 'premium' in food production implies an exclusive price point, but Keterfoods challenges this paradigm. Affordability is not a concession to quality; rather, it is a deliberate strategic goal. By optimizing production workflows such as the digital transformation of inventory and supply chain management Keterfoods reduces operational waste and streamlines overhead costs. These efficiencies allow the company to offer superior products at a price point that remains accessible to a broader demographic.")

    st.markdown("## Vision for the future")
    st.write("The vision for Keterfoods extends far beyond current product lines. It is centered on the integration of technology and artisanal craftsmanship. The company looks toward a future where data driven insights ranging from real time climate monitoring in production facilities to AI powered stock forecasting further enhance the efficiency and sustainability of their operations. Ultimately, Keterfoods is not just selling food; it is building a system that values the consumer's well-being. By maintaining a balance between the precision of technology and the care of traditional methods, the company aims to become a standard bearer for how modern food enterprises should operate: with quality at the forefront, reliability in every package, and affordability at the core of its mission.")

    st.markdown("<br><h2 style='text-align: center;'>OUR <span style='color: #2ecc71;'>PRODUCTS</span></h2>", unsafe_allow_html=True)

    # 4-Column Category Grid
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown("<div class='category-box'><h4>VEGETABLES</h4><p style='font-size:14px;'>Naturally grown, expertly sliced, and dehydrated vegetables keeping core nutrients preserved.</p></div>", unsafe_allow_html=True)
        if st.button("View Products", key="btn_veg", use_container_width=True):
            st.session_state.page = "vegetables"
            st.rerun()

    with col2:
        st.markdown("<div class='category-box'><h4>FRUITS</h4><p style='font-size:14px;'>Sweet and tangy premium dehydrated fruit slices perfect for healthy snacking .</p></div>", unsafe_allow_html=True)
        if st.button("View Products", key="btn_fruit", use_container_width=True):
            st.session_state.page = "fruits"
            st.rerun()

    with col3:
        st.markdown("<div class='category-box'><h4>SPICES & POWDERS</h4><p style='font-size:14px;'>Finely processed aromatic dehydrated whole spices and herbal blends.</p></div>", unsafe_allow_html=True)
        if st.button("View Products", key="btn_spices", use_container_width=True):
            st.session_state.page = "spices"
            st.rerun()

    with col4:
        st.markdown("<div class='category-box'><h4>PICKLES, CHAPATHI & POORI</h4><p style='font-size:14px;'>Chapatis and pooris made from whole wheat flour alongside delicious traditional pickles.</p></div>", unsafe_allow_html=True)
        if st.button("View Products", key="btn_other", use_container_width=True):
            st.session_state.page = "other"
            st.rerun()


# =========================================================
# 2. VEGETABLES PAGE FUNCTION (Replicates Screenshot)
# =========================================================
def show_vegetables_page():
    # Navigation Bar back setup
    col_nav, col_title = st.columns([1, 4])
    with col_nav:
        if st.button("🏠 Home", key="back_veg"):
            st.session_state.page = "home"
            st.rerun()
    with col_title:
        st.markdown("## 🧅 Dehydrated Vegetables")
    st.markdown("---")

    # Catalog Data Array
    vegetables = [
        {
            "name": "DEHYDRATED BEANS",
             
            "rating": "⭐⭐⭐⭐⭐ (4.3 Rating & 4 Reviews)",
            "description_bullets": [
                "Dehydrated beans are a healthy version of beans. These crispy beans are a fun way to eat a healthy snack to take with you on the go.",
                "Dehydrated green beans are loaded with fiber, vitamins, micronutrients, and have enormous health benefits.",
                "We use a unique dehydration process and advanced technology to keep the nutrition profile and quality intact.",
                "Dehydrated beans are tossed into soups, salads, stews, etc.",
                "They are rehydrated instantly by simmering in water."
            ],
            "standards_bullets": [
                "We are one of the leading manufacturers, exporters, and sellers of dehydrated green beans.",
                "All the raw materials we use to manufacture are NON-GMO in origin.",
                "Our dehydrated products are benchmarked by international global safety and production standards."
            ]
        }
        # 💡 You can paste more vegetables blocks here anytime!
    ]

    # Grid Display Loop matching screenshot layout
    for product in vegetables:
        col_left_img, col_right_details = st.columns([2, 3])

        with col_left_img:
            try:
                st.image(product["image"], use_container_width=True)
            except:
                st.warning(f"Please upload '{product['image']}' into Replit side menu.")

        with col_right_details:
            st.markdown(f"### {product['name'].upper()}")
            st.markdown(f"<span style='color:#3498db; font-size:14px; font-weight:600;'>{product['rating']}</span>", unsafe_allow_html=True)
            st.write("") 

            # Description Block
            c_lbl1, c_blt1 = st.columns([1, 4])
            with c_lbl1:
                st.markdown("<span style='color:#2ecc71; font-weight:bold;'>Description:</span>", unsafe_allow_html=True)
            with c_blt1:
                for bullet in product["description_bullets"]:
                    st.markdown(f"• {bullet}")

            st.write("") 

            # Standards Block
            c_lbl2, c_blt2 = st.columns([1, 4])
            with c_lbl2:
                st.markdown("<span style='color:#2ecc71; font-weight:bold;'>Our Standards:</span>", unsafe_allow_html=True)
            with c_blt2:
                for bullet in product["standards_bullets"]:
                    st.markdown(f"• {bullet}")

        st.markdown("<br><hr style='border: 0; border-top: 1px dashed #e0e0e0;'><br>", unsafe_allow_html=True)


# =========================================================
# 3. OTHER CATEGORY PLACEHOLDERS (Fill these in next)
# =========================================================
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
    st.markdown("##  Pickles, Chapathi & Poori")
    st.write("Pickles and bakery inventory coming soon.")


# =========================================================
# 4. ROUTING ROUTER ENGINE
# =========================================================
if st.session_state.page == "home":
    show_home_page()
elif st.session_state.page == "vegetables":
    show_vegetables_page()
elif st.session_state.page == "fruits":
    show_fruits_page()
elif st.session_state.page == "spices":
    show_spices_page()
elif st.session_state.page == "other":
    show_other_page()
