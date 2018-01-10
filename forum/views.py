from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, RedirectView
from django.http import HttpResponseRedirect
from django.urls import reverse

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions

from .models import Question


class QuestionListView(ListView):
    model = Question


class QuestionDetailView(DetailView):
    def get_object(self, *args, **kwargs):
        print(self.request)

        question = Question.objects.get(slug=self.kwargs['slug'])
        question.increment_visualization()

        return question


class QuestionToggleLike(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        slug = self.kwargs.get('slug')
        question = get_object_or_404(Question, slug=slug)
        url_ = question.get_absolute_url()
        user = self.request.user

        if user.is_authenticated():
            if user in question.likes.all():
                question.likes.remove(user)
            else:
                question.likes.add(user)

        return url_


class QuestionToggleLikeAPI(APIView):
    authentication_classes = (authentication.SessionAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, slug=None, format=None):
        question = get_object_or_404(Question, slug=slug)
        url_ = question.get_absolute_url()
        user = self.request.user
        updated = liked = False

        if user.is_authenticated:
            if user in question.likes.all():
                question.likes.remove(user)
            else:
                liked = True
                question.likes.add(user)
            
            updated = True
        
        data = {'updated': updated, 'liked': liked}

        return Response(data)
