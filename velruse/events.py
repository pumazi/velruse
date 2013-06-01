# -*- coding: utf-8 -*-
"""Custom events for identity provider login."""
import functools
from pyramid.events import NewRequest

def with_events(before=None, after=None):
    """Decorator to create event book ends on a method."""
    def decorator(method):
        @functools.wraps(method)
        def new_method(obj, request):
            request.registry.notify(before(request))
            response = method(obj, request)
            request.registry.notify(after(request))
            return response
        return new_method
    return decorator


class BeforeLogin(NewRequest):
    """Used to tap into the request before
    the identity provider logic is run.
    """


class AfterLogin(NewRequest):
    """Used to tap into the request after
    the identity provider logic has run.
    """
