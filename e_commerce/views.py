from django.contrib.auth import authenticate, login, get_user_model
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import ContactForm, LoginForm, RegisterForm


def home_page(request):
    context = {
        "title": "Pagina Principal",
        "content": "Bem vindo a página principal"
    }
    if request.user.is_authenticated:
        context["premium_content"] = "Você é um usuário Premium"
    return render(request, "home_page.html", context)


def about_page(request):
    context = {
        "title": "Página sobre",
        "content": "Bem vindo a página sobre"
    }
    return render(request, "about/view.html", context)


def contact_page(request):
    contact_form = ContactForm(request.POST or None)
    context = {
        "title": "Página de contato",
        "content": "Bem vindo a página de contato",
        "form": contact_form
    }
    if contact_form.is_valid():
        print(contact_form.cleaned_data)
    """
    if request.method == "POST":
        print(request.POST)
        print(request.POST.get('nome_completo'))
        print(request.POST.get('email'))
        print(request.POST.get('mensagem')) 
    """
    return render(request, "contact/view.html", context)


def login_page(request):
    form = LoginForm(request.POST or None)
    context = {
                "form": form
              }
    print("User logged in")
    # print(request.user.is_authenticated)
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(request, username=username, password=password)
        print(user)
        # print(request.user.is_authenticated)
        if user is not None:
            # print(request.user.is_authenticated)
            login(request, user)
            print("Login válido")
            # Redireciona para uma página de sucesso.
            return redirect("/")
        else:
            # Retorna uma mensagem de erro de 'invalid login'.
            print("Login inválido")
    return render(request, "auth/login.html", context)


User = get_user_model()


def register_page(request):
    form = RegisterForm(request.POST or None)
    context = {
                    "form": form
              }
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get("username")
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        new_user = User.objects.create_user(username, email, password)
        print(new_user)
    return render(request, "auth/register.html", context)

