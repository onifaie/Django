from django.contrib import admin
from . models import obeid,customer
# Register your models here.
admin.site.register(obeid)
admin.site.register(customer)
admin.site.site_header="Obeid -Project"
admin.site.site_title="this obeid title"