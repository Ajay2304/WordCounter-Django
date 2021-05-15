from django.http import HttpResponse 
from django.shortcuts import render

def homepage(request):
    return render(request, 'home.html' )
def words(request):
    return render(request,'words.html')
def count(request):
    fulltext=request.GET['fulltext']
    count=0
    punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    for i in range(len(fulltext)):
        count+=1
    for ele in fulltext: 
        if ele in punc: 
            fulltext = fulltext.replace(ele, "")
    wordlist=fulltext.split()
    words={}
    for word in wordlist:
        if word not in words:
            words[word]=1
        else:
            words[word]+=1
    dictionary=sorted(words.items(),reverse=False)
    return render(request,'count.html',{'fulltext':fulltext,'count':len(wordlist),'worddict':dictionary,'counter':count})
def about(request):
    return render(request,'about.html')
