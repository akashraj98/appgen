from rest_framework import serializers

from create_proj.models import (BackEndChoices,
                                DatabaseChoices,
                                FrontEndChoices,
                                Project,
                                )


class ProjectSerializer(serializers.ModelSerializer):
    """."""

    backend = serializers.ChoiceField(choices=BackEndChoices.choices)
    frontend = serializers.ChoiceField(choices=FrontEndChoices.choices)
    database = serializers.ChoiceField(choices=DatabaseChoices.choices)


    class Meta:
        """."""

        model = Project
        fields = [
            'backend',
            'frontend',
            'database',
        ]


class ProjectChoicesSerializer(serializers.Serializer):
    """."""

    backend = serializers.DictField(child=serializers.CharField())
    frontend = serializers.DictField(child=serializers.CharField())
    database = serializers.DictField(child=serializers.CharField())
