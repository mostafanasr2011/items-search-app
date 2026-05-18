import streamlit as st
import pandas as pd
import io
import os

# 1. إعداد واجهة المنظومة وإخفاء السايد بار تماماً
st.set_page_config(
    page_title="منظومة الهندسة الكهربائية الذكية", 
    page_icon="⚡", 
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ✨ 2. هندسة الـ CSS الموحدة: باليتة ألوان جوجل + عمق ثلاثي الأبعاد + خطوط عملاقة لكل الصفحات
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght=400;600;700;900&display=swap');
    
    html, body, .stApp, .stMarkdown, p, h1, h2, h3, h4, h5, h6, span, label, input, button, select {
        font-family: 'Cairo', sans-serif !important;
        text-align: right !important;
        direction: rtl !important;
    }
    
    /* إخفاء السايد بار والعلائم الافتراضية تماماً */
    [data-testid="stSidebar"], .viewerBadge_link__1S137, .styles_viewerBadge__3uC9V, [data-testid="bundle-footer"], footer {
        display: none !important;
        visibility: hidden !important;
    }
    .block-container { padding-top: 1rem !important; }

    /* عنوان المنظومة الكبير بألوان جوجل */
    .main-header-title {
        background: linear-gradient(45deg, #4285F4, #34A853, #FBBC05, #EA4335);
        background-size: 300% 300%;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 42px !important;
        font-weight: 900;
        text-align: center !important;
        margin-bottom: 5px;
    }
    
    .main-subtitle {
        text-align: center !important;
        font-size: 18px;
        color: #5f6368;
        margin-bottom: 25px;
    }

    /* 💎 كروت 3D عميقة وفخمة */
    .card-3d-deep {
        background: #ffffff;
        border-radius: 20px;
        box-shadow: 12px 12px 25px rgba(0, 0, 0, 0.12), -8px -8px 20px rgba(255, 255, 255, 0.9);
        padding: 25px 30px;
        margin-bottom: 15px;
        transition: all 0.4s ease;
        border: 1px solid rgba(0,0,0,0.02);
    }
    
    .card-3d-deep:hover {
        transform: translateY(-6px);
        box-shadow: 20px 20px 35px rgba(0, 0, 0, 0.16), -12px -12px 25px rgba(255, 255, 255, 1);
    }

    /* المربع الملكي المطور داخل صفحة البحث */
    .gold-card-3d {
        background: #ffffff;
        border-radius: 20px;
        box-shadow: 12px 12px 25px rgba(0, 0, 0, 0.12), -8px -8px 20px rgba(255, 255, 255, 0.9);
        padding: 30px;
        margin-top: 20px;
        margin-bottom: 20px;
        border-right: 12px solid #FBBC05;
    }
    .gold-card-3d h3 { color: #B07D00 !important; font-weight: 900 !important; font-size: 26px !important; }
    .gold-card-3d p { font-size: 19px !important; font-weight: 600 !important; line-height: 1.9 !important; color: #202124 !important; }

    /* تلوين الكروت بباليتة جوجل */
    .google-blue { border-right: 12px solid #4285F4; }
    .google-green { border-right: 12px solid #34A853; }
    .google-yellow { border-right: 12px solid #FBBC05; }
    .google-red { border-right: 12px solid #EA4335; }

    .icon-3d { font-size: 48px; float: left; filter: drop-shadow(4px 6px 8px rgba(0,0,0,0.15)); margin-top: -5px; }
    
    /* 🚀 أزرار الصواريخ والتنقل العملاقة */
    div.stButton > button {
        font-size: 22px !important;
        font-weight: 700 !important;
        padding: 14px 30px !important;
        border-radius: 14px !important;
        box-shadow: 0 5px 18px rgba(0,0,0,0.12) !important;
        transition: all 0.3s ease !important;
    }
    div.stButton > button:hover { transform: scale(1.015) !important; box-shadow: 0 8px 25px rgba(0,0,0,0.18) !important; }

    /* أزرار التنقل الفرعية (السابق والتالي) */
    .nav-btn div.stButton > button { background-color: #f1f5f9 !important; color: #1e293b !important; font-size: 18px !important; }

    .help-box { background: #f8f9fa; border-radius: 14px; padding: 20px; margin-bottom: 18px; border-left: 6px solid #4285F4; font-size: 16px; }
    .footer-credits { text-align: center !important; font-size: 16px; color: #3c4043; font-weight: 600; margin-top: 60px; padding: 25px; border-top: 2px dashed #dadce0; background: #f8f9fa; border-radius: 10px; }
    </style>
""", unsafe_allow_html=True)

# 🏢 3. اسم المنظومة الثابت
st.markdown('<h1 class="main-header-title">⚡ المنظومة الذكية لتسعير وبحوث بنود الكهرباء</h1>', unsafe_allow_html=True)
st.markdown('<p class="main-subtitle">الهيئة العامة للأبنية التعليمية | الإشراف الفني: المهندس مصطفى نصر &copy; ٢٠٢٦</p>', unsafe_allow_html=True)

# 🌐 4. شريط التحكم السريع العلوي الألوان
st.markdown("<h4 style='text-align: center; color: #202124; margin-bottom: 15px; font-weight:700;'>🌐 لوحة التحكم السريع للمنظومة</h4>", unsafe_allow_html=True)
col_nav1, col_nav2, col_nav3, col_nav4, col_nav5 = st.columns([1.2, 2, 2, 2, 1.2])

if "current_page" not in st.session_state:
    st.session_state.current_page = "main"

with col_nav1:
    if st.button("🏠 HOME", key="nav_home", use_container_width=True): st.session_state.current_page = "main"; st.rerun()
with col_nav2:
    if st.button("🔍 1. محرك البحث العام", key="nav_search", use_container_width=True): st.session_state.current_page = "search"; st.rerun()
with col_nav3:
    if st.button("🔌 2. صفحة مهندس اللوحات", key="nav_panels", use_container_width=True): st.session_state.current_page = "panels"; st.rerun()
with col_nav4:
    if st.button("🌳 3. التصفح الهرمي", key="nav_tree", use_container_width=True): st.session_state.current_page = "tree"; st.rerun()
with col_nav5:
    if st.button("💡 HELP", key="nav_help", use_container_width=True): st.session_state.current_page = "help"; st.rerun()

st.markdown("---")

# دالة ذكية لتشغيل الصفحات الفرعية بأمان بدون كسر التصميم الإخراجي
def run_sub_page(file_path):
    if os.path.exists(file_path):
        try:
            with open(file_path, encoding="utf-8") as f:
                code = f.read()
                # إزالة أي إعداد واجهة فرعي قد يسبب اختفاء باقي الصفحات
                clean_code = code.replace("st.set_page_config", "# st.set_page_config")
                exec(clean_code, globals())
        except Exception as e:
            st.error(f"حدث خطأ أثناء تشغيل الصفحة: {e}")
    else:
        st.error(f"❌ لم يتم العثور على ملف الصفحة في المسار: {file_path}")

# 🗺️ 5. إدارة التنقل بين الصفحات
if st.session_state.current_page == "main":
    st.markdown("<h3 style='color: #202124; font-weight:700; margin-bottom:15px;'>📂 الأقسام الهندسية المتاحة للدخول الفوري:</h3>", unsafe_allow_html=True)
    
    # كارت 1
    st.markdown('<div class="card-3d-deep google-blue"><span class="icon-3d">🔎</span><h2 style="color: #4285F4; font-weight: 700; font-size:24px; margin-bottom:5px;">🔍 1. محرك البحث الشامل والسريع</h2><p style="color: #5f6368; font-size: 16px; font-weight:600;">البحث الفوري والذكي في كافة بنود مقايسة الكهرباء مع ميزة الكشيدة والمربع الملكي التفاعلي.</p></div>', unsafe_allow_html=True)
    if st.button("🚀 فتح محرك البحث العام الشامل", key="btn_go_search", use_container_width=True): st.session_state.current_page = "search"; st.rerun()

    # كارت 2
    st.markdown('<div class="card-3d-deep google-green"><span class="icon-3d">🎛️</span><h2 style="color: #34A853; font-weight: 700; font-size:24px; margin-bottom:5px;">🔌 2. صفحة مهندس اللوحات الكهربائية</h2><p style="color: #5f6368; font-size: 16px; font-weight:600;">الفلترة الفنية الدقيقة المخصصة لوصف وجداول لوحات التوزيع بناءً على سعة القاطع والأمبير.</p></div>', unsafe_allow_html=True)
    if st.button("🚀 فتح صفحة مهندس اللوحات التخصصية", key="btn_go_panels", use_container_width=True): st.session_state.current_page = "panels"; st.rerun()

    # كارت 3
    st.markdown('<div class="card-3d-deep google-yellow"><span class="icon-3d">📊</span><h2 style="color: #FBBC05; font-weight: 700; font-size:24px; margin-bottom:5px;">🌳 3. التصفح الهرمي والمقارنة الذكية</h2><p style="color: #5f6368; font-size: 16px; font-weight:600;">استكشاف شجري منظم للمجموعات الكهربائية الكبرى وفروعها لتتبع الفروق السعرية.</p></div>', unsafe_allow_html=True)
    if st.button("🚀 فتح منظومة التصفح الهرمي والمقارنة", key="btn_go_tree", use_container_width=True): st.session_state.current_page = "tree"; st.rerun()

elif st.session_state.current_page == "search":
    run_sub_page("pages/search.py")

elif st.session_state.current_page == "panels":
    run_sub_page("pages/2_⚡_مهندس_اللوحات.py")

elif st.session_state.current_page == "tree":
    run_sub_page("pages/3_🌳_التصفح_الهرمي.py")

elif st.session_state.current_page == "help":
    # عرض صفحة المساعدة الفاخرة
    st.markdown('<div class="card-3d-deep google-red"><span class="icon-3d">ℹ️</span><h2 style="color: #EA4335; font-weight: 700; font-size:26px;">💡 دليل المساعدة والدعم الفني للمنظومة</h2></div>', unsafe_allow_html=True)
    st.markdown('<div class="help-box"><h4>🔍 محرك البحث</h4><p>يدعم البحث العادي وبحث كود الكشيدة للأبنية التعليمية مع المربع الملكي التفاعلي وأزرار النسخ السريع.</p></div>', unsafe_allow_html=True)

# 👤 6. التوقيع
st.markdown('<div class="footer-credits">🛠️ <b>فريق الإعداد والتطوير للمنظومة:</b> تم التصميم والتطوير بالكامل تحت الإشراف الهندسي لـ <b>المهندس مصطفى نصر</b> &copy; ٢٠٢٦</div>', unsafe_allow_html=True)
