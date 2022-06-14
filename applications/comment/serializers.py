from   rest_framework import serializers

from applications.product.models import Product
from .models import Comment

class CommentSerializer(serializers.ModelSerializer):
    author = serializers.CharField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(), write_only=True)

    class Meta:
        model = Comment
        fields = "__all__"




