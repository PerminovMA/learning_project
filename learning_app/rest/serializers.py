__author__ = 'PerminovMA@live.ru'

from django.contrib.auth.models import User, Group
from learning_app.models import Link
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    links_set = serializers.PrimaryKeyRelatedField(many=True, queryset=Link.objects.all())

    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups', 'links_set')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


# class LinkSerializer(serializers.Serializer):
#     pk = serializers.IntegerField(read_only=True)
#     original_link = serializers.CharField(required=True)
#     analytic_link = serializers.CharField()
#
#     def create(self, validated_data):
#         return Link.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.original_link = validated_data.get('original_link', instance.original_link)
#         instance.analytic_link = validated_data.get('analytic_link', instance.analytic_link)
#         instance.save()
#         return instance


class LinkSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Link
        fields = ('url', 'original_link', 'analytic_link', 'owner')