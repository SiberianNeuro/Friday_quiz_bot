from .admin import AdminFilter
from loader import dp

if __name__ == "filters":
    dp.filters_factory.bind(AdminFilter)