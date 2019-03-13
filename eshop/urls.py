from django.urls import include, path
from django.conf.urls import url
from django.contrib import admin

from graphene_django.views import GraphQLView


urlpatterns = [
    path('grappelli/', include('grappelli.urls')), # grappelli URLS
    url(r'^admin/', admin.site.urls),
    url(r'^graphql', GraphQLView.as_view(graphiql=True)),
]
