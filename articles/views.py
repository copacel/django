from django.shortcuts import render, render_to_response, RequestContext
from .forms import ArticleForm

# Create your views here.
def home(request):

    form = ArticleForm(request.POST or None)

    if form.is_valid():
        form_save = form.save(commit=False)
        form_save.save()

    return render_to_response('article.html',
                              locals(),
                              RequestContext(request)
    )
