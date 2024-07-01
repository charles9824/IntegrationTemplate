from django.urls import path

from website.views import index_website, about, readmore

urlpatterns = [
    path('', index_website, name='Acceuil' ),
    path('about',  about,name='apropos'),
    path('readmore/<id>/', readmore, name='read_more'),
]
