from django.conf import settings
from django.template.loaders import app_directories
from django.template import Template

class ExtensionLoader(app_directories.Loader):
    is_usable = True

    def load_template(self, template_name, template_dirs=None):
        """Template loader that loads templates with the _extended suffix or
            reviewboard/ prefix"""

        template_dirs = getattr(settings, "TEMPLATE_DIRS", [])

        # if the path starts with reviewboard/ then this is an extended template
        # that is including a default template, so load the default
        # otherwise try to load an extended version first
        if template_name.startswith("reviewboard/"):
            template_name = template_name.replace("reviewboard/", "")
        else:
            template_name = template_name.replace(".html", "_extended.html")

        source, origin = self.load_template_source(template_name, template_dirs)
        template = Template(source)
        return template, origin
