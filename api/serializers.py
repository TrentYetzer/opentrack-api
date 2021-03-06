from rest_framework import serializers
from api.models import Profile, Track, Material, TrackRating, MaterialRating, TrackFavorite, MaterialFavorite
from users.serializers import UserSerializer


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('user_id', 'image_relative_path', 'location', 'website',
                  'work', 'education', 'skills')


class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = ('material_id', 'title', 'description', 'views',
                  'website', 'track', 'display_order', 'author')


class TrackSerializer(serializers.ModelSerializer):
    materials = MaterialSerializer(many=True, read_only=True)

    class Meta:
        model = Track
        fields = ('track_id', 'title', 'description',
                  'views', 'author', 'materials')


class GetTrackSerializer(serializers.ModelSerializer):
    materials = MaterialSerializer(many=True, read_only=True)
    author = UserSerializer(many=False, read_only=True)

    class Meta:
        model = Track
        fields = ('track_id', 'title', 'description',
                  'views', 'author', 'materials', 'rating')


class TrackRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrackRating
        fields = ('track_rating_id', 'rating', 'user_fk', 'track_fk')


class MaterialRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaterialRating
        fields = ('material_rating_id', 'rating', 'user_fk', 'material_fk')


class TrackFavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrackFavorite
        fields = ('track_favorite_id', 'user_fk', 'track_fk')


class MaterialFavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaterialFavorite
        fields = ('material_favorite_id', 'user_fk', 'material_fk')
