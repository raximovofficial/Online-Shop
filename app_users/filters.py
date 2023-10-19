from rest_framework.filters import BaseFilterBackend
import coreapi


class UsersFilterBackend(BaseFilterBackend):
    def get_schema_fields(self, view):
        fields = [
            coreapi.Field(
                name='name',
                location='query',
                required=False,
                type='string',
                description='Filter user by last_name or first_name',
            )
        ]
        return fields

    def filter_queryset(self, request, queryset, view):
        name = request.query_params.get('name', None)
        if name:
            queryset = queryset.filter(first_name__icontains=name) | queryset.filter(last_name__icontains=name)
        return queryset