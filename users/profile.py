def profile_processor(request):
    return {"profile": request.user.profile}
