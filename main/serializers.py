from .models import Timetable, Group, GroupMembers, MainTest, Subject, SubjectItems, UserSubject, UserAbsence
from rest_framework import serializers
from accounts.serializers import UserSerializer


class MainTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainTest
        fields = ['id', 'answer_true', 'question_name', 'answer_a', 'answer_b', 'answer_c', 'answer_d']


class TimetableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Timetable
        fields = ['id', 'name', 'file', 'created_at']


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['id', 'name', 'get_count']


class GroupMembersSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = GroupMembers
        fields = ['id', 'user']


class UserSubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSubject
        fields = ['subject']


class SubjectItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubjectItems
        fields = ['id', 'deadline', 'ball_max', 'task_file', 'group']


class SubjectSerializer(serializers.ModelSerializer):
    teacher = UserSerializer()

    class Meta:
        model = Subject
        fields = ['id', 'name', 'teacher']


class UserSubjectListSerializer(serializers.ModelSerializer):
    subject = SubjectSerializer()

    class Meta:
        model = UserSubject
        fields = ['id', 'subject']


class UserAbsenceSerializer(serializers.ModelSerializer):
    subject = SubjectSerializer()

    class Meta:
        model = UserAbsence
        fields = ['id', 'subject', 'count_nb']
