from rest_framework import serializers
from projects.models import Project, Tag, Review
from users.models import Profile


class ReviewSerializer(serializers.ModelSerializer):
    """
    profile serializer
    """
    class Meta:
        """
        meta
        """
        model = Review
        fields = '__all__'


class ProfileSerializer(serializers.ModelSerializer):
    """
    profile serializer
    """
    class Meta:
        """
        meta
        """
        model = Profile
        fields = '__all__'


class TagSerializer(serializers.ModelSerializer):
    """
    profile serializer
    """
    class Meta:
        """
        meta
        """
        model = Tag
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):
    """
    Project serializer
    """
    owner = ProfileSerializer(many=False)
    tags = TagSerializer(many=True)
    reviews = serializers.SerializerMethodField()

    class Meta:
        """
        meta
        """
        model = Project
        fields = '__all__'

    def get_reviews(self, obj):
        """
        get reviews
        """
        reviews = obj.review_set.all()
        serializer = ReviewSerializer(reviews, many=True)
        return serializer.data
