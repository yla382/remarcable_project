from django.shortcuts import render

from remarcable.models import Product, Category, Tag


def product_list(request):
    query = request.GET.get('q')
    category_id = request.GET.get('Category', '')
    selected_tags = request.GET.getlist('Tag')
    products = Product.objects.all()

    if query:
        products = products.filter(name__icontains=query)
    if category_id:
        products = products.filter(category_id=category_id)
    if selected_tags:
        products = products.filter(tags__id__in=selected_tags).distinct()


    categories = Category.objects.all()
    tags = Tag.objects.all()

    context = {
        'products': products,
        'categories': categories,
        'tags': tags,
        'query': query,
        'selected_category': category_id,
        'selected_tags': selected_tags,
    }

    return render(request, 'remarcable/product_list.html', context)
