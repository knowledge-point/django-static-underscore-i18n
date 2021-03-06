from django.http import HttpRequest
from django.template import loader
from django import http
from django.utils.html import escapejs
from django.utils.translation import activate


def js_templates(language, templates, context):
    compiled_js = "var underscore_vars={};"
    activate(language)
    request = HttpRequest()
    request.LANGUAGE_CODE = language
    context.update({
        'LANGUAGE_CODE': language
    })
    for (name, template) in templates.items():
        template = loader.get_template(template_name=template)
        text = template.render(context)
        compiled_js += "underscore_vars['%s'] = '%s';\r\n" % (name, escapejs(text))
    return http.HttpResponse(compiled_js, 'text/javascript')
