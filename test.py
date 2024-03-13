import unittest
from lex import *


class TestCompiler(unittest.TestCase):

    def test_numbers(self):
        source = "+-123 9.8654*/"
        lexer = Lexer(source)

        token = lexer.getToken()
        output = ""
        while token.kind != TokenType.EOF:
            # print(token.kind)
            output += str(token.kind)
            token = lexer.getToken()

        self.assertEqual(
            "TokenType.PLUSTokenType.MINUSTokenType.NUMBERTokenType.NUMBERTokenType.ASTERISKTokenType.SLASHTokenType.NEWLINE", output)

    def test_keyword(self):
        source = "IF+-123 foo*THEN/"
        lexer = Lexer(source)
        token = lexer.getToken()
        output = ""

        while token.kind != TokenType.EOF:
            # print(token.kind)
            output += str(token.kind)
            token = lexer.getToken()

        self.assertEqual(
            """TokenType.IFTokenType.PLUSTokenType.MINUSTokenType.NUMBERTokenType.IDENTTokenType.ASTERISKTokenType.THENTokenType.SLASHTokenType.NEWLINE""", output)


if __name__ == '__main__':
    unittest.main()
