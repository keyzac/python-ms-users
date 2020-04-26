from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()

    def create(self, validate_date):
        instance = User()

        instance.first_name = validate_date.get('first_name')
        instance.last_name = validate_date.get('last_name')
        instance.username = validate_date.get('username')
        instance.email = validate_date.get('email')
        instance.set_password(validate_date.get('password'))
        instance.save()

        return instance

    def validate_username(self, data):
        users = User.objects.filter(username=data)

        if len(users) != 0:
            raise serializers.ValidationError('El nombre de usuario ya se encuentra registrado')
        else:
            return data

    def update(self, instance, validated_data):
        pass
