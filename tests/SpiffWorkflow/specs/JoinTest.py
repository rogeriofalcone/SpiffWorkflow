import os
import sys
import unittest
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..'))

from TaskSpecTest import TaskSpecTest
from SpiffWorkflow.specs import Join
from SpiffWorkflow import Workflow


class JoinTest(TaskSpecTest):
    CORRELATE = Join

    def create_instance(self):
        if 'testtask' in self.wf_spec.task_specs:
            del self.wf_spec.task_specs['testtask']

        return Join(self.wf_spec,
                       'testtask',
                       description='foo')

def suite():
    tests = unittest.TestLoader().loadTestsFromTestCase(JoinTest)
    return tests
if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(suite())