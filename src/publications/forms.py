from django.forms import ModelForm
from publications.models import Publication


class ModelFormWithFileField(ModelForm):
    class Meta:
        model = Publication
        fields = '__all__'


class PublicationEditForm(ModelForm):
    class Meta:
        model = Publication
        fields = ['comments',]