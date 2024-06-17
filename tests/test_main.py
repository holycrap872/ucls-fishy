#!/usr/bin/python3
from pong.main import get_rgb_color


def test_get_rgb_color_1() -> None:
    assert get_rgb_color("white") == (255, 255, 255)


def test_get_rgb_color_2() -> None:
    assert get_rgb_color("black") == (0, 0, 0)
