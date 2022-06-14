from rest_framework import generics

from .models import Comment
from .serializers import CommentSerializer
from .permissions import IsCommentAuthor
from rest_framework import generics


class CreateCommentView(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsCommentAuthor]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class RetrieveEditDestroyCommentView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsCommentAuthor]

    def perform_update(self, serializer):
        serializer.save(author=self.request.user)