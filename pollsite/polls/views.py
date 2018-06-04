from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question
from django.template import loader
from django.urls import reverse
# Create your views here.
def index(request):
	print("masuk")
	latest_question_list = Question.objects.order_by('-pub_date')[:5]
	#template = loader.get_template('polls/index.html')
	context = {
		'latest_question_list' : latest_question_list,
	}
	#output = ', '.join([q.question_text for q in latest_question_list])
	return render(request, 'polls/index.html', context)

def detail(request, question_id):
	q = get_object_or_404(Question, pk=question_id)
	return render(request, 'polls/details.html', {'question' : q})

def results(request, question_id):
	q = get_object_or_404(Question, pk=question_id)
	return render(request, 'polls/results.html', {'question' : q})

def vote(request, question_id):
	q = get_object_or_404(Question, pk=question_id)

	try:
		selected_choice = q.choice_set.get(pk=request.POST['choice'])
	except  (KeyError, Choice.DoesNotExist):
		return render(request, 'polls/detail.html', {
			'question' : q,
			'error_message' : "You didn't choose anything!",
			})
	else:
		selected_choice.votes += 1
		selected_choice.save()

		return HttpResponseRedirect(reverse('polls:results', args={q.id,}))

