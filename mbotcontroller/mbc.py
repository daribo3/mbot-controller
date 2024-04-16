import asyncio
import pprint

import click
from evdev import InputDevice, list_devices, categorize

from mbotcontroller.logging import setup_logging


@click.group()
@click.option("--debug", is_flag=True, help="Enable debug logging")
@click.pass_context
def cli(ctx, debug):
    if debug:
        setup_logging(log_level="debug")


@cli.command()
def show_devices():
    devices = [InputDevice(path) for path in list_devices()]
    for device in devices:
        click.echo(f"{device.path} {device.name} {device.phys}")

    async def read_events(device):
        async for event in device.async_read_loop():
            click.echo(categorize(event))

    dev = InputDevice("/dev/input/event5")
    pp = pprint.PrettyPrinter(depth=4)
    pp.pprint(dev.capabilities(verbose=True, absinfo=True))
    asyncio.run(read_events(dev))


@cli.command()
def run():
    click.echo("Running...")


if __name__ == "__main__":
    # pylint: disable=no-value-for-parameter
    cli()
