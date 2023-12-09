from main import *
from meteor_data_class import *
import pytest
from io import StringIO
# from testfixtures import TempDirectory

from user_input import open_option_prompter, bound_finder, filter_prompter, file_presence_tester


def test_filter_prompter_complete(monkeypatch, capfd):
    """Test the filter_prompter function in user_input. Input: 1
    """
    test_string = "1"
    simulated_input = StringIO(test_string)
    monkeypatch.setattr('sys.stdin', simulated_input)
    assert filter_prompter() == 4
    out, err = capfd.readouterr()
    assert out == ('What attribute would you like to filter the data on?\n'
                   '1. meteor MASS (g)\n'
                   '2. The YEAR the meteor fell to Earth\n'
                   '3. QUIT\n'
                   '>>\t')

    """Test the filter_prompter function in user_input. Input: 2
    """
    test_string = "2"
    simulated_input = StringIO(test_string)
    monkeypatch.setattr('sys.stdin', simulated_input)
    assert filter_prompter() == 6
    out, err = capfd.readouterr()
    assert out == ('What attribute would you like to filter the data on?\n'
                   '1. meteor MASS (g)\n'
                   '2. The YEAR the meteor fell to Earth\n'
                   '3. QUIT\n'
                   '>>\t')

    """Test the filter_prompter function in user_input. Input: 3
    """
    test_string = "3"
    simulated_input = StringIO(test_string)
    monkeypatch.setattr('sys.stdin', simulated_input)
    out, err = capfd.readouterr()
    assert out == ''
    # Need to find a way to assert that quit_program_gracefully() works

    """Test the filter_prompter function in user_input. Input: 4
    """
    with pytest.raises(ValueError) as error:
        test_string = "4"
        simulated_input = StringIO(test_string)
        monkeypatch.setattr('sys.stdin', simulated_input)
        filter_prompter()
    assert error.type is ValueError

    """Test the filter_prompter function in user_input. Input: 0
    """
    with pytest.raises(ValueError) as error:
        test_string = "0"
        simulated_input = StringIO(test_string)
        monkeypatch.setattr('sys.stdin', simulated_input)
        filter_prompter()
    assert error.type is ValueError

    """Test the filter_prompter function in user_input. Input: None
    """
    with pytest.raises(EOFError) as error:
        test_string = None
        simulated_input = StringIO(test_string)
        monkeypatch.setattr('sys.stdin', simulated_input)
        filter_prompter()
    assert error.type is EOFError

    """Test the filter_prompter function in user_input. Input: aosdkjf;oasijer[oaiwjefc'lksadjf[oiwua4f]p9aiwj
    """
    with pytest.raises(ValueError) as error:
        test_string = "aosdkjf;oasijer[oaiwjefc'lksadjf[oiwua4f]p9aiwj"
        simulated_input = StringIO(test_string)
        monkeypatch.setattr('sys.stdin', simulated_input)
        filter_prompter()
    assert error.type is ValueError

    """Test the filter_prompter function in user_input. Input: '' (empty string)
    """
    with pytest.raises(EOFError) as error:
        test_string = ''
        simulated_input = StringIO(test_string)
        monkeypatch.setattr('sys.stdin', simulated_input)
        filter_prompter()
    assert error.type is EOFError


# bound_finder(a, b) tests
def test_bound_finder_10000(monkeypatch, capfd):
    """Test the bound_finder function in user_input. Input: '10000'
    """
    selected_bound = "UPPER"
    mass_or_year = 4
    test_string = '10000'
    simulated_input = StringIO(test_string)
    monkeypatch.setattr('sys.stdin', simulated_input)
    bound_finder_output = bound_finder(selected_bound, mass_or_year)
    assert bound_finder_output == '10000'
    out, err = capfd.readouterr()
    assert out == ("Enter the " + selected_bound + " limit (inclusive) for the meteor's " +
                   'MASS (g)' + " ('Q' to QUIT):\t")


def test_bound_finder_stupid_big_number(monkeypatch, capfd):
    """Test the bound_finder function in user_input. Input: '9999999999999999999999999999999999999999999999999'
    """
    selected_bound = "UPPER"
    mass_or_year = 4
    test_string = '9999999999999999999999999999999999999999999999999'
    simulated_input = StringIO(test_string)
    monkeypatch.setattr('sys.stdin', simulated_input)
    bound_finder_output = bound_finder(selected_bound, mass_or_year)
    assert bound_finder_output == '9999999999999999999999999999999999999999999999999'
    out, err = capfd.readouterr()
    assert out == ("Enter the " + selected_bound + " limit (inclusive) for the meteor's " +
                   'MASS (g)' + " ('Q' to QUIT):\t")


def test_bound_finder_garbage(monkeypatch, capfd):
    """Test the bound_finder function in user_input. Input: 'alskdfjasldk'
    """
    selected_bound = "UPPER"
    mass_or_year = 4
    with pytest.raises(TypeError) as error:
        test_string = 'alskdfjasldk'
        simulated_input = StringIO(test_string)
        monkeypatch.setattr('sys.stdin', simulated_input)
        bound_finder(selected_bound, mass_or_year)
    assert error.type is TypeError


def test_bound_finder_empty(monkeypatch, capfd):
    """Test the bound_finder function in user_input. Input: ''
    """
    selected_bound = "UPPER"
    mass_or_year = 4
    with pytest.raises(EOFError) as error:
        test_string = ''
        simulated_input = StringIO(test_string)
        monkeypatch.setattr('sys.stdin', simulated_input)
        bound_finder(selected_bound, mass_or_year)
    assert error.type is EOFError


def test_bound_finder_quit():
    pass
    # STILL NEED TO FIND SOME WAY TO TEST THAT IT QUITS


def test_open_option_prompter_1(monkeypatch, capfd):
    """Test the filter_prompter function in user_input"""
    test_string = "1"
    simulated_input = StringIO(test_string)
    monkeypatch.setattr('sys.stdin', simulated_input)
    assert filter_prompter() == 4
    out, err = capfd.readouterr()
    assert out == ('What attribute would you like to filter the data on?\n'
                   '1. meteor MASS (g)\n'
                   '2. The YEAR the meteor fell to Earth\n'
                   '3. QUIT\n'
                   '>>\t')


def test_open_option_prompter_2(monkeypatch, capfd):
    """Test the filter_prompter function in user_input"""
    test_string = "2"
    simulated_input = StringIO(test_string)
    monkeypatch.setattr('sys.stdin', simulated_input)
    assert filter_prompter() == 4
    out, err = capfd.readouterr()
    assert out == ('What attribute would you like to filter the data on?\n'
                   '1. meteor MASS (g)\n'
                   '2. The YEAR the meteor fell to Earth\n'
                   '3. QUIT\n'
                   '>>\t')


def test_open_option_prompter_3(monkeypatch, capfd):
    """Test the filter_prompter function in user_input"""
    test_string = "3"
    simulated_input = StringIO(test_string)
    monkeypatch.setattr('sys.stdin', simulated_input)
    assert filter_prompter() == 4
    out, err = capfd.readouterr()
    assert out == ('What attribute would you like to filter the data on?\n'
                   '1. meteor MASS (g)\n'
                   '2. The YEAR the meteor fell to Earth\n'
                   '3. QUIT\n'
                   '>>\t')

