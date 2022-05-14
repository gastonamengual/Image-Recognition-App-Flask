from abc import ABC, abstractmethod


class AbstractModel(ABC):
    @abstractmethod
    def fit(self):
        ...

    def predict(self):
        ...
