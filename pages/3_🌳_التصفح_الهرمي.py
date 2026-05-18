import streamlit as st
import pandas as pd
import io
import os

st.title("🌳 التصفح الشجري والهرمي لبنود الكهرباء")
st.write("اكتشف المجموعات وقارن بين البنود المتشابهة وفروق أسعارها بسهولة عبر التسلسل الهرمي.")

# إعادة تطبيق الـ CSS الموحد لضمان ثبات الخطوط والاتجاه وإخفاء الهيدر
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
    </style>
""", unsafe_allow_html=True)

# مسار ملف المجموعات الشجري
GROUPS_PATH = os.path.join("data", "groups.xlsx")

@st.cache_data
def load_groups_data():
    if os.path.exists(GROUPS_PATH):
        # قراءة الملف (يدعم xlsx و xlsm تلقائياً عبر openpyxl)
        df = pd.read_excel(GROUPS_PATH, engine='openpyxl')
        
        # تنظيف أسماء الأعمدة من المسافات الزائدة
        df.columns = df.columns.str.strip()
        
        # 🧪 الحل السحري لعلاج الخلايا الفاضية هندسياً:
        # نقوم بعمل ملء تلقائي للأسفل (Forward Fill) للأعمدة الأساسية لتكرار المجموعات في الذاكرة
        target_cols = ["Group  \n المجموعه الرئيسية", "Sub-group \n المجموعه الفرعية", "Sub-sub-group  \n الوصف السريع"]
        
        # التأكد من وجود الأعمدة أولاً قبل تطبيق الأمر منعاً للأخطاء
        for col in target_cols:
            if col in df.columns:
                df[col] = df[col].ffill().astype(str).str.strip()
                
        return df
    else:
        st.error(f"❌ تعذر العثور على ملف المجموعات الشجري في المسار: {GROUPS_PATH}")
        return None

df_groups = load_groups_data()

if df_groups is not None:
    
    # 1. تحديد أسماء الأعمدة البرمجية بدقة كما هي بالملف
    main_group_col = "Group  \n المجموعه الرئيسية"
    sub_group_col = "Sub-group \n المجموعه الفرعية"
    desc_group_col = "Sub-sub-group  \n الوصف السريع"
    
    st.markdown("### 🌲 شجرة الاختيار التتابعي:")
    
    # القائمة المنسدلة 1: المجموعة الرئيسية
    main_options = sorted(list(df_groups[main_group_col].dropna().unique()))
    selected_main = st.selectbox("📁 اختر المجموعة الرئيسية:", main_options)
    
    # تصفية البيانات بناءً على الاختيار الأول تمهيداً للقائمة الثانية
    df_filtered_1 = df_groups[df_groups[main_group_col] == selected_main]
    
    # القائمة المنسدلة 2: المجموعة الفرعية (تتغير خياراتها تلقائياً حسب الاختيار الأول!)
    sub_options = sorted(list(df_filtered_1[sub_group_col].dropna().unique()))
    selected_sub = st.selectbox("📂 اختر المجموعة الفرعية التابعة:", sub_options)
    
    # تصفية البيانات بناءً على الاختيار الثاني تمهيداً للقائمة الثالثة
    df_filtered_2 = df_filtered_1[df_filtered_1[sub_group_col] == selected_sub]
    
    # القائمة المنسدلة 3: الوصف السريع للبنود المتشابهة
    desc_options = sorted(list(df_filtered_2[desc_group_col].dropna().unique()))
    selected_desc = st.selectbox("📝 اختر الوصف السريع (لعرض البنود المتشابهة والمقارنة):", desc_options)
    
    # التصفية النهائية لعرض الجدول المقصود
    final_display_df = df_filtered_2[df_filtered_2[desc_group_col] == selected_desc]
    
    st.markdown("---")
    
    # 📊 عرض الجدول النهائي للمقارنة بين الفروق البسيطة للبنود
    if not final_display_df.empty:
        # استخراج وتصفيف الأعمدة الأساسية فقط للمعاينة النظيفة والمنظمة
        columns_to_show = ["Item Code \n كود البند", "Item Description   \n  بيان الأعمال", "Category  \n الوحدة", "Numerical Price \n الفئة رقما", "Written Price \n الفئة كتابة"]
        
        # التأكد من وجود هذه الأعمدة في الملف الفعلي للمستخدم
        existing_cols = [c for c in columns_to_show if c in final_display_df.columns]
        
        grid_df = final_display_df[existing_cols]
        
        st.success(f"✅ تم حصر ({len(grid_df)}) بنود متشابهة تحت اختيارك الحالي. قارن الفروق والأسعار أدناه:")
        
        # عرض الجدول بكامل العرض وبدون أندكس
        st.dataframe(grid_df, use_container_width=True, hide_index=True)
        
        # 📥 زر تحميل مجموعة البنود المتشابهة لإكسيل مخصص
        try:
            buffer = io.BytesIO()
            with pd.ExcelWriter(buffer, engine='openpyxl') as writer:
                grid_df.to_excel(writer, index=False, sheet_name='مقارنة البنود المتشابهة')
            
            st.download_button(
                label="📥 تحميل هذه المجموعة المقارنة كملف Excel",
                data=buffer.getvalue(),
                file_name=f"مجموعة_{selected_desc}.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )
        except Exception as e:
            st.error(f"تعذر إعداد ملف التحميل: {e}")
            
    else:
        st.info("💡 الرجاء تحديد توليفة التصفح الشجري من القوائم أعلاه لعرض البنود الفردية.")