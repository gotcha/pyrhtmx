from pyramid.view import view_config

from ..models import MyModel


@view_config(context=MyModel, renderer='pyr_htmx:templates/mytemplate.pt')
def my_view(request):
    return {'project': 'Pyramid and HTMX'}
