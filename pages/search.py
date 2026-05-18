import streamlit as st
import pandas as pd
import io
import os

st.markdown("<h2 style='color: #4285F4; font-weight: 900;'>🔍 محرك البحث العام الذكي وتطويع الكشيدة</h2>", unsafe_allow_html=True)

FILE_NAME = "data.xlsx"

@st.cache_data
def load_fixed_data():
    if os.path.exists(FILE_NAME):
        try: return pd.read_excel(FILE_NAME)
        except: return pd.DataFrame()
    return pd.DataFrame()

def convert_to_kashida_code(input_str):
    num_map = {'0':'٠', '1':'١', '2':'٢', '3':'٣', '4':'٤', '5':'٥', '6':'٦', '7':'٧', '8':'٨', '9':'٩'}
    clean_str = input_str.strip()
    arabic_digits = "".join([num_map.get(char, char) for char in clean_str])
    if len(arabic_digits) == 4 and arabic_digits.isdigit():
        return f"{arabic_digits[0]}ــ{arabic_digits[1]}ــ{arabic_digits[2]}ــ{arabic_digits[3]}"
    return arabic_digits

df = load_fixed_data()

if "current_index" not in st.session_state: st.session_state.current_index = 0
if "last_query" not in st.session_state: st.session_state.last_query = ""

if not df.empty:
    search_type = st.radio(
        "🗂️ اختر طريقة البحث المناسبة لكود البند:",
        ["🔍 بحث عام / بنود كهرباء (أرقام عادية أو نصوص)", "✍️ بنود كود الكشيدة (اكتب الأرقام عادية مثل 1124)"], horizontal=True
    )

    col_input, col_btn = st.columns([6, 1])
    with col_input:
        search_query = st.text_input("✍️ أدخل كلمة البحث أو الكود هنا بدون شرط:", placeholder="مثال: 6010151 أو 1124...", label_visibility="collapsed")
    with col_btn:
        search_clicked = st.button("بحث 🔍", use_container_width=True)

    if search_query != st.session_state.last_query:
        st.session_state.current_index = 0
        st.session_state.last_query = search_query

    if (search_clicked or search_query) and search_query:
        final_query = search_query.strip().lower()
        if "بنود كود الكشيدة" in search_type:
            final_query = convert_to_kashida_code(search_query)

        try:
            mask = df.astype(str).apply(lambda x: x.str.lower().str.contains(final_query, na=False)).any(axis=1)
            search_result = df[mask].reset_index(drop=True)
        except:
            search_result = df.reset_index(drop=True)

        if not search_result.empty:
            total_items = len(search_result)
            st.markdown(f"### 📊 النتائج المتاحة ({total_items} بند)")
            
            # عرض العداد واختيار البند مباشرة
            item_options = [f"بند {i+1} : كود ({search_result.iloc[i].iloc[0]})" for i in range(total_items)]
            if st.session_state.current_index >= total_items: st.session_state.current_index = 0
                
            selected_option = st.selectbox("🎯 اختر البند مباشرة من هنا للعرض السريع في الكارت:", options=item_options, index=st.session_state.current_index)
            chosen_index = item_options.index(selected_option)
            if chosen_index != st.session_state.current_index:
                st.session_state.current_index = chosen_index
                st.rerun()

            current_row = search_result.iloc[st.session_state.current_index]
            item_code = str(current_row.iloc[0])
            item_desc = str(current_row.iloc[1])
            
            # 🏆 عرض المربع الملكي ثلاثي الأبعاد المطور بالكامل وبخطوط كبيرة جداً
            st.markdown(f"""
            <div class="gold-card-3d">
                <h3>🏆 المربع الملكي لبيانات البند التفصيلية</h3>
                <p><b>📌 موقف البند:</b> عرض بند رقم ({st.session_state.current_index + 1} من إجمالي {total_items})</p>
                <hr style="margin: 12px 0; border: 0; border-top: 2px dashed #FBBC05;">
                <p><b>🔢 كود البند الحالي:</b> <span style="color:#1a73e8; font-weight:bold;">{item_code}</span></p>
                <p><b>📝 وصف وبيان الأعمال:</b> {item_desc}</p>
                <p><b>📐 الفئة / الوحدة:</b> {current_row.iloc[2]}</p>
                <p><b>💰 السعر التقريبي بالسوق:</b> <span style="color:#b45309; font-weight:bold; font-size:22px;">{current_row.iloc[3]} ج.م</span></p>
            </div>
            """, unsafe_allow_html=True)

            # أزرار النسخ الذكي المريحة
            col_cp1, col_cp2 = st.columns(2)
            with col_cp1:
                if st.button(f"📋 نسخ كود البند الحالي ({item_code})", key="cp_code_btn", use_container_width=True):
                    st.components.v1.html(f"<script>navigator.clipboard.writeText('{item_code}');</script>", height=0)
                    st.toast("✅ تم نسخ كود البند بنجاح!", icon="📋")
            with col_cp2:
                if st.button("📝 نسخ وصف البند بالكامل", key="cp_desc_btn", use_container_width=True):
                    safe_desc = item_desc.replace("'", "\\'").replace('"', '\\"')
                    st.components.v1.html(f"<script>navigator.clipboard.writeText('{safe_desc}');</script>", height=0)
                    st.toast("✅ تم نسخ وصف البند بنجاح!", icon="📝")

            # أزرار التنقل اليدوي (التالي والسابق) المدمجة بتصميم عريض
            st.markdown("<br>", unsafe_allow_html=True)
            col_prev, col_next = st.columns(2)
            with col_prev:
                if st.button("➡️ الانتقال للبند السابق", key="nav_prev_btn", use_container_width=True):
                    if st.session_state.current_index > 0:
                        st.session_state.current_index -= 1; st.rerun()
            with col_next:
                if st.button("الانتقال للبند التالي ⬅️", key="nav_next_btn", use_container_width=True):
                    if st.session_state.current_index < total_items - 1:
                        st.session_state.current_index += 1; st.rerun()

            st.write("---")
            
            # الجدول الإجمالي المستقر
            display_df = search_result[[search_result.columns[0], search_result.columns[1], search_result.columns[2], search_result.columns[3]]]
            st.markdown("#### 📊 استعراض جدول نتائج الفلترة بالكامل:")
            st.dataframe(display_df, use_container_width=True, hide_index=True)
            
            # تصدير ملف الإكسيل الجاهز للتحميل
            try:
                buffer = io.BytesIO()
                with pd.ExcelWriter(buffer, engine='openpyxl') as writer:
                    search_result.to_excel(writer, index=False, sheet_name='نتائج البحث')
                st.download_button(label="📥 تحميل هذه النتائج كملف Excel متكامل", data=buffer.getvalue(), file_name=f"نتائج_بحث_{search_query}.xlsx", mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet", key="dl_excel_final")
            except: pass
        else: st.info("ℹ️ لم يتم العثور على بنود تطابق كلمة البحث.")
    else: st.info("💡 الشاشة جاهزة ونظيفة.. اكتب الكود أو كلمة فنية واضغط 'بحث 🔍' لبدء التصفح الفاخر.")
