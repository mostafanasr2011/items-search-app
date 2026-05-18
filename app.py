import streamlit as st

# 1. إعداد واجهة البرنامج الأساسية
st.set_page_config(
    page_title="منظومة الهندسة الكهربائية", 
    page_icon="⚡", 
    layout="wide"
)

# ✨ 2. هندسة الـ CSS وتوحيد الخطوط والاتجاه RTL
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
    
    /* ستايل كروت الترحيب العادية */
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

# الرابط الفعلي لصفحة البحث العام
if st.button("🚀 اضغط هنا للدخول إلى محرك البحث العام", key="btn_search"):
    st.switch_page("pages/1_🔍_البحث_العام.py")


st.markdown("<br>", unsafe_allow_html=True)

# --- القسم الثاني ---
st.markdown("""
<div class="welcome-card" style="border-right-color: #28a745;">
    <h3>⚡ 2. رادار مهندس اللوحات</h3>
    <p>صفحة هندسية متخصصة لبنود اللوحات الكهربائية فقط، تتيح لك الفلترة الدقيقة بناءً على سعة القاطع، درجة الحماية IP، ونظام الطور.</p>
</div>
""", unsafe_allow_html=True)

# الرابط الفعلي لصفحة اللوحات
if st.button("🚀 اضغط هنا للدخول إلى رادار اللوحات", key="btn_panels"):
    st.switch_page("pages/2_⚡_مهندس_اللوحات.py")


st.markdown("<br>", unsafe_allow_html=True)

# --- القسم الثالث ---
st.markdown("""
<div class="welcome-card" style="border-right-color: #ffc107;">
    <h3>🌳 3. التصفح الهرمي والمقارنة</h3>
    <p>تصفح شجري ذكي للمجموعات لمساعدتك على فهم السوق والمقارنة بين البنود المتشابهة ومعرفة فروق الأسعار.</p>
</div>
""", unsafe_allow_html=True)

# الرابط الفعلي لصفحة التصفح الهرمي
if st.button("🚀 اضغط هنا للدخول إلى التصفح الهرمي", key="btn_groups"):
    st.switch_page("pages/3_🌳_التصفح_الهرمي.py")
