# from app.Main import main
# from app.Main import Command
from app import Main
from pathlib import Path
import os
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

def test_run_external_command1(mock_input):
    command = Main.Command("Python")
    mock_input.send_text("exit()\n")
    result = Main.run_external_command(command)

    assert result == True

def test_run_external_command2():
    command = Main.Command("SomeCommandHere")
    result = Main.run_external_command(command)

    assert result == False


def test_pwd_helper1():
    """
    Test Case: Tests if a value (correct or not) is returned.
    """
    result = Main.pwd_helper()
    assert result

def test_pwd_helper2(tmp_path, monkeypatch):
    """
    Test Case: Tests current working directory path is correct 
    with expected input.
    """
    # path = tmp_path
    monkeypatch.chdir(tmp_path)
    result = Main.pwd_helper()
    assert result == tmp_path

def test_change_directory1(tmp_path, monkeypatch):
    """
    Test Case: Tests changing directories into an existing directory.
    """
    destination = tmp_path / "example"
    destination.mkdir()

    monkeypatch.chdir(tmp_path)
    command = Main.Command(f"cd {str(destination)}")
    Main.change_directory(command)

    assert Path.cwd() == destination.resolve()

def test_change_directory2(tmp_path, monkeypatch, capsys):
    """
    Test Case: Tests changing into a non-existent directory.
    """
    monkeypatch.chdir(tmp_path)
    oringinal_directory = Path.cwd()
    destination = str(tmp_path / "someDirectoryHere")
    command = Main.Command(f"cd {destination}")
    Main.change_directory(command)
    captured_output = capsys.readouterr()
    assert captured_output.out == f"cd: {os.path.realpath(destination)}: No such file or directory\n"
    assert Path.cwd() == oringinal_directory


def test_print_history1(capsys):
    """
    Test Case: Tests for correct output for when we print the full
    history.
    """
    memory = Main.InMemoryHistory()
    memory.append_string("echo Hello")
    memory.append_string("type echo")
    memory.append_string("history")
    Main.print_history(Main.Command("history"), memory)
    captured_output = capsys.readouterr()
    assert captured_output.out == "    1 echo Hello\n    2 type echo\n    3 history\n"

def test_print_history2(capsys):
    """
    Test Case: Tests for correct output for when the only command 
    is the history command.
    """
    memory = Main.InMemoryHistory()
    memory.append_string("history")
    Main.print_history(Main.Command("history"), memory)
    captured_output = capsys.readouterr()
    assert captured_output.out == "    1 history\n"

def test_print_history3(capsys):
    """
    Test Case: Tests for correct output for when we limit the 
    amount of entries the print_history function prints.
    """
    memory = Main.InMemoryHistory()
    memory.append_string("echo hello")
    memory.append_string("echo goodbye")
    memory.append_string("history 2")
    Main.print_history(Main.Command("history 2"), memory)
    captured_output = capsys.readouterr()
    assert captured_output.out == "    2 echo goodbye\n    3 history 2\n"

