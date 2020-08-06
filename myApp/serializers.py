from .models import Contact,Category,Course,Branch
from rest_framework import serializers

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields=[
            'name',
            'imgpath'
        ]
    
    def create(self,validated_data):
       return Category.objects.create(**validated_data)


class BranchSerializer(serializers.ModelSerializer):
    
    id=serializers.IntegerField(required=False)

    class Meta:
        model = Branch
        fields = [
            'id',
            'latitude',
            'longtitude',
            'address'
            ]
    
    def create(self,validated_data):
       return Branch.objects.create(**validated_data)


class ContactSerializer(serializers.ModelSerializer):
    
    id = serializers.IntegerField(required=False)
    
    class Meta:
        model = Contact
        fields = [
            'id',
            'type',
            'value'
        ]
    
    def create(self,validated_data):
       return Contact.objects.create(**validated_data)


class CourseSerializer(serializers.ModelSerializer):
    
    branch_set = BranchSerializer(many=True)
    contact = ContactSerializer(many=True) 
    category = CategorySerializer()
    class Meta:
        model = Course
        fields = [
            'id',
            'name',
            'description',
            'category',
            'logo',
            'branch_set',
            'contact'
        ]
        depth=1
        
    def create(self,validated_data):
        branches = validated_data.pop('branch_set')
        contacts = validated_data.pop('contact')
        jsoncategory = validated_data.pop('category')
        tocategory = Category.objects.create(**jsoncategory)
        course = Course.objects.create(**validated_data,category=tocategory)

        for branche in branches:
            Branch.objects.create(branchers = course,**branche)

        for contact in contacts:
            Contact.objects.create(**contact,contacts =  course)
        return course