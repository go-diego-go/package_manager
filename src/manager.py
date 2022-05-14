from collections import defaultdict
from typing import List, Set, Dict


# TODO: This class is doing too much.
# Split responsibilities into multiple entities
class DependenciesManager:
    def __init__(self):
        self.dependencies: Dict[str, Set[str]] = defaultdict(set)
        self.dependents: Dict[str, Set[str]] = defaultdict(set)
        self.installed: Set[str] = set()

    def add_dependencies(self, package: str, dependencies: List[str]) -> List[str]:
        # assuming that we want to re-define the dependencies every time
        self.dependencies[package] = set(dependencies)

        for dependency in dependencies:
            self.dependencies[package].add(dependency)

        # we don't add any dependents yet, that happens while installing

        return []

    def install_package(self, package: str) -> List[str]:
        pending_to_process = [package]
        already_processed: Set[str] = set()
        result: List[str] = []

        while pending_to_process:
            current = pending_to_process.pop(0)
            if current in already_processed:
                continue

            # Don't log this for dependencies, only for main package
            if current in self.installed:
                if current == package:
                    result.append(f"{current} is already installed")
            else:
                result.append(f"{current} successfully installed")

            own_dependencies = self.dependencies[current]

            for dependency in own_dependencies:
                self.dependents[dependency].add(current)

            pending_to_process.extend(own_dependencies)

            self.installed.add(current)
            already_processed.add(current)

        return result

    def remove_package(self, package: str) -> List[str]:
        pending_to_process = [package]
        pending_to_process.extend(self.dependencies[package])
        already_processed: Set[str] = set()
        result: List[str] = []

        while pending_to_process:
            current = pending_to_process.pop(0)
            if current in already_processed:
                continue

            if current not in self.installed:
                if current == package:
                    result.append(f"{current} is not installed")
                    break

            if self.dependents[current]:
                if current == package:
                    result.append(f"{current} is still needed")
                continue

            own_dependencies = self.dependencies[current]

            # explicitly not removing dependencies for package, in case we reinstall it later
            for dependency in own_dependencies:
                self.dependents[dependency].remove(current)

            # we don't recursively remove unused dependencies
            # just the ones immediately related to the removed package
            # but we should consider it maybe?
            # no point in leaving unused dependencies
            # pending_to_process.extend(own_dependencies)

            self.installed.remove(current)
            already_processed.add(current)

            if current != package:
                result.append(f"{current} is no longer needed")
            result.append(f"{current} successfully removed")

        return result

    def list_packages(self) -> List[str]:
        return list(self.installed)
