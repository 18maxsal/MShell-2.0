from prompt_toolkit import PromptSession
from prompt_toolkit.history import InMemoryHistory

class Command:

    def __init__(self, command: str, is_redirected: bool = False, is_redirected_error: bool = False, 
                 is_redirected_append: bool = False, is_redirected_append_error: bool = False):
        self.command = command
        self.is_redirected = is_redirected
        self.is_redirected_error = is_redirected_error
        self.is_redirected_append = is_redirected_append
        self.is_redirected_append_error = is_redirected_append_error

        self.sub_commands = [] # Only used when the command contains a pipeline symbol

    def string_parser(self) -> list[str]:
        pass

    def find_redirects(self):
        pass

    def pipeline_parser(self):
        pass


BUILT_INS = ["exit"]


def main():
    # print("Hello")
    memory = InMemoryHistory()
    session = PromptSession(
        history=memory
    )


    # The main Read-Eval-Print-Loop (i.e. REPL)
    while True:
        # command = session.prompt("$ ")
        command = Command(session.prompt("$ "))
        print(f"{command.command}: command not found")
        # print(f"Given command: {command.command}")
        break


if __name__ == "__main__":
    main()