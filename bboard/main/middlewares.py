# D:\User\Documents\PycharmProjects\MoloshopBY\bboard\main\middlewares.py

from .models import SubRubric


def bboard_context_processor(request):
    context = {}
    context['rubrics'] = SubRubric.objects.all()
    return context