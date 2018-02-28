from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, "quadratic/index.html")

def rez_nul(request):
    print(request)
    print(request.path)
    print(request.method)
    print(request.POST)
    print(request.GET)
    print(request.GET['a'])    
    print(request.GET['b'])
    print(request.GET['c'])
    #print(dir(request.GET))
    return HttpResponse("This is rez_nul views!!")

def quadratic_results(request, a, b, c):
    print("par a = %s, b = %s, c= %s." % (a, b , c))
    print(request)
    print(request.method)
    print(request.POST)
    print(request.GET)
      

    return HttpResponse("You're looking at question %s, %s, %s." % (a, b , c))

    # question = get_object_or_404(Question, pk=question_id)
    # try:
    #     selected_choice = question.choice_set.get(pk=request.POST['choice'])
    # except (KeyError, Choice.DoesNotExist):
    #     # Redisplay the question voting form.
    #     return render(request, 'polls/detail.html', {
    #         'question': question,
    #         'error_message': "You didn't select a choice.",
    #     })
    # else:
    #     selected_choice.votes += 1
    #     selected_choice.save()
    #     # Always return an HttpResponseRedirect after successfully dealing
    #     # with POST data. This prevents data from being posted twice if a
    #     # user hits the Back button.
    #     return HttpResponseRedirect(reverse('quadratic:results', args=(question.id,)))