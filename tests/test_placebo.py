from pipeline_kit.placebo import hello

def test_hello_default() -> None:
    assert hello() == "Hello, world!"

def test_hello_custom() -> None:
    assert hello("ND") == "Hello, ND!"

def test_hello_blank_becomes_world() -> None:
    assert hello("   ") == "Hello, world!"
