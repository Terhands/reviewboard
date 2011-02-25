from django.conf import settings
from django.template import TemplateDoesNotExist

def load_template_source(template_name, template_dirs=None):
    """Template loader that loads templates from a ZIP file."""

    template_files = getattr(settings, "TEMPLATE_DIRS", [])

    # looking for extended templates
    for file_name in template_files:
        if file_name == "extended_" + template_name:
            # found an extended template so return it
            template_path = "%s:%s" % (file_name, template_name)
            return (source, template_path)

    # failed to find an extended template so this loader will
    # fail and the default loader will load the default template
    raise TemplateDoesNotExist(template_name)

# setting this loader to usable (always want to try the extensions
# before the default templates)
load_template_source.is_usable = True

