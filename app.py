import streamlit.hello.mapping_demo
import streamlit as st
# 1. Force the layout to use the entire width of your iPad screen
st.set_page_config(layout="wide")
# 2. Add custom CSS to style the background and cards
st.markdown("""
    <style>
    /* Change the main background color to a soft, modern cream/off-white */
    .stApp {
        background-color: #FDFBF7;
    }
    /* Make the main container look like a premium full-scale dashboard */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        max-width: 95% !important;
    }
    </style>
""", unsafe_allow_html=True)
st.image("static/images/keter-hero.png", use_container_width=True)      
st.header("About us")
st.subheader("The Keterfoods Philosophy: A Foundation of Excellence")
st.write("""In the competitive landscape of artisanal food production, the success of a brand is measured not merely by its reach, but by the integrity of its core pillars. Keterfoods stands as a testament to the belief that high-quality, processed food products can be both accessible and reliable. By harmonizing rigorous quality standards with a vision for sustainable growth, Keterfoods is redefining what it means to be a trusted provider in the modern food market.""")
st.subheader("Quality and Reliability: The Bedrock of Trust")
st.subheader("Affordability: Democratizing Excellence")
st.write("""Often, the term "premium" in food production implies an exclusive price point, but Keterfoods challenges this paradigm. Affordability is not a concession to quality; rather, it is a deliberate strategic goal. By optimizing production workflows—such as the digital transformation of inventory and supply chain management—Keterfoods reduces operational waste and streamlines overhead costs. These efficiencies allow the company to offer superior products at a price point that remains accessible to a broader demographic. This democratization ensures that high-quality nutrition is not reserved for the elite, but is a viable option for the everyday consumer.""")
st.subheader("Vision: A Future Built on Innovation")
st.write("""The vision for Keterfoods extends far beyond current product lines. It is centered on the integration of technology and artisanal craftsmanship. The company looks toward a future where data-driven insights—ranging from real-time climate monitoring in production facilities to AI-powered stock forecasting—further enhance the efficiency and sustainability of their operations. By embracing digital tools, Keterfoods intends to scale its impact without diluting the handmade quality that defines its brand.
Ultimately, Keterfoods is not just selling food; it is building a system that values the consumer’s well-being. By maintaining a balance between the precision of technology and the care of traditional methods, the company aims to become a standard-bearer for how modern food enterprises should operate: with quality at the forefront, reliability in every package, and affordability at the core of its mission. Through this clear and evolving vision, Keterfoods is positioning itself to lead the market into a future where good food is a standard, rather than a luxury.""")