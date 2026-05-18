import streamlit as st

# 1. إعداد الصفحة وتخريب السايد بار الافتراضي (هنخفيه تماماً عشان نعتمد على الشريط العلوي)
st.set_page_config(
    page_title="منظومة الهندسة الكهربائية الذكية", 
    page_icon="⚡", 
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ✨ 2. الشخلعة والألوان وتصميم الشريط العلوي الثابت
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght=400;600;700;900&display=swap');
    
    html, body, .stApp, .stMarkdown, p, h1, h2, h3, h4, h5, h6, span, label, input, button, select {
        font-family: 'Cairo', sans-serif !important;
        text-align: right !important;
        direction: rtl !important;
    }
    
    /* إخفاء القائمة الجانبية تماماً وأي أزرار افتراضية مسببة للمشاكل */
    [data-testid="stSidebar"], .viewerBadge_link__1S137, .styles_viewerBadge__3uC9V, [data-testid="bundle-footer"], footer {
        display: none !important;
        visibility: hidden !important;
    }
    .block-container { padding-top: 1rem !important; }

    /* عنوان رئيسي متوهج */
    .main-title {
        background: linear-gradient(45deg, #007bff, #00ffcc, #ff007f);
        background-size: 300% 300%;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 38px !important;
        font-weight: 900;
        text-align: center !important;
        margin-bottom: 20px;
    }

    /* كروت التصميم ثلاثي الأبعاد */
    .card-3d {
        background: rgba(255, 255, 255, 0.9);
        border-radius: 16px;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.08);
        border-right: 8px solid #007bff;
        padding: 25px;
        margin-bottom: 20px;
    }
    .icon-3d { font-size: 40px; float: left; }
    </style>
""", unsafe_allow_html=True)

# 3. عمل شريط التنقل العلوي الاحترافي والأزرار
st.markdown("<h3 style='text-align: center; color: #333; margin-bottom: 5px;'>🌐 لوحة التحكم السريع للمنظومة</h3>", unsafe_allow_html=True)
col_nav1, col_nav2, col_nav3, col_nav4 = st.columns([1, 2, 2, 2])

with col_nav1:
    if st.button("🏠 HOME", key="nav_home", use_container_width=True):
        st.session_state.current_page = "main"
        st.rerun()

with col_nav2:
    if st.button("🔍 1. محرك البحث العام", key="nav_search", use_container_width=True):
        st.session_state.current_page = "search"
        st.rerun()

with col_nav3:
    if st.button("⚡ 2. رادار مهندس اللوحات", key="nav_panels", use_container_width=True):
        st.session_state.current_page = "panels"
        st.rerun()

with col_nav4:
    if st.button("🌳 3. التصفح الهرمي", key="nav_tree", use_container_width=True):
        st.session_state.current_page = "tree"
        st.rerun()

st.markdown("---")

# 4. إدارة الصفحات الذكية بناءً على الضغط (تجنباً لمشاكل المسارات المقفولة)
if "current_page" not in st.session_state:
    st.session_state.current_page = "main"

# --- عرض محتوى الصفحة الرئيسية ---
if st.session_state.current_page == "main":
    st.markdown('<h1 class="main-title">⚡ المنظومة الذكية لتسعير وبحوث بنود الكهرباء</h1>', unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 18px; color: #555;'>مرحباً بك يا هندسة. استخدم شريط الأزرار العلوي الأزرق للانتقال الفوري بين أقسام المنظومة وعش التجربة الاحترافية.</p>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("""
    <div class="card-3d">
        <span class="icon-3d">🔎</span>
        <h3>🔍 1. محرك البحث الشامل والسريع</h3>
        <p>البحث الفوري والذكي في كافة البنود بمجرد كتابة كلمة أو كود، مع خاصية استخراج وتقارير إكسيل فورية.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="card-3d" style="border-right-color: #00cc66;">
        <span class="icon-3d">🎛️</span>
        <h3>⚡ 2. رادار مهندس اللوحات الكهربائية</h3>
        <p>الفلترة الهندسية الدقيقة للوحات الكهرباء بناءً على سعة القاطع، الأمبير، درجة الحماية IP، ونظام الأطوار.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="card-3d" style="border-right-color: #ffaa00;">
        <span class="icon-3d">📊</span>
        <h3>🌳 3. التصفح الهرمي والمقارنة الذكية</h3>
        <p>تصفح شجري ذكي لاستكشاف المجموعات، وفهم فروق الأسعار بين البنود المتشابهة في السوق.</p>
    </div>
    """, unsafe_allow_html=True)

# --- استدعاء صفحة البحث العام في نفس المكان وبدون قطع ---
elif st.session_state.current_page == "search":
    try:
        with open("pages/search.py", encoding="utf-8") as f:
            code = f.read()
            exec(code)
    except Exception as e:
        st.error(f"حدث خطأ أثناء تحميل صفحة البحث: {e}")

elif st.session_state.current_page == "panels":
    st.info("🚧 صفحة رادار مهندس اللوحات قيد التشغيل الفوري.. استخدم أزرار التحكم بالأعلى للتنقل.")

elif st.session_state.current_page == "tree":
    st.info("🚧 صفحة التصفح الهرمي قيد التشغيل الفوري.. استخدم أزرار التحكم بالأعلى للتنقل.")
