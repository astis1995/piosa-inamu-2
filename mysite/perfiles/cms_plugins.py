from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from . import models
from django.utils.translation import ugettext as _


@plugin_pool.register_plugin  # register the plugin
class PerfilesPluginPublisher(CMSPluginBase):
    model = models.PerfilesPluginModel  # model where plugin data are saved
    module = _("Perfiles")
    name = _("Perfiles Plugin")  # name of the plugin in the interface
    render_template = "temp_pic/index.html"

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context
