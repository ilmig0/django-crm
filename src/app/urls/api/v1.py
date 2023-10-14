from django.urls import include, path

urlpatterns = [
    path('v1/products/', include('products.urls')),
]
