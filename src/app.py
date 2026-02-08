"""
تطبيق تحليل المشاعر - سليم صامت
تصميم احترافي مع تأثيرات بصرية
"""

import streamlit as st
import random

# إعدادات الصفحة
st.set_page_config(
    page_title="تحليل المشاعر | الدارجة الجزائرية",
    page_icon="🇩🇿",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# CSS مخصص للتصميم
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Tajawal:wght@400;700;900&display=swap');
    
    * {
        font-family: 'Tajawal', sans-serif;
    }
    
    .main {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 0;
    }
    
    .stApp {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
    }
    
    .title-container {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 20px;
        text-align: center;
        margin-bottom: 2rem;
        box-shadow: 0 20px 60px rgba(0,0,0,0.3);
    }
    
    .title-text {
        color: white;
        font-size: 2.5rem;
        font-weight: 900;
        margin: 0;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }
    
    .subtitle-text {
        color: #e0e0e0;
        font-size: 1.1rem;
        margin-top: 0.5rem;
    }
    
    .input-container {
        background: white;
        padding: 2rem;
        border-radius: 20px;
        box-shadow: 0 10px 40px rgba(0,0,0,0.1);
        margin-bottom: 2rem;
    }
    
    .result-positive {
        background: linear-gradient(135deg, #11998e 0%, #38ef7d 100%);
        color: white;
        padding: 2rem;
        border-radius: 20px;
        text-align: center;
        animation: slideIn 0.5s ease-out;
        box-shadow: 0 10px 40px rgba(17, 153, 142, 0.3);
    }
    
    .result-negative {
        background: linear-gradient(135deg, #eb3349 0%, #f45c43 100%);
        color: white;
        padding: 2rem;
        border-radius: 20px;
        text-align: center;
        animation: slideIn 0.5s ease-out;
        box-shadow: 0 10px 40px rgba(235, 51, 73, 0.3);
    }
    
    .result-neutral {
        background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
        color: white;
        padding: 2rem;
        border-radius: 20px;
        text-align: center;
        animation: slideIn 0.5s ease-out;
        box-shadow: 0 10px 40px rgba(79, 172, 254, 0.3);
    }
    
    @keyframes slideIn {
        from {
            opacity: 0;
            transform: translateY(-20px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    .emoji-big {
        font-size: 4rem;
        margin-bottom: 1rem;
    }
    
    .confidence-bar {
        background: rgba(255,255,255,0.3);
        height: 10px;
        border-radius: 5px;
        margin-top: 1rem;
        overflow: hidden;
    }
    
    .confidence-fill {
        height: 100%;
        background: white;
        border-radius: 5px;
        transition: width 1s ease-out;
    }
    
    .example-btn {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        padding: 0.5rem 1rem;
        border-radius: 25px;
        margin: 0.25rem;
        cursor: pointer;
        transition: transform 0.2s;
    }
    
    .example-btn:hover {
        transform: scale(1.05);
    }
    
    .footer {
        text-align: center;
        padding: 2rem;
        color: #666;
        font-size: 0.9rem;
    }
    
    .developer-name {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 700;
    }
    
    /* تخصيص حقل الإدخال */
    .stTextArea textarea {
        border-radius: 15px;
        border: 2px solid #e0e0e0;
        font-size: 1.1rem;
        transition: border-color 0.3s;
    }
    
    .stTextArea textarea:focus {
        border-color: #667eea;
        box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
    }
    
    /* تخصيص الزر */
    .stButton button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
        color: white !important;
        border-radius: 30px !important;
        padding: 0.75rem 3rem !important;
        font-size: 1.2rem !important;
        font-weight: 700 !important;
        border: none !important;
        box-shadow: 0 10px 30px rgba(102, 126, 234, 0.3) !important;
        transition: transform 0.2s, box-shadow 0.2s !important;
    }
    
    .stButton button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 15px 40px rgba(102, 126, 234, 0.4) !important;
    }
</style>
""", unsafe_allow_html=True)

# العنوان الرئيسي
st.markdown("""
<div class="title-container">
    <h1 class="title-text">🇩🇿 تحليل المشاعر</h1>
    <p class="subtitle-text">الدارجة الجزائرية | Algerian Sentiment Analysis</p>
</div>
""", unsafe_allow_html=True)

# حاوية الإدخال
st.markdown('<div class="input-container">', unsafe_allow_html=True)

text = st.text_area(
    "",
    placeholder="✍️ اكتب هنا بالدارجة الجزائرية...",
    height=120,
    label_visibility="collapsed"
)

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    analyze_btn = st.button("🔍 حلل المشاعر", use_container_width=True)

st.markdown('</div>', unsafe_allow_html=True)

# أمثلة سريعة
st.markdown("### ✨ جرب هذه الأمثلة:")
example_cols = st.columns(3)
examples = [
    "الله يبارك عليك خويا",
    "ما عجبنيش الحال اليوم",
    "معلومة عادية"
]

for i, ex in enumerate(examples):
    with example_cols[i]:
        if st.button(f"💬 {ex[:15]}...", key=f"ex_{i}"):
            text = ex
            analyze_btn = True

# التحليل
if analyze_btn and text:
    # كلمات التحليل
    positive_words = ['بارك', 'فرح', 'حب', 'جيد', 'ممتاز', 'الله', 'نقية', 'روعة', 
                      'عجب', 'حفظ', 'نجح', 'توفيق', 'صحة', 'هني', 'برافو', 'عظيم', 
                      'ماشاء', 'تبارك', 'يهون', 'سهل', 'جميل', 'رائع']
    negative_words = ['ما', 'عجب', 'كره', 'سيء', 'صعب', 'تعب', 'مل', 'زعف', 'غضب', 
                      'حزن', 'مشكل', 'صعيب', 'نرفز', 'مقلق', 'خايف', 'نقص', 'غلط', 
                      'مشي', 'صعبان', 'ندم', 'كره', 'بغض']
    
    pos_count = sum(1 for w in positive_words if w in text)
    neg_count = sum(1 for w in negative_words if w in text)
    
    if pos_count > neg_count:
        label = "positive"
        emoji = "😊"
        title = "مشاعر إيجابية!"
        desc = "النص يحمل طاقة إيجابية جميلة"
        confidence = min(95, 60 + (pos_count - neg_count) * 15)
    elif neg_count > pos_count:
        label = "negative"
        emoji = "😔"
        title = "مشاعر سلبية"
        desc = "النص يعبر عن شعور سلبي أو صعب"
        confidence = min(95, 60 + (neg_count - pos_count) * 15)
    else:
        label = "neutral"
        emoji = "😐"
        title = "مشاعر محايدة"
        desc = "النص محايد، لا يحمل مشاعر قوية"
        confidence = 50
    
    # عرض النتيجة
    st.markdown(f"""
    <div class="result-{label}">
        <div class="emoji-big">{emoji}</div>
        <h2>{title}</h2>
        <p>{desc}</p>
        <div style="margin-top: 1.5rem;">
            <strong>نسبة الثقة: {confidence}%</strong>
            <div class="confidence-bar">
                <div class="confidence-fill" style="width: {confidence}%;"></div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # تفاصيل إضافية
    with st.expander("🔍 تفاصيل التحليل"):
        st.write(f"**النص الأصلي:** {text}")
        st.write(f"**الكلمات الإيجابية الم found:** {pos_count}")
        st.write(f"**الكلمات السلبية الم found:** {neg_count}")

elif analyze_btn and not text:
    st.warning("⚠️ الرجاء إدخال نص للتحليل")

# التذييل
st.markdown("""
<div class="footer">
    <p>مشروع تعليمي في معالجة اللغة الطبيعية | NLP</p>
    <p>تم التطوير بواسطة <span class="developer-name">سليم صامت</span> | 2025</p>
    <p style="font-size: 0.8rem; margin-top: 1rem;">🇩🇿 من الجزائر، للعالم</p>
</div>
""", unsafe_allow_html=True)