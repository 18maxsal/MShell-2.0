from app import Main
import pytest




def test_command_class():
    """
    Test Case: A normal initialization of the command class
    """
    command = Main.Command("echo hello world")
    assert command.command == "echo"
    assert command.args == ["hello", "world"]
    assert command.is_redirected == False
    assert command.is_redirected_error == False
    assert command.is_redirected_append == False
    assert command.is_redirected_append_error == False

def test_command_class2():
    """
    Test Case: Initializing with a blank string (Edge Case)
    """
    command = Main.Command("")
    assert command.command == ""
    assert command.args == []
    assert command.is_redirected == False
    assert command.is_redirected_error == False
    assert command.is_redirected_append == False
    assert command.is_redirected_append_error == False

def test_command_class3():
    """
    Test Case: Initializing with a single space (Edge Case)
    """
    command = Main.Command(" ")
    assert command.command == ""
    assert command.args == [""]
    assert command.is_redirected == False
    assert command.is_redirected_error == False
    assert command.is_redirected_append == False
    assert command.is_redirected_append_error == False
