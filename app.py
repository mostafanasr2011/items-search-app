import streamlit as st

# 1. إعداد واجهة البرنامج الأساسية (يجب أن يكون أول أمر)
st.set_page_config(
    page_title="منظومة الهندسة الكهربائية", 
    page_icon="⚡", 
    layout="wide"
)

# ✨ 2. هندسة الـ CSS وتوحيد الخطوط والاتجاه RTL (مع الحفاظ على القائمة الجانبية)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght=400;600;700&display=swap');
    
    html, body, .stApp, .stMarkdown, p, h1, h2, h3, h4, h5, h6, span, label, input, button, select {
        font-family: 'Cairo', sans-serif !important;
        text-align: right !important;
        direction: rtl !important;
    }
    
    /* إخفاء العلامات المائية لـ Streamlit فقط دون المساس بأزرار القائمة الجانبية */
    .viewerBadge_link__1S137, .styles_viewerBadge__3uC9V, [data-testid="bundle-footer"], footer {
        visibility: hidden !important;
        display: none !important;
    }
    
    .block-container {
        padding-top: 2rem !important;
        padding-bottom: 2rem !important;
    }
    
    /* تحسين شكل بطاقات الترحيب */
    .welcome-card {
        background-color: #f8f9fa;
        border-right: 5px solid #007bff;
        padding: 20px;
        border-radius: 5px;
        margin-bottom: 15px;
    }
    </style>
""", unsafe_allow_html=True)

# 3. محتوى صفحة الترحيب الرئيسية
st.title("⚡ المنظومة الذكية لتسعير وبحوث بنود الكهرباء")
st.write("مرحباً بك يا هندسة في مستودعك الرقمي الذكي. تم تصميم هذه المنظومة لمساعدتك في تصفح، وفلترة، وفهم بنود مقايسات الكهرباء بسرعة ودقة عالية.")

st.markdown("---")

st.header("📂 أقسام المنظومة المتوفرة (اطلع عليها من القائمة الجانبية):")

st.markdown("""
<div class="welcome-card">
    <h3>🔍 1. صفحة البحث العام والسريع</h3>
    <p>البحث التقليدي السريع في كافة بنود الكهرباء بمجرد كتابة كلمة أو جزء من الكود، مع إمكانية تحميل النتائج إكسيل.</p>
</div>

<div class="welcome-card" style="border-right-color: #28a745;">
    <h3>⚡ 2. رادار مهندس اللوحات</h3>
    <p>صفحة هندسية متخصصة لبنود اللوحات الكهربائية فقط، تتيح لك الفلترة الدقيقة بناءً على سعة القاطع، درجة الحماية IP، ونظام الطور.</p>
</div>

<div class="welcome-card" style="border-right-color: #ffc107;">
    <h3>🌳 3. التصفح الهرمي والمقارنة</h3>
    <p>تصفح شجري ذكي للمجموعات (رئيسية، فرعية، وصف سريع) لمساعدتك على فهم السوق والمقارنة بين البنود المتشابهة ومعرفة فروق الأسعار.</p>
</div>
""", unsafe_allow_html=True)

st.info("💡 نصيحة للتنقل: استخدم السهم الصغير الموجود في أعلى الزاوية (يسار أو يمين الشاشة حسب لغة متصفحك) لفتح القائمة الجانبية والتنقل بين الصفحات المتاحة.")
