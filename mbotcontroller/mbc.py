import click

from mbotcontroller.logging import setup_logging

@click.group()
@click.option("--debug", is_flag=True, help="Enable debug logging")
@click.pass_context
def cli(ctx, debug):
    if debug:
        setup_logging(log_level='debug')

@cli.command()
def run():
    click.echo("Running...")

if __name__ == '__main__':
    cli()