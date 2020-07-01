from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool


@apphook_pool.register  # register the application
class NewsApphook(CMSApp):
    app_name = "News"
    name = "News Application"

    def get_urls(self, page=None, language=None, **kwargs):
        return ["News.urls"]
