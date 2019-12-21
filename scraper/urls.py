
from django.contrib import admin
from django.urls import include, path
from scraper.views import PhysicsView


urlpatterns = [
	path('', PhysicsView.as_view()),

]



