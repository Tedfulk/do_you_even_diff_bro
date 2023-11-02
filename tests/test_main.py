import pytest
from py_do_you_even_diff_bro.main import get_bro_mode, display_diff_summary, main
from py_do_you_even_diff_bro.models import BroMode

def test_get_bro_mode():
    assert get_bro_mode(True, False, False) == BroMode.CHILL
    assert get_bro_mode(False, True, False) == BroMode.MID
    assert get_bro_mode(False, False, True) == BroMode.CHAD
    assert get_bro_mode(False, False, False) == BroMode.CHILL

def test_display_diff_summary(mocker):
    mocker.patch('py_do_you_even_diff_bro.main.console')
    display_diff_summary("Test summary")
    py_do_you_even_diff_bro.main.console.print.assert_called_once()

@pytest.mark.parametrize("chill, mid, chad, model, only, ignore, prompt, summarize, peer_review", [
    (True, False, False, 'gpt-4', ['.py'], [], '', False, ''),
    (False, True, False, 'gpt-3.5-turbo', ['.py'], ['.txt'], 'Test prompt', True, 'main')
])
def test_main(chill, mid, chad, model, only, ignore, prompt, summarize, peer_review, mocker):
    mocker.patch('py_do_you_even_diff_bro.main.get_git_diff', return_value="Test diff")
    mocker.patch('py_do_you_even_diff_bro.main.gpt_prompt', return_value="Test response")
    main(chill, mid, chad, model, only, ignore, prompt, summarize, peer_review)
    py_do_you_even_diff_bro.main.get_git_diff.assert_called_once_with(only, ignore, peer_review)
    py_do_you_even_diff_bro.main.gpt_prompt.assert_called()
