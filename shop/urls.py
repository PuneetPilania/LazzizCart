from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='shopHome'),
    path('about/',views.about,name='AboutUs'),
    path('contact/',views.contact,name='ContactUs'),
    path('tracker/',views.tracker,name='TrackingStatus'),
    path('search/',views.search,name='Search'),
    path('products/<int:id>',views.prodview,name='ProductView'),
    path('checkout/',views.checkout,name='Checkout'),
    path('orderHistory/',views.orderHistory,name='orderHistory'),
]


