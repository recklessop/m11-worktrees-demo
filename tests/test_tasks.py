import unittest
from tasks import Task, TaskList

class TaskListTests(unittest.TestCase):
    def test_add_appends(self):
        tl = TaskList()
        tl.add("write M14 post")
        self.assertEqual(len(tl.tasks), 1)

    def test_complete_marks_done(self):
        tl = TaskList([Task("x")])
        tl.complete(0)
        self.assertTrue(tl.tasks[0].done)

if __name__ == "__main__":
    unittest.main()
