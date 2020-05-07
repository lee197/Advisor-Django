from rest_framework import serializers
from core.models import MentoringTags, SeekingTags

class SeekingTagSerializer(serializers.ModelSerializer):
    """Serializer for seeker object"""

    class Meta:
        model = SeekingTags
        fields = ('id', 'name')
        read_only_Fields = ('id',)


class MentorTagSerializer(serializers.ModelSerializer):
    """Serializer for an mentor object"""

    class Meta:
        model = MentoringTags
        fields = ('id', 'name')
        read_only_fields = ('id',)

# class ProfileSerializer(serializers.ModelSerializer):
#     # filed in source= reflects to the database,
#     # field in left variable reflects to the json fields
#     # you have to be very careful about the name standards
#     gender_read = serializers.CharField(source='get_gender_display',
#                                         required=False,
#                                         read_only=True)
#     gender = serializers.CharField(write_only=True, required=False)
#     # read only
#     icon = serializers.SerializerMethodField(source='get_icon')
#     user_id = serializers.CharField(read_only=False,
#                                     required=True,
#                                     error_messages={"required": "please include user_id"})
#
#     # this def work with SerializerMethodField to add customized field
#     def get_icon(self, row):
#         return row.icon_url
#
#     class Meta:
#         model = Profile
#         fields = (
#             'user',
#             'user_id',
#             'icon',
#             'tags',
#             'gender_read',
#             'gender',
#             'personal_des',
#             'birthday',
#             'mentoring_fields',
#             'seeking_fields',
#             'isAvailable',
#         )
#         depth = 1
