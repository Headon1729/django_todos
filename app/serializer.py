from rest_framework import serializers
from app.models import Todo


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['title', 'description',
                  'completed', 'created_at', 'priority']
        # fields = '__all__'

    # title =
    # description =
    # completed =
    # created_by =
    # priority =
