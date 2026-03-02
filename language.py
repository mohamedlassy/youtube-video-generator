class LanguageSupport:
    def __init__(self, language='en'):
        self.language = language
        self.translations = {
            'en': {
                'welcome': 'Welcome to the YouTube Video Generator!',
                'goodbye': 'Thank you for using our service.',
            },
            'ar': {
                'welcome': 'مرحبًا بك في مولد فيديوهات يوتيوب!',
                'goodbye': 'شكرًا لاستخدامك خدمتنا.',
            }
        }

    def translate(self, key):
        return self.translations.get(self.language, {}).get(key, key)

    def set_language(self, language):
        if language in self.translations:
            self.language = language
        else:
            raise ValueError('Language not supported!')

# Example Usage
if __name__ == '__main__':
    lang_support = LanguageSupport('en')
    print(lang_support.translate('welcome'))
    lang_support.set_language('ar')
    print(lang_support.translate('welcome'))
