from abc import ABC, abstractmethod


class GetClass(ABC):
    """Basic representation of get class."""

    @abstractmethod
    def get_information(self) -> None:
        """Provides information for the related OCPI module"""


class ListClass(ABC):
    """Basic representation of list class."""

    @abstractmethod
    def list_information(self) -> None:
        """Provides list based data for the related OCPI module"""


class CreateClass(ABC):
    """Basic representation of create class."""

    @abstractmethod
    def create_entry(self) -> None:
        """Create a new entry based on the given data"""


class UpdateClass(ABC):
    """Basic representation of update class."""

    @abstractmethod
    def update_entry(self) -> None:
        """Updates the existing data as per OCPI protocol"""
