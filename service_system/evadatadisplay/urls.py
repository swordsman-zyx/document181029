from django.conf.urls import url
from evadatadisplay.views import EvaluationView

urlpatterns = [
    url(r'^evaluation$', EvaluationView.as_view()),
    url(r'^evaluation/(?P<user_id>\w+)$', EvaluationView.as_view()),
]