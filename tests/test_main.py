from app.Main import main
import pytest

# TODO: Update this test as it will now fail when running pytest
def test_main(capsys):
    main()
    captured_output = capsys.readouterr()

    assert captured_output.out == "Hello\n"