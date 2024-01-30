from textual.app import *
from textual.widgets import *
from textual.widgets.option_list import *
from textual.containers import *
import sys

class EnvironmentMain(Static):
    """PLACEHOLDER"""

    def compose(self) -> ComposeResult:
        yield OptionList(
           Option("Applications", disabled=True),
           Option("Dock"),
           Option("File System"),
           Separator(),
           Option("System", disabled=True),
           Option("Settings"),
           Option("Terminal"),
           Separator()
        )


class EnvironmentApp(App):
    """PLACEHOLDER"""

    # Define UI functions
    def compose(self) -> ComposeResult:
        """PLACEHOLDER"""
        yield Header()
        yield Footer()
        yield ScrollableContainer(EnvironmentMain())

    # Define mounting function
    def on_mount(self) -> None:
        self.title = "Wyvern Environment"

    # Define event functions

    # Define keybind functions

