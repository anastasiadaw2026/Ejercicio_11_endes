class Member:
    """
    Represents a member in the system.

    This class models a member by storing essential information such as a unique
    member ID, name, address, membership type, and registration/expiry dates.

    Default dates for member registration and expiry are handled using the
    ``ConstantsDates`` inner class.

    :ivar _member_id: Unique identifier of the member.
    :vartype _member_id: int
    :ivar name: Name of the member.
    :vartype name: str
    :ivar address: Address of the member.
    :vartype address: str
    :ivar member_type: Type of membership.
    :vartype member_type: str
    :ivar _member_date: Date the member was registered.
    :vartype _member_date: str
    :ivar _expiry_date: Membership expiry date.
    :vartype _expiry_date: str
    """

    class ConstantsDates:
        """
        Stores constants related to default dates for members.

        :cvar SYSDATE: Default system date assigned to a new membership.
        :vartype SYSDATE: str
        :cvar EXPIRE_DATE: Default expiry date of a membership.
        :vartype EXPIRE_DATE: str
        """
        SYSDATE: str = '15.03.2026'
        EXPIRE_DATE: str = '15.03.2027'

    def __init__(self, member_id):
        """
        Initializes a ``Member`` instance.

        :param member_id: The unique identifier assigned to the member.
        :type member_id: int
        """
        self._member_id: int = member_id
        self.name: str = ''
        self.address: str = ''
        self.member_type: str = ''
        self._member_date: str = Member.ConstantsDates.SYSDATE
        self._expiry_date: str = Member.ConstantsDates.EXPIRE_DATE

    @property
    def member_id(self) -> int:
        """
        Retrieves the unique identifier of the member.

        :return: The unique member ID.
        :rtype: int
        """
        return self._member_id

    def __str__(self) -> str:
        """
        Provides a string representation of the ``Member`` instance.

        :return: A detailed string representation of the member.
        :rtype: str
        """
        return (f"Member id: {self._member_id}\n"
                f"Member name: {self.name}\n"
                f"Membership type: {self.member_type}\n"
                f"Member address: {self.address}\n"
                f"Member register date: {self._member_date}\n"
                f"Member expiry date: {self._expiry_date}")
