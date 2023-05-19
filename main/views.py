from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import Timetable, Group, GroupMembers, MainTest, Subject, SubjectItems, UserSubject, UserAbsence
from rest_framework import generics, status
from .serializers import TimetableSerializer, SubjectSerializer, UserSubjectSerializer, UserSubjectListSerializer, \
    UserAbsenceSerializer, GroupSerializer, SubjectItemsSerializer, GroupMembersSerializer, MainTestSerializer


class MainTestListAPIView(generics.ListAPIView):
    serializer_class = MainTestSerializer

    def get_queryset(self):
        queryset = MainTest.objects.all()
        sub = self.request.GET.get('subject_id')
        if sub:
            queryset = queryset.filter(subject_id=sub)
        return queryset


class MainTestCreateAPIView(generics.CreateAPIView):
    serializer_class = MainTestSerializer
    queryset = MainTest.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        user = self.request.user
        subject = Subject.objects.filter(teacher=user).first()
        serializer.is_valid(raise_exception=True)
        serializer.validated_data['subject'] = subject
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class GroupMembersListAPIView(generics.ListAPIView):
    serializer_class = GroupMembersSerializer

    def get_queryset(self):
        group_id = self.request.GET.get('group_id')
        queryset = GroupMembers.objects.all()
        if group_id:
            queryset = queryset.filter(group_id=group_id)
        return queryset


class GroupListAPIView(generics.ListAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class TimeTableAPIView(generics.ListAPIView):
    queryset = Timetable.objects.all()
    serializer_class = TimetableSerializer


class SubjectListAPIView(generics.ListAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class TakeSubjectAPIView(generics.CreateAPIView):
    serializer_class = UserSubjectSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.validated_data['user'] = self.request.user
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class UserAbsenceListAPIView(generics.ListAPIView):
    serializer_class = UserAbsenceSerializer

    def get_queryset(self):
        queryset = UserAbsence.objects.filter(user=self.request.user)
        return queryset


class UserSubjectsListAPIView(generics.ListAPIView):
    serializer_class = UserSubjectListSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = UserSubject.objects.filter(user=self.request.user)
        return queryset


class TaskCreateAPIView(generics.CreateAPIView):
    queryset = SubjectItems.objects.all()
    serializer_class = SubjectItemsSerializer

    def create(self, request, *args, **kwargs):
        user = self.request.user
        subject = Subject.objects.filter(teacher=user).first()
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.validated_data['teacher'] = user
        serializer.validated_data['subject'] = subject
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
