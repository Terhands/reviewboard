from django.conf import settings
from django.template import Template
from django.template.loaders import app_directories


class ExtensionLoader(app_directories.Loader):
    is_usable = True

    def load_template(self, template_name, template_dirs=None):
        """
        Template loader that loads extended templates.

        This loader searches for templates in the form original_extended.html.
        """

        template_dirs = getattr(settings, "TEMPLATE_DIRS", [])

        # If the path starts with reviewboard/ then this is an extended template
        # that is including a default template. In this case load the default
        # otherwise try to load an extended version first.
        if template_name.startswith("reviewboard/"):
            template_name = template_name.replace("reviewboard/", "")
        else:
            template_name = template_name.replace(".html", "_extended.html")

        source, origin = self.load_template_source(template_name, template_dirs)
        template = Template(source)
        return template, origin
