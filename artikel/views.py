from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from artikel.models import Kategori, Artikel
from artikel.forms import KategoriForms, ArtikelForms

# Cek apakah user termasuk group 'Operator'
def in_operator(user):
    return user.groups.filter(name='Operator').exists()

################# USER ######################

@login_required(login_url='/auth-login')
def artikel_list(request):
    template_name = "dashboard/pengguna/artikel_list.html"
    artikel = Artikel.objects.filter(created_by=request.user)
    context = {
        "artikel": artikel,
    }
    return render(request, template_name, context)


@login_required(login_url='/auth-login')
def artikel_tambah(request):
    template_name = "dashboard/artikel_forms.html"  # ✅ GANTI ke file form yang BENAR
    if request.method == "POST":
        forms = ArtikelForms(request.POST, request.FILES)
        if forms.is_valid():
            pub = forms.save(commit=False)
            pub.created_by = request.user
            pub.save()
            messages.success(request, 'Berhasil melakukan tambah artikel')
            return redirect("artikel_list")
    else:
        forms = ArtikelForms()
    context = {
        "forms": forms
    }
    return render(request, template_name, context)

@login_required(login_url='/auth-login')
def update(request, id_artikel):
    template_name = "dashboard/artikel_forms.html"
    artikel = Artikel.objects.get(Artikel, id=id_artikel, created_by=request.user)
    if request.method == "POST":
        forms = ArtikelForms(request.POST, request.FILES, instance=artikel)
        if forms.is_valid():
            pub = forms.save(commit=False)
            pub.created_by = request.user
            pub.save()
            messages.success(request, 'Berhasil melakukan update artikel')
            return redirect("artikel_list")
    else:
        forms = ArtikelForms(instance=artikel)
    context = {
        "forms": forms
    }
    return render(request, template_name, context)

@login_required(login_url='/auth-login')
def artikel_delete(request, id_artikel):
    artikel = get_object_or_404(Artikel, id=id_artikel, created_by=request.user)
    artikel.delete()
    messages.success(request, 'Berhasil melakukan delete artikel')
    return redirect("artikel_list")


################## ADMIN / OPERATOR ###########################

@login_required(login_url='/auth-login')
@user_passes_test(in_operator, login_url='/')
def admin_kategori_list(request):
    template_name = "dashboard/admin/kategori_list.html"
    kategori = Kategori.objects.all()
    context = {
        "kategori": kategori
    }
    return render(request, template_name, context)

@login_required(login_url='/auth-login')
@user_passes_test(in_operator, login_url='/')
def admin_kategori_tambah(request):
    template_name = "dashboard/admin/kategori_forms.html"
    if request.method == "POST":
        forms = KategoriForms(request.POST)
        if forms.is_valid():
            pub = forms.save(commit=False)
            pub.created_by = request.user
            pub.save()
            messages.success(request, 'Berhasil tambah kategori')
            return redirect("admin_kategori_list")
    else:
        forms = KategoriForms()
    context = {
        "forms": forms
    }
    return render(request, template_name, context)

@login_required(login_url='/auth-login')
@user_passes_test(in_operator, login_url='/')
def admin_kategori_update(request, id_kategori):
    template_name = "dashboard/admin/kategori_forms.html"
    kategori = get_object_or_404(Kategori, id=id_kategori)
    if request.method == "POST":
        forms = KategoriForms(request.POST, instance=kategori)
        if forms.is_valid():
            pub = forms.save(commit=False)
            pub.created_by = request.user
            pub.save()
            messages.success(request, 'Berhasil melakukan update kategori')
            return redirect("admin_kategori_list")
    else:
        forms = KategoriForms(instance=kategori)
    context = {
        "forms": forms
    }
    return render(request, template_name, context)

@login_required(login_url='/auth-login')
@user_passes_test(in_operator, login_url='/')
def admin_kategori_delete(request, id_kategori):
    kategori = get_object_or_404(Kategori, id=id_kategori)
    kategori.delete()
    messages.success(request, 'Berhasil melakukan delete kategori')
    return redirect("admin_kategori_list")

################## ADMIN ARTIKEL ####################

@login_required(login_url='/auth-login')
@user_passes_test(in_operator, login_url='/')
def admin_artikel_list(request):
    template_name = "dashboard/admin/artikel_list.html"
    artikel = Artikel.objects.all()
    context = {
        "artikel": artikel
    }
    return render(request, template_name, context)

@login_required(login_url='/auth-login')
@user_passes_test(in_operator, login_url='/')
def admin_artikel_tambah(request):
    template_name = "dashboard/admin/artikel_forms.html"
    if request.method == "POST":
        forms = ArtikelForms(request.POST, request.FILES)
        if forms.is_valid():
            pub = forms.save(commit=False)
            pub.created_by = request.user
            pub.save()
            messages.success(request, 'Berhasil melakukan tambah artikel')
            return redirect("admin_artikel_list")
    else:
        forms = ArtikelForms()
    context = {
        "forms": forms
    }
    return render(request, template_name, context)

@login_required(login_url='/auth-login')
@user_passes_test(in_operator, login_url='/')
def admin_artikel_update(request, id_artikel):
    template_name = "dashboard/admin/artikel_forms.html"
    artikel = get_object_or_404(Artikel, id=id_artikel)
    if request.method == "POST":
        forms = ArtikelForms(request.POST, request.FILES, instance=artikel)
        if forms.is_valid():
            pub = forms.save(commit=False)
            pub.created_by = request.user
            pub.save()
            messages.success(request, 'Berhasil melakukan update artikel')
            return redirect("admin_artikel_list")
    else:
        forms = ArtikelForms(instance=artikel)
    context = {
        "forms": forms
    }
    return render(request, template_name, context)

@login_required(login_url='/auth-login')
@user_passes_test(in_operator, login_url='/')
def admin_artikel_delete(request, id_artikel):
    artikel = get_object_or_404(Artikel, id=id_artikel)
    artikel.delete()
    messages.success(request, 'Berhasil melakukan delete artikel')
    return redirect("admin_artikel_list")
