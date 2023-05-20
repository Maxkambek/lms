from django.db import models
from accounts.models import User


class Timetable(models.Model):
    name = models.CharField(max_length=123)
    file = models.FileField(upload_to='files/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Group(models.Model):
    name = models.CharField(max_length=123)

    def __str__(self):
        return self.name

    @property
    def get_count(self):
        return self.group_members.count()


class GroupMembers(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='group_members')


class Subject(models.Model):
    name = models.CharField(max_length=223)
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class MainTest(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    question_name = models.TextField()
    answer_a = models.CharField(max_length=223)
    answer_b = models.CharField(max_length=223)
    answer_c = models.CharField(max_length=223)
    answer_d = models.CharField(max_length=223)
    answer_true = models.CharField(max_length=223)

    def __str__(self):
        return self.question_name


class UserSubject(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.phone


class UserAbsence(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    count_nb = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.user.phone


class SubjectItems(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.SET_NULL, null=True)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    deadline = models.CharField(max_length=30)
    ball_max = models.FloatField(default=10)
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)
    task_file = models.FileField(upload_to='files/')

    def __str__(self):
        return self.group.name
