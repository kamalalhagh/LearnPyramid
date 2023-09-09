from HelloWorld.views.default import my_view
from HelloWorld.views.notfound import notfound_view


def test_my_view(app_request):
    info = my_view(app_request)
    assert app_request.response.status_int == 200
    assert info['project'] == 'HelloWorld'

def test_notfound_view(app_request):
    info = notfound_view(app_request)
    assert app_request.response.status_int == 404
    assert info == {}
