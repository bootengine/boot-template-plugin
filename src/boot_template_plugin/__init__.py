import extism
from jinja2 import Template


@extism.plugin_fn
def applyTemplate():
    templateString = extism.input_json()

    values = templateString["values"]

    rtemplate = Template(templateString["template"])

    extism.output_str(rtemplate.render(values))
