import re

from pygments.lexer import RegexLexer, include
from pygments.token import Text, Comment, Operator, Keyword, Name, Number, Punctuation

__all__ = ['IJVMLexer']

class IJVMLexer(RegexLexer):
  name = 'IJVM'
  aliases = ['ijvm']
  filenames = ['*.j']
  flags = re.IGNORECASE | re.MULTILINE

  decn = r'(?:0x[0-9a-fA-F]+|[0-9]+)'
  operators = r'(?:=|\+|\-)'
  identifier = r'[a-z$._?][\w$.?#@~]*'
  directives = (r'(?:\.method|\.args|\.locals|\.define)\s+')
  ukeywords = (r'(?:dup|iadd|iand|ior|ireturn|isub|nop|pop|swap)')
  keywords = (r'(?:bipush|goto|ifeq|iflt|if_icmpeq|iinc|iload|invokevirtual|istore|ldc_w)\s+')

  tokens = {
    'root': [
      include('whitespace'),
      (directives, Keyword, 'expr'),
      (ukeywords, Keyword, 'expr'),
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