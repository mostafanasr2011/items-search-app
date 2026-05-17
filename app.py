import streamlit as st
import pandas as pd
import io
import os

# 1. إعداد واجهة البرنامج وإخفاء القوائم الافتراضية لمنصات الـ Cloud
st.set_page_config(page_title="منظومة البحث الذكي", page_icon="🔍", layout="centered")

# ✨ 2. هندسة الـ CSS المتقدمة لضبط الأزرار أفقياً حتى على الموبايل
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght=400;600;700&display=swap');
    
    html, body, .stMarkdown, p, h1, h2, h3, h4, h5, h6, span, label, input, button {
        font-family: 'Cairo', sans-serif !important;
        text-align: right;
        direction: rtl !important;
    }
    
    /* إخفاء أيقونات جيت هاب، الثلاث نقاط، والشريط السفلي تماماً لنظافة التطبيق */
    #MainMenu, header, footer, [data-testid="stHeader"], [data-testid="stDecoration"] {
        visibility: hidden !important;
        display: none !important;
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
        font-size: 16px !important;
        font-weight: 700 !important;
        color: #2e7d32 !important;
    }
    [data-testid="stMetricLabel"] {
        font-size: 12px !important;
    }
    
    /* تصميم كارت عرض البند الفردي باللون الأصفر الذهبي الملكي */
    .gold-card {
        background-color: #fef08a !important;
        border-right: 8px solid #ca8a04 !important;
        padding: 15px !important;
        border-radius: 8px !important;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05) !important;
        margin-bottom: 15px !important;
        color: #1e293b !important;
    }
    
    div.stTextInput > div > div > input {
        border-radius: 8px !important;
        border: 2px solid #1e3a8a !important;
        padding: 10px !important;
        font-size: 16px !important;
    }
    
    /* زرار البحث الأزرق */
    div.stButton > button {
        background-color: #1e3a8a !important;
        color: white !important;
        font-weight: 700 !important;
        font-size: 16px !important;
        padding: 10px 15px !important;
        border-radius: 8px !important;
        border: none !important;
        border-bottom: 4px solid #0f172a !important;
        width: 100% !important;
        cursor: pointer;
    }
    
    /* 🌟 سحر الـ CSS: إجبار أزرار التنقل والبحث على البقاء أفقياً حتى في الشاشات الصغيرة للمحمول */
    [data-testid="stHorizontalBlock"] {
        display: flex !important;
        flex-direction: row !important;
        align-items: center !important;
        gap: 10px !important;
    }
    [data-testid="stHorizontalBlock"] > div {
        width: auto !important;
        flex-grow: 1 !important;
    }
    
    .nav-btn div.stButton > button {
        background-color: #f1f5f9 !important;
        color: #1e293b !important;
        border: 1px solid #cbd5e1 !important;
        border-bottom: 3px solid #94a3b8 !important;
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

st.markdown('<div class="main-title">🔍 منظومة البحث الذكي والفحص المتتالي</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">تصميم هندسي فاخر مخصص للهواتف الذكية</div>', unsafe_allow_html=True)

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

def convert_to_kashida_code(input_str):
    num_map = {'0':'٠', '1':'١', '2':'٢', '3':'٣', '4':'٤', '5':'٥', '6':'٦', '7':'٧', '8':'٨', '9':'٩'}
    clean_str = input_str.strip()
    arabic_digits = "".join([num_map.get(char, char) for char in clean_str])
    if len(arabic_digits) == 4 and arabic_digits.isdigit():
        return f"{arabic_digits[0]}ــ{arabic_digits[1]}ــ{arabic_digits[2]}ــ{arabic_digits[3]}"
    return arabic_digits

df = load_fixed_data()

if "current_index" not in st.session_state:
    st.session_state.current_index = 0
if "last_query" not in st.session_state:
    st.session_state.last_query = ""

if not df.empty:
    search_type = st.radio(
        "🗂️ اختر طريقة البحث المناسبة لكود البند:",
        ["🔍 بحث عام / بنود كهرباء (أرقام عادية أو نصوص)", "✍️ بنود كود الكشيدة (اكتب الأرقام عادية مثل 1124)"]
    )

    col_input, col_btn = st.columns([4, 1])
    with col_input:
        search_query = st.text_input("✍️ أدخل كلمة البحث أو الكود هنا بدون شرط:", placeholder="مثال: 6010151 أو 1124...", label_visibility="collapsed")
    with col_btn:
        search_clicked = st.button("بحث 🔍")

    if search_query != st.session_state.last_query:
        st.session_state.current_index = 0
        st.session_state.last_query = search_query

    if (search_clicked or search_query) and search_query:
        final_query = search_query.strip().lower()
        if "بنود كود الكشيدة" in search_type:
            final_query = convert_to_kashida_code(search_query)

        try:
            mask = df.astype(str).apply(lambda x: x.str.lower().str.contains(final_query, na=False)).any(axis=1)
            search_result = df[mask]
        except Exception as e:
            st.error(f"حدثت مشكلة أثناء الفلترة: {e}")
            search_result = df

        if not search_result.empty:
            total_items = len(search_result)
            st.markdown(f"### 📊 النتائج المتاحة ({total_items} بند)")
            
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

            if st.session_state.current_index >= total_items:
                st.session_state.current_index = 0

            current_row = search_result.iloc[st.session_state.current_index]
            
            st.markdown(f"""
            <div class="gold-card">
                <strong>📌 البند الحالي المختار ({st.session_state.current_index + 1} من {total_items}):</strong><br>
                <hr style="margin: 8px 0; border: 0; border-top: 1px solid #e2e8f0;">
                • <b>كود البند:</b> {current_row.iloc[0]}<br>
                • <b>وصف البند:</b> {current_row.iloc[1]}<br>
                • <b>الفئة/الوحدة:</b> {current_row.iloc[2]}<br>
                • <b>السعر:</b> <span style="color:#b45309; font-weight:bold;">{current_row.iloc[3]} ج.م</span>
            </div>
            """, unsafe_allow_html=True)

            col_prev, col_next = st.columns(2)
            with col_prev:
                st.markdown('<div class="nav-btn">', unsafe_allow_html=True)
                if st.button("➡️ البند السابق"):
                    if st.session_state.current_index > 0:
                        st.session_state.current_index -= 1
                        st.rerun()
                st.markdown('</div>', unsafe_allow_html=True)
                
            with col_next:
                st.markdown('<div class="nav-btn">', unsafe_allow_html=True)
                if st.button("⬅️ البند التالي"):
                    if st.session_state.current_index < total_items - 1:
                        st.session_state.current_index += 1
                        st.rerun()
                st.markdown('</div>', unsafe_allow_html=True)

            st.write("---")
            st.dataframe(search_result, use_container_width=True, hide_index=True)
            
            try:
                buffer = io.BytesIO()
                with pd.ExcelWriter(buffer, engine='openpyxl') as writer:
                    search_result.to_excel(writer, index=False, sheet_name='نتائج البحث')
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
        st.info("💡 الشاشة جاهزة ونظيفة.. اختر النوع، اكتب الكود واضغط 'بحث 🔍' لبدء التصفح الفاخر.")