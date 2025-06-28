from django import forms
from django_ckeditor_5.widgets import CKEditor5Widget
from artikel.models import Kategori
from artikel.models import Artikel



class KategoriForms(forms.ModelForm):  # ✅ Perbaiki nama kelas agar lebih jelas dan sesuai PEP8
    class Meta:
        model = Kategori
        fields = ['nama']  # ✅ Gunakan list untuk konsistensi
        widgets = {
            "nama": forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'required': True,
                    'placeholder': 'Masukkan Nama Kategori',  # ✅ Tambahkan placeholder agar lebih user-friendly
                }
            ),
        }



class ArtikelForms(forms.ModelForm):  
    class Meta:
        model =  Artikel
        fields = ('kategori', 'judul','konten','gambar','status')
        widgets = {
            "kategori": forms.Select(
                attrs={
                    'class': 'form-control',
                    'required': True,

                }),

            "judul" : forms.TextInput(
                 attrs={
                    'class': 'form-control',
                    'required': True,
                }),

            "konten" : CKEditor5Widget(
                  attrs={
                      "class": "django_ckeditor_5"}, config_name="extends"
            )
                

            # "gambar" : forms.TextInput(
            #      attrs={
            #         'class': 'form-control',
            #         'required': True,
            #     }),

        #      "status" : forms.TextInput(
        #          attrs={
        #             'class': 'form-control',
        #             'required': True,
        #         }),
        #
        }