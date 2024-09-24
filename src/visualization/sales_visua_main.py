import mesop as me
from modules.sales_predict_plot import predict_plot

@me.page(
  security_policy=me.SecurityPolicy(
    allowed_iframe_parents=["https://google.github.io", "https://huggingface.co"]
  ),
  path="/",
)

def main():
  fig = predict_plot()
  with me.box(style=me.Style(gap=12, width="100%")):
    me.plot(fig, style=me.Style(width="100%"))

