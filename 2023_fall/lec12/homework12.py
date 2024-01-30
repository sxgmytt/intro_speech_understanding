from gtts import gTTS

def synthesize(text, lang, filename):
    '''
    Use gtts.gTTS(text=text, lang=lang) to synthesize speech, then write it to filename.
    
    @params:
    text (str) - the text you want to synthesize
    lang (str) - the language in which you want to synthesize it
    filename (str) - the filename in which it should be saved
    '''
    # Create a gTTS object
    tts = gTTS(text=text, lang=lang, slow=False)

    # Save the synthesized speech to the specified file
    tts.save(filename)

# Example usage:
text_to_synthesize = "Hello, this is a test."
language = "en"
output_filename = "output.mp3"

synthesize(text_to_synthesize, language, output_filename)
