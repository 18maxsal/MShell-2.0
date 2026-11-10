from prompt_toolkit import PromptSession
from prompt_toolkit.history import InMemoryHistory

class Command:

    def __init__(self, command: str, is_redirected: bool = False, is_redirected_error: bool = False, 
                 is_redirected_append: bool = False, is_redirected_append_error: bool = False):
        command = command.split(" ")
        self.command = command[0]
        self.args = command[1:]
        self.is_redirected = is_redirected
        self.is_redirected_error = is_redirected_error
        self.is_redirected_append = is_redirected_append
        self.is_redirected_append_error = is_redirected_append_error
    # def __init__(self, command: str, is_redirected: bool = False, is_redirected_error: bool = False, 
    #              is_redirected_append: bool = False, is_redirected_append_error: bool = False):
    #     self.command = command
    #     self.is_redirected = is_redirected
    #     self.is_redirected_error = is_redirected_error
    #     self.is_redirected_append = is_redirected_append
    #     self.is_redirected_append_error = is_redirected_append_error

        self.sub_commands = [] # Only used when the command contains a pipeline symbol

    def string_parser(self) -> list[str]:
        pass

    def find_redirects(self):
        pass

    def pipeline_parser(self):
        pass


BUILT_INS = ["exit", "echo", "type"]

def echo_helper(command: Command) -> str | None:
    return " ".join(command.args).strip()

def type_helper(command: Command) -> str | None:
    if command.args[0] in BUILT_INS:
        return f"{command.command} is a shell builtin"
    else:
        return f"{command.command}: not found"

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
        if command.command == "echo":
            result = echo_helper(command)
            print(result)
        elif command.command == "type":
            result = type_helper(command)
            print(result)
        # if command.command == "exit":
        else:
            break
        # print(type(command.command))
        # print(f"command: {command.command}, args: {command.args}")
        print(f"{command.args[0]}: command not found")
        # print(f"Given command: {command.command}")
        # break


if __name__ == "__main__":
    main()