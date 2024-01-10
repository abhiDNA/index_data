from django.contrib import admin


from import_export.admin import ImportExportModelAdmin
from .models import Nifty50, NiftyMidcap150, NiftyMidcap50, NiftySmallcap50, NiftyNext50
from .resources import Nifty50Resource, NiftyNext50Resource, NiftyMidcap50Resource, NiftySmallcap50Resource, \
    NiftyMidcap150Resource


@admin.register(Nifty50)
class Nifty50Admin(ImportExportModelAdmin):
    resource_class = Nifty50Resource


@admin.register(NiftyMidcap150)
class Nifty50Admin(ImportExportModelAdmin):
    resource_class = NiftyMidcap150Resource


@admin.register(NiftyMidcap50)
class Nifty50Admin(ImportExportModelAdmin):
    resource_class = NiftyMidcap50Resource


@admin.register(NiftySmallcap50)
class Nifty50Admin(ImportExportModelAdmin):
    resource_class = NiftySmallcap50Resource


@admin.register(NiftyNext50)
class Nifty50Admin(ImportExportModelAdmin):
    resource_class = NiftyNext50Resource
