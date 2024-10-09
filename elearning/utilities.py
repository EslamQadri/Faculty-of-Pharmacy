from django.contrib.sessions.models import Session
from django.utils import timezone

"""
this code is for delete all sessions of user to force user to open the account in one device 
"""


def all_unexpired_sessions_for_user(user):
    user_sessions = []
    all_sessions = Session.objects.filter(expire_date__gte=timezone.now())
    for session in all_sessions:
        session_data = session.get_decoded()
        if str(user.pk) == session_data.get("_auth_user_id"):
            #print(f"i'm get all sessions for user {user}")

            user_sessions.append(session.pk)
    return Session.objects.filter(pk__in=user_sessions)


def delete_all_unexpired_sessions_for_user(user, session_to_omit=None):

    session_list = all_unexpired_sessions_for_user(user)
    if session_to_omit is not None:
        session_list.exclude(session_key=session_to_omit.session_key)
    session_list.delete()
