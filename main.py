from textual.app import *
from textual.widgets import *
from textual.containers import *

class MainContainer(Static):

    def compose(self) -> ComposeResult:
        with Horizontal():
            with Collapsible(title="File Browser"):
                with TabbedContent():
                    with TabPane("System Drive"):
                        yield DirectoryTree("C:/")
                    with TabPane("Wyvern Subdrive"):
                        yield Label("never got around to this 🤷‍♂️")
            yield Rule(orientation="vertical")
            with Collapsible(title="Editor"):
                yield ScrollableContainer(EditorContainer())

class EditorContainer(Static):

    def compose(self) -> ComposeResult:
        yield Label("i never finished this so uhhh")
        with Horizontal():
            yield Button(label="here take a button i guess")
class MainApp(App):

    def compose(self) -> ComposeResult:
        yield Header()
        yield ScrollableContainer(MainContainer())
        yield Footer()

if __name__ == "__main__":
    MainApp().run()