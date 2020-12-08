from django.conf import settings
from django.db import models
from mptt.models import TreeManager

from rdmo.accounts.utils import is_site_manager
from rdmo.core.managers import CurrentSiteManagerMixin


class ProjectQuerySet(models.QuerySet):

    def filter_current_site(self):
        return self.filter(site=settings.SITE_ID)

    def filter_user(self, user):
        if user.is_authenticated:
            if user.has_perm('projects.view_project'):
                return self.all()
            elif is_site_manager(user):
                return self.filter_current_site()
            else:
                return self.filter(user=user)
        else:
            return self.none()


class MembershipQuerySet(models.QuerySet):

    def filter_current_site(self):
        return self.filter(project__site=settings.SITE_ID)


class IssueQuerySet(models.QuerySet):

    def filter_current_site(self):
        return self.filter(project__site=settings.SITE_ID)

    def active(self):
        return [issue for issue in self if issue.resolve()]


class IntegrationQuerySet(models.QuerySet):

    def filter_current_site(self):
        return self.filter(project__site=settings.SITE_ID)


class SnapshotQuerySet(models.QuerySet):

    def filter_current_site(self):
        return self.filter(project__site=settings.SITE_ID)


class ValueQuerySet(models.QuerySet):

    def filter_current_site(self):
        return self.filter(project__site=settings.SITE_ID)


class ProjectManager(CurrentSiteManagerMixin, TreeManager):

    def get_queryset(self):
        return ProjectQuerySet(self.model, using=self._db)

    def filter_user(self, user):
        return self.get_queryset().filter_user(user)


class MembershipManager(CurrentSiteManagerMixin, TreeManager):

    def get_queryset(self):
        return MembershipQuerySet(self.model, using=self._db)


class IssueManager(CurrentSiteManagerMixin, TreeManager):

    def get_queryset(self):
        return IssueQuerySet(self.model, using=self._db)

    def active(self):
        return self.get_queryset().active()


class IntegrationManager(CurrentSiteManagerMixin, TreeManager):

    def get_queryset(self):
        return IntegrationQuerySet(self.model, using=self._db)


class SnapshotManager(CurrentSiteManagerMixin, TreeManager):

    def get_queryset(self):
        return SnapshotQuerySet(self.model, using=self._db)


class ValueManager(CurrentSiteManagerMixin, TreeManager):

    def get_queryset(self):
        return ValueQuerySet(self.model, using=self._db)
