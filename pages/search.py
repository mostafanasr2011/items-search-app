import streamlit as st
import pandas as pd
import io
import os

st.title("🔍 محرك البحث العام في بنود الكهرباء")
st.write("استخدم صندوق البحث في الأسفل للعثور على أي بند من بنود مقايسة الكهرباء الشاملة.")

EXCEL_PATH = os.path.join("data", "items.xlsx")

@st.cache_data
def load_data():
    if os.path.exists(EXCEL_PATH):
        df = pd.read_excel(EXCEL_PATH, engine='openpyxl')
        df.columns = df.columns.str.strip()
        return df
    elif os.path.exists("data.xlsx"):
        df = pd.read_excel("data.xlsx", engine='openpyxl')
        df.columns = df.columns.str.strip()
        return df
    else:
        st.error("❌ تعذر العثور على ملف البيانات إكسيل.")
        return None

df = load_data()

if df is not None:
    search_query = st.text_input("✍️ اكتب كلمة البحث أو الكود (مثال: كشاف، لوحة، كابل):", key="global_search_input").strip()

    if search_query:
        mask = df.astype(str).apply(lambda row: row.str.contains(search_query, case=False, na=False)).any(axis=1)
        search_result = df[mask]

        if not search_result.empty:
            st.success(f"✅ تم العثور على ({len(search_result)}) بند يطابق كلمة: '{search_query}'")
            st.dataframe(search_result, use_container_width=True, hide_index=True)
            
            try:
                buffer = io.BytesIO()
                with pd.ExcelWriter(buffer, engine='openpyxl') as writer:
                    search_result.to_excel(writer, index=False, sheet_name='نتائج البحث')
                
                st.download_button(
                    label="📥 تحميل هذه النتائج كملف Excel",
                    data=buffer.getvalue(),
                    file_name=f"نتائج_بحث_{search_query}.xlsx",
                    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                    key="btn_download_search"
                )
            except Exception as e:
                st.error(f"تعذر تجهيز ملف التحميل: {e}")
        else:
            st.info("ℹ️ لم يتم العثور على بنود تطابق كلمة البحث.")
