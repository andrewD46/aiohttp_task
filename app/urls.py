from app.views import UserListCreateView, UserRetrieveUpdateDestroyView, ItemListCreateView, \
    ItemRetrieveUpdateDestroyView


def add_urls(app):
    app.router.add_view('/users', UserListCreateView)
    app.router.add_view('/users/{id}', UserRetrieveUpdateDestroyView)
    app.router.add_view('/items', ItemListCreateView)
    app.router.add_view('/items/{id}', ItemRetrieveUpdateDestroyView)
