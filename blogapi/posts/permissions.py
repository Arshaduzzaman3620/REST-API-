from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
  """ only authors can edit or delete therir posts"""
  def has_object_permission(self, request, view, obj):
    """ Read permissions are allowed for any request (GET, HEAD, OPTIONS)."""
    if request.method in permissions.SAFE_METHODS:
      return True

    """ Write permissions are only allowed to the author of the post."""
    return obj.author == request.user
  