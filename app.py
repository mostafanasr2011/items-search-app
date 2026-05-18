import streamlit as st

# 1. إعداد واجهة البرنامج الأساسية
st.set_page_config(
    page_title="منظومة الهندسة الكهربائية", 
    page_icon="⚡", 
    layout="wide"
)

# 2. هندسة الـ CSS وتوحيد الخطوط والاتجاه RTL
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght=400;600;700&display=swap');
    html, body, .stApp, .stMarkdown, p, h1, h2, h3, h4, h5, h6, span, label, input, button, select {
        font-family: 'Cairo', sans-serif !important;
        text-align: right !important;
        direction: rtl !important;
    }
    .viewerBadge_link__1S137, .styles_viewerBadge__3uC9V, [data-testid="bundle-footer"], footer {
        visibility: hidden !important;
        display: none !important;
    }
    .block-container { padding-top: 2rem !important; }
    
    .welcome-card {
        background-color: #f8f9fa;
        border-right: 5px solid #007bff;
        padding: 20px;
        border-radius: 5px;
        margin-bottom: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# 3. محتوى صفحة الترحيب الرئيسية
st.title("⚡ المنظومة الذكية لتسعير وبحوث بنود الكهرباء")
st.write("مرحباً بك يا هندسة في مستودعك الرقمي الذكي. اضغط على زر الدخول الموجود أسفل القسم الذي تريده لفتح الصفحة فوراً.")

st.markdown("---")

st.header("📂 أقسام المنظومة المتاحة للدخول الفوري:")

# --- القسم الأول ---
st.markdown("""
<div class="welcome-card">
    <h3>🔍 1. صفحة البحث العام والسريع</h3>
    <p>البحث التقليدي السريع في كافة بنود الكهرباء بمجرد كتابة كلمة أو جزء من الكود، مع إمكانية تحميل النتائج إكسيل.</p>
</div>
""", unsafe_allow_html=True)

# الرابط الفعلي لصفحة البحث العام الإنجليزية النظيفة
if st.button("🚀 اضغط هنا للدخول إلى محرك البحث العام", key="btn_search"):
    st.switch_page("pages/search.py")
