from django.contrib import admin

from remarcable.models import Category, Tag, Product

# model registration

admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Product)

