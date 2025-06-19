from django.shortcuts import render, redirect
from .models import Question

def home(request):
    if request.method == 'POST':
        players = request.POST

        request.session['players'] = [players[key] for key in players if 'player' in key and players[key]]

        return redirect('select_game')

    context = {}

    return render(request, 'app/home.html', context)

def select_game(request):
    if request.method == 'POST':
        count = int(request.POST.get('count').split()[0])

        request.session['count'] = count

        return redirect('game')

    context = {}

    return render(request, 'app/select_game.html', context)

def game(request):
    context = {
        'count' : request.session['count'] * len(request.session['players']),
        'players' : request.session['players'],
        'player_count' : len(request.session['players'])
    }

    return render(request, 'app/game.html', context)

def winner(request, index):
    if index == 69:
        context = {
            'tie' : True
        }

        return render(request, 'app/winner.html', context)

    name = request.session['players'][index]

    context = {
        'winner' : name,
        'tie' : False
    }

    return render(request, 'app/winner.html', context)

def add_question(request):
    if request.method == 'POST':
        args = request.POST

        Question.objects.create(
            question_text = args.get('question_text'),
            variant_a = args.get('variant_a'),
            variant_b = args.get('variant_b'),
            variant_c = args.get('variant_c'),
            variant_d = args.get('variant_d'),
            correct_answer = ['a', 'b', 'c', 'd'].index(args.get('correct_answer').lower())
        )

        return redirect('add_question')

    context = {}

    return render(request, 'app/add_question.html', context)

def update_question(request):
    if request.method == 'POST':
        args = request.POST

        query_question = Question.objects.get(
            id = int(args.get('id'))
        )

        query_question.question_text = args.get('question_text')

        query_question.variant_a = args.get('variant_a')
        query_question.variant_b = args.get('variant_b')
        query_question.variant_c = args.get('variant_c')
        query_question.variant_d = args.get('variant_d')

        query_question.correct_answer = ['a', 'b', 'c', 'd'].index(args.get('correct_answer').lower())

        query_question.save()

        return redirect('update_question')

    context = {}

    return render(request, 'app/update_question.html', context)
