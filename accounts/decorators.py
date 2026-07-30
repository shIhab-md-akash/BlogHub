from django.contrib.auth.decorators import user_passes_test


def expert_required(view_func):
    decorated_view = user_passes_test(
        lambda user: user.is_authenticated and (
            user.role == "EXPERT" or user.role == "ADMIN"
        )
    )(view_func)
    return decorated_view


def admin_required(view_func):
    decorated_view = user_passes_test(
        lambda user: user.is_authenticated and user.role == "ADMIN"
    )(view_func)
    return decorated_view