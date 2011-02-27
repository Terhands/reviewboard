from django.conf import settings
from django.template.loaders import app_directories
from django.template import Template

class ExtensionLoader(app_directories.Loader):
    is_usable = True

    def load_template(self, template_name, template_dirs=None):
        """Template loader that loads templates with the _extended suffix"""

        template_dirs = getattr(settings, "TEMPLATE_DIRS", [])

#        import pdb; pdb.set_trace()
        template_name = template_name.replace(".html", "_extended.html")

        source, origin = self.load_template_source(template_name, template_dirs)
        template = Template(source)
        return template, origin


class DefaultLoader(app_directories.Loader):
    is_usable = True

    def load_template(self, template_name, template_dirs=None):
        """Template loader that loads templates with the _extended suffix"""

        template_dirs = getattr(settings, "TEMPLATE_DIRS", [])

#        import pdb; pdb.set_trace()
        template_name = template_name.replace("_default", "");

        source, origin = self.load_template_source(template_name, template_dirs)
        template = Template(source)
        return template, origin
