from .models import UserProfile


def profile_context(request):
    profile = UserProfile.objects.first()
    return {'profile': profile} if profile else {}
