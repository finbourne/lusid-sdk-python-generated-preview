# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.3579
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


class FieldSchema(object):
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
        'id': 'ResourceId',
        'display_name': 'str',
        'description': 'str',
        'type': 'str',
        'display_order': 'int'
    }

    attribute_map = {
        'id': 'id',
        'display_name': 'displayName',
        'description': 'description',
        'type': 'type',
        'display_order': 'displayOrder'
    }

    required_map = {
        'id': 'optional',
        'display_name': 'optional',
        'description': 'optional',
        'type': 'optional',
        'display_order': 'optional'
    }

    def __init__(self, id=None, display_name=None, description=None, type=None, display_order=None, local_vars_configuration=None):  # noqa: E501
        """FieldSchema - a model defined in OpenAPI"
        
        :param id: 
        :type id: lusid.ResourceId
        :param display_name: 
        :type display_name: str
        :param description: 
        :type description: str
        :param type:  The available values are: String, Int, Decimal, DateTime, Boolean, Map, List, PropertyArray, Percentage, Code, Id, Uri, CurrencyAndAmount, TradePrice, Currency, MetricValue, ResourceId, ResultValue, CutLocalTime, DateOrCutLabel
        :type type: str
        :param display_order: 
        :type display_order: int

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._display_name = None
        self._description = None
        self._type = None
        self._display_order = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.display_name = display_name
        self.description = description
        if type is not None:
            self.type = type
        if display_order is not None:
            self.display_order = display_order

    @property
    def id(self):
        """Gets the id of this FieldSchema.  # noqa: E501


        :return: The id of this FieldSchema.  # noqa: E501
        :rtype: lusid.ResourceId
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this FieldSchema.


        :param id: The id of this FieldSchema.  # noqa: E501
        :type id: lusid.ResourceId
        """

        self._id = id

    @property
    def display_name(self):
        """Gets the display_name of this FieldSchema.  # noqa: E501


        :return: The display_name of this FieldSchema.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this FieldSchema.


        :param display_name: The display_name of this FieldSchema.  # noqa: E501
        :type display_name: str
        """

        self._display_name = display_name

    @property
    def description(self):
        """Gets the description of this FieldSchema.  # noqa: E501


        :return: The description of this FieldSchema.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this FieldSchema.


        :param description: The description of this FieldSchema.  # noqa: E501
        :type description: str
        """

        self._description = description

    @property
    def type(self):
        """Gets the type of this FieldSchema.  # noqa: E501

        The available values are: String, Int, Decimal, DateTime, Boolean, Map, List, PropertyArray, Percentage, Code, Id, Uri, CurrencyAndAmount, TradePrice, Currency, MetricValue, ResourceId, ResultValue, CutLocalTime, DateOrCutLabel  # noqa: E501

        :return: The type of this FieldSchema.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this FieldSchema.

        The available values are: String, Int, Decimal, DateTime, Boolean, Map, List, PropertyArray, Percentage, Code, Id, Uri, CurrencyAndAmount, TradePrice, Currency, MetricValue, ResourceId, ResultValue, CutLocalTime, DateOrCutLabel  # noqa: E501

        :param type: The type of this FieldSchema.  # noqa: E501
        :type type: str
        """
        allowed_values = ["String", "Int", "Decimal", "DateTime", "Boolean", "Map", "List", "PropertyArray", "Percentage", "Code", "Id", "Uri", "CurrencyAndAmount", "TradePrice", "Currency", "MetricValue", "ResourceId", "ResultValue", "CutLocalTime", "DateOrCutLabel"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def display_order(self):
        """Gets the display_order of this FieldSchema.  # noqa: E501


        :return: The display_order of this FieldSchema.  # noqa: E501
        :rtype: int
        """
        return self._display_order

    @display_order.setter
    def display_order(self, display_order):
        """Sets the display_order of this FieldSchema.


        :param display_order: The display_order of this FieldSchema.  # noqa: E501
        :type display_order: int
        """

        self._display_order = display_order

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
        if not isinstance(other, FieldSchema):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FieldSchema):
            return True

        return self.to_dict() != other.to_dict()
