import os

import click


@click.group()
def cli():
    pass


@cli.command()
@click.argument("ms_name")
def create(ms_name):
    """Creates a new FastAPI microservice with default structure."""
    click.echo(f"Creating new FastAPI ms: {ms_name}")

    dir = [ms_name, os.path.join(ms_name, "app"), os.path.join(ms_name, "tests")]

    for d in dir:
        os.makedirs(d, exist_ok=True)
        click.echo(f"Creating directory: {d}")

    main_content = """
    from fastapi import FastAPI

    app = FastAPI()

    @app.get("/")
    async def root():
        return {"message": "Hello, World!"}
    """

    with open(os.path.join(ms_name, "app", "main.py"), "w") as f:
        f.write(main_content)
        click.echo(f"Creating file: {os.path.join(ms_name, "app", "main.py")}")

    click.echo("FastAPI microservice created successfully!")
