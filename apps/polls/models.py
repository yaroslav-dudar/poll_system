from django.db import models

class Question(models.Model):
	description = models.CharField(max_length=1024)
	multipe_choice = models.BooleanField(default=False)

	def __unicode__(self):
		return self.description


class Answer(models.Model):
	text = models.CharField(max_length=1024)
	question_answers = models.ForeignKey(Question)
	value = models.IntegerField()

	def __unicode__(self):
		return self.text

		
class Poll(models.Model):
	name = models.CharField(max_length=256)
	questions = models.ManyToManyField(Question)

	def __unicode__(self):
		return self.name


class PollResult(models.Model):
	poll = models.OneToOneField(Poll, primary_key=True)
	date = models.DateField()
	total_value = models.IntegerField()

	def __unicode__(self):
		return self.poll.name
