from typing import List

from src.manager import DependenciesManager
from src.errors import FinishExecutionException, InvalidCommandException


class CommandRunner:
    def __init__(self, manager: DependenciesManager = None):
        # TODO: add an abstract interface for the manager
        self.manager = manager or DependenciesManager()

    def run_command(self, input: str) -> List[str]:
        if len(input) > 80:
            raise InvalidCommandException("Invalid command, please try again")

        command, *args = input.split()

        # TODO: This logic is quite redundant and not so clean, refactor later
        if command == "DEPEND":
            if len(args) < 2:
                raise InvalidCommandException("Invalid command, please try again")
            package, *dependencies = args
            return self.manager.add_dependencies(package, dependencies)
        elif command == "INSTALL":
            if len(args) != 1:
                raise InvalidCommandException("Invalid command, please try again")
            return self.manager.install_package(args[0])
        elif command == "REMOVE":
            if len(args) != 1:
                raise InvalidCommandException("Invalid command, please try again")
            return self.manager.remove_package(args[0])
        elif command == "LIST":
            if args:
                raise InvalidCommandException("Invalid command, please try again")
            return self.manager.list_packages()
        elif command == "END":
            if args:
                raise InvalidCommandException("Invalid command, please try again")
            raise FinishExecutionException
        else:
            raise InvalidCommandException("Invalid command, please try again")
