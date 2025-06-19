from rest_framework.decorators import api_view
from rest_framework.response import Response
from app.models import Question
from .serializers import QuestionSerializer

@api_view(['GET'])
def getRoutes(request):
    routes = [
        'GET /api',
        'GET /api/questions',
        'GET /api/questions/:count'
    ]

    return Response(routes)

@api_view(['GET'])
def getQuestionsAll(request):
    questions = Question.objects.all()
    serializer = QuestionSerializer(questions, many = True)

    return Response(serializer.data)

@api_view(['GET'])
def getQuestionsCount(request, count):
    questions = Question.objects.order_by('?').all()

    data = [questions[idx] for idx in range(count * 4)]

    serializer = QuestionSerializer(data, many = True)

    return Response(serializer.data)