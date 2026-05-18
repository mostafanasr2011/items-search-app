import streamlit as st

# 1. إعداد واجهة المنظومة وتحديد التصميم العريض
st.set_page_config(
    page_title="منظومة الهندسة الكهربائية الذكية", 
    page_icon="⚡", 
    layout="wide"
)

# ✨ 2. الشخلعة والألوان (هندسة الـ CSS والتصميم ثلاثي الأبعاد والخطوط العربي)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght=400;600;700;900&display=swap');
    
    /* توحيد الخطوط والاتجاه العربي المظبوط */
    html, body, .stApp, .stMarkdown, p, h1, h2, h3, h4, h5, h6, span, label, input, button, select {
        font-family: 'Cairo', sans-serif !important;
        text-align: right !important;
        direction: rtl !important;
    }
    
    /* إخفاء علامات ومخلفات ستريمليت المزعجة */
    .viewerBadge_link__1S137, .styles_viewerBadge__3uC9V, [data-testid="bundle-footer"], footer {
        visibility: hidden !important;
        display: none !important;
    }
    .block-container { padding-top: 1.5rem !important; }

    /* تصميم العنوان الرئيسي المتوهج */
    .main-title {
        background: linear-gradient(45deg, #ff9a9e, #fecfef, #feada6, #f33b57);
        background-size: 400% 400%;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 40px !important;
        font-weight: 900;
        text-align: center !important;
        margin-bottom: 5px;
    }

    /* كروت التصميم الاحترافي ثلاثي الأبعاد المشخلع */
    .card-3d {
        background: rgba(255, 255, 255, 0.85);
        border-radius: 16px;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1), inset 0 1px 3px rgba(255, 255, 255, 0.5);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.2);
        padding: 25px;
        margin-bottom: 25px;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    .card-3d:hover {
        transform: translateY(-5px) scale(1.01);
        box-shadow: 0 20px 40px rgba(0, 77, 255, 0.15);
    }

    /* أنظمة تلوين الحواف للكروت */
    .search-border { border-right: 8px solid #0052cc; }
    .panels-border { border-right: 8px solid #00cc66; }
    .tree-border { border-right: 8px solid #ffaa00; }

    /* أيقونات ثلاثية الأبعاد متحركة */
    .icon-3d {
        font-size: 45px;
        float: left;
        filter: drop-shadow(3px 5px 5px rgba(0,0,0,0.15));
    }
    </style>
""", unsafe_allow_html=True)

# 3. نظام الملاحة الذكي لإصلاح قطع الصفحة والـ Sidebar
pg_main = st.Page("app.py", title="الشاشة الرئيسية للمنظومة", icon="🏠")
pg_search = st.Page("pages/search.py", title="1. محرك البحث العام والسريع", icon="🔍")
pg_panels = st.Page("pages/2_⚡_مهندس_اللوحات.py", title="2. رادار مهندس اللوحات", icon="⚡")
pg_tree = st.Page("pages/3_🌳_التصفح_الهرمي.py", title="3. التصفح الهرمي والمقارنة", icon="🌳")

pg = st.navigation([pg_main, pg_search, pg_panels, pg_tree])
pg.run()

# 4. عرض محتوى الشاشة الترحيبية الفخمة فقط إذا كنا في الصفحة الرئيسية
if pg == pg_main:
    st.markdown('<h1 class="main-title">⚡ المنظومة الذكية لتسعير وبحوث بنود الكهرباء</h1>', unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 18px; color: #555;'>مرحباً بك يا هندسة في مستودعك الرقمي الفخم. اختر وجهتك الآن بضغطة واحدة من الكروت الملونة بالأسفل أو من القائمة الجانبية.</p>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    # --- كارت 1: البحث العام الشامل ---
    st.markdown("""
    <div class="card-3d search-border">
        <span class="icon-3d">🔎</span>
        <h3 style="color: #0052cc; font-weight: 700;">🔍 1. محرك البحث الشامل والسريع</h3>
        <p style="color: #444; font-size: 15px;">البحث الفوري والذكي في كافة البنود بمجرد كتابة كلمة أو كود، مع خاصية استخراج وتقارير إكسيل فورية.</p>
    </div>
    """, unsafe_allow_html=True)
    if st.button("🚀 دخول محرك البحث العام", key="go_search", use_container_width=True):
        st.switch_page(pg_search)

    # --- كارت 2: رادار اللوحات ---
    st.markdown("""
    <div class="card-3d panels-border">
        <span class="icon-3d">🎛️</span>
        <h3 style="color: #00cc66; font-weight: 700;">⚡ 2. رادار مهندس اللوحات الكهربائية</h3>
        <p style="color: #444; font-size: 15px;">الفلترة الهندسية الدقيقة للوحات الكهرباء بناءً على سعة القاطع، الأمبير، درجة الحماية IP، ونظام الأطوار.</p>
    </div>
    """, unsafe_allow_html=True)
    if st.button("🚀 دخول رادار اللوحات", key="go_panels", use_container_width=True):
        st.switch_page(pg_panels)

    # --- كارت 3: التصفح الهرمي ---
    st.markdown("""
    <div class="card-3d tree-border">
        <span class="icon-3d">📊</span>
        <h3 style="color: #ffaa00; font-weight: 700;">🌳 3. التصفح الهرمي والمقارنة الذكية</h3>
        <p style="color: #444; font-size: 15px;">تصفح شجري ذكي لاستكشاف المجموعات، وفهم فروق الأسعار بين البنود المتشابهة في السوق.</p>
    </div>
    """, unsafe_allow_html=True)
    if st.button("🚀 دخول التصفح الهرمي", key="go_tree", use_container_width=True):
        st.switch_page(pg_tree)
