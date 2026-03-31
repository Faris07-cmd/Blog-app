def profile_processor(request):
    try:
        return {"profile": request.user.profile}
    except AttributeError:
        return {}
