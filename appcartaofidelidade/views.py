from django.contrib.auth.models import User, Group
from django.shortcuts import render, get_object_or_404, redirect
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter


# Create your views here.
from rest_framework import viewsets

from appcartaofidelidade.models import Registros, Servicos, Premios
from appcartaofidelidade.serializers import UserSerializer, GroupSerializer, RegistrosSerializer, ServicosSerializer, \
    PremiosSerializer


def index(request):

    return render(request, 'appcartaofidelidade/index.html',{})


'''def cliente_list(request):
    clientes = Clientes.objects.all()
    return render(request, 'appcartaofidelidade/cliente_list.html', {'clientes':clientes})

def cliente_detail(request, pk):
    cliente = get_object_or_404(Clientes, pk=pk)
    return render(request, 'appcartaofidelidade/cliente_detail.html', {'cliente':cliente})
'''
'''def cliente_new(request):

    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            cliente = form.save(commit=True)
            print(cliente.pk)
            return redirect('cliente_detail', pk=cliente.pk)
    else:
        form = ClienteForm()
    return render(request, 'appcartaofidelidade/cliente_edit.html',{'form': form})


def cliente_edit(request, pk):
    cliente = get_object_or_404(Clientes, pk=pk)
    if request.method == "POST":
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            cliente = form.save(commit=True)
            print(cliente.pk)
            return redirect('cliente_detail', pk=cliente.pk)
    else:
        form = ClienteForm(instance=cliente)
    return render(request, 'appcartaofidelidade/cliente_edit.html',{'form': form})

'''


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

'''class ClienteFilter(django_filters.FilterSet):
    nome = django_filters.CharFilter(lookup_expr='icontains')

    #year_joined = django_filters.NumberFilter(name='date_joined', lookup_expr='year')

    class Meta:
        model = Clientes
        fields = ['nome',]
'''
#class ClientesViewSet(viewsets.ModelViewSet):
#    """
#    API endpoint that allows users to be viewed or edited.
#    """
#    __basic_fields =  ('nome', 'email','cpf')
#    queryset = Clientes.objects.all()
#    serializer_class = ClientesSerializer
#    #filter_backends = (filters.SearchFilter,)
#    filter_backends = (filters.DjangoFilterBackend, SearchFilter, OrderingFilter)
#    filter_fields = __basic_fields
#    search_fields = __basic_fields
#    #filter_class = ClienteFilter
#    #together = ['nome']
#    #search_fields = ('id','nome', 'email','cpf')



'''
class EmpresasViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Empresas.objects.all()
    serializer_class = EmpresasSerializer
 '''

#class EnderecoClientesViewSet(viewsets.ModelViewSet):
#   """
#    API endpoint that allows users to be viewed or edited.
#    """
#    queryset = EnderecoClientes.objects.all()
#    serializer_class = EnderecoClientesSerializer

class RegistrosViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    __basic_fields = ('data', 'servico', 'cliente', 'status')

    queryset = Registros.objects.all()
    serializer_class = RegistrosSerializer

    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    filter_fields = __basic_fields
    search_fields = __basic_fields

class ServicosViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    __basic_fields = ('cod_servico','idempresa', 'descricao', 'validade', 'entradas','premio')
    queryset = Servicos.objects.all()
    serializer_class = ServicosSerializer

    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    filter_fields = __basic_fields
    search_fields = __basic_fields

class PremiosViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    __basic_fields = ('data', 'servico', 'cliente', 'baixado')

    queryset = Premios.objects.all()
    serializer_class = PremiosSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    filter_fields = __basic_fields
    search_fields = __basic_fields
