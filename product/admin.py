from django.contrib import admin
import csv
import datetime
from django.http import HttpResponse
from django.urls import reverse
from django.utils.safestring import mark_safe
from .models import Category, Product, ProductImage

class CategoryAdmin(admin.ModelAdmin):
    list_display  = ('name', 'slug')
    list_filter = ('name', 'slug')
    search_fields = ('name',)
admin.site.register(Category, CategoryAdmin)



class ProductImageInlineAdmin(admin.StackedInline):
    model = ProductImage
    extra = 0

def export_to_csv(modeladmin, request, queryset):
    opts = modeladmin.model._meta
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment;' \
        'filename={}.csv'.format(opts.verbose_name)
    writer = csv.writer(response)

    fields = [field for field in opts.get_fields() if not field.many_to_many and not field.one_to_many]
    # Write a first row with header information
    writer.writerow([field.verbose_name for field in fields])
    # Write data rows
    for obj in queryset:
        data_row = []
        for field in fields:
            value = getattr(obj, field.name)
            if isinstance(value, datetime.datetime):
                value = value.strftime('%d/%m/%Y')
            data_row.append(value)
        writer.writerow(data_row)
    return response

export_to_csv.short_description = 'Export to CSV'




class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInlineAdmin]
    list_display  = ('name', 'slug', 'category', 'price', 'available','created',)
    list_filter = ('name', 'slug', 'available')
    search_fields = ('name', 'slug', 'available')
    actions = [export_to_csv]
admin.site.register(Product, ProductAdmin)
