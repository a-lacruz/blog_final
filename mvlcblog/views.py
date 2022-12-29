from django.shortcuts import render
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from mvlcblog.models import Post
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.admin import User
from django.core.exceptions import PermissionDenied
from mvlcblog.forms import UsuarioForm
from mvlcblog.models import Avatar, Post, Mensaje


def inicio(request):
    posts = Post.objects.order_by('-publicado_el').all()
    return render(request,"mvlcblog/inicio.html",{'posts': posts})

class PostDetalle(DetailView):
    model = Post

class PostList(ListView):
    model = Post

class PostCrear(LoginRequiredMixin, CreateView):
     model = Post
     success_url = reverse_lazy("mvlcblog-listar")
     fields = '__all__'

class PostBorrar(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy("mvlcblog-listar")

class PostActualizar(LoginRequiredMixin, UpdateView):
    model = Post
    success_url = reverse_lazy("mvlcblog-listar")
    fields = "__all__"

class UserSignUp(CreateView):
    form_class = UsuarioForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('mvlcblog-listar')

class UserLogin(LoginView):
    next_page = reverse_lazy('mvlcblog-listar')

class UserLogout(LogoutView):
    next_page = reverse_lazy('mvlcblog-inicio')

class AvatarActualizar(UpdateView):
    model = Avatar
    fields = ['imagen']
    success_url = reverse_lazy('mvlcblog-listar')
    def get_object(self):
    # Obtener el avatar del usuario logueado
        avatar = Avatar.objects.get(user=self.request.user)
    # Verificar que el usuario esté tratando de modificar su propio avatar
        if self.request.user.pk != self.kwargs['id']:
    # Si no es el mismo usuario, lanzar una excepción 403 (Forbidden)
            raise PermissionDenied()
    # Si es el mismo usuario, devolver el objeto
        return avatar
    
class UserActualizar(UpdateView):
    model = User
    fields = ['first_name','last_name', 'email' ]
    success_url = reverse_lazy('mvlcblog-listar')
    def get_object(self, *args, **kwargs):
        # Obtener el objeto de la base de datos
        object = super(UserActualizar, self).get_object(*args, **kwargs)
        # Comprobar si el usuario logueado es el mismo que el usuario que se está intentando modificar
        if self.request.user != object:
            # Si no es el mismo usuario, lanzar una excepción 403 (Forbidden)
            raise PermissionDenied()
        # Si es el mismo usuario, devolver el objeto
        return object

class MensajeDetalle(DetailView):
    model = Mensaje

class MensajeListar(LoginRequiredMixin, ListView):
    model = Mensaje  

class MensajeCrear(SuccessMessageMixin, CreateView):
    model = Mensaje
    success_url = reverse_lazy("mvlcblog-mensajes-crear")
    fields = ['nombre', 'email', 'texto']
    success_message = "Mensaje de contacto enviado!!"

    def form_valid(self, form):
        response = super().form_valid(form)
        self.extra_context = {'mensaje_exito': self.success_message}
        return response

class MensajeBorrar(LoginRequiredMixin, DeleteView):
    model = Mensaje
    success_url = reverse_lazy("mvlcblog-mensajes-listar")
