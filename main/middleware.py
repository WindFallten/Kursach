from sentry_sdk import configure_scope

class SentryMiddleware():
    def init(self, get_response):
        self.get_response = get_response

    def call(self, request):
        with configure_scope() as scope:
            scope.user = {"id": request.user.id}
        response = self.get_response(request)
        return response