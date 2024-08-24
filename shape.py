from abc import ABC, abstractmethod


class Shape(ABC):

    def __init__(self, color: str) -> None:
        self._color = color

    def get_color(self) -> str:
        return self._color

    def set_color(self, color: str) -> None:
        self._color = color

    @abstractmethod
    def calculate_area(self) -> float:
        pass

    @abstractmethod
    def calculate_perimeter(self) -> float:
        pass
