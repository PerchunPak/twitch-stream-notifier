from src.utils import Singleton
from src.config import  BASE_DIR
import typing as t
import json


class DatabaseContent(t.TypedDict):
    last_status: t.Dict[str, bool]


class Database(metaclass=Singleton):
    """Simple JSON database for storing whether user last time checked streamed or not."""

    def __init__(self) -> None:
        self._path = BASE_DIR / "data" / "db.json"
        self._data: DatabaseContent = {"last_status": {}}
        self._read()

    def _read(self) -> None:
        if self._path.exists():
            with self._path.open("r") as f:
                self._data = json.load(f)

    def write(self) -> None:
        with self._path.open("w") as f:
            json.dump(self._data, f)

    def update_status(self, new_status: t.Dict[str, bool]) -> None:
        self._data["last_status"] = new_status
        self.write()

    def get_last_status(self) -> t.Dict[str, bool]:
        return self._data["last_status"]
