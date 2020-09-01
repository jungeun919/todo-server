from .models import Todo
from rest_framework import generics
from .serializers import TodoSerializer
from rest_framework.filters import SearchFilter

class TodoListGenerics(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    filter_backends = [SearchFilter] # 필터링을 하는 클래스들
    search_fields = ['todo'] # 검색할 모델의 필드 입력

    def get_queryset(self):
        qs = super().get_queryset()
        done = self.request.query_params.get('done')
        search = self.request.query_params.get('search')
        print(search)
        if done == None:
            return qs

        done = done.capitalize() # true => True false = False
        return qs.filter(done = done)

class TodoDetailGenerics(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    def get_queryset(self):
        pk = self.kwargs.get('pk') # kwargs라는 어트리뷰트를 통해 pk 혹은 
        print(pk)
        return super().get_queryset()