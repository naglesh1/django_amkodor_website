from myamkodor.models import Viewer

def get_client_ip(request):
    """
    Get client ip address from HTTP request

    :param request: HTTP request
    :return: IP Address
    """
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    return x_forwarded_for.split(',')[-1].strip() if x_forwarded_for else request.META.get('REMOTE_ADDR')

class CountViewerMixin:

    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        if hasattr(self.object, 'viewers'):
            viewer, created = Viewer.objects.get_or_create(
                ipaddress=None if request.user.is_authenticated else get_client_ip(request),
                user=request.user if request.user.is_authenticated else None
            )

            if self.object.viewers.filter(id=viewer.id).count() == 0:
                self.object.viewers.add(viewer)

        return response