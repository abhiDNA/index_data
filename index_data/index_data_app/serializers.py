from rest_framework import serializers
from .models import Nifty50, NiftyMidcap150, NiftyMidcap50, NiftyNext50, NiftySmallcap50


class Nifty50Serializer(serializers.ModelSerializer):
    class Meta:
        model = Nifty50
        fields = "__all__"


class NiftyMidcap150Serializer(serializers.ModelSerializer):
    class Meta:
        model = NiftyMidcap150
        fields = "__all__"


class NiftyMidcap50Serializer(serializers.ModelSerializer):
    class Meta:
        model = NiftyMidcap50
        fields = "__all__"


class NiftyNext50Serializer(serializers.ModelSerializer):
    class Meta:
        model = NiftyNext50
        fields = "__all__"


class NiftySmallcap50Serializer(serializers.ModelSerializer):
    class Meta:
        model = NiftySmallcap50
        fields = "__all__"


