from django.contrib import admin
from .models import products,productvariation
from import_export.admin import ImportExportModelAdmin

# Register your models here.
@admin.register(products)
class ProductsAdmin(ImportExportModelAdmin):
	list_display = ('productname','productlowestprice')

@admin.register(productvariation)
class ProductvariationAdmin(ImportExportModelAdmin):
	list_display = ('variationtext','stock','lastupdated')