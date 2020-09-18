from rest_framework import serializers
from .models import *
from accounts.models import User
from accounts.api.serializers import UserSerializer


class WorkExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkExperience
        fields = ['position', 'company', 'start_date', 'end_date', 'location']


class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = ['institution', 'degree', 'start_date', 'end_date']


class EmployeeProfileSerializer(serializers.ModelSerializer):
    workexperience = WorkExperienceSerializer(many=True)
    education = EducationSerializer(many=True, required=True)

    class Meta:
        model = EmployeeProfile
        fields = ['id', 'user', 'first_name', 'last_name', 'gender', 'about', 'phone_number', 'email', 'dob',
                  'title', 'industry', 'location', 'skills', 'portfolio', 'github', 'linkedin', 'twitter', 'image', 'workexperience', 'education']

    def create(self, validated_data):
        works_data = validated_data.pop('workexperience')
        education_data = validated_data.pop('education')
        emp = EmployeeProfile.objects.create(**validated_data)
        for work_data in works_data:
            WorkExperience.objects.create(employee=emp, **work_data)
        for edu_data in education_data:
            Education.objects.create(employee=emp, **edu_data)
        return emp

    def update(self, instance, validated_data):
        works_data = validated_data.pop('workexperience')
        works = (instance.workexperience).all()
        works = list(works)
        edu_data = validated_data.pop('education')
        degrees = (instance.education).all()
        degrees = list(degrees)
        instance.user = validated_data.get(
            'user', instance.user)
        instance.first_name = validated_data.get(
            'first_name', instance.first_name)
        instance.last_name = validated_data.get(
            'last_name', instance.last_name)
        instance.gender = validated_data.get(
            'gender', instance.gender)
        instance.about = validated_data.get('about', instance.about)
        instance.dob = validated_data.get('dob', instance.dob)
        instance.phone_number = validated_data.get(
            'phone_number', instance.phone_number)
        instance.email = validated_data.get('email', instance.email)
        instance.title = validated_data.get(
            'title', instance.title)
        instance.industry = validated_data.get(
            'industry', instance.industry)
        instance.location = validated_data.get(
            'location', instance.location)
        instance.skills = validated_data.get(
            'skills', instance.skills)
        instance.portfolio = validated_data.get(
            'portfolio', instance.portfolio)
        instance.github = validated_data.get('github', instance.github)
        instance.linkedin = validated_data.get('linkedin', instance.linkedin)
        instance.twitter = validated_data.get('twitter', instance.twitter)
        instance.image = validated_data.get('image', instance.image)
        instance.save()

        for work_data in works_data:
            work = works.pop(0)
            work.position = work_data.get('position', work.position)
            work.company = work_data.get('company', work.company)
            work.start_date = work_data.get('start_date', work.start_date)
            work.end_date = work_data.get('end_date', work.end_date)
            work.location = work_data.get('location', work.location)
            work.save()

        for edu in edu_data:
            degree = degrees.pop(0)
            degree.institution = edu.get('institution', degree.institution)
            degree.degree = edu.get('degree', degree.degree)
            degree.start_date = edu.get('start_date', degree.start_date)
            degree.end_date = edu.get('end_date', degree.end_date)
            degree.save()
        return instance


class EmployerProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployerProfile
        fields = ['id', 'user', 'email', 'company_name', 'full_form', 'location', 'website',
                  'industry', 'company_size', 'company_type', 'pan', 'linkedin', 'twitter', 'overview', 'image']
