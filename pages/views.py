from django.shortcuts import render

from pages.admin import ScrollModel, GaleryModel

def home_page_view(request):
    scrolls = ScrollModel.object.all().order_by('-pk')[:5]
    images = GaleryModel.object.all().order_by('-pk')
    context = {
        "scrolls":scrolls,
        "images":images
    }
    return render(request, template_name="index.html", context=context)