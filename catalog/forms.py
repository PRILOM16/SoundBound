from django import forms
from .models import Song


class SongForm(forms.ModelForm):

    artist_choice = forms.ChoiceField(
        label='Автор',
        choices=[],
        required=False,
        widget=forms.Select(attrs={
            'class': 'w-full bg-white border border-gray-300 rounded-xl px-4 py-3'
        })
    )

    new_artist = forms.CharField(
        label='Новый автор',
        required=False,
        max_length=250,
        widget=forms.TextInput(attrs={
            'class': 'w-full bg-white border border-gray-300 rounded-xl px-4 py-3',
            'placeholder': 'Введите имя автора'
        })
    )

    class Meta:
        model = Song
        fields = [
            'title',
            'year',
            'price',
            'demo_audio',
            'full_audio',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        artists = Song.objects.values_list(
            'artist', flat=True
        ).distinct().order_by('artist')

        choices = [('', 'Выберите автора')]
        choices += [(artist, artist) for artist in artists]

        self.fields['artist_choice'].choices = choices

    def clean(self):
        cleaned_data = super().clean()

        artist_choice = cleaned_data.get('artist_choice')
        new_artist = cleaned_data.get('new_artist', '').strip()

        if new_artist:
            cleaned_data['artist'] = new_artist

        elif artist_choice:
            cleaned_data['artist'] = artist_choice

        else:
            self.add_error(
                'artist_choice',
                'Выберите автора или добавьте нового.'
            )

        return cleaned_data

    def save(self, commit=True):
        song = super().save(commit=False)
        song.artist = self.cleaned_data['artist']

        if commit:
            song.save()

        return song