def get_avatar(backend, strategy, details, response, user=None, *args, **kargs):

    url = None
    if backend.name == 'facebook':
        url = "http://graph.facebook.com/%s/picture?type=small"%response['id']
    if backend.name == 'twitter':
        url = response.get('profile_image_url', '').replace('_normal','')
    if url:
        user.avatar = url
        user.save()
