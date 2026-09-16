from .models import SiteSetting

def site_settings_processor(request):
    try:
        settings_obj = SiteSetting.objects.first()
        if not settings_obj:
            settings_obj = SiteSetting()
    except Exception:
        settings_obj = SiteSetting()

    return {
        'site_settings': settings_obj
    }
