from django.core.exceptions import ObjectDoesNotExist
from django.http.response import HttpResponseRedirect,  HttpResponseNotFound
from django.shortcuts import render
from publications.forms import PublicationEditForm
from publications.models import Publication
from publications.forms import ModelFormWithFileField


def add_publication(request):
    if request.method == 'POST':
        form = ModelFormWithFileField(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(f'/publication/show/')

    elif request.method == 'GET':
        form = ModelFormWithFileField()

    return render(
        request,
        template_name='publication/publication_add.html',
        context={
            'form': form
        }
    )


def publication_show(request):
    img = Publication.objects.all()
    return render(
        request,
        template_name='publication/publication_show.html',
        context={
            'img': img
        }
    )


def get_publication(request, slug):
    img = Publication.objects.filter(profile_id=slug)
    return render(
        request,
        template_name='publication/publication_show.html',
        context={
            'img': img
        }
    )


def edit_publication(request, slug):
    try:
        publication = Publication.objects.get(id=slug)
    except ObjectDoesNotExist:
        return HttpResponseNotFound(f'Profile id {slug} not found')
    if request.method == 'POST':
        form = PublicationEditForm(request.POST, request.FILES, instance=publication)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(f'/publication/show/')

    elif request.method == 'GET':
        form = PublicationEditForm(instance=publication)

    return render(
        request,
        template_name='publication/publication_edit.html',
        context={
            'form': form
        }
    )