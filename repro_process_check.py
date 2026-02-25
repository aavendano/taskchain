from taskchain.components.process import Process
from taskchain.core.executable import Executable
from taskchain.core.context import ExecutionContext
from taskchain.core.outcome import Outcome

class MockTask(Executable):
    def __init__(self, is_async=False):
        self._is_async = is_async
    @property
    def is_async(self):
        print("MockTask.is_async called")
        return self._is_async
    def execute(self, ctx): pass
    def compensate(self, ctx): pass

steps = [MockTask(), MockTask()]
p = Process("test", steps)
print("Process created")
print(f"Process.is_async: {p.is_async}")
print(f"Process.is_async: {p.is_async}")
