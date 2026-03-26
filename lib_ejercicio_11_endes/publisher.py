class Publisher:
    """
    Represent a publisher entity in the system.

    This class stores the basic information of a publisher, including
    its unique identifier, name, and address.

    :ivar _pub_id: Unique identifier of the publisher.
    :vartype _pub_id: int
    :ivar name: Name of the publisher.
    :vartype name: str
    :ivar address: Address of the publisher.
    :vartype address: str
    """

    def __init__(self, pub_id: int):
        """
        Initialize a new Publisher instance.

        :param pub_id: Unique identifier assigned to the publisher.
        :type pub_id: int
        """
        self._pub_id: int = pub_id
        self.address: str = ''
        self.name: str = ''

    def __str__(self) -> str:
        """
        Return a string representation of the publisher.

        This method returns a formatted string containing the publisher's
        identifier, name, and address.

        :return: Formatted string describing the publisher.
        :rtype: str
        """
        return (f"Publisher id: {self._pub_id}\n"
                f"Publisher name: {self.name}\n"
                f"Publisher address: {self.address}\n")

