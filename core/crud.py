from crud_views.lib.views import (
    CreateViewPermissionRequired,
    DeleteViewPermissionRequired,
    DetailViewPermissionRequired,
    ListViewPermissionRequired,
    ListViewTableFilterMixin,
    ListViewTableMixin,
    MessageMixin,
    UpdateViewPermissionRequired,
)


class CrudListView(
    ListViewTableMixin, ListViewTableFilterMixin, ListViewPermissionRequired
):
    paginate_by = 20
    cv_filter_persistence = False


class CrudDetailView(DetailViewPermissionRequired):
    cv_path = ""


class CrudCreateView(MessageMixin, CreateViewPermissionRequired):
    cv_path = "add"


class CrudUpdateView(MessageMixin, UpdateViewPermissionRequired):
    cv_path = "edit"


class CrudDeleteView(MessageMixin, DeleteViewPermissionRequired):
    pass
