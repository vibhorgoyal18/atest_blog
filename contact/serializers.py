from rest_framework import serializers


class ContactSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    subject = serializers.CharField(max_length=100, required=True)
    body = serializers.CharField(max_length=1000, required=True)

    class Meta:
        fields = '__all__'

