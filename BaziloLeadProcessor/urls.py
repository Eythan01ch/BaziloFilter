from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from . import views

urlpatterns = [
    path('process_lead/', views.LeadAddView.as_view()),
    path('api-token-auth/', obtain_auth_token)

]