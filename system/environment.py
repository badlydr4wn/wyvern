from textual.app import *
from textual.widgets import *
from textual.widgets.option_list import *
from textual.containers import *
import sys

class MainContainer(Static):
    """PLACEHOLDER"""

    def compose(self) -> ComposeResult:
        with Horizontal():
            with Collapsible(title="File Browser"):
              yield DirectoryTree("C:/")
            yield Rule(orientation="vertical", line_style="solid")
            with Collapsible(title="Edit File"):
                yield Label("coming soon 👀")

    
        

class FileSystemApp(App):
    """PLACEHOLDER"""

    # Define UI functions
    def compose(self) -> ComposeResult:
        """PLACEHOLDER"""
        yield Header()
        yield Container(MainContainer())
        yield Footer()

    # Define mounting function
    def on_mount(self) -> None:
        self.title = "Wyvern"

    # Define event functions
        
    # Define keybind functions
