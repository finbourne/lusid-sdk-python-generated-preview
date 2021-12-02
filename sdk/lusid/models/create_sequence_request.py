# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.3794
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


class CreateSequenceRequest(object):
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
        'code': 'str',
        'increment': 'int',
        'min_value': 'int',
        'max_value': 'int',
        'start': 'int',
        'cycle': 'bool',
        'pattern': 'str',
        'links': 'list[Link]'
    }

    attribute_map = {
        'code': 'code',
        'increment': 'increment',
        'min_value': 'minValue',
        'max_value': 'maxValue',
        'start': 'start',
        'cycle': 'cycle',
        'pattern': 'pattern',
        'links': 'links'
    }

    required_map = {
        'code': 'required',
        'increment': 'optional',
        'min_value': 'optional',
        'max_value': 'optional',
        'start': 'optional',
        'cycle': 'optional',
        'pattern': 'optional',
        'links': 'optional'
    }

    def __init__(self, code=None, increment=None, min_value=None, max_value=None, start=None, cycle=None, pattern=None, links=None, local_vars_configuration=None):  # noqa: E501
        """CreateSequenceRequest - a model defined in OpenAPI"
        
        :param code:  The code of the sequence definition to create (required)
        :type code: str
        :param increment:  The value to increment between each value in the sequence
        :type increment: int
        :param min_value:  The minimum value of the sequence
        :type min_value: int
        :param max_value:  The maximum value of the sequence
        :type max_value: int
        :param start:  The start value of the sequence
        :type start: int
        :param cycle:  Indicates if the sequence would start from minimun value once it reaches maximum value. If set to false, a failure would return if the sequence reaches maximum value. Default to false.
        :type cycle: bool
        :param pattern:  The pattern to be used to generate next values in the sequence. Default to null. Please provide a null value until further notice.
        :type pattern: str
        :param links:  Collection of links.
        :type links: list[lusid.Link]

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._code = None
        self._increment = None
        self._min_value = None
        self._max_value = None
        self._start = None
        self._cycle = None
        self._pattern = None
        self._links = None
        self.discriminator = None

        self.code = code
        self.increment = increment
        self.min_value = min_value
        self.max_value = max_value
        self.start = start
        if cycle is not None:
            self.cycle = cycle
        self.pattern = pattern
        self.links = links

    @property
    def code(self):
        """Gets the code of this CreateSequenceRequest.  # noqa: E501

        The code of the sequence definition to create  # noqa: E501

        :return: The code of this CreateSequenceRequest.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this CreateSequenceRequest.

        The code of the sequence definition to create  # noqa: E501

        :param code: The code of this CreateSequenceRequest.  # noqa: E501
        :type code: str
        """
        if self.local_vars_configuration.client_side_validation and code is None:  # noqa: E501
            raise ValueError("Invalid value for `code`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                code is not None and len(code) > 64):
            raise ValueError("Invalid value for `code`, length must be less than or equal to `64`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                code is not None and len(code) < 1):
            raise ValueError("Invalid value for `code`, length must be greater than or equal to `1`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                code is not None and not re.search(r'^[a-zA-Z0-9\-_]+$', code)):  # noqa: E501
            raise ValueError(r"Invalid value for `code`, must be a follow pattern or equal to `/^[a-zA-Z0-9\-_]+$/`")  # noqa: E501

        self._code = code

    @property
    def increment(self):
        """Gets the increment of this CreateSequenceRequest.  # noqa: E501

        The value to increment between each value in the sequence  # noqa: E501

        :return: The increment of this CreateSequenceRequest.  # noqa: E501
        :rtype: int
        """
        return self._increment

    @increment.setter
    def increment(self, increment):
        """Sets the increment of this CreateSequenceRequest.

        The value to increment between each value in the sequence  # noqa: E501

        :param increment: The increment of this CreateSequenceRequest.  # noqa: E501
        :type increment: int
        """

        self._increment = increment

    @property
    def min_value(self):
        """Gets the min_value of this CreateSequenceRequest.  # noqa: E501

        The minimum value of the sequence  # noqa: E501

        :return: The min_value of this CreateSequenceRequest.  # noqa: E501
        :rtype: int
        """
        return self._min_value

    @min_value.setter
    def min_value(self, min_value):
        """Sets the min_value of this CreateSequenceRequest.

        The minimum value of the sequence  # noqa: E501

        :param min_value: The min_value of this CreateSequenceRequest.  # noqa: E501
        :type min_value: int
        """

        self._min_value = min_value

    @property
    def max_value(self):
        """Gets the max_value of this CreateSequenceRequest.  # noqa: E501

        The maximum value of the sequence  # noqa: E501

        :return: The max_value of this CreateSequenceRequest.  # noqa: E501
        :rtype: int
        """
        return self._max_value

    @max_value.setter
    def max_value(self, max_value):
        """Sets the max_value of this CreateSequenceRequest.

        The maximum value of the sequence  # noqa: E501

        :param max_value: The max_value of this CreateSequenceRequest.  # noqa: E501
        :type max_value: int
        """

        self._max_value = max_value

    @property
    def start(self):
        """Gets the start of this CreateSequenceRequest.  # noqa: E501

        The start value of the sequence  # noqa: E501

        :return: The start of this CreateSequenceRequest.  # noqa: E501
        :rtype: int
        """
        return self._start

    @start.setter
    def start(self, start):
        """Sets the start of this CreateSequenceRequest.

        The start value of the sequence  # noqa: E501

        :param start: The start of this CreateSequenceRequest.  # noqa: E501
        :type start: int
        """

        self._start = start

    @property
    def cycle(self):
        """Gets the cycle of this CreateSequenceRequest.  # noqa: E501

        Indicates if the sequence would start from minimun value once it reaches maximum value. If set to false, a failure would return if the sequence reaches maximum value. Default to false.  # noqa: E501

        :return: The cycle of this CreateSequenceRequest.  # noqa: E501
        :rtype: bool
        """
        return self._cycle

    @cycle.setter
    def cycle(self, cycle):
        """Sets the cycle of this CreateSequenceRequest.

        Indicates if the sequence would start from minimun value once it reaches maximum value. If set to false, a failure would return if the sequence reaches maximum value. Default to false.  # noqa: E501

        :param cycle: The cycle of this CreateSequenceRequest.  # noqa: E501
        :type cycle: bool
        """

        self._cycle = cycle

    @property
    def pattern(self):
        """Gets the pattern of this CreateSequenceRequest.  # noqa: E501

        The pattern to be used to generate next values in the sequence. Default to null. Please provide a null value until further notice.  # noqa: E501

        :return: The pattern of this CreateSequenceRequest.  # noqa: E501
        :rtype: str
        """
        return self._pattern

    @pattern.setter
    def pattern(self, pattern):
        """Sets the pattern of this CreateSequenceRequest.

        The pattern to be used to generate next values in the sequence. Default to null. Please provide a null value until further notice.  # noqa: E501

        :param pattern: The pattern of this CreateSequenceRequest.  # noqa: E501
        :type pattern: str
        """
        if (self.local_vars_configuration.client_side_validation and
                pattern is not None and len(pattern) > 44):
            raise ValueError("Invalid value for `pattern`, length must be less than or equal to `44`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                pattern is not None and len(pattern) < 1):
            raise ValueError("Invalid value for `pattern`, length must be greater than or equal to `1`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                pattern is not None and not re.search(r'^[A-Za-z0-9_-]*\{\{seqValue\}\}[A-Za-z0-9_-]*$', pattern)):  # noqa: E501
            raise ValueError(r"Invalid value for `pattern`, must be a follow pattern or equal to `/^[A-Za-z0-9_-]*\{\{seqValue\}\}[A-Za-z0-9_-]*$/`")  # noqa: E501

        self._pattern = pattern

    @property
    def links(self):
        """Gets the links of this CreateSequenceRequest.  # noqa: E501

        Collection of links.  # noqa: E501

        :return: The links of this CreateSequenceRequest.  # noqa: E501
        :rtype: list[lusid.Link]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this CreateSequenceRequest.

        Collection of links.  # noqa: E501

        :param links: The links of this CreateSequenceRequest.  # noqa: E501
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
        if not isinstance(other, CreateSequenceRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateSequenceRequest):
            return True

        return self.to_dict() != other.to_dict()
