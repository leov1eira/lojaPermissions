from django.urls import path, include

from appproduto.views.create_produto_view import ProdutoCreateView
from appproduto.views.list_produto_view import ProdutoListView

app_name = 'appproduto'

urlpatterns = [
    path('', ProdutoListView.as_view(), name='produto_list_view'),
    path('produto/cadastrar', ProdutoCreateView.as_view(), name='produto_create_view'),
]