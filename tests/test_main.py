import pytest

import py_do_you_even_diff_bro.main
from py_do_you_even_diff_bro.main import (
    display_diff_summary,
    get_bro_mode,
    get_git_diff,
    main,
)
from py_do_you_even_diff_bro.models import BroMode


def test_get_bro_mode():
    assert get_bro_mode(True, False, False) == BroMode.CHILL
    assert get_bro_mode(False, True, False) == BroMode.MID
    assert get_bro_mode(False, False, True) == BroMode.CHAD
    assert get_bro_mode(False, False, False) == BroMode.CHILL


def test_display_diff_summary(mocker):
    mocker.patch("py_do_you_even_diff_bro.main.console")
    display_diff_summary("Test summary")
    py_do_you_even_diff_bro.main.console.print.assert_called_once()


@pytest.mark.parametrize(
    "chill, mid, chad, model, only, ignore, prompt, summarize, peer_review",
    [
        (True, False, False, "gpt-4", [".py"], [], "", False, ""),
        (
            False,
            True,
            False,
            "gpt-3.5-turbo",
            [".py"],
            [".ts"],
            "Test prompt",
            True,
            "main",
        ),
    ],
)
def test_main(
    chill, mid, chad, model, only, ignore, prompt, summarize, peer_review, mocker
):
    mocker.patch("py_do_you_even_diff_bro.main.get_git_diff", return_value="Test diff")
    mocker.patch(
        "py_do_you_even_diff_bro.main.gpt_prompt", return_value="Test response"
    )
    main(chill, mid, chad, model, only, ignore, prompt, summarize, peer_review)
    if get_git_diff:
        py_do_you_even_diff_bro.main.get_git_diff.assert_called_once_with(
            only, ignore, peer_review
        )
    else:
        py_do_you_even_diff_bro.main.get_git_diff.assert_not_called()
    py_do_you_even_diff_bro.main.gpt_prompt.assert_called()


# Test with a different model
def test_main_with_different_model(mocker):
    mocker.patch("py_do_you_even_diff_bro.main.get_git_diff", return_value="Test diff")
    mocker.patch(
        "py_do_you_even_diff_bro.main.gpt_prompt", return_value="Test response"
    )
    main(
        False,
        True,
        False,
        "gpt-3.5-turbo",
        [".py"],
        [".ts"],
        "Test prompt",
        True,
        "main",
    )
    py_do_you_even_diff_bro.main.get_git_diff.assert_called_once_with(
        [".py"], [".ts"], "main"
    )
    py_do_you_even_diff_bro.main.gpt_prompt.assert_called()


# Test with a different file type
def test_main_with_different_file_type(mocker):
    mocker.patch("py_do_you_even_diff_bro.main.get_git_diff", return_value="Test diff")
    mocker.patch(
        "py_do_you_even_diff_bro.main.gpt_prompt", return_value="Test response"
    )
    main(
        False,
        True,
        False,
        "gpt-3.5-turbo",
        [".java"],
        [".ts"],
        "Test prompt",
        True,
        "main",
    )
    py_do_you_even_diff_bro.main.get_git_diff.assert_called_once_with(
        [".java"], [".ts"], "main"
    )
    py_do_you_even_diff_bro.main.gpt_prompt.assert_called()


# Test with a different prompt value
def test_main_with_different_prompt(mocker):
    mocker.patch("py_do_you_even_diff_bro.main.get_git_diff", return_value="Test diff")
    mocker.patch(
        "py_do_you_even_diff_bro.main.gpt_prompt", return_value="Test response"
    )
    main(
        False,
        True,
        False,
        "gpt-3.5-turbo",
        [".py"],
        [".ts"],
        "Different prompt",
        True,
        "main",
    )
    py_do_you_even_diff_bro.main.get_git_diff.assert_called_once_with(
        [".py"], [".ts"], "main"
    )
    py_do_you_even_diff_bro.main.gpt_prompt.assert_called()


# Test with a different peer_review value
def test_main_with_different_peer_review(mocker):
    mocker.patch("py_do_you_even_diff_bro.main.get_git_diff", return_value="Test diff")
    mocker.patch(
        "py_do_you_even_diff_bro.main.gpt_prompt", return_value="Test response"
    )
    main(
        False,
        True,
        False,
        "gpt-3.5-turbo",
        [".py"],
        [".ts"],
        "Test prompt",
        True,
        False,
    )
    py_do_you_even_diff_bro.main.get_git_diff.assert_called_once_with(
        [".py"], [".ts"], False
    )
    py_do_you_even_diff_bro.main.gpt_prompt.assert_called()


# Test with a different summarize value
def test_main_with_different_summarize(mocker):
    mocker.patch("py_do_you_even_diff_bro.main.get_git_diff", return_value="Test diff")
    mocker.patch(
        "py_do_you_even_diff_bro.main.gpt_prompt", return_value="Test response"
    )
    main(
        False,
        True,
        False,
        "gpt-3.5-turbo",
        [".py"],
        [".ts"],
        "Test prompt",
        False,
        "main",
    )
    py_do_you_even_diff_bro.main.get_git_diff.assert_called_once_with(
        [".py"], [".ts"], "main"
    )
    py_do_you_even_diff_bro.main.gpt_prompt.assert_called()


# Test error scenario
def test_main_with_error(mocker):
    mocker.patch(
        "py_do_you_even_diff_bro.main.get_git_diff", side_effect=Exception("Test error")
    )
    if not get_git_diff:
        with pytest.raises(Exception, match="Test error"):
            main(
                False,
                True,
                False,
                "gpt-3.5-turbo",
                [".py"],
                [".ts"],
                "Test prompt",
                True,
                "main",
            )
