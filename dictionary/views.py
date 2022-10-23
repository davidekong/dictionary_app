import difflib
from django.shortcuts import redirect, render
from PyDictionary import PyDictionary
from english_words import english_words_set
# Create your views here.
def home(request):
    if request.method == "GET":
        if 'search_button' in request.GET:
            word = request.GET.get('word')
            return redirect('output', word)
    return render(request, 'dictionary/dict.html')

def output(request, word):
    dictionary = PyDictionary()
    meanings = dictionary.meaning(difflib.get_close_matches(word, english_words_set)[0])
    new_list = []
    if meanings is not None:
        for key, value in meanings.items():
            new_list.append((key, value))
    context = {
        'suggested': list(difflib.get_close_matches(word, english_words_set)), 
        'word': word, 
        'list': new_list, 
        'meanings': meanings
    }
    print(context['suggested'])
    return render(request, 'dictionary/output.html', context)