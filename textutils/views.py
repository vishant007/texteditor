#added manually by Vishant
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
    # return HttpResponse("<h1>Hello</h1>")
def analyze(request):
    #get the text 
    #check th values of checkbox
    djtext = request.GET.get('text', 'default')
    removepunc = request.GET.get('removepunc', 'off')
    fullcaps = request.GET.get('fullcaps', 'off')
    newlinerem = request.GET.get('newlinerem', 'off')
    extraspaceremover = request.GET.get('extraspaceremover', 'off')

    #checks which checkbox is on and runs accordingly
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose':'Removed Punctuations', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    elif(fullcaps=="on"):
        analyzed = ""
        for char in djtext:
            # upper is the python function use to capitalize the letter or to convert them in uppercase
            analyzed = analyzed + char.upper()
        params = {'purpose':'changed to uppercase', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    elif(extraspaceremover=="on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if djtext[index] == " " and djtext[index+1] == " ":
                pass
            else:
                analyzed = analyzed + char
        params = {'purpose':'removes newline', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    elif(newlinerem=="on"):
        analyzed = ""
        for char in djtext:
            if char != "\n":
                analyzed = analyzed + char
        params = {'purpose':'removes newline', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    else:
        return HttpResponse("Error")

