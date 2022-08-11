from http.client import HTTPResponse
from django.shortcuts import render
from .models import Candidate
from rest_framework.response import Response 
from .serializers import CandidateSerializer, StatusSerializer
from rest_framework.decorators import api_view
from django.core.files import File
from .forms import CandidateForm

# Create your views here.

@api_view(['GET'])
def showall(request):
    candidates = Candidate.objects.all()
    serializer = CandidateSerializer(candidates, many=True)
    obj = serializer.data
    return render(request, template_name='homepage.html', context={'obj':obj})


@api_view(['GET'])
def candidate_info(request,pk):
    aplicant = Candidate.objects.get(id=pk)
    serializer = CandidateSerializer(aplicant, many=False)
    candidate_data = serializer.data
    # return Response(serializer.data)
    return render(request, template_name='candidate_info.html', context={'candidate':candidate_data})


def react(request):
    candidates = Candidate.objects.all()
    serializer = CandidateSerializer(candidates, many=True)
    obj = serializer.data
    # return Response(obj)
    return render(request, template_name='homepage.html', context={'obj':obj})


def readfile(request):
    f = open('job_portal', 'r')
    if f.mode == 'r':
       contents =f.read()
       print (contents)
    return HTTPResponse()   

@api_view(['GET'])
def accept_or_reject(request,pk):
    # import pdb
    # pdb.set_trace()
    # serializer = CandidateSerializer(data=request.data)
    # if request.method == 'POST':
    #     current_user = Candidate.objects.get(pk=id)
    #     form = CandidateForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    # return HTTPResponse('<h1>{{current_user}}</h1>')

    import pdb
    pdb.set_trace()
    data_to_change = {'status': request.data.get("status")}
    # Partial update of the data
    user = request.user
    serializer = StatusSerializer(user, data=data_to_change, partial=True)
    if serializer.is_valid():
        (serializer.save())
    obj = serializer.data
    return render(request, template_name="index.html" ,context={'obj':obj})
