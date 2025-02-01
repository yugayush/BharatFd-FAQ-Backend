from django.db import models
from ckeditor.fields import RichTextField
from googletrans import Translator

class FAQ(models.Model):
    # English fields (default)
    question_en = models.TextField()
    answer_en = RichTextField()

    # Hindi translations (optional)
    question_hi = models.TextField(blank=True)
    answer_hi = RichTextField(blank=True)

    # Bengali translations (optional)
    question_bn = models.TextField(blank=True)
    answer_bn = RichTextField(blank=True)

    def get_translated_text(self, lang):
        # Dynamically fetch translated text (fallback to English)
        question = getattr(self, f'question_{lang}', self.question_en)
        answer = getattr(self, f'answer_{lang}', self.answer_en)
        return {'question': question, 'answer': answer}

    def save(self, *args, **kwargs):
        # Auto-translate on first save (creation)
        if not self.pk:  # Only on creation (not update)
            try:
                translator = Translator()
                # Translate to Hindi
                self.question_hi = translator.translate(self.question_en, dest='hi').text
                self.answer_hi = translator.translate(self.answer_en, dest='hi').text
                # Translate to Bengali
                self.question_bn = translator.translate(self.question_en, dest='bn').text
                self.answer_bn = translator.translate(self.answer_en, dest='bn').text
            except Exception as e:
                pass  # Fallback to English if translation fails
        super().save(*args, **kwargs)

    def __str__(self):
        return self.question_en