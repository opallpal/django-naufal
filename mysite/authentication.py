from  django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout

def login(request):
    template_name = "login.html"
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        if not username or not password:
            pesan = "username dan password wajib diisi"
        else :
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                pesan = "berhasil Login"
                return redirect('/')
            else:
                pesan = "username atau passworf salah"

    context = {}
    return render(request, template_name, context)

def registrasi(request):
    template_name = "registrasi.html"
    if request.method == "POST":
        username = request.POST.get('username')
        nama_depan = request.POST.get('nama_depan')
        nama_belakang = request.POST.get('nama_belakang')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 != password2:
            context = {'error': "Password tidak cocok"}
            return render(request, template_name, context)

        if User.objects.filter(username=username).exists():
            context = {'error': "Username sudah digunakan"}
            return render(request, template_name, context)

        user = User.objects.create_user(
            username=username,
            password=password1,
            first_name=nama_depan,
            last_name=nama_belakang
        )
        user.save()
        return redirect("/auth-login")

    return render(request, template_name)



def logout(request):
    auth_logout(request)
    return redirect('/')