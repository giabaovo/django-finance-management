from rest_framework import serializers

from .models import Account


class MutationAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('id', 'name', 'plaid_id', 'user',)
        extra_kwargs = {
            'user': {'required': False},
        }

    def to_representation(self, instance):
        account = super().to_representation(instance)

        account['plaidId'] = account.pop('plaid_id')
        account['userId'] = account.pop('user')

        return account


class GetAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('id', 'name',)
