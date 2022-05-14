from typing import List

import click

from command_runner import CommandRunner
from errors import FinishExecutionException


# TODO: mypy is broken in this file, no time to fix all typing issues

def print_command_output(lines: List[str]):
    for line in lines:
        click.echo(click.style(f"\t{line}", fg="blue"))

# Assumes a CLI approach, but reading the inputs as files could also be considered
# The CLI is easier to test one command at a time
# But some other form of "batch processing" (like reading from a file) would probably be more realistic

@click.command()
def runner() -> None:
    click.echo(
        click.style(
            (
                "Welcome, please introduce one or more of these commands:\n\n"
                "DEPEND item1 item2 [item3]\n"
                "\tPackage item1 depends on package item2 (and item3 or any additional packages).\n\n"
                "INSTALL item1\n"
                "\tInstalls item1 and any other packages required by item1\n\n"
                "REMOVE item1\n"
                "\tRemoves item1 and, if possible, packages required by item1.\n\n"
                "LIST\n"
                "\tLists the names of all currently installed packages.\n\n"
                "END\n"
                "\tMarks the end of input, when used in a line by itself."
            ),
            fg="magenta",
        )
    )
    runner = CommandRunner()
    while True:
        try:
            input: str = click.prompt(
                text="", prompt_suffix=click.style("> ", fg="green")
            )
            print_command_output(runner.run_command(input))
        except FinishExecutionException:
            break
        except Exception as e:
            print(e)


if __name__ == "__main__":
    runner()
