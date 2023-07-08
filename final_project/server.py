from machinetranslation import translator
from flask import Flask, render_template, request
import json
import machinetranslation
from deep_translator import MyMemoryTranslator

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench(textToTranslate):
    
    textToTranslate = request.args.get('textToTranslate')
    frenchText = MyMemoryTranslator(source='en-EN', target='fr-FR').translate(textToTranslate)
    
    return frenchText

@app.route("/frenchToEnglish")
def frenchToEnglish(textToTranslate):
    textToTranslate = request.args.get('textToTranslate')
    englishText = MyMemoryTranslator(source='fr-FR', target='en-EN').translate(textToTranslate)
    
    return englishText

@app.route("/")
def renderIndexPage():
    return render_template("index.html")
    

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
