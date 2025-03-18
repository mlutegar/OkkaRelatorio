"""
class RelatorioSerializer(serializers.ModelSerializer):
    class Meta:
        model = TokenIC
        fields = '__all__'
        extra_kwargs = {
            'quantidade_ic': {'required': True},
            'expiracao': {'read_only': True}
        }

    def create(self, validated_data):
        validated_data['expiracao'] = now() + timedelta(seconds=110)
        return super().create(validated_data)
"""