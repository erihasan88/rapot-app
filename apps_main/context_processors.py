from .models import SchoolProfile

def school_profile(request):
    school = SchoolProfile.objects.first()
    return {
        'school_profile': school
    }
