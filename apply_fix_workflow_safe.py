import sys

filepath = "src/taskchain/components/workflow.py"

with open(filepath, "r") as f:
    content = f.read()

# We need to match the previous optimized version I just applied
search = """    def __init__(self, name: str, steps: List[Executable[T]], strategy: FailureStrategy = FailureStrategy.ABORT):
        self.name = name
        self.steps = steps
        self.strategy = strategy
        self._is_async = any(step.is_async for step in self.steps)"""

replace = """    def __init__(self, name: str, steps: List[Executable[T]], strategy: FailureStrategy = FailureStrategy.ABORT):
        self.name = name
        self.steps = list(steps)
        self.strategy = strategy
        self._is_async = any(step.is_async for step in self.steps)"""

if search in content:
    new_content = content.replace(search, replace)
    with open(filepath, "w") as f:
        f.write(new_content)
    print("Successfully patched workflow.py with safe list conversion")
else:
    # Maybe I need to revert first? Or check what is currently there.
    print("Could not find search block in workflow.py")
    # Let's print the relevant part to debug
    start_idx = content.find("def __init__")
    if start_idx != -1:
        print("Current content around __init__:")
        print(content[start_idx:start_idx+300])
    sys.exit(1)
