import pytest
from io import StringIO

from user_input import open_option_prompter, bound_finder, filter_prompter


def test_filter_prompter_complete(monkeypatch, capfd):
    """Test the limits and extremes of filter_prompter()
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
    with pytest.raises(SystemExit) as error:
        test_string = '3'
        simulated_input = StringIO(test_string)
        monkeypatch.setattr('sys.stdin', simulated_input)
        filter_prompter()
    assert error.type is SystemExit

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


def test_bound_finder_complete(monkeypatch, capfd):
    """Test the limits and extremes of bound_finder()
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

    """Test the bound_finder function in user_input. Input: '0'
    """
    selected_bound = "UPPER"
    mass_or_year = 4
    test_string = '0'
    simulated_input = StringIO(test_string)
    monkeypatch.setattr('sys.stdin', simulated_input)
    bound_finder_output = bound_finder(selected_bound, mass_or_year)
    assert bound_finder_output == '0'
    out, err = capfd.readouterr()
    assert out == ("Enter the " + selected_bound + " limit (inclusive) for the meteor's " +
                   'MASS (g)' + " ('Q' to QUIT):\t")

    """Test the bound_finder function in user_input. Input: 'alskdfjasldk'
    """
    with pytest.raises(TypeError) as error:
        selected_bound = "UPPER"
        mass_or_year = 4
        test_string = 'alskdfjasldk'
        simulated_input = StringIO(test_string)
        monkeypatch.setattr('sys.stdin', simulated_input)
        bound_finder(selected_bound, mass_or_year)
    assert error.type is TypeError

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

    """Test the filter_prompter function in user_input. Input: None
        """
    with pytest.raises(EOFError) as error:
        selected_bound = "UPPER"
        mass_or_year = 4
        test_string = None
        simulated_input = StringIO(test_string)
        monkeypatch.setattr('sys.stdin', simulated_input)
        bound_finder(selected_bound, mass_or_year)
    assert error.type is EOFError

    """Test the filter_prompter function in user_input. Input: Q
        """
    with pytest.raises(SystemExit) as error:
        selected_bound = "UPPER"
        mass_or_year = 4
        test_string = 'Q'
        simulated_input = StringIO(test_string)
        monkeypatch.setattr('sys.stdin', simulated_input)
        bound_finder(selected_bound, mass_or_year)
    assert error.type is SystemExit

    """Test the filter_prompter function in user_input. Input: q
            """
    with pytest.raises(TypeError) as error:
        selected_bound = "UPPER"
        mass_or_year = 4
        test_string = 'q'
        simulated_input = StringIO(test_string)
        monkeypatch.setattr('sys.stdin', simulated_input)
        bound_finder(selected_bound, mass_or_year)
    assert error.type is TypeError


def test_open_option_prompter_complete(monkeypatch, capfd):
    """Test 'r'"""
    test_string = 'r'
    simulated_input = StringIO(test_string)
    monkeypatch.setattr('sys.stdin', simulated_input)
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
                   '\x1b[92mFile mode: r\x1b[0m\n'
                   '\n')

    """Test 'w'"""
    test_string = 'w'
    simulated_input = StringIO(test_string)
    monkeypatch.setattr('sys.stdin', simulated_input)
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
                   '\x1b[92mFile mode: w\x1b[0m\n'
                   '\n')

    """Test 'x'"""
    test_string = 'x'
    simulated_input = StringIO(test_string)
    monkeypatch.setattr('sys.stdin', simulated_input)
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
                   '\x1b[92mFile mode: x\x1b[0m\n'
                   '\n')

    """Test 'a'"""
    test_string = 'a'
    simulated_input = StringIO(test_string)
    monkeypatch.setattr('sys.stdin', simulated_input)
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
                   '\x1b[92mFile mode: a\x1b[0m\n'
                   '\n')

    with pytest.raises(ValueError) as error:
        test_string = 'aoiusdfa;sdjnkf'
        simulated_input = StringIO(test_string)
        monkeypatch.setattr('sys.stdin', simulated_input)
        open_option_prompter()
    assert error.type is ValueError

    with pytest.raises(EOFError) as error:
        test_string = None
        simulated_input = StringIO(test_string)
        monkeypatch.setattr('sys.stdin', simulated_input)
        open_option_prompter()
    assert error.type is EOFError
