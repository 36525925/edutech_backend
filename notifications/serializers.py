from rest_framework import serializers

from notifications.models import Notifications


class NotificationsSerializers(serializers.ModelSerializer):

    class Meta:
        model = Notifications
        fields = "__all__"
