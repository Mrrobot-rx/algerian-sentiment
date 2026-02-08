"""
ملف التنبؤ - سليم صامت
للتنبؤ بمشاعر نص جديد
"""

from preprocessing import AlgerianTextPreprocessor

class SentimentPredictor:
    def __init__(self):
        self.preprocessor = AlgerianTextPreprocessor()
        # كلمات مفتاحية للتصنيف السريع
        self.positive_words = [
            'بارك', 'فرح', 'حب', 'جيد', 'ممتاز', 'الله', 'نقية',
            'روعة', 'عجب', 'حفظ', 'نجح', 'توفيق', 'صحة', 'هني'
        ]
        self.negative_words = [
            'ما', 'عجب', 'كره', 'سيء', 'صعب', 'تعب', 'مل', 'زعف',
            'غضب', 'حزن', 'مشكل', 'صعيب', 'صعب', 'نرفز'
        ]
    
    def predict(self, text):
        """التنبؤ بمشاعر النص"""
        # معالجة النص
        clean_text = self.preprocessor.process(text)
        
        # عد الكلمات الإيجابية والسلبية
        pos_count = sum(1 for w in self.positive_words if w in clean_text)
        neg_count = sum(1 for w in self.negative_words if w in clean_text)
        
        # تحديد النتيجة
        if pos_count > neg_count:
            label = "positive"
            confidence = min(0.95, 0.7 + (pos_count - neg_count) * 0.1)
        elif neg_count > pos_count:
            label = "negative"
            confidence = min(0.95, 0.7 + (neg_count - pos_count) * 0.1)
        else:
            label = "neutral"
            confidence = 0.5
        
        return {
            "label": label,
            "confidence": round(confidence, 2),
            "clean_text": clean_text
        }

# اختبار سريع
if __name__ == "__main__":
    predictor = SentimentPredictor()
    
    test_texts = [
        "الله يبارك عليك خويا",
        "ما عجبنيش الحال",
        "معلومة عادية",
    ]
    
    for text in test_texts:
        result = predictor.predict(text)
        print(f"\nالنص: {text}")
        print(f"التنبؤ: {result['label']} ({result['confidence']})")