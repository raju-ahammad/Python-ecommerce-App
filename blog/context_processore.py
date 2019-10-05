from .models import BlogCategory



def blogcategory(request):
    return {
    'blogcategories': BlogCategory.objects.order_by('name').distinct(),
    }
