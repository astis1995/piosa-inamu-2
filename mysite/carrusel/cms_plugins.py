from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
#from polls_cms_integration.models import PollPluginModel
from . import models
from django.utils.translation import ugettext as _


@plugin_pool.register_plugin  # register the plugin
class CarruselPluginPublisher(CMSPluginBase):
    model = models.CarruselPluginModel  # model where plugin data are saved
    module = _("Carrusel")
    name = _("Carrusel Plugin")  # name of the plugin in the interface
    render_template = "carrusel/carrusel.html"

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context
