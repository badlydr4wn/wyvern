from textual.app import *
from textual.widgets import *
from textual.widgets.option_list import *
from textual.containers import *
import sys

class MainContainer(Static):
    """PLACEHOLDER"""

    def compose(self) -> ComposeResult:
        yield OptionList(
            Option("Applications", disabled=True),
            Option("Dock"),
            Option("Terminal"),
            Separator(),
            Option("System", disabled=True),
            Option("Settings"),
            Option("Directory"),
            Separator(),
        )

class EnvironmentApp(App):
    """PLACEHOLDER"""

    # Define UI functions
    def compose(self) -> ComposeResult:
        """PLACEHOLDER"""
        yield Header()
        yield ScrollableContainer(MainContainer())
        yield Footer()

    # Define mounting function
    def on_mount(self) -> None:
        self.title = "Wyvern"
        self.title = "Environment"

    # Define event functions
    def on_option_list_option_selected(self, event: OptionList.OptionSelected):
        self.notify(f"y{event.option_index}", title="option!!!")
        
    # Define keybind functions
