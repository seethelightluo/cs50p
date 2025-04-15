from twttr import shorten


def test_UppercaseAEIOU():
    assert shorten("YAEILOUY")=="YLY"

def test_Lowercaseaeiou():
    assert shorten("bigger")=="bggr"

def test_numbers():
    assert shorten("Y28,ou76.")=="Y28,76."
