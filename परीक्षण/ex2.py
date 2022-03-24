from parsimonious.nodes import NodeVisitor
from parsimonious.grammar import Grammar
from itertools import groupby

grammar = Grammar(
    r"""
    term            = course (operator course)*
    course          = coursename? ws coursenumber
    coursename      = ~"[A-Z]+"
    coursenumber    = ~"\d+"
    operator        = ws (and / or / comma) ws
    and             = "and"
    or              = (comma ws)? "or"
    comma           = ","
    ws              = ~"\s*"
    """
)

class CourseVisitor(NodeVisitor):
    def __init__(self):
        self.current = None
        self.courses = []
        self.listnum = 1

    def generic_visit(self, node, children):
        pass

    def visit_coursename(self, node, children):
        if node.text:
            self.current = node.text

    def visit_coursenumber(self, node, children):
        course = (self.current, int(node.text), self.listnum)
        self.courses.append(course)

    def visit_or(self, node, children):
        self.listnum += 1

courses = ["CS 2110", "CS 2110 and INFO 3300",
           "CS 2110, INFO 3300", "CS 2110, 3300, 3140",
           "CS 2110 or INFO 3300", "MATH 2210, 2230, 2310, or 2940"]

for course in courses:
    tree = grammar.parse(course)
    cv = CourseVisitor()
    cv.visit(tree)
    courses = [list(v) for _, v in groupby(cv.courses, lambda x: x[2])]
    print(courses)