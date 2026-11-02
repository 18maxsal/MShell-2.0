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

    def string_parser(self):
        pass

    def find_redirects(self):
        pass

    def pipeline_parser(self):
        pass





def main():
    # print("Hello")
    memory = InMemoryHistory()
    session = PromptSession(
        history=memory
    )


    while True:
        command = session.prompt("$ ")
        print(f"Given command: {command}")
        break


if __name__ == "__main__":
    main()