from main import *
from meteor_data_class import *
from user_input import *
import pytest
from io import StringIO
from user_input import quit_program_gracefully, bound_finder, filter_prompter


"""
    
    PLEASE IGNORE THESE UNIT TESTS, THEY WILL ALMOST DEFINITELY BE DELETED AND REWRITTEN AS THEY ARE NOT
    MY OWN CODE. SOME OF THEM ARE BUT I THOUGHT IT WAS WORTH NOTING ANYWAYS.

"""

def test_quit_program_gracefully(capfd, monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 'q')
    with pytest.raises(SystemExit) as excinfo:
        quit_program_gracefully()
    captured = capfd.readouterr()
    assert str(excinfo.value) == 'None'
    assert 'The program is now exiting... GOODBYE' in captured.out


def test_bound_finder(capfd, monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 'q')
    with pytest.raises(SystemExit) as excinfo:
        bound_finder("upper", 4)
    assert str(excinfo.value) == 'None'


def test_filter_prompter(monkeypatch, capfd):
    # Simulate user input for option 1 (MASS)
    monkeypatch.setattr('builtins.input', lambda _: '1')

    # Call filter_prompter and check the output
    result = filter_prompter()

    # Capture the printed output
    captured = capfd.readouterr()

    # Check the function result and printed output
    assert result == 4
    assert 'Invalid option' not in captured.out


def test_filter_prompter_quit(monkeypatch, capfd):
    # Simulate user input for option 3 (QUIT)
    test_string = '3'
    simulated_input = StringIO(test_string)
    monkeypatch.setattr('sys.stdin', simulated_input)

    # Use pytest.raises to check if quit_program_gracefully() is called
    with pytest.raises(SystemExit):
        filter_prompter()

    out, err = capfd.readouterr()
    assert out == ('What attribute would you like to filter the data on?\n'
                   '1. meteor MASS (g)\n'
                   '2. The YEAR the meteor fell to Earth\n'
                   '3. QUIT\n'
                   '>>\t\n'
                   'The program is now exiting... GOODBYE\n')


def test_r_option(monkeypatch, capfd):
    test_string = 'r'
    simulated_input = StringIO(test_string)
    monkeypatch.setattr('sys.stdin', simulated_input)

    # Capture stdout when calling open_option_prompter
    with capfd.disabled():
        open_option_prompter()
    # Check the printed output
    out, err = capfd.readouterr()
    assert out == ''


def test_open_option_prompter_quit(monkeypatch, capfd):
    # Simulate user input for ">q"
    test_string = '>q'
    simulated_input = StringIO(test_string)
    monkeypatch.setattr('sys.stdin', simulated_input)

    # Use pytest.raises to check if quit_program_gracefully() is called
    with pytest.raises(SystemExit):
        open_option_prompter()
    out, err = capfd.readouterr()

    assert out == ('What mode would you like to open the file with?\n'
                   '"r" - open for reading (default)\n'
                   '"w" - open for writing, truncating the file first (WARNING: This will '
                   'delete\n'
                   'the contents of an existing file!)\n'
                   '"x" - open for exclusive creation, failing if the file already exists\n'
                   '"a" - open for writing, appending to the end of file if it exists\n'
                   'Enter ">q" or ">Q" to quit\n'
                   'Mode >> \n'
                   'The program is now exiting... GOODBYE\n')

    def file_prompter_test(monkeypatch, capfd):
        # The 'enter_first_name()' function makes a call to the Python built-in 'input' function.
        # The 'input' function is a "blocking" function that waits for user input in the terminal.
        # To test 'enter_first_name()', user input must be SIMULATED; a human user should not
        # become part of the test by manually inputting text at the command line:
        test_string = '>Q'
        # wrap the test string in a StringIO object
        simulated_input = StringIO(test_string)
        # use a test fixture called 'monkeypatch' to "mock" user input - (the monkeypatch fixture must
        # be passed to this test to be used inside the test function body).
        # We do this with the 'setattr()' method contained in the monkeypatch class.
        # The 'setattr()' function assists with "replacing" the input that would normally be returned from the
        # 'sys.stdin' FileIO stream object with the StringIO object 'Joe'. We must do this because
        # a human user is not manually typing input in the terminal in this test function. Therefore,
        # we will "pretend" that the StringIO object we declared as 'simulated_input' is the 'sys.stdin'
        # fileIO stream. Now, the call to the 'input' function in 'enter_first_name()' will look at the
        # 'simulated_input' StringIO object for user input instead of the 'sys.stdin' FileIO as it normally would.
        monkeypatch.setattr('sys.stdin', simulated_input)
        assert file_prompter() == '>Q'
        # Now, we confirm that output to the terminal should be what we expect from 'enter_first_name()'.
        # Use the 'capfd' fixture to "capture" output to the terminal. The 'capfd' fixture must be
        # passed as a parameter to this test to be used inside the test's function body.
        # Terminal output is stored in the 'out' variable:
        out, err = capfd.readouterr()
        # Confirm that the "Enter your first name: " prompt is indeed printed to the terminal according
        # to 'enter_first_name()'s function body:
        assert out == 'The program is now exiting... GOODBYE'

        # Test some invalid input. The 'enter_first_name()' function does not accept strings with
        # characters outside the "alpha" set (A-Z, a-z). "Joe9" is invalid because it contains a number.
        test_string = 'Joe9'
        simulated_input = StringIO(test_string)
        monkeypatch.setattr('sys.stdin', simulated_input)
        assert enter_first_name() is None
        out, err = capfd.readouterr()
        # Confirm that 'enter_first_name()'s error message is indeed printed to the terminal as expected.
        # The prompt "Enter your first name: " is also printed to the terminal during 'enter_first_name()'s
        # execution, so we must account for the prompt output in the captured terminal output.
        assert out == f'Enter your first name: The name \'{test_string}\' is not valid.\n'

        # This test case examines the behavior of 'enter_first_name()' when the user does not type
        # anything, but simply presses <ENTER>. A newline character simulates the user pressing the
        # <ENTER> key. An empty string will be read as the user input.
        test_string = '\n'
        simulated_input = StringIO(test_string)
        monkeypatch.setattr('sys.stdin', simulated_input)
        assert enter_first_name() is None
        out, err = capfd.readouterr()
        assert out == f'Enter your first name: The name \'\' is not valid.\n'

        # If an empty string StringIO object is mocked as the 'sys.stdin' fileIO object, an "end of file"
        # (EOFError) exception is thrown. This is because when the input function tries to read the mocked
        # 'sys.stdin' fileIO object, it approximates an empty file with no content. Use the 'pytest.raises()' function to
        # confirm this behavior.
        # (It is important to note that it's impossible for the 'sys.stdin' fileIO stream to be
        # empty after a call to the 'input' function. The 'input' function is a "blocking" function that waits for a user to
        # type something and press <ENTER>. The minimum a user could do is just press <ENTER> without typing any characters
        # first. Therefore, at minimum, the user sends a newline character ('\n') to 'sys.stdin'. Therefore, the following
        # test case is just for illustrative purposes, as it does not simulate a realistic behavior.)
        with pytest.raises(EOFError) as error:
            test_string = ''
            simulated_input = StringIO(test_string)
            monkeypatch.setattr('sys.stdin', simulated_input)
            enter_first_name()
        assert error.type is EOFError
