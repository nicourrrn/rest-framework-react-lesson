from logging import exception
from rest_framework import permissions
from rest_framework.request import Request

class IsOwnerOrOreadOnly(permissions.BasePermission):

    def has_object_permission(self, request: Request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        try:
            return obj.owner == request.user
        except AttributeError:
            return obj.project.owner == request.user
