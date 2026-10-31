from app.Main import main
import pytest


def test_main(capsys):
    main()
    captured_output = capsys.readouterr()

    assert captured_output.out == "Hello\n"