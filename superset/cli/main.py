import importlib
import logging
import pkgutil
from typing import Any

import click
from colorama import Fore, Style
from flask.cli import with_appcontext, FlaskGroup

from superset import app, cli
from superset.extensions import appbuilder, security_manager
from superset.cli.lib import normalize_token


@click.group(
    cls=FlaskGroup,
    context_settings={"token_normalize_func": normalize_token},
)
@with_appcontext
def superset() -> None:

    @app.shell_context_processor
    def make_shell_context() -> dict[str, Any]:
        return {"app": app}


for load, module_name, is_pkg in pkgutil.walk_packages(cli.__path__, cli.__name__ + "."):
    module = importlib.import_module(module_name)
    for attribute in module.__dict__.values():
        if isinstance(attribute, (click.core.Command, click.core.Group)):
            superset.add_command(attribute)

            if isinstance(attribute, click.core.Group):
                break


@superset.command()
@with_appcontext
def init() -> None:
    """Inits the Superset application"""
    appbuilder.add_permissions(update_perms=True)
    security_manager.sync_role_definitions()

#
# @superset.command()
# @with_appcontext
# @click.option("--verbose", "-v", is_flag=True, help="Show extra information")
# def version(verbose: bool) -> None:
#     """Prints the current version number"""
#     print(Fore.BLUE + "-=" * 15)
#     print(Fore.YELLOW + "Superset " + Fore.CYAN + f"{app.config['VERSION_STRING']}")
#     print(Fore.BLUE + "-=" * 15)
#



