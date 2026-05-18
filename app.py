import streamlit as st

st.set_page_config(
    page_title="منظومة الهندسة الكهربائية", 
    page_icon="⚡", 
    layout="wide"
)

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght=400;600;700&display=swap');
    html, body, .stApp, .stMarkdown, p, h1, h2, h3, h4, h5, h6, span, label, input, button, select {
        font-family: 'Cairo', sans-serif !important;
        text-align: right !important;
        direction: rtl !important;
    }
    #MainMenu, header, footer, [data-testid="stHeader"], [data-testid="stDecoration"], 
    .viewerBadge_link__1S137, .styles_viewerBadge__3uC9V, [data-testid="bundle-footer"],
    [data-testid="stStatusWidget"], .stDeployButton, [data-testid="stToolbar"] {
        visibility: hidden !important;
        display: none !important;
    }
    .block-container { padding-top: 2rem !important; }
    .welcome-card { background-color: #f8f9fa; border-right: 5px solid #007bff; padding: 20px; border-radius: 5px; margin-bottom: 15px; }
    </style>
""", unsafe_allow_html=True)

st.title("⚡ المنظومة الذكية لتسعير وبحوث بنود الكهرباء")
st.write("مرحباً بك يا هندسة. تم تصميم هذه المنظومة لمساعدتك في تصفح وفلترة بنود مقايسات الكهرباء بسرعة ودقة عالية.")
st.markdown("---")
st.header("📂 أقسام المنظومة المتوفرة (اطلع عليها من القائمة الجانبية):")

st.markdown("""
<div class="welcome-card">
    <h3>🔍 1. صفحة البحث العام والسريع</h3>
    <p>البحث التقليدي السريع في كافة بنود الكهرباء بمجرد كتابة كلمة أو جزء من الكود.</p>
</div>
""", unsafe_allow_html=True)
