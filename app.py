%%writefile app.py
import streamlit as st
import pandas as pd
import io

# 1. إعداد واجهة البرنامج
st.set_page_config(page_title="منظومة البحث الذكي في البنود", page_icon="🔍", layout="centered")

# ✨ 2. لمسات الـ CSS السحرية للأزرار والخطوط والجدول
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700&display=swap');
    
    html, body, [data-testid="stSidebar"], .stMarkdown, p, h1, h2, h3, h4, h5, h6, span, label, input, button {
        font-family: 'Cairo', sans-serif !important;
        text-align: right;
    }
    
    .block-container {
        padding-top: 2rem !important;
        padding-bottom: 2rem !important;
        max-width: 900px !important;
    }
    
    [data-testid="stFileUploadDropzone"] {
        border: 2px dashed #3f51b5 !important;
        background-color: #f5f7ff;
        border-radius: 12px;
    }
    
    /* ضبط اتجاه الجداول لتكون من اليمين للشمال مخصصة للعربي */
    [data-testid="stDataFrame"] {
        direction: rtl !important;
    }
    
    /* تصميم الأزرار الـ 3D الحقيقية */
    div.stDownloadButton > button {
        background-color: #2e7d32 !important;
        color: white !important;
        font-weight: 700 !important;
        font-size: 16px !important;
        padding: 12px 24px !important;
        border-radius: 8px !important;
        border: none !important;
        border-bottom: 5px solid #1b5e20 !important; 
        box-shadow: 0 5px 10px rgba(0,0,0,0.2) !important;
        transition: all 0.1s ease !important;
        width: 100%;
        cursor: pointer;
    }
    
    div.stDownloadButton > button:hover {
        background-color: #338a3e !important;
    }
    
    div.stDownloadButton > button:active {
        border-bottom: 1px solid #1b5e20 !important;
        transform: translateY(4px) !important;
        box-shadow: 0 1px 3px rgba(0,0,0,0.2) !important;
    }
    
    div.stTextInput > div > div > input {
        border-radius: 8px !important;
        border: 1px solid #ccc !important;
        padding: 10px !important;
    }
    </style>
""", unsafe_allow_html=True)

# 3. محتوى الواجهة الرئيسي
st.title("🔍 منظومة البحث الذكي في بيانات البنود")
st.write("ارفع ملف أو عدة ملفات أكسيل معاً، وابحث في آلاف الصفوف المدمجة فوراً!")

# 4. أداة رفع الملفات
uploaded_files = st.file_uploader(
    "📂 اسحب وأفلت ملفات الأكسيل هنا (يمكنك اختيار أكثر من ملف معاً):", 
    type=["xlsx", "xls", "csv"],
    accept_multiple_files=True
)

@st.cache_data
def load_and_combine_data(files_list):
    combined_df = pd.DataFrame()
    for file in files_list:
        try:
            if file.name.endswith('.csv'):
                current_df = pd.read_csv(file)
            else:
                current_df = pd.read_excel(file)
            combined_df = pd.concat([combined_df, current_df], ignore_index=True)
        except Exception as e:
            st.error(f"❌ حصلت مشكلة في ملف {file.name}: {e}")
    return combined_df

if uploaded_files:
    df = load_and_combine_data(uploaded_files)
    
    st.sidebar.markdown("### 🛠️ تصفية وفلترة البحث")
    search_query = st.sidebar.text_input("✍️ اكتب كلمة البحث هنا:", placeholder="مثال: كشاف، جوكي، متر...")

    if not df.empty and search_query:
        try:
            col_id = df.columns[0]     
            col_spec = df.columns[1]   
            col_unit = df.columns[2]   
            col_price = df.columns[3]  
            
            search_result = df[
                df[col_id].astype(str).str.contains(search_query, case=False, na=False) |
                df[col_spec].astype(str).str.contains(search_query, case=False, na=False) |
                df[col_unit].astype(str).str.contains(search_query, case=False, na=False) |
                df[col_price].astype(str).str.contains(search_query, na=False)
            ]
        except Exception as e:
            st.error(f"حدثت مشكلة أثناء الفلترة: {e}")
            search_result = df
    else:
        search_result = df 

    if not df.empty:
        st.subheader(f"📊 النتائج المتاحة ({len(search_result)} بند مدمج)")
        
        try:
            col_price = df.columns[3]
            prices = pd.to_numeric(search_result[col_price], errors='coerce')
            
            col1, col2 = st.columns(2)
            with col1:
                st.metric("أعلى سعر في نتائج البحث", f"{prices.max():,.2f} ج.م" if not pd.isna(prices.max()) else "N/A")
            with col2:
                st.metric("أقل سعر في نتائج البحث", f"{prices.min():,.2f} ج.م" if not pd.isna(prices.min()) else "N/A")
        except:
            pass 
            
        # 💡 التعديل السحري هنا: hide_index=True عشان يشيل العمود (0, 1, 2) ويوفر مساحة على الموبايل
        st.dataframe(search_result, use_container_width=True, hide_index=True)
        
        st.write("---")
        try:
            buffer = io.BytesIO()
            with pd.ExcelWriter(buffer, engine='openpyxl') as writer:
                search_result.to_excel(writer, index=False, sheet_name='نتائج البحث')
            
            st.download_button(
                label="📥 اضغط هنا لتحميل نتائج البحث كملف Excel مدمج",
                data=buffer.getvalue(),
                file_name=f"نتائج_بحث_مدمجة_{search_query if search_query else 'الكل'}.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )
        except Exception as e:
            st.error(f"تعذر تجهيز ملف التحميل: {e}")
else:
    st.info("💡 في انتظار رفع ملف أكسيل واحد أو أكثر لبدء تشغيل المنظومة...")