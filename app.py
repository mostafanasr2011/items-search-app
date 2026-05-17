import streamlit as st
import pandas as pd
import io
import os

# 1. إعداد واجهة البرنامج
st.set_page_config(page_title="منظومة البحث الذكي", page_icon="🔍", layout="centered")

# ✨ 2. هندسة الـ CSS لتعديل مقاسات الموبايل وتنسيق الأزرار والعناوين
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght=400;600;700&display=swap');
    
    html, body, .stMarkdown, p, h1, h2, h3, h4, h5, h6, span, label, input, button {
        font-family: 'Cairo', sans-serif !important;
        text-align: right;
        direction: rtl !important;
    }
    .main-title {
        font-size: 24px !important;
        font-weight: 700 !important;
        color: #1e3a8a;
        margin-bottom: 5px !important;
        text-align: center !important;
    }
    .sub-title {
        font-size: 14px !important;
        color: #666;
        text-align: center !important;
        margin-bottom: 20px !important;
    }
    [data-testid="stMetricValue"] {
        font-size: 18px !important;
        font-weight: 700 !important;
        color: #2e7d32 !important;
    }
    [data-testid="stMetricLabel"] {
        font-size: 13px !important;
    }
    div.stTextInput > div > div > input {
        border-radius: 8px !important;
        border: 2px solid #1e3a8a !important;
        padding: 12px !important;
        font-size: 16px !important;
    }
    div.stButton > button {
        background-color: #1e3a8a !important;
        color: white !important;
        font-weight: 700 !important;
        font-size: 16px !important;
        padding: 10px 20px !important;
        border-radius: 8px !important;
        border: none !important;
        border-bottom: 4px solid #0f172a !important;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1) !important;
        width: 100% !important;
        cursor: pointer;
    }
    div.stButton > button:active {
        border-bottom: 1px solid #0f172a !important;
        transform: translateY(3px) !important;
    }
    div.stDownloadButton > button {
        background-color: #2e7d32 !important;
        color: white !important;
        font-weight: 700 !important;
        font-size: 15px !important;
        padding: 10px !important;
        border-radius: 8px !important;
        border: none !important;
        border-bottom: 4px solid #1b5e20 !important;
        width: 100% !important;
    }
    [data-testid="stDataFrame"] {
        direction: rtl !important;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">🔍 منظومة البحث الذكي في البنود</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">قاعدة البيانات مدمجة.. اكتب كلمة البحث واضغط على زر البحث لعرض النتائج</div>', unsafe_allow_html=True)

FILE_NAME = "data.xlsx"

def load_fixed_data():
    if os.path.exists(FILE_NAME):
        try:
            return pd.read_excel(FILE_NAME)
        except Exception as e:
            st.error(f"❌ حصلت مشكلة أثناء قراءة ملف البيانات: {e}")
            return pd.DataFrame()
    else:
        st.warning(f"⚠️ تحذير: ملف البيانات الأساسي '{FILE_NAME}' غير موجود.")
        return pd.DataFrame()

df = load_fixed_data()

if not df.empty:
    search_query = st.text_input("✍️ أدخل كلمة البحث أو الكود هنا:", placeholder="مثال: كشاف، كابل، حجر...")
    search_clicked = st.button("ابحث الآن 🔍")

    if "search_active" not in st.session_state:
        st.session_state.search_active = False

    if search_clicked:
        st.session_state.search_active = True

    if st.session_state.search_active and search_query:
        try:
            q = str(search_query).strip().lower()
            mask = df.astype(str).apply(lambda x: x.str.lower().str.contains(q, na=False)).any(axis=1)
            search_result = df[mask]
        except Exception as e:
            st.error(f"حدثت مشكلة أثناء الفلترة: {e}")
            search_result = df

        st.markdown(f"### 📊 النتائج المتاحة ({len(search_result)} بند)")
        
        if not search_result.empty:
            try:
                col_price = df.columns[3]
                prices = pd.to_numeric(search_result[col_price], errors='coerce')
                
                c1, c2 = st.columns(2)
                with c1:
                    st.metric("أعلى سعر في البحث", f"{prices.max():,.2f} ج.م" if not pd.isna(prices.max()) else "0.00")
                with c2:
                    st.metric("أقل سعر في البحث", f"{prices.min():,.2f} ج.م" if not pd.isna(prices.min()) else "0.00")
            except:
                pass 
                
            st.dataframe(search_result, use_container_width=True, hide_index=True)
            
            try:
                buffer = io.BytesIO()
                with pd.ExcelWriter(buffer, engine='openpyxl') as writer:
                    search_result.to_excel(writer, index=False, sheet_name='نتائج البحث')
                
                st.write("")
                st.download_button(
                    label="📥 تحميل هذه النتائج كملف Excel",
                    data=buffer.getvalue(),
                    file_name=f"نتائج_بحث_{search_query}.xlsx",
                    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                )
            except Exception as e:
                st.error(f"تعذر تجهيز ملف التحميل: {e}")
        else:
            st.info("ℹ️ لم يتم العثور على بنود تطابق كلمة البحث. جرب كلمة أخرى!")
    else:
        st.write("")
        st.info("💡 الشاشة جاهزة ونظيفة.. اكتب كلمة فوق واضغط 'ابحث الآن 🔍' لإظهار البنود المطلوبة ومداها السعري.")