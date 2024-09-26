class Token:

    pass

class BytecodeStream:

    pass

class Scanner:
    def __init__(self, input_stream):
        self._input_stream = input_stream

    def scan(self):

        return Token()

class ProgramNode:
    def get_source_position(self):

        pass

    def add(self, node):

        pass

    def remove(self, node):

        pass

    def traverse(self, code_generator):

        code_generator.visit(self)

class StatementNode(ProgramNode):
    def traverse(self, code_generator):

        code_generator.visit_statement_node(self)

class ExpressionNode(ProgramNode):
    def traverse(self, code_generator):

        code_generator.visit_expression_node(self)

class ProgramNodeBuilder:
    def __init__(self):
        self._node = ProgramNode()

    def new_variable(self, variable_name):

        pass

    def new_assignment(self, variable, expression):

        pass

    def new_return_statement(self, value):

        pass

    def new_condition(self, condition, true_part, false_part):

        pass

    def get_root_node(self):
        return self._node

class Parser:
    def parse(self, scanner, builder):

        pass

class CodeGenerator:
    def __init__(self, output):
        self._output = output

    def visit_statement_node(self, node):

        pass

    def visit_expression_node(self, node):

        pass

class Compiler:
    def compile(self, input_stream, output_stream):
        scanner = Scanner(input_stream)
        builder = ProgramNodeBuilder()
        parser = Parser()
        parser.parse(scanner, builder)
        generator = CodeGenerator(output_stream)
        parse_tree = builder.get_root_node()
        parse_tree.traverse(generator)