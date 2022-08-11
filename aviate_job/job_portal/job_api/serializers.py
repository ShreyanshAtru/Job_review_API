from telnetlib import STATUS
from rest_framework import serializers
from .models import Candidate 

class CandidateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Candidate
        fields = '__all__'
    
    def get_status(self,obj):
        return obj.get_status_display()


class StatusSerializer(serializers.ModelSerializer):
   class Meta:
        model = Candidate
        fields = ('status',)

   def update(self, instance, validated_data): 
        instance.name = validated_data.get('status', instance.status)
        instance.save()
        return instance