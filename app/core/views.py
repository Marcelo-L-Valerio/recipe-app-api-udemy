'''
Core views for app
'''
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def health_check(request):
    '''Returns sucessful response'''
    return Response({'healthy': True})

@api_view(['GET'])
def home_page(request):
    '''Returns an spceific phrase'''
    return Response({'pipoquinha, princesa da putaria': 'https://www.youtube.com/watch?v=zAmHQk-OW3k'})