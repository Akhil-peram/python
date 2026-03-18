from abc import ABC, abstractmethod


class Vehicles(ABC):
    @abstractmethod
    def type(self):
        pass
