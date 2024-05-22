from datetime import datetime
import uuid
from models import storage


class BaseModel:
    """
    The BaseModel class serves as the backbone of our project,
    encapsulating common attributes and methods
    shared by other classes.
    It is responsible for initialization,
    serialization, deserialization,
    and other functionalities to be explained later.
    """

    def __init__(self, *args, **kwargs) -> None:
        """
        This is the constructor method for the BaseModel class,
        it initializes the instance variables
        and won't return any value.

        If keyword arguments are provided,
        they are used to set the instance attributes.
        Otherwise, default values are used for
        id, created_at, and updated_at.

        Args:
            *args: Variable length argument list (not used).
            **kwargs: Arbitrary keyword arguments for instance attributes.

        Attributes:
            id (str): Unique identifier for the instance.
            created_at (datetime): Timestamp when the instance was created.
            updated_at (datetime): Timestamp when the instance
                                   was last updated.
        """

        def parse_datetime(date_str: str) -> datetime:
            """
            Parse a datetime string into a datetime object.

            Args:
                date_str (str): String representation of the datetime.

            Returns:
                datetime: A datetime object.
            """
            return datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S.%f")

        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                if key in ("created_at", "updated_at"):
                    self.__dict__[key] = parse_datetime(value)
                else:
                    self.__dict__[key] = value
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self) -> str:
        """
        Return a string representation of the instance.

        Returns:
            str: String representation of the instance in the format
                 [<class name>] (<self.id>) <self.__dict__>.
        """
        return "[{}] ({}) {}".format(type(self).__name__,
                                     self.id, self.__dict__)

    def save(self) -> None:
        """
        Update the public instance attribute updated_at
        with the current datetime and save the instance.
        """
        self.updated_at = datetime.now()
        storage.save()
        storage.new(self)

    def to_dict(self) -> dict:
        """
        Return a dictionary containing all keys/values
        of __dict__ of the instance.

        Returns:
            dict: Dictionary representation of the instance.
        """
        my_dict = self.__dict__.copy()
        my_dict["__class__"] = type(self).__name__
        my_dict["created_at"] = my_dict["created_at"].isoformat()
        my_dict["updated_at"] = my_dict["updated_at"].isoformat()
        return my_dict
