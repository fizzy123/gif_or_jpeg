import random

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from gif_or_jpeg.models import Session, Question

def index(request):
    if request.META['REQUEST_METHOD'] == 'GET':
        context = {}
        return render(request, 'gif_or_jpeg/index.html', context)

def question(request, session_id = ''):
    if session_id:
        session = Session.objects.get(id=int(session_id))
    else:    
        session = Session.objects.create()
    session.save()
    if request.META['REQUEST_METHOD'] == 'GET':
        questions  = session.questions.split(',')
        if len(questions) > 9:
            return HttpResponseRedirect(reverse('gif_or_jpeg:results', args=(session.id,)))
        else:
            if session.questions:
                questions = [Question.objects.get(id=int(x)).photo_id for x in session.questions.split(',')]
            else:
                questions = []
            id_array = range(1,30)
            id_array = [id for id in id_array if id not in questions] 
            question = Question.objects.create(photo_id=random.choice(id_array), gif= True if random.random() > .5 else False)
            session.questions = session.questions + (',' if session.questions else '') + str(question.id)
            question.save()
            session.save()
            context = {'filename':'/gif_or_jpg/' + str(question.photo_id) + ('.gif' if question.gif else '.jpg'),'session_id':session.id}
            return render(request, 'gif_or_jpeg/question.html', context)
    if request.META['REQUEST_METHOD'] == 'POST':
        questions = session.questions.split(',')
        question  = Question.objects.get(id=int(questions[-1]))
        if (question.gif == (request.POST['type'] == 'GIF')):
            question.correct = True
        question.save()
        return HttpResponseRedirect(reverse('gif_or_jpeg:question', args=(session.id,)))

def results(request, session_id):
    session = Session.objects.get(id=int(session_id))
    questions = session.questions.split(',')
    score = len([Question.objects.get(id=int(x)).correct for x in questions if Question.objects.get(id=int(x)).correct])
    answers = []
    for x in questions:
        question = Question.objects.get(id=int(x))
        answers.append({'filename': '/gif_or_jpg/' + str(question.photo_id) + '.','correct':question.correct,'type': 'gif' if question.gif else 'jpg'})
        question.delete()
    context = {'answers':answers,'score':score}
    session.delete()
    return render(request, 'gif_or_jpeg/results.html', context)
