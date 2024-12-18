from translate import Translator

def translate(text):
    translator = Translator(to_lang="de")
    translation = translator.translate(text)
    return translation

