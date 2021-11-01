"""World_books URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from catalog.views import *
from django.conf.urls import url

urlpatterns = [
    path('', index, name='index'),
    path('authors_add/', authors_add, name='authors_add'),
    path('edit1/<int:id>/', edit1, name='edit1'),
    path('create/', create, name='create'),
    path('delete/<int:id>/', delete, name='delete'),
    path('admin/', admin.site.urls),
    url(r'^books/$', BookListView.as_view(), name='books'),
    url(r'^book/(?P<pk>\d+)$', BookDetailView.as_view(), name='book-detail'),
    url(r'^authors/$', AuthorListView.as_view(), name='authors'),
    ]

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]

urlpatterns += [
    url(r'^mybooks/$', LoanedBooksByUserListView.as_view(), name='my-borrowed'),
]

urlpatterns += [
    url(r'^book/create/$', BookCreate.as_view(), name='book_create'),
    url(r'^book/update/(?P<pk>\d+)$', BookUpdate.as_view(), name='book_update'),
    url(r'^book/delete/(?P<pk>\d+)$', BookDelete.as_view(), name='book_delete'),
]