# from app.Main import main
# from app.Main import Command
from app import Main
import pytest

# from prompt_toolkit.application import create_app_session
# from prompt_toolkit.input import create_pipe_input
# from prompt_toolkit.output import DummyOutput
# from prompt_toolkit.shortcuts import PromptSession


# @pytest.fixture(autouse=True, scope="function")
# def mock_input():
#     with create_pipe_input() as pipe_input:
#         with create_app_session(input=pipe_input, output=DummyOutput()):
#             yield pipe_input


# @pytest.fixture(autouse=True, scope="function")
# def _pt_app_session():
#     with create_app_session():
#         yield




# TODO: Update this test as it will now fail when running pytest
def test_main(mock_input, capsys):
    # mock_input.send_text("Hello\nexit\n")
    mock_input.send_text("Hello\n")
    mock_input.send_text("exit\n")

    # _pt_app_session()
    Main.main()
    captured_output = capsys.readouterr()

    assert captured_output.out == "Hello: command not found\n"

def test_echo_helper():
    command = Main.Command("echo hello world")
    result = Main.echo_helper(command)
    assert result == "hello world"

# ORIGINAL TEST
# # TODO: Update this test as it will now fail when running pytest
# def test_main(capsys):
#     main()
#     captured_output = capsys.readouterr()

#     assert captured_output.out == "Hello\n"