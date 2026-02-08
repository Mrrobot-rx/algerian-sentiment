"""
تطبيق تحليل المشاعر - سليم صامت
"""

import streamlit as st
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from predict import SentimentPredictor

st.set_page_config(
    page_title="تحليل المشاعر الجزائرية",
    page_icon="🇩🇿",
    layout="centered"
)

# تهيئة المتنبئ
predictor = SentimentPredictor()

st.title("🇩🇿 تحليل المشاعر - الدارجة الجزائرية")
st.markdown("**المطور:** سليم صامت | **2025**")

# نموذج الإدخال
text = st.text_area(
    "أدخل نصاً بالدارجة الجزائرية:",
    height=100,
    placeholder="مثال: الله يبارك عليك خويا..."
)

# زر التحليل
if st.button("🔍 حلل المشاعر", type="primary"):
    if text.strip():
        result = predictor.predict(text)
        
        label = result['label']
        confidence = result['confidence']
        
        # عرض النتيجة بالألوان
        if label == "positive":
            st.success(f"😊 **إيجابي** - الثقة: {confidence:.0%}")
        elif label == "negative":
            st.error(f"😔 **سلبي** - الثقة: {confidence:.0%}")
        else:
            st.info(f"😐 **محايد** - الثقة: {confidence:.0%}")
        
        # تفاصيل إضافية
        with st.expander("🔧 تفاصيل التحليل"):
            st.write(f"**النص الأصلي:** {text}")
            st.write(f"**النص المعالج:** {result['clean_text']}")
            st.write(f"**التصنيف:** {label}")
            st.write(f"**نسبة الثقة:** {confidence:.2f}")
    else:
        st.warning("⚠️ الرجاء إدخال نص للتحليل")

# أمثلة للتجربة
st.markdown("---")
st.subheader("📝 أمثلة للتجربة")

examples = [
    "الله يبارك عليك خويا",
    "ما عجبنيش الحال",
    "معلومة عادية",
]

for ex in examples:
    if st.button(f"جرب: {ex}"):
        result = predictor.predict(ex)
        st.write(f"**النتيجة:** {result['label']} ({result['confidence']})")

# التذييل
st.markdown("---")
st.caption("🚀 مشروع تعليمي في معالجة اللغة الطبيعية | NLP for Algerian Darja")