from rest_framework.serializers import ModelSerializer
from .models import Category,Course

class CategorySerialisers(ModelSerializer):
    class Meta:
        models = Category
        fielsd = ('name','description')
        