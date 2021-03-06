from django.db import models


class Quiz(models.Model):
    title = models.CharField(max_length=250)
    image = models.ImageField(
        upload_to='quiz/%Y/%m/',
        null=True, blank=True,
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{pk}'.format(pk=self.id)


class Question(models.Model):
    quiz = models.ForeignKey(Quiz)
    title = models.CharField(max_length=250)
    image = models.ImageField(
        upload_to='question/%Y/%m/',
        null=True, blank=True,
    )
    sequence = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{} : {}'.format(self.sequence, self.title)

class Answer(models.Model):
    question = models.ForeignKey(Question)
    content = models.CharField(max_length=250)
    sequence = models.IntegerField(default=0)
    code = models.CharField(max_length=2)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class Result(models.Model):
    quiz = models.ForeignKey(Quiz)
    content = models.TextField()
    code = models.CharField(max_length=2)
    image = models.ImageField(
        upload_to='result/%Y/%m/',
        null=True, blank=True,
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class UserScore(models.Model):
    session_key = models.CharField(max_length=32)
    previous = models.OneToOneField('self', null=True)
    quiz = models.ForeignKey(Quiz)
    answer = models.ForeignKey(Answer)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{pk}'.format(pk=self.id)
