import datetime

from django.shortcuts import render, redirect
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework import viewsets, permissions
from .filters import *
from django.views import generic, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponse
from .forms import *


class CountryViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]

    queryset = Country.objects.all().order_by('name')
    serializer_class = CountrySerializer

    filter_class = LanguageFilterSet
    search_fields = ['name']

    def get_serializer_class(self):

        if self.action == 'create' or self.action == 'update' or self.action == 'partial_update':
            return CountryWriteSerializer

        return CountrySerializer

    @action(detail=True, methods=['GET'])
    def neighbours(self, request, pk=None):
        serializer = NeighbourIdSerializer(
            Country.objects.get(pk=pk).neighbours, many=True)
        return Response(serializer.data)


class CountryView(LoginRequiredMixin, generic.TemplateView):
    login_url = '/login/'
    template_name = 'countries/countries.html'


class LoginView(View):
    template_name = 'countries/registration/login.html'

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('countries')

        return render(request, self.template_name)

    def post(self, request):
        if request.user.is_authenticated:
            return redirect('countries')
        else:
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(
                request, username=username, password=password)

            if user is not None:
                login(request, user)
                response = redirect('countries')
                # response.set_cookie('user_password', password, max_age = 24 * 60 * 60)
                return response
            else:
                messages.info(request, 'Username OR password is incorrect')

        return render(request, self.template_name)


class LogoutView(View):

    def get(self, request):
        logout(request)
        return redirect('login')


class RegistrationView(View):
    template_name = 'countries/registration/registration.html'
    registration_form = UserRegistrationForm

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('countries')

        context = {
            "form": self.registration_form
        }
        return render(request, self.template_name, context)

    def post(self, request):
        registered_form = UserRegistrationForm(request.POST)

        if registered_form.is_valid():
            registered_form.save()
            user = registered_form.cleaned_data.get('username')
            messages.success(request, "Registration successful for " + user)
            return redirect('login')

        context = {
            "form": registered_form
        }
        return render(request, self.template_name, context)
