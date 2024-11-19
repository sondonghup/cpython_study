import ast
from pprint import pprint

# 파싱할 코드
code = "a + b - 3"

# 코드 -> AST 변환
parsed_ast = ast.parse(code, mode='eval')

# AST 출력
pprint(parsed_ast)
