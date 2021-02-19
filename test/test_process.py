from delineation.base import Config, config


def test_singleton():
    assert id(Config()) == id(config)