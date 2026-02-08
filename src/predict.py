"""
ملف التنبؤ - سليم صامت
للتنبؤ بمشاعر نص جديد (بدون torch)
"""

import sys
import os

# إضافة المسار
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from preprocessing import AlgerianTextPreprocessor

class SentimentPredictor:
    def __init__(self):
        self.preprocessor = AlgerianTextPreprocessor()
        # كلمات مفتاحية للتصنيف
        self.positive_words = [
            'بارك', 'فرح', 'حب', 'جيد', 'ممتاز', 'الله', 'نقية',
            'روعة', 'عجب', 'حفظ', 'نجح', 'توفيق', 'صحة', 'هني',
            'برافو', 'عظيم', 'ماشاء', 'تبارك', 'يهون', 'سهل'
        ]
        self.negative_words = [
            'ما', 'عجب', 'كره', 'سيء', 'صعب', 'تعب', 'مل', 'زعف',
            'غضب', 'حزن', 'مشكل', 'صعيب', 'نرفز', 'مقلق', 'خايف',
            'نقص', 'غلط', 'مشي', 'صعبان', 'ندم'
        ]
    
    def predict(self, text):
        """التنبؤ بمشاعر النص"""
        clean_text = self.preprocessor.process(text)
        
        pos_count = sum(1 for w in self.positive_words if w in clean_text)
        neg_count = sum(1 for w in self.negative_words if w in clean_text)
        
        if pos_count > neg_count:
            label = "positive"
            confidence = min(0.95, 0.6 + (pos_count - neg_count) * 0.15)
        elif neg_count > pos_count:
            label = "negative"
            confidence = min(0.95, 0.6 + (neg_count - pos_count) * 0.15)
        else:
            label = "neutral"
            confidence = 0.5
        
        return {
            "label": label,
            "confidence": round(confidence, 2),
            "clean_text": clean_text
        }

# اختبار
if __name__ == "__main__":
    predictor = SentimentPredictor()
    test = predictor.predict("الله يبارك عليك")
    print(f"نتيجة: {test}")