from django.shortcuts import render
from googletrans import Translator
from . import my_store

# Create your views here.
def index(request):
    result = {
        'lang': my_store.LANGUAGE,
    }
    if request.method == 'POST':
        text = request.POST.get('txt')
        lang = request.POST.get('lang')

        translator = Translator()
        tr = translator.translate(text, lang)
        result['trans'] = tr.text
        result['text'] = text
        return render(request, 'my_app/index.html', result)

    return render(request, 'my_app/index.html', result)