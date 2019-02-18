from pprint import pformat
from six import iteritems


class LiveVideo(object):
    def __init__(self, id=None, created_at=None, applicant_id=None, href=None, download_href=None, file_name=None,
                 file_size=None, file_type=None):
        """
        LivePhoto - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'created_at': 'datetime',
            'applicant_id': 'str',
            'href': 'str',
            'download_href': 'str',
            'file_name': 'str',
            'file_size': 'int',
            'file_type': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'created_at': 'created_at',
            'applicant_id': 'applicant_id',
            'href': 'href',
            'download_href': 'download_href',
            'file_name': 'file_name',
            'file_size': 'file_size',
            'file_type': 'file_type'
        }

        self._id = id
        self._created_at = created_at
        self._applicant_id = applicant_id
        self._href = href
        self._download_href = download_href
        self._file_name = file_name
        self._file_size = file_size
        self._file_type = file_type

    @property
    def id(self):
        """
        Gets the id of this LivePhoto.
        The unique identifier for the document.

        :return: The id of this LivePhoto.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this LivePhoto.
        The unique identifier for the document.

        :param id: The id of this LivePhoto.
        :type: str
        """

        self._id = id

    @property
    def created_at(self):
        """
        Gets the created_at of this LivePhoto.
        The date and time at which the document was uploaded.

        :return: The created_at of this LivePhoto.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """
        Sets the created_at of this LivePhoto.
        The date and time at which the document was uploaded.

        :param created_at: The created_at of this LivePhoto.
        :type: datetime
        """

        self._created_at = created_at

    @property
    def applicant_id(self):
        """
        Gets the applicant_id of this LivePhoto.
        The id of the applicant the live photo belongs to.

        :return: The applicant_id of this LivePhoto.
        :rtype: str
        """
        return self._applicant_id

    @applicant_id.setter
    def applicant_id(self, applicant_id):
        """
        Sets the applicant_id of this LivePhoto.
        The id of the applicant the live photo belongs to.

        :param applicant_id: The applicant_id of this LivePhoto.
        :type: str
        """

        self._applicant_id = applicant_id

    @property
    def href(self):
        """
        Gets the href of this LivePhoto.
        The uri of this resource.

        :return: The href of this LivePhoto.
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """
        Sets the href of this LivePhoto.
        The uri of this resource.

        :param href: The href of this LivePhoto.
        :type: str
        """

        self._href = href

    @property
    def download_href(self):
        """
        Gets the download_href of this LivePhoto.
        The uri that can be used to download the document.

        :return: The download_href of this LivePhoto.
        :rtype: str
        """
        return self._download_href

    @download_href.setter
    def download_href(self, download_href):
        """
        Sets the download_href of this LivePhoto.
        The uri that can be used to download the document.

        :param download_href: The download_href of this LivePhoto.
        :type: str
        """

        self._download_href = download_href

    @property
    def file_name(self):
        """
        Gets the file_name of this LivePhoto.
        The name of the uploaded file.

        :return: The file_name of this LivePhoto.
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        """
        Sets the file_name of this LivePhoto.
        The name of the uploaded file.

        :param file_name: The file_name of this LivePhoto.
        :type: str
        """

        self._file_name = file_name

    @property
    def file_size(self):
        """
        Gets the file_size of this LivePhoto.
        The size of the file in bytes.

        :return: The file_size of this LivePhoto.
        :rtype: int
        """
        return self._file_size

    @file_size.setter
    def file_size(self, file_size):
        """
        Sets the file_size of this LivePhoto.
        The size of the file in bytes.

        :param file_size: The file_size of this LivePhoto.
        :type: int
        """

        self._file_size = file_size

    @property
    def file_type(self):
        """
        Gets the file_type of this LivePhoto.
        The file type of the uploaded file.

        :return: The file_type of this LivePhoto.
        :rtype: str
        """
        return self._file_type

    @file_type.setter
    def file_type(self, file_type):
        """
        Sets the file_type of this LivePhoto.
        The file type of the uploaded file.

        :param file_type: The file_type of this LivePhoto.
        :type: str
        """

        self._file_type = file_type

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
