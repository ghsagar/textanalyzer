
from django.http import HttpResponse
from django.shortcuts import render
import string
def index(request):
    params={"name":"Sagar Ghimire","address":"magonilia Steet"}
    return render(request, 'index.html',params)

def punc(request):
    text=request.GET.get('anything', 'default')
    checkingtick=request.GET.get('remove','off')
    checkcounttick=request.GET.get('totalcount','off')
    checkspacetick=request.GET.get('spaceremove','off')
    ckeckcapitalized=request.GET.get('capitalize','off')

    if checkingtick =="on" and checkcounttick=="on" and checkspacetick=="on" and ckeckcapitalized=="on":
        cleaned="please click only one box"
        params={"value":cleaned}
        return render(request,'removepunc.html',params)
    elif checkingtick=='on':
        lspunc=string.punctuation
        
        cleaned=''
        for i in text:
            if i not in lspunc:
                cleaned+=i
        params={'display':"After removing the punctuations",'value':cleaned}
        return render(request, "removepunc.html",params)
    
#for counting the total characters
    elif checkcounttick=='on':
        count=0
        for i in text:
            count+=1
        params={"display":"Total numbers of characters is ;",'value':count}
        return render(request, "removepunc.html",params)
        #for removing spaces
    elif checkspacetick=="on":
        cleaned=''
        for j in range(len(text)-1):
            if not (text[j] ==" " and text[j+1]==" "):
                cleaned+=text[j]
        pars={"display":"removing unwanted spaces...",'value':cleaned}
            
        return render(request, "removepunc.html",pars)

    # for capitalizing all
    elif ckeckcapitalized=="on":
        cleaned=''
        for i in text:
            cleaned+=i.upper()
        params={"display":"after capitalizing all:",'value':cleaned}
        return render(request,'removepunc.html', params)

    else:
        return HttpResponse("please tick on the box")
    

    #return render(request, 'removepunc.html',params)