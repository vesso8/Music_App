from django import forms

from exam_web.web.models import Profile, Album


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('username', 'email', 'age')
        widgets = {
            'username': forms.TextInput(
                attrs= {
                    'placeholder': 'Username',
                }

            ),
            'email': forms.EmailInput(
                attrs= {
                    'placeholder': 'Email',
                }
            ),
            'age': forms.TextInput(
                attrs= {
                    'placeholder': 'Age',
                }
            ),
        }

class CreateAlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ('name', 'artist', 'genre', 'description', 'image', 'price')
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Album Name',
                }
            ),
            'artist': forms.TextInput(
                attrs={
                    'placeholder': 'Artist',
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'placeholder': 'Description',
                }
            ),
            'image': forms.URLInput(
                attrs={
                    'placeholder': 'Image URL',
                }
            ),
            'price': forms.TextInput(
                attrs={
                    'placeholder': 'Price',
                }
            ),
        }

class EditAlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ('name', 'artist', 'genre', 'description', 'image', 'price')

class DeleteAlbumForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.required = False

    def save(self, commit=True):
        self.instance.delete()
        return self.instance
    class Meta:
        model = Album
        fields = ('name', 'artist', 'genre', 'description', 'image', 'price')


class DeleteProfileForm(forms.ModelForm):
    def save(self, commit=True):
        self.instance.delete()
        Album.objects.all().delete()
        return self.instance
    class Meta:
        model = Profile
        fields = ()
