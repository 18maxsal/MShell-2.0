from prompt_toolkit import PromptSession
from prompt_toolkit.history import InMemoryHistory

def main():
    # print("Hello")
    memory = InMemoryHistory()
    session = PromptSession(
        history=memory
    )


    while True:
        command = session.prompt("$ ")


if __name__ == "__main__":
    main()