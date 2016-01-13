from schematics.models import Model
from schematics.types import URLType, StringType


class NewsItem(Model):
    url = URLType(required=True)
    title = StringType(required=True, max_length=1)
    user = StringType(required=True, max_length=50)
