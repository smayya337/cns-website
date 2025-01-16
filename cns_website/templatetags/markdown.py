import mistune
from pygments import highlight
from pygments.formatters import html
from pygments.lexers import get_lexer_by_name

from django import template

register = template.Library()


class HighlightRenderer(mistune.HTMLRenderer):
    def block_code(self, code, info=None):
        if info:
            lexer = get_lexer_by_name(info, stripall=True)
            formatter = html.HtmlFormatter()
            return highlight(code, lexer, formatter)
        return "<pre><code>" + mistune.escape(code) + "</code></pre>"


@register.filter(name="markdown")
def convert_markdown(text: str):
    """Convert text to markdown HTML."""
    markdown = mistune.create_markdown(
        renderer=HighlightRenderer(),
        plugins=["footnotes", "strikethrough", "table"],
        escape=False,
    )
    return markdown(text)


@register.filter(name="remove_p_tags")
def remove_p_tags(text: str):
    text = text.strip()
    if text.startswith("<p>"):
        text = text[len("<p>") :]
    if text.endswith("</p>"):
        text = text[: -len("</p>")]
    return text
