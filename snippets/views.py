from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Course, Category, Branch, Contact
from . serializer import CourseSerializer
from .serializer import CategorySerializer
from .serializer import BranchSerializer
from .serializer import ContactSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser


@csrf_exempt
def branch(request):

    if request.method == 'GET':
        snippets = Branch.objects.all()
        serializer = BranchSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = BranchSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def contact(request):

    if request.method == 'GET':
        snippets = Contact.objects.all()
        serializer = ContactSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ContactSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def category(request):

    if request.method == 'GET':
        snippets = Category.objects.all()
        serializer = CategorySerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CategorySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def category_id(request, pk):

    try:
        snippet = Category.objects.get(pk=pk)
    except Category.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = CategorySerializer(snippet)
        return JsonResponse(serializer.data)

    elif request.method == 'DELETE':
        snippet.delete()
        return HttpResponse(status=204)


@csrf_exempt
def course(request):

    if request.method == 'GET':
        snippets = Course.objects.all()
        serializer = CourseSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CourseSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def course_id(request, pk):

    try:
        snippet = Course.objects.get(pk=pk)
    except Course.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = CourseSerializer(snippet)
        return JsonResponse(serializer.data)

    elif request.method == 'DELETE':
        snippet.delete()
        return HttpResponse(status=204)
