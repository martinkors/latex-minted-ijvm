import re

from pygments.lexer import RegexLexer, include, bygroups, default, using, \
    this, words, combined
from pygments.token import Text, Comment, Operator, Keyword, Name, String, \
    Number, Punctuation, Other
from pygments.util import get_bool_opt
import pygments.unistring as uni

__all__ = ['IJVMLexer']

class IJVMLexer(RegexLexer):
  name = 'IJVM'
  aliases = ['ijvm']
  filenames = ['*.j']
  flags = re.IGNORECASE | re.MULTILINE

  decn = r'[0-9]+'
  operators = r'(?:=|\+|\-)'
  identifier = r'[a-z$._?][\w$.?#@~]*'
  directives = (r'(?:\.method|\.args|\.locals|\.define)\s+')
  keywords = (r'(?:bipush|dup|goto|iadd|iand|ifeq|iflt|if_icmpeq|iinc|iload|invokevirtual|ior|ireturn|istore|isub|ldc_w|nop|pop|swap)\s+')

  tokens = {
    'root': [
      include('whitespace'),
      (directives, Keyword, 'expr'),
      (keywords, Keyword, 'expr'),
      (identifier + ':', Name.Label),
      (r'[\r\n]+', Text)
    ],
    'whitespace': [
      (r'\n', Text),
      (r'[ \t]+', Text),
      (r'\/\/.*', Comment.Single)
    ],
    'expr': [
      (decn, Number.Integer),
      (operators, Operator),
      (r'(?:\,|\(|\))', Punctuation),
      (identifier, Name.Variable),
      (r'[\r\n]+', Text, '#pop'),
      include('whitespace')
    ]
  }

from pygments import highlight
from pygments.formatters import HtmlFormatter
print(highlight('.define 1\n.define a = 2', IJVMLexer(), HtmlFormatter()))