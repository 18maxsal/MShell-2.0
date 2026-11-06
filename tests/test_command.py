from app import Main
import pytest




def test_command():
    command = Main.Command("echo hello world")
    assert command.command == "echo"
    assert command.args == ["hello", "world"]