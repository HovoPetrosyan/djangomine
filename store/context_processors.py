from store.models import Banner, Category


def all_in_one(request):
    return {
        'categories': Category.objects.all(),
        'banners': Banner.objects.all()
    }