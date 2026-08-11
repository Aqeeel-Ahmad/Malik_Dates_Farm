from .models import SiteSetting

def site_settings_processor(request):
    settings_obj = SiteSetting.objects.first()
    if not settings_obj:
        settings_obj = SiteSetting.objects.create()
    return {
        'site_settings': settings_obj
    }
