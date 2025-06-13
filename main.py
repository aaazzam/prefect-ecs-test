from prefect import flow


@flow
def hello_world():
    print("Hello from prefect-ecs-test!")


if __name__ == "__main__":
    flow.from_source(
        source="https://github.com/aaazzam/prefect-ecs-test.git",
        entrypoint="main.py:hello_world",
    ).deploy(
        name="hello-world",
        work_pool_name="noice",
    )
