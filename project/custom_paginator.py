from rest_framework.pagination import PageNumberPagination

class CustomPageNumberPagination(PageNumberPagination):
    page_size = 3  # Set the number of items per page
    page_size_query_param = 'page_size'
    max_page_size = 100  # Optional: Set a maximum page size
