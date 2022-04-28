from testapp.models import Exit
from rest_framework import serializers

class ExitSerializer(serializers.ModelSerializer):
    class Meta:
        model=Exit
        fields='__all__'