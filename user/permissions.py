from rest_framework import permissions
import logging

logger = logging.getLogger(__name__)


class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        result = obj.id == request.user.id
        if not result:
            logger.info('ids are different')
        return result
