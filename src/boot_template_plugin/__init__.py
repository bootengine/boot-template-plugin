import extism
from jinja2 import Environment, BaseLoader


@extism.plugin_fn
def applyTemplate():
    templateString = extism.input_str()
    values = extism.Config.get_json("values")
    rtemplate = Environment(loader=BaseLoader).from_string(templateString)

    extism.log(extism.LogLevel.Info, values)
    extism.output_str(rtemplate.render(values))
