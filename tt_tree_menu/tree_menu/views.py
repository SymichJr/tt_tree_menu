from django.shortcuts import render

from .models import MenuItem


def test_tree(request):
    tree = MenuItem.objects.all()
    context = {"tree": tree}
    template = 'tree_menu/test_tree.html'
    return render(request, template, context) 