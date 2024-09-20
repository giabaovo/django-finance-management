from rest_framework import serializers

from .models import Category


class MutationCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'plaid_id', 'user',)
        extra_kwargs = {
            'user': {'required': False},
        }

    def to_representation(self, instance):
        category = super().to_representation(instance)

        category['plaidId'] = category.pop('plaid_id')
        category['userId'] = category.pop('user')

        return category


class GetCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name',)
