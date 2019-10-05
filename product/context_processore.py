from .models import Category



def category(request):
    return {
    'categories': Category.objects.order_by('name').distinct(),
    }
