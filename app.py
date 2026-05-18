import streamlit as st
import pandas as pd
import io
import os

# تكبير العناوين والخطوط جوه صفحة البحث
st.markdown("""
    <style>
    .gold-box {
        background: linear-gradient(135deg, #FFF7E6, #FFF1D0);
        border: 2px solid #FBBC05;
        border-radius: 15px;
        padding: 25px;
        margin-top: 20px;
        margin-bottom: 20px;
        box-shadow: 0 10px 25px rgba(251, 188, 5, 0.2);
        direction: rtl !important;
        text-align: right !important;
    }
    .gold-box h3 {
        color: #B07D00 !important;
        font-weight: 900 !important;
        font-size: 24px !important;
        margin-bottom: 15px;
    }
    .gold-box p {
        font-size: 18px !important;
        font-weight: 600 !important;
        line-height: 1.8 !important;
        color: #3c4043 !important;
    }
    /* تكبير خطوط أزرار التنقل */
    div.stButton > button {
        font-size: 18px !important;
        font-weight: 700 !important;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🔍 محرك البحث العام في بنود الكهرباء")
st.write("استخدم صندوق البحث في الأسفل للعثور على أي بند، وتصفح التفاصيل بالمربع الذهبي.")

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
    # صندوق البحث العام المكبّر
    search_query = st.text_input("✍️ اكتب كلمة البحث أو الكود (مثال: كشاف، لوحة، كابل):", key="global_search_input").strip()

    if search_query:
        mask = df.astype(str).apply(lambda row: row.str.contains(search_query, case=False, na=False)).any(axis=1)
        search_result = df[mask].reset_index(drop=True)

        if not search_result.empty:
            st.success(f"✅ تم العثور على ({len(search_result)}) بند يطابق كلمة: '{search_query}'")
            
            # --- 🌟 بداية كود المربع الذهبي التفاعلي مع أزرار التالي والسابق 🌟 ---
            if 'current_index' not in st.session_state:
                st.session_state.current_index = 0
                
            # لو عدد نتائج البحث اتغير، صفر العداد عشان ما يضربش
            if st.session_state.current_index >= len(search_result):
                st.session_state.current_index = 0

            # تصميم أزرار التحكم (السابق والتالي) فوق المربع الذهبي
            col_btn1, col_btn2, col_btn3 = st.columns([2, 4, 2])
            
            with col_btn1:
                if st.button("➡️ البند السابق", key="prev_item_btn", use_container_width=True):
                    if st.session_state.current_index > 0:
                        st.session_state.current_index -= 1
                        st.rerun()

            with col_btn2:
                st.markdown(f"<p style='text-align: center; font-size: 18px; font-weight: bold; margin-top: 8px;'>📋 استعراض البند رقم ({st.session_state.current_index + 1} من أصل {len(search_result)})</p>", unsafe_allow_html=True)

            with col_btn3:
                if st.button("البند التالي ⬅️", key="next_item_btn", use_container_width=True):
                    if st.session_state.current_index < len(search_result) - 1:
                        st.session_state.current_index += 1
                        st.rerun()

            # سحب بيانات البند الحالي النشط
            current_row = search_result.iloc[st.session_state.current_index]

            # 🏆 عرض المربع الذهبي بكامل التفاصيل والخطوط الكبيرة
            item_code = current_row.get('الكود', 'غير متوفر')
            item_desc = current_row.get('بيان الأعمال', current_row.get('الوصف', 'غير متوفر'))
            item_unit = current_row.get('الوحدة', 'غير متوفر')
            item_price = current_row.get('الفئة', current_row.get('السعر', 'غير متوفر'))

            st.markdown(f"""
            <div class="gold-box">
                <h3>🏆 المربع الذهبي لبيانات البند الفنية</h3>
                <p><b>🔢 كود البند:</b> {item_code}</p>
                <p><b>📝 تفاصيل ووصف البند:</b> {item_desc}</p>
                <p><b>📐 وحدة القياس:</b> {item_unit}</p>
                <p><b>💰 السعر المتوقع / الفئة:</b> {item_price}</p>
            </div>
            """, unsafe_allow_html=True)
            # --- 🌟 نهاية كود المربع الذهبي التفاعلي 🌟 ---

            # عرض الجدول الكامل تحت المربع الذهبي للمعاينة الإجمالية
            st.markdown("#### 📊 جدول النتائج الشامل:")
            st.dataframe(search_result, use_container_width=True, hide_index=True)
            
            # زرار تحميل الإكسيل
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
