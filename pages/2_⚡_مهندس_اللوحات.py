import streamlit as st
import pandas as pd
import io
import os

st.title("⚡ رادار مهندس اللوحات الكهربائية المتطور")
st.write("صفحة متخصصة لبحوث وتصفية بنود اللوحات فقط بناءً على المحددات الهندسية الفنية.")

# إعادة تطبيق الـ CSS لثبات المظهر والخطوط والـ RTL وإخفاء الهيدر
st.markdown("""
    <style>
    html, body, .stApp, .stMarkdown, p, h1, h2, h3, h4, h5, h6, span, label, input, button, select {
        font-family: 'Cairo', sans-serif !important;
        text-align: right !important;
        direction: rtl !important;
    }
    #MainMenu, header, footer, [data-testid="stHeader"], [data-testid="stDecoration"], 
    .viewerBadge_link__1S137, .styles_viewerBadge__3uC9V, [data-testid="bundle-footer"],
    [data-testid="stStatusWidget"], .stDeployButton, [data-testid="stToolbar"] {
        visibility: hidden !important;
        display: none !important;
    }
    .block-container { padding-top: 1rem !important; }
    
    /* تحسين مظهر صناديق الفلترة الجانبية */
    div[data-testid="stExpander"] {
        direction: rtl !important;
        text-align: right !important;
    }
    </style>
""", unsafe_allow_html=True)

# مسار ملف اللوحات المتخصصة الجديد
PANELS_PATH = os.path.join("data", "panels.xlsx")

@st.cache_data
def load_panels_data():
    if os.path.exists(PANELS_PATH):
        df = pd.read_excel(PANELS_PATH, engine='openpyxl')
        df.columns = df.columns.str.strip()
        # تحويل الأعمدة لنصوص لتفادي أي أخطاء في الفلترة والبحث
        for col in df.columns:
            df[col] = df[col].astype(str).str.strip()
        return df
    else:
        st.error(f"❌ تعذر العثور على ملف اللوحات في المسار: {PANELS_PATH}")
        return None

df_panels = load_panels_data()

if df_panels is not None:
    
    # 🎛️ تصميم لوحة الفلاتر الذكية (استخدام نظام الـ Columns لتوفير المساحة على الموبايل)
    st.markdown("### 🎛️ فلاتر التحكم الهندسي السريع:")
    col1, col2 = st.columns(2)
    col3, col4 = st.columns(2)
    
    with col1:
        # فلتر جهة العمل (يجلب الخيارات الفريدة تلقائياً من الملف)
        all_clients = ["الكل"] + sorted(list(df_panels["جهة العمل"].unique()))
        selected_client = st.selectbox("🏢 فلتر بجهة العمل:", all_clients)
        
    with col2:
        # فلتر نظام الطور (سواء 3 فاز أو سنـجل فاز)
        all_phases = ["الكل"] + sorted(list(df_panels["نظام الطور"].unique()))
        selected_phase = st.selectbox("🔌 نظام الطور (Phases):", all_phases)
        
    with col3:
        # فلتر درجة الحماية من الأتربة والمياه IP
        all_ip = ["الكل"] + sorted(list(df_panels["درجة الحماية (IP)"].unique()))
        selected_ip = st.selectbox("🛡️ درجة الحماية (IP):", all_ip)
        
    with col4:
        # صندوق البحث النصي التقليدي داخل مواصفات اللوحة
        keyword = st.text_input("🔍 بحث بكلمة مفتاحية (مثال: سعة قطع، سمك الصاج):", "").strip()

    # ⚙️ محرك الفلترة البرمجي المدمج
    filtered_df = df_panels.copy()
    
    if selected_client != "الكل":
        filtered_df = filtered_df[filtered_df["جهة العمل"] == selected_client]
        
    if selected_phase != "الكل":
        filtered_df = filtered_df[filtered_df["نظام الطور"] == selected_phase]
        
    if selected_ip != "الكل":
        filtered_df = filtered_df[filtered_df["درجة الحماية (IP)"] == selected_ip]
        
    if keyword:
        # البحث في عمود المواصفات أو الملاحظات الفنية
        mask = filtered_df.astype(str).apply(lambda row: row.str.contains(keyword, case=False, na=False)).any(axis=1)
        filtered_df = filtered_df[mask]

    st.markdown("---")
    
    # 📊 عرض النتائج المفلترة
    if not filtered_df.empty:
        st.success(f"📊 تم العثور على ({len(filtered_df)}) بند لوحات يطابق خياراتك الحالية.")
        
        # عرض الجدول بكامل العرض وبدون أندكس
        st.dataframe(filtered_df, use_container_width=True, hide_index=True)
        
        # 📥 زر تحميل النتائج المفلترة لملف إكسيل فرعي مخصص
        try:
            buffer = io.BytesIO()
            with pd.ExcelWriter(buffer, engine='openpyxl') as writer:
                filtered_df.to_excel(writer, index=False, sheet_name='بنود اللوحات المفلترة')
            
            st.download_button(
                label="📥 تحميل هذه اللوحات المفلترة كملف Excel",
                data=buffer.getvalue(),
                file_name="تقرير_بنود_اللوحات_المخصصة.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )
        except Exception as e:
            st.error(f"تعذر إعداد ملف التحميل: {e}")
            
    else:
        st.warning("⚠️ لا توجد بنود لوحات تطابق توليفة الفلاتر المختارة حالياً. يرجى إعادة ضبط الفلاتر!")