from QPT cimport QuestionPaper

cdef class QPTGenerator:
    cdef QuestionPaper c_qpt

    def __cinit__(self, mark_of, question_no):
        marks = {}
        for i, j in mark_of.items():
            marks[i.encode()] = j
        self.c_qpt = QuestionPaper(marks, question_no)

    def generate(self):
        self.c_qpt.generate()
        c_output = self.c_qpt.allot_by_question_no
        output = {}
        for i in c_output:
            output[i.first.decode()] = i.second
        return output
