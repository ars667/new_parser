class Parser:
    def __init__(self, input_string):
        self.input = input_string
        self.pos = 0

    def current_char(self):
        if self.pos < len(self.input):
            return self.input[self.pos]
        return None  # Конец строки

    def read_char(self):
        if self.pos < len(self.input):
            ch = self.input[self.pos]
            self.pos += 1
            return ch
        return None  # Конец строки

    def symb(self):
        """Чтение символа из {a, b, c, ..., z}"""
        ch = self.current_char()
        if ch and ch.isalpha() and ch.islower():
            self.read_char()
            return True
        return False

    def sub_ending(self):
        """Обработка <выч окончание> ::= -<выражение>"""
        if self.current_char() == '-':
            self.read_char()
            return self.expression()
        return False

    def brack_start(self):
        """Обработка <начало скобочного выражения> ::= <буква>|<скобочное выражение>"""
        if self.symb():
            return True
        return self.brack_expr()

    def brack_expr(self):
        """Обработка <скобочное выражение> ::= (<начало скобочного выражения><выч окончание>)"""
        if self.current_char() == '(':
            self.read_char()
            if self.brack_start() and self.sub_ending() and self.current_char() == ')':
                self.read_char()
                return True
        return False

    def ending(self):
        """Обработка <окончание> ::= +<выражение>|-<выражение>|Λ"""
        ch = self.current_char()
        if ch == '+' or ch == '-':
            self.read_char()
            return self.expression()
        # Λ (пустой символ) всегда возвращает True
        return True

    def expression(self):
        """Обработка <выражение> ::= <буква><окончание>|<скобочное выражение><окончание>"""
        if self.symb() or self.brack_expr():
            return self.ending()
        return False

    def parse(self):
        """Начало парсинга"""
        if self.expression() and self.pos == len(self.input):
            return True
        return False


# Пример использования
def process(input_string):
    parser = Parser(input_string)
    if parser.parse():
        print(f"Выражение '{input_string}' соответствует грамматике.")
    else:
        print(f"Выражение '{input_string}' не соответствует грамматике.")




print('Эта программа проверяет выражения на соответствие описанной далее грамматике. Чтобы выйти нажмите q')
print('Алгебраические формулы со скобками и знаками операций + и -. \nПри этом сумма операндов никогда не берется в скобки, а разность может браться, а может нет\nПример: a+b-(c-(d-f))')
print('\nДалее будет выведено 5 примеров и 5 контрпримеров. Нажмите ENTER\n')
input()
process("a")
process("a-b")
process("a-b-c-d-e")
process('(a-(b-(c-d)))')
process(('a+b-c'))

process("+")
process("+a+b-c-")
process("((a-b)")
process("((a-b))(")
process("a+-b")

while True:
    print('Теперь попробуйте свой пример')
    a = input()
    if a == 'q':
        exit(0)
    else:
        process(a)
