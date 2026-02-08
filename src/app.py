import streamlit as st

st.set_page_config(page_title="تحليل المشاعر", page_icon="🇩🇿")

st.title("🇩🇿 تحليل المشاعر - الدارجة الجزائرية")
st.markdown("**المطور:** سليم صامت")

text = st.text_area("أدخل نصاً:", placeholder="مثال: الله يبارك عليك")

if st.button("حلل", type="primary"):
    if text:
        # تحليل بسيط بدون مكتبات خارجية
        positive = ['بارك', 'فرح', 'حب', 'جيد', 'الله']
        negative = ['ما', 'عجب', 'كره', 'سيء', 'صعب']
        
        pos = sum(1 for w in positive if w in text)
        neg = sum(1 for w in negative if w in text)
        
        if pos > neg:
            st.success("😊 إيجابي")
        elif neg > pos:
            st.error("😔 سلبي")
        else:
            st.info("😐 محايد")
    else:
        st.warning("أدخل نصاً")