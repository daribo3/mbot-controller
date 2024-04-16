import logging

from evdev import InputDevice

logger = logging.getLogger(__name__)


class Controller:
    _path: str | None = None
    _name: str | None = None
    _device: InputDevice = None

    def __init__(self, path: str | None, *, name: str = None):
        self._path = path
        self._name = name
