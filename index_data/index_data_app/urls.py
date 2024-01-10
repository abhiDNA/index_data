from django.urls import path
from .views import Nifty50Filter,NiftyMidcap50Filter,NiftyMidcap150Filter,NiftyNext50Filter,NiftySmallcap50Filter

urlpatterns = [
    path('nifty-50/', Nifty50Filter.as_view(), name='nifty50-filter'),
    path('nifty-midcap50/', NiftyMidcap50Filter.as_view(), name='nifty-midcap50-filter'),
    path('nifty-midcap150/', NiftyMidcap150Filter.as_view(), name='nifty-midcap150-filter'),
    path('nifty-next50/', NiftyNext50Filter.as_view(), name='nifty-next50-filter'),
    path('nifty-smallcap50/', NiftySmallcap50Filter.as_view(), name='nifty-smallcap50-filter'),
]
