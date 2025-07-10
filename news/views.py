from django.shortcuts import render

from news.models import New
def news_list(request):
    news = New.objects.all()
    context = {
        'datas': news
    }
    return render(request, 'index.html', context=context)




