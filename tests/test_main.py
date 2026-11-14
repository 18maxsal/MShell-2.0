# from app.Main import main
# from app.Main import Command
from app import Main
import pytest

def test_main(mock_input, capsys):
    """
    Test Case: Iterating through the main loop
    with an invalid command and then exiting
    """
    mock_input.send_text("Hello\n")
    mock_input.send_text("exit\n")

    # _pt_app_session()
    Main.main()
    captured_output = capsys.readouterr()

    assert captured_output.out == "Hello: command not found\n"

def test_echo_helper():
    """
    Test Case: Giving the shell a valid echo command
    and checking for valid input
    """
    command = Main.Command("echo hello world")
    result = Main.echo_helper(command)
    assert result == "hello world"

def test_echo_helper2():
    """
    Test Case: Testing the echo command with a single 
    space character.
    """
    command = Main.Command("echo ")
    result = Main.echo_helper(command)
    assert result == ""

def test_type_helper1():
    """
    Test Case: Testing type built-in command with a 
    valid built-in command. 
    """
    command = Main.Command("type echo")
    result = Main.type_helper(command)
    assert result == "echo is a shell builtin"

def test_type_helper2():
    """
    Test Case: Testing type built-in command with a 
    command that does not exist.
    """
    command = Main.Command("type someCommandHere")
    result = Main.type_helper(command)
    assert result == "someCommandHere: not found"

def test_type_helper3():
    """
    Test Case: Testing type built-in when searching for 
    an external command that is on PATH environment 
    variable.  

    NOTE: This test assumes that you have Python installed
    """
    command = Main.Command("type Python")
    result = Main.type_helper(command)
    assert result