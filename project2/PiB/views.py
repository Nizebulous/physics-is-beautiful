from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .models import Curriculum, Unit, Module, Lesson, Question, DrawVector, Choice

class Curriculum(generic.ListView):
    model = Unit
    template_name = 'PiB/Curriculum.html'
    context_object_name = 'unit_list'


class ModulePage(generic.DetailView):
    model = Module
    template_name = 'PiB/ModulePage.html'


class LessonPage(generic.DetailView):
    model = Lesson
    template_name = 'PiB/LessonPage.html'


class MultipleChoice(generic.DetailView):
    model = Question
    template_name = 'PiB/problemTemplates/MultipleChoice.html'


class DrawVector(generic.DetailView):
    model = DrawVector
    template_name = 'PiB/problemTemplates/DrawVector.html'


def DrawVectorValidation(request, question_id):
    question = get_object_or_404(DrawVector, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
