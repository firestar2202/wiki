from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from random import seed
from random import randint
from django.db import models
from django import forms

import markdown2

from . import util


class SearchForm(forms.Form):
    search = forms.CharField(label="Wiki Search")


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def page(request, pagename):
    if pagename.upper() in map(str.upper, util.list_entries()):
        return render(request, "encyclopedia/page.html", {
            "Title": pagename, "page": markdown2.markdown(util.get_entry(pagename))
        })
    else:
        return render(request, "encyclopedia/error.html", {
            "error": pagename
        })


def random(request):
    value = randint(1, len(util.list_entries()) - 1)
    return render(request, "encyclopedia/page.html", {
        "Title": "Random", "page": markdown2.markdown(util.get_entry(util.list_entries()[value]))
    })


def get_search(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populat
        # e it with data from the request:
        form = SearchForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            search = form.cleaned_data['search']
            if search.upper() in map(str.upper, util.list_entries()):
                return render(request, "encyclopedia/page.html", {
                    "Title": search, "page": markdown2.markdown(util.get_entry(search))
                })
            else:
                results = []
                for entry in util.list_entries():
                    if search.upper() in entry.upper():
                        results.append(entry)
                return render(request, 'encyclopedia/search_results.html', {'entries': results})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = SearchForm()

    return render(request, 'encyclopedia/search.html', {'form': form, 'entries': util.list_entries()})
