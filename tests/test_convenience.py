import pytest
from dataclasses import dataclass

from taskchain import execute_workflow, task, Workflow
from taskchain.core.context import ExecutionContext

@dataclass
class MyData:
    value: int

@task()
def add_one(ctx: ExecutionContext[MyData]):
    ctx.data.value += 1

@task()
async def add_one_async(ctx: ExecutionContext[MyData]):
    ctx.data.value += 1

def test_execute_workflow_sync():
    workflow = Workflow("sync_workflow", [add_one])
    data = MyData(value=1)

    outcome = execute_workflow(workflow, data)

    assert outcome.status == "SUCCESS"
    assert outcome.context.data.value == 2

@pytest.mark.asyncio
async def test_execute_workflow_async():
    workflow = Workflow("async_workflow", [add_one_async])
    data = MyData(value=1)

    outcome = await execute_workflow(workflow, data, async_mode=True)

    assert outcome.status == "SUCCESS"
    assert outcome.context.data.value == 2

def test_execute_workflow_sync_with_task():
    # Test passing a task directly instead of a workflow
    data = MyData(value=10)
    outcome = execute_workflow(add_one, data)

    assert outcome.status == "SUCCESS"
    assert outcome.context.data.value == 11

@pytest.mark.asyncio
async def test_execute_workflow_async_with_task():
    # Test passing an async task directly
    data = MyData(value=10)
    outcome = await execute_workflow(add_one_async, data, async_mode=True)

    assert outcome.status == "SUCCESS"
    assert outcome.context.data.value == 11
