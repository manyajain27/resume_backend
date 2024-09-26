from rest_framework import serializers
from .models import PersonalDetail, WorkExperience, Education, Skill, Interest

class WorkExperienceSerializer(serializers.ModelSerializer):
    description = serializers.ListField(child=serializers.CharField())

    class Meta:
        model = WorkExperience
        fields = ['company', 'start_date', 'end_date', 'position', 'location', 'description']

class EducationSerializer(serializers.ModelSerializer):
    description = serializers.ListField(child=serializers.CharField())

    class Meta:
        model = Education
        fields = ['university', 'start_date', 'end_date', 'degree', 'location', 'description']

class SkillSerializer(serializers.ModelSerializer):
    skill_name = serializers.CharField()

    class Meta:
        model = Skill
        fields = ['skill_name']

class InterestSerializer(serializers.ModelSerializer):
    interest_name = serializers.CharField()

    class Meta:
        model = Interest
        fields = ['interest_name']

class PersonalDetailSerializer(serializers.ModelSerializer):
    work_experience = WorkExperienceSerializer(many=True, required=True)
    education = EducationSerializer(many=True, required=True)
    skills = SkillSerializer(many=True, required=True)
    interests = InterestSerializer(many=True, required=True)

    class Meta:
        model = PersonalDetail
        fields = ['name', 'email', 'phone', 'website', 'work_experience', 'education', 'skills', 'interests']

    def create(self, validated_data):
        work_experience_data = validated_data.pop('work_experience')
        education_data = validated_data.pop('education')
        skills_data = validated_data.pop('skills')
        interests_data = validated_data.pop('interests')

        personal_detail = PersonalDetail.objects.create(**validated_data)

        for work in work_experience_data:
            WorkExperience.objects.create(personal_detail=personal_detail, **work)

        for edu in education_data:
            Education.objects.create(personal_detail=personal_detail, **edu)

        for skill in skills_data:
            Skill.objects.create(personal_detail=personal_detail, skill_name=skill['skill_name'])

        for interest in interests_data:
            Interest.objects.create(personal_detail=personal_detail, interest_name=interest['interest_name'])

        return personal_detail
