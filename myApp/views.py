from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from .models import Course,Contact,Category,Branch
from rest_framework.parsers import JSONParser
# Create your views here.

class CourseAPI(APIView):
    def get(self,request):
        courses=Course.objects.all()
        ser=CourseSerializer(courses,many=True)
        return Response(ser.data,status=200)

    def post(self,request):
        data = request.data
        s = CourseSerializer(data=data)
        if s.is_valid():
            Coursedata = s.save()
            return Response(s.data,status=201)
        return Response(s.errors,status=400)
        
'''
class CategoryAPI(APIView):
     def get(self,request):
        courses=Category.objects.all()
        ser=CategorySerializer(courses,many=True)           
        return Response(ser.data,status=200)    
     
     def post(self,request):
        data = request.data
        s = CategorySerializer(data=data)
        if s.is_valid():
            Categorydata = s.save()
            return Response({'Category:post true'}) 
        return Response({'Category:post err'})

class BranchAPI(APIView):
     def get(self,request):
        courses=Branch.objects.all()
        ser=BranchSerializer(courses,many=True)           
        return Response(ser.data,status=200)

     def post(self,request):
        data = request.data
        s = BranchSerializer(data=data)
        if s.is_valid():
            Branchdata = s.save()
            return Response({'Branch:post true'}) 
        return Response({'Branch:post err'})

class ContactAPI(APIView):
     def get(self,request):
        courses=Contact.objects.all()
        ser=ContactSerializer(courses,many=True)           
        return Response(ser.data,status=200)

     def post(self,request):
        data = request.data
        s = ContactSerializer(data=data)
        if s.is_valid():
            Contactdata = s.save()
            return Response({'Contact:post true'}) 
        return Response({'Contact:post err'})   
'''
class CourseDetailAPI(APIView):
    def get_course(self,id):
        try:
            return Course.objects.get(id=id)
        except Course.DoesNotExist:
            return Response({"error":"Object is not found"},status = 404)

    def get(self,request,id):
        obj = self.get_course(id)
        ser = CourseSerializer(obj)
        return Response(ser.data)

    def delete(self,request,id):
        obj = self.get_course(id)
        obj.delete()
        return Response({"delete":"true"},status=204)
'''
class CategoryDetailAPI(APIView):
    def get_category(self,id):
            try:
                return Category.objects.get(id=id)
            except Category.DoesNotExist:
                return Response({"error":"Object is not found"},status = 404)
    def get(self,request,id):
            obj = self.get_category(id)
            ser = CategorySerializer(obj)
            return Response(ser.data)

class BranchDetailAPI(APIView):
    def get_branch(self,id):
            try:
                return Branch.objects.get(id=id)
            except Branch.DoesNotExist:
                return Response({"error":"Object is not found"},status = 404)
    def get(self,request,id):
            obj = self.get_branch(id)
            ser = BranchSerializer(obj)
            return Response(ser.data)



class ContactDetailAPI(APIView):
    def get_contact(self,id):
            try:
                return Contact.objects.get(id=id)
            except Contact.DoesNotExist:
                return Response({"error":"Object is not found"},status = 404)
    def get(self,request,id):
            obj = self.get_contact(id)
            ser = ContactSerializer(obj)
            return Response(ser.data)
'''