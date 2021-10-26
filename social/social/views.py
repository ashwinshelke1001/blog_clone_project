''' first view for testing'''
from django.views.generic import TemplateView

class TestPage(TemplateView):
    """
    showing test page view
    """
    template_name = 'test.html'

class ThanksPage(TemplateView):
    """
    showing the thanks page
    """
    template_name = 'thanks.html'

class HomePage(TemplateView):
    """
    showing the index page
    """
    template_name = 'index.html'
