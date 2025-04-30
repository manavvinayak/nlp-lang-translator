from flask import Flask, render_template, request
from langdetect import detect, DetectorFactory
from deep_translator import GoogleTranslator

# Set seed for consistent language detection
DetectorFactory.seed = 0

# Map language codes to full names
LANGUAGE_CODE_MAP = {
    'af': 'Afrikaans',
    'ar': 'Arabic',
    'az': 'Azerbaijani',
    'be': 'Belarusian',
    'bg': 'Bulgarian',
    'bn': 'Bengali',
    'ca': 'Catalan',
    'cs': 'Czech',
    'cy': 'Welsh',
    'da': 'Danish',
    'de': 'German',
    'el': 'Greek',
    'en': 'English',
    'es': 'Spanish',
    'et': 'Estonian',
    'fa': 'Persian',
    'fi': 'Finnish',
    'fr': 'French',
    'ga': 'Irish',
    'gl': 'Galician',
    'gu': 'Gujarati',
    'he': 'Hebrew',
    'hi': 'Hindi',
    'hr': 'Croatian',
    'hu': 'Hungarian',
    'hy': 'Armenian',
    'id': 'Indonesian',
    'is': 'Icelandic',
    'it': 'Italian',
    'ja': 'Japanese',
    'ka': 'Georgian',
    'kk': 'Kazakh',
    'km': 'Khmer',
    'kn': 'Kannada',
    'ko': 'Korean',
    'ky': 'Kyrgyz',
    'lb': 'Luxembourgish',
    'lt': 'Lithuanian',
    'lv': 'Latvian',
    'mk': 'Macedonian',
    'ml': 'Malayalam',
    'mn': 'Mongolian',
    'mr': 'Marathi',
    'ms': 'Malay',
    'mt': 'Maltese',
    'ne': 'Nepali',
    'nl': 'Dutch',
    'no': 'Norwegian',
    'pa': 'Punjabi',
    'pl': 'Polish',
    'pt': 'Portuguese',
    'ro': 'Romanian',
    'ru': 'Russian',
    'si': 'Sinhala',
    'sk': 'Slovak',
    'sl': 'Slovenian',
    'so': 'Somali',
    'sq': 'Albanian',
    'sr': 'Serbian',
    'sv': 'Swedish',
    'sw': 'Swahili',
    'ta': 'Tamil',
    'te': 'Telugu',
    'th': 'Thai',
    'tl': 'Tagalog',
    'tr': 'Turkish',
    'uk': 'Ukrainian',
    'ur': 'Urdu',
    'uz': 'Uzbek',
    'vi': 'Vietnamese',
    'xh': 'Xhosa',
    'yi': 'Yiddish',
    'zh': 'Chinese',
    'zu': 'Zulu'
}

app = Flask(__name__)

def detect_and_translate(text, target_lang):
    # Detect source language
    result_lang = detect(text)
    result_lang_full = LANGUAGE_CODE_MAP.get(result_lang, result_lang)  # Map to full name

    # Validate if the detected language is supported by GoogleTranslator
    supported_languages = [lang.lower() for lang in GoogleTranslator().get_supported_languages()]  # Normalize to lowercase
    if result_lang_full.lower() not in supported_languages:
        result_lang_full = "Unsupported Language"

    # Translate using deep-translator
    translate_text = GoogleTranslator(source='auto', target=target_lang).translate(text)

    return result_lang_full, translate_text

@app.route('/')
def index():
    # Create an instance of GoogleTranslator to get supported languages
    translator = GoogleTranslator()
    languages = translator.get_supported_languages()

    return render_template('index.html', languages=languages)

# @app.route('/trans', methods=['POST'])
# def trans():
#     translation = ""
#     detected_lang = ""
#     if request.method == 'POST':
#         text = request.form['text']
#         target_lang = request.form['target_lang']
#         detected_lang, translation = detect_and_translate(text, target_lang)

#     return render_template('index.html', translation=translation, detected_lang=detected_lang, languages=GoogleTranslator().get_supported_languages())

@app.route('/trans', methods=['POST'])
def trans():
    translation = ""
    detected_lang = ""
    text = ""  # Default value
    if request.method == 'POST':
        text = request.form['text']
        target_lang = request.form['target_lang']
        detected_lang, translation = detect_and_translate(text, target_lang)

    return render_template(
        'index.html',
        translation=translation,
        detected_lang=detected_lang,
        languages=GoogleTranslator().get_supported_languages(),
        old_text=text,  # 👈 Inject original input
        selected_lang=target_lang  # Optional: Retain selected dropdown
    )


if __name__ == '__main__':
    app.run(debug=True)