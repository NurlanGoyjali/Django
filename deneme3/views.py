from django.http import HttpResponseRedirect
from django.shortcuts import render


def my_custom_page_not_found_view(request, exception):
    return HttpResponseRedirect('/404h')


def custom_error_view(request, exception=None):
    return HttpResponseRedirect('/404h')


def custom_permission_denied_view(request, exception=None):
    return HttpResponseRedirect('/404h')


def custom_bad_request_view(request, exception=None):
    return HttpResponseRedirect('/404h')
