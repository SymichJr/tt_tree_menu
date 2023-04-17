from django import template

from tree_menu.models import MenuItem

register = template.Library()

@register.simple_tag(takes_context=True)
def draw_menu(context, name):
    request = context['request']
    menu_items = MenuItem.objects.filter(parent__isnull=True, name=name)

    def build_tree(items):
        result=[]
        for item in items:
            children = item.get_children()
            result.append({
                'item': item,
                'children': build_tree(children),
                'active': item.get_absolute_url() in request.path
            })
        return result
    
    return build_tree(menu_items)