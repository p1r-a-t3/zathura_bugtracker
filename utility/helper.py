from user.models import CustomUser
from organization.models import Organization
from projects.models import Projects
from token_manager.models import ProjectToken
from datetime import datetime, timedelta
from zathura_bugtracker import settings


def get_user_object(email=None, username=None):
    try:
        if email is not None:
            return CustomUser.objects.get(email=email)
        elif username is not None:
            return CustomUser.objects.get(username=username)
    except CustomUser.DoesNotExist:
        # Token Invalid
        return None


def get_org_object(org_id):
    try:
        return Organization.objects.get(org_id=org_id)
    except Organization.DoesNotExist:
        return None


def get_project_object(project_id):
    try:
        return Projects.objects.get(project_id=project_id)
    except Projects.DoesNotExist:
        return None


def get_project_token_by_project_id(project):
    try:
        return ProjectToken.objects.get(project=project)
    except ProjectToken.DoesNotExist:
        return None


def get_project_token_object(project_token):
    try:
        return ProjectToken.objects.get(token=project_token)
    except ProjectToken.DoesNotExist:
        return None

# cookie setter


def set_cookie(response, key, value, days_expire=10, expired_at: datetime = None):
    if expired_at is None:
        max_age = days_expire * 24 * 60 * 60  # either 10 days or user input
        expires = datetime.strftime(datetime.utcnow() +
                                    timedelta(seconds=max_age),
                                    "%a, %d-%b-%Y %H:%M:%S GMT")
    else:
        max_age = days_expire * 24 * 60 * 60
        expires = datetime.strftime(expired_at,
                                    "%a, %d-%b-%Y %H:%M:%S GMT")
    response.set_cookie(key, value, max_age=max_age, expires=expires)
