from django.urls import path
from estoque import views as v

app_name= 'estoque'

urlpatterns = [
    path('estoque/', v.estoque_entrada_list, name="estoque_entrada_list"),

]