from rest_framework import serializers
from .models import Course
from .models import Contact
from .models import Branch
from .models import Category


class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    branches = BranchSerializer(many=True)
    contacts = ContactSerializer(many=True)

    class Meta:
        model = Course
        fields = '__all__'

    def create(self, validated_data):
        branches_data = validated_data.pop('branches')
        contacts_data = validated_data.pop('contacts')
        courses = Course.objects.create(**validated_data)
        for branch_data in branches_data:
            Branch.objects.create(courses=courses, **branch_data)
        for contact_data in contacts_data:
            Contact.objects.create(courses=courses, **contact_data)
        return courses

