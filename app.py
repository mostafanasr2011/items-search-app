import streamlit as st
import pandas as pd
import io
import os

# 1. إعداد الصفحة وإخفاء القائمة الجانبية تماماً لتوحيد الرؤية
st.set_page_config(
    page_title="منظومة الهندسة الكهربائية الذكية", 
    page_icon="⚡", 
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ✨ 2. هندسة الـ CSS والشخلعة والألوان الاحترافية الثابتة
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght=400;600;700;900&display=swap');
    
    html, body, .stApp, .stMarkdown, p, h1, h2, h3, h4, h5, h6, span, label, input, button, select {
        font-family: 'Cairo', sans-serif !important;
        text-align: right !important;
        direction: rtl !important;
    }
    
    /* إخفاء السايد بار تماماً والعلائم الافتراضية */
    [data-testid="stSidebar"], .viewerBadge_link__1S137, .styles_viewerBadge__3uC9V, [data-testid="bundle-footer"], footer {
        display: none !important;
        visibility: hidden !important;
    }
    .block-container { padding-top: 1rem !important; }

    /* عنوان المنظومة المتوهج الثابت */
    .main-header-title {
        background: linear-gradient(45deg, #0052cc, #00ffcc, #ff007f);
        background-size: 300% 300%;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 36px !important;
        font-weight: 900;
        text-align: center !important;
        margin-bottom: 5px;
    }
    
    .main-subtitle {
        text-align: center !important;
        font-size: 16px;
        color: #555;
        margin-bottom: 20px;
    }

    /* كروت التصميم ثلاثي الأبعاد */
    .card-3d {
        background: rgba(255, 255, 255, 0.95);
        border-radius: 14px;
        box-shadow: 0 8px 25px rgba(0, 0, 0, 0.07);
        border-right: 8px solid #0052cc;
        padding: 20px;
        margin-bottom: 15px;
    }
    .icon-3d { font-size: 35px; float: left; }
    
    /* ستايل التوقيع وفريق الإعداد */
    .footer-credits {
        text-align: center !important;
        font-size: 14px;
        color: #777;
        margin-top: 50px;
        padding: 15px;
        border-top: 1px dashed #ccc;
    }
    </style>
""", unsafe_allow_html=True)

# 🏢 3. تثبيت اسم المنظومة في أعلى الشاشة دائماً وأبداً في كل الصفحات
st.markdown('<h1 class="main-header-title">⚡ المنظومة الذكية لتسعير وبحوث بنود الكهرباء</h1>', unsafe_allow_html=True)
st.markdown('<p class="main-subtitle">مستودعك الرقمي الهندسي الشامل لتصفح وفلترة مقايسات وبنود الكهرباء</p>', unsafe_allow_html=True)

# 🌐 4. شريط أزرار التنقل العلوي المطور (إضافة زر HOME وزر HELP)
st.markdown("<h4 style='text-align: center; color: #333; margin-bottom: 10px;'>🌐 لوحة التحكم السريع للمنظومة</h4>", unsafe_allow_html=True)
col_nav1, col_nav2, col_nav3, col_nav4, col_nav5 = st.columns([1.2, 2, 2, 2, 1.2])

if "current_page" not in st.session_state:
    st.session_state.current_page = "main"

with col_nav1:
    if st.button("🏠 HOME", key="nav_home", use_container_width=True):
        st.session_state.current_page = "main"
        st.rerun()

with col_nav2:
    if st.button("🔍 1. محرك البحث العام", key="nav_search", use_container_width=True):
        st.session_state.current_page = "search"
        st.rerun()

with col_nav3:
    if st.button("🔌 2. مهندس اللوحات", key="nav_panels", use_container_width=True):
        st.session_state.current_page = "panels"
        st.rerun()

with col_nav4:
    if st.button("🌳 3. التصفح الهرمي", key="nav_tree", use_container_width=True):
        st.session_state.current_page = "tree"
        st.rerun()

with col_nav5:
    if st.button("💡 HELP", key="nav_help", use_container_width=True):
        st.session_state.current_page = "help"
        st.rerun()

st.markdown("---")

# 📊 دالة مساعدة لتشغيل الأكواد الفرعية بكفاءة
def run_sub_page(file_path):
    if os.path.exists(file_path):
        try:
            with open(file_path, encoding="utf-8") as f:
                code = f.read()
                exec(code, globals())
        except Exception as e:
            st.error(f"حدث خطأ أثناء تشغيل الصفحة: {e}")
    else:
        st.error(f"❌ تعذر العثور على ملف الصفحة في المسار: {file_path}")

# 🗺️ 5. إدارة فتح وتوجيه الصفحات (بناءً على طلبك HOME هي الأساس والمسارات متحكم بها هنا)
if st.session_state.current_page == "main":
    st.markdown("<h3 style='color: #222;'>📂 الأقسام الهندسية المتاحة للدخول الفوري:</h3>", unsafe_allow_html=True)
    
    # كارت 1
    st.markdown("""
    <div class="card-3d">
        <span class="icon-3d">🔎</span>
        <h3>🔍 1. محرك البحث الشامل والسريع</h3>
        <p>البحث التقليدي الفوري في كافة بنود مقايسة الكهرباء الشاملة بمجرد كتابة كلمة أو كود، مع إمكانية استخراج تقارير إكسيل.</p>
    </div>
    """, unsafe_allow_html=True)
    if st.button("🚀 فتح محرك البحث العام", key="btn_go_search", use_container_width=True):
        st.session_state.current_page = "search"
        st.rerun()

    # كارت 2 (شيلنا كلمة رادار)
    st.markdown("""
    <div class="card-3d" style="border-right-color: #00cc66;">
        <span class="icon-3d">🎛️</span>
        <h3>🔌 2. صفحة مهندس اللوحات الكهربائية</h3>
        <p>الفلترة الفنية الدقيقة المخصصة للوحات التوزيع والقدرة بناءً على سعة القاطع، الأمبير، درجة الحماية IP ونوع الأطوار.</p>
    </div>
    """, unsafe_allow_html=True)
    if st.button("🚀 فتح صفحة مهندس اللوحات", key="btn_go_panels", use_container_width=True):
        st.session_state.current_page = "panels"
        st.rerun()

    # كارت 3
    st.markdown("""
    <div class="card-3d" style="border-right-color: #ffaa00;">
        <span class="icon-3d">📊</span>
        <h3>🌳 3. التصفح الهرمي والمقارنة الذكية</h3>
        <p>استكشاف شجري منظم للمجموعات الكهربائية الكبرى وفروعها، وفهم الفروق السعرية بين البنود المتشابهة بالسوق.</p>
    </div>
    """, unsafe_allow_html=True)
    if st.button("🚀 فتح التصفح الهرمي", key="btn_go_tree", use_container_width=True):
        st.session_state.current_page = "tree"
        st.rerun()

elif st.session_state.current_page == "search":
    run_sub_page("pages/search.py")

elif st.session_state.current_page == "panels":
    run_sub_page("pages/2_⚡_مهندس_اللوحات.py")

elif st.session_state.current_page == "tree":
    run_sub_page("pages/3_🌳_التصفح_الهرمي.py")

elif st.session_state.current_page == "help":
    st.header("💡 دليل مساعدة المنظومة الذكية")
    st.info("مرحباً بك في قسم الدعم الفني والمساعدة السريعة للمنظومة.")
    st.markdown("""
    * **للعودة للقائمة الرئيسية**: اضغط دائماً على زرار **🏠 HOME** الثابت في الأعلى.
    * **البحث العام**: يتيح لك البحث الجزئي والكلي، عند كتابة الرقم (مثل 6010) سيقوم بفلترة كافة الأكواد المتطابقة فوراً.
    * **تصدير البيانات**: بعد فلترة أي جدول، سيظهر لك زر أخضر لتحميل النتائج مباشرة إلى ملف Excel على جهازك.
    """)

# 👤 6. إضافة اسمك رسمياً في فريق الإعداد أسفل المنظومة
st.markdown(f"""
    <div class="footer-credits">
        🛠️ <b>فريق الإعداد والتطوير:</b> تم التطوير والإشراف الهندسي بواسطة <b>المهندس مصطفى نصر</b> &copy; {st.date_input("اليوم", disabled=True).year}
    </div>
""", unsafe_allow_html=True)
