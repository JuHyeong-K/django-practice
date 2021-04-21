from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def count(request):
    if request.method == 'POST':
        text = request.POST['text_string']
        text_length = len(text)
        text_length_no_space = len(''.join(text.strip().split(' ')))
        
        print(text_length, text_length_no_space)
        context = {
            'text': text,
            'length': text_length,
            'length_no_space': text_length_no_space,
        }
    return render(request, 'count.html', context)