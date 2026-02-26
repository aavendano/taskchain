from typing import TypeVar, Union, Awaitable

from taskchain.core.context import ExecutionContext
from taskchain.core.executable import Executable
from taskchain.core.outcome import Outcome
from taskchain.runtime.runner import AsyncRunner, SyncRunner

T = TypeVar("T")

def execute_workflow(
    workflow: Executable[T],
    data: T,
    async_mode: bool = False,
) -> Union[Outcome[T], Awaitable[Outcome[T]]]:
    """
    Executes a workflow, hiding the creation of context and runner.

    Args:
        workflow: The workflow or task to execute.
        data: The input data object for the workflow.
        async_mode: If True, uses AsyncRunner; otherwise, uses SyncRunner.

    Returns:
        The outcome of the workflow execution.
    """
    ctx = ExecutionContext(data=data)
    if async_mode:
        runner = AsyncRunner()
        return runner.run(workflow, ctx)
    else:
        runner = SyncRunner()
        return runner.run(workflow, ctx)
