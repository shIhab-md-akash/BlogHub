from django.contrib.auth.mixins import UserPassesTestMixin


class ExpertRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return (
            self.request.user.is_authenticated
            and self.request.user.role in ["ADMIN", "EXPERT"]
        )


class AdminRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return (
            self.request.user.is_authenticated
            and self.request.user.role == "ADMIN"
        )