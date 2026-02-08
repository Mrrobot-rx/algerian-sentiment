"""
معالجة النص الجزائري - تنظيف وتوحيد
"""

import re
import string

class AlgerianTextPreprocessor:
    def __init__(self):
        # قاموس الكلمات الشائعة في الدارجة ومعادلاتها
        self.darija_mapping = {
            'كيما': 'كما',
            'هاذا': 'هذا',
            'هاذي': 'هذه',
            'واش': 'هل',
            'شحال': 'كم',
            'بزاف': 'كثير',
            'برك': 'فقط',
            'خويا': 'أخي',
            'صحبي': 'صديقي',
            'هضرة': 'كلام',
            'شغل': 'عمل',
            'نحب': 'أحب',
            'نقدر': 'أستطيع',
            'نقدرش': 'لا أستطيع',
            'ما': 'لا',
            'شي': 'شيء',
            'واحد': 'أحد',
            'كاين': 'موجود',
            'رايحين': 'ذاهبون',
            'هون': 'هون',
            'ملينا': 'مللنا',
        }
    
    def clean_text(self, text):
        """تنظيف النص"""
        if not isinstance(text, str):
            return ""
        
        # إزالة الروابط
        text = re.sub(r'http\S+|www\S+|@\w+', '', text)
        
        # إزالة الإيموجي
        emoji_pattern = re.compile("["
            u"\U0001F600-\U0001F64F"
            u"\U0001F300-\U0001F5FF"
            u"\U0001F680-\U0001F6FF"
            u"\U0001F1E0-\U0001F1FF"
            "]+", flags=re.UNICODE)
        text = emoji_pattern.sub(r'', text)
        
        # إزالة علامات الترقيم الزائدة
        text = re.sub(r'[!]{2,}', '!', text)
        text = re.sub(r'[?]{2,}', '?', text)
        text = re.sub(r'[.]{3,}', '...', text)
        
        # توحيد المسافات
        text = ' '.join(text.split())
        
        return text.strip()
    
    def normalize_darija(self, text):
        """توحيد كلمات الدارجة"""
        words = text.split()
        normalized = []
        
        for word in words:
            # البحث في القاموس
            lower_word = word.lower()
            if lower_word in self.darija_mapping:
                normalized.append(self.darija_mapping[lower_word])
            else:
                normalized.append(word)
        
        return ' '.join(normalized)
    
    def preprocess(self, text):
        """المعالجة الكاملة"""
        text = self.clean_text(text)
        text = self.normalize_darija(text)
        return text

# اختبار سريع
if __name__ == "__main__":
    processor = AlgerianTextPreprocessor()
    
    test_texts = [
        "الله يبارك خويا ربي يحفظك!!!",
        "ما عجبنيش الحال، خدمة مقلقة",
        "شحال ثمن هاذا؟",
    ]
    
    for text in test_texts:
        print(f"الأصلي: {text}")
        print(f"المعالج: {processor.preprocess(text)}")
        print("-" * 40)