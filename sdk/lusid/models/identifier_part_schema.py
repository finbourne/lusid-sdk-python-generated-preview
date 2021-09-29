# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.3550
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from lusid.configuration import Configuration


class IdentifierPartSchema(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
      required_map (dict): The key is attribute name
                           and the value is whether it is 'required' or 'optional'.
    """
    openapi_types = {
        'index': 'int',
        'name': 'str',
        'display_name': 'str',
        'description': 'str',
        'required': 'bool',
        'links': 'list[Link]'
    }

    attribute_map = {
        'index': 'index',
        'name': 'name',
        'display_name': 'displayName',
        'description': 'description',
        'required': 'required',
        'links': 'links'
    }

    required_map = {
        'index': 'required',
        'name': 'required',
        'display_name': 'required',
        'description': 'required',
        'required': 'required',
        'links': 'optional'
    }

    def __init__(self, index=None, name=None, display_name=None, description=None, required=None, links=None, local_vars_configuration=None):  # noqa: E501
        """IdentifierPartSchema - a model defined in OpenAPI"
        
        :param index:  The typical index in the identifier in which this part appears (required)
        :type index: int
        :param name:  The name of the identifier part that can/should be provided for this resource type (required)
        :type name: str
        :param display_name:  The display name of the identifier part (required)
        :type display_name: str
        :param description:  A brief description of the point of this identifier part (required)
        :type description: str
        :param required:  Whether a value is required to be provided (required)
        :type required: bool
        :param links:  Collection of links.
        :type links: list[lusid.Link]

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._index = None
        self._name = None
        self._display_name = None
        self._description = None
        self._required = None
        self._links = None
        self.discriminator = None

        self.index = index
        self.name = name
        self.display_name = display_name
        self.description = description
        self.required = required
        self.links = links

    @property
    def index(self):
        """Gets the index of this IdentifierPartSchema.  # noqa: E501

        The typical index in the identifier in which this part appears  # noqa: E501

        :return: The index of this IdentifierPartSchema.  # noqa: E501
        :rtype: int
        """
        return self._index

    @index.setter
    def index(self, index):
        """Sets the index of this IdentifierPartSchema.

        The typical index in the identifier in which this part appears  # noqa: E501

        :param index: The index of this IdentifierPartSchema.  # noqa: E501
        :type index: int
        """
        if self.local_vars_configuration.client_side_validation and index is None:  # noqa: E501
            raise ValueError("Invalid value for `index`, must not be `None`")  # noqa: E501

        self._index = index

    @property
    def name(self):
        """Gets the name of this IdentifierPartSchema.  # noqa: E501

        The name of the identifier part that can/should be provided for this resource type  # noqa: E501

        :return: The name of this IdentifierPartSchema.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this IdentifierPartSchema.

        The name of the identifier part that can/should be provided for this resource type  # noqa: E501

        :param name: The name of this IdentifierPartSchema.  # noqa: E501
        :type name: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def display_name(self):
        """Gets the display_name of this IdentifierPartSchema.  # noqa: E501

        The display name of the identifier part  # noqa: E501

        :return: The display_name of this IdentifierPartSchema.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this IdentifierPartSchema.

        The display name of the identifier part  # noqa: E501

        :param display_name: The display_name of this IdentifierPartSchema.  # noqa: E501
        :type display_name: str
        """
        if self.local_vars_configuration.client_side_validation and display_name is None:  # noqa: E501
            raise ValueError("Invalid value for `display_name`, must not be `None`")  # noqa: E501

        self._display_name = display_name

    @property
    def description(self):
        """Gets the description of this IdentifierPartSchema.  # noqa: E501

        A brief description of the point of this identifier part  # noqa: E501

        :return: The description of this IdentifierPartSchema.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this IdentifierPartSchema.

        A brief description of the point of this identifier part  # noqa: E501

        :param description: The description of this IdentifierPartSchema.  # noqa: E501
        :type description: str
        """
        if self.local_vars_configuration.client_side_validation and description is None:  # noqa: E501
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def required(self):
        """Gets the required of this IdentifierPartSchema.  # noqa: E501

        Whether a value is required to be provided  # noqa: E501

        :return: The required of this IdentifierPartSchema.  # noqa: E501
        :rtype: bool
        """
        return self._required

    @required.setter
    def required(self, required):
        """Sets the required of this IdentifierPartSchema.

        Whether a value is required to be provided  # noqa: E501

        :param required: The required of this IdentifierPartSchema.  # noqa: E501
        :type required: bool
        """
        if self.local_vars_configuration.client_side_validation and required is None:  # noqa: E501
            raise ValueError("Invalid value for `required`, must not be `None`")  # noqa: E501

        self._required = required

    @property
    def links(self):
        """Gets the links of this IdentifierPartSchema.  # noqa: E501

        Collection of links.  # noqa: E501

        :return: The links of this IdentifierPartSchema.  # noqa: E501
        :rtype: list[lusid.Link]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this IdentifierPartSchema.

        Collection of links.  # noqa: E501

        :param links: The links of this IdentifierPartSchema.  # noqa: E501
        :type links: list[lusid.Link]
        """

        self._links = links

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = getfullargspec(x.to_dict).args
                if len(args) == 1:
                    return x.to_dict()
                else:
                    return x.to_dict(serialize)
            else:
                return x

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            attr = self.attribute_map.get(attr, attr) if serialize else attr
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: convert(x),
                    value
                ))
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], convert(item[1])),
                    value.items()
                ))
            else:
                result[attr] = convert(value)

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, IdentifierPartSchema):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IdentifierPartSchema):
            return True

        return self.to_dict() != other.to_dict()
