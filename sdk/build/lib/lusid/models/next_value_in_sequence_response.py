# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.3548
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


class NextValueInSequenceResponse(object):
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
        'values': 'list[str]',
        'links': 'list[Link]'
    }

    attribute_map = {
        'values': 'values',
        'links': 'links'
    }

    required_map = {
        'values': 'required',
        'links': 'optional'
    }

    def __init__(self, values=None, links=None, local_vars_configuration=None):  # noqa: E501
        """NextValueInSequenceResponse - a model defined in OpenAPI"
        
        :param values:  The next set of values for the specified Sequence. (required)
        :type values: list[str]
        :param links:  Collection of links.
        :type links: list[lusid.Link]

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._values = None
        self._links = None
        self.discriminator = None

        self.values = values
        self.links = links

    @property
    def values(self):
        """Gets the values of this NextValueInSequenceResponse.  # noqa: E501

        The next set of values for the specified Sequence.  # noqa: E501

        :return: The values of this NextValueInSequenceResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._values

    @values.setter
    def values(self, values):
        """Sets the values of this NextValueInSequenceResponse.

        The next set of values for the specified Sequence.  # noqa: E501

        :param values: The values of this NextValueInSequenceResponse.  # noqa: E501
        :type values: list[str]
        """
        if self.local_vars_configuration.client_side_validation and values is None:  # noqa: E501
            raise ValueError("Invalid value for `values`, must not be `None`")  # noqa: E501

        self._values = values

    @property
    def links(self):
        """Gets the links of this NextValueInSequenceResponse.  # noqa: E501

        Collection of links.  # noqa: E501

        :return: The links of this NextValueInSequenceResponse.  # noqa: E501
        :rtype: list[lusid.Link]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this NextValueInSequenceResponse.

        Collection of links.  # noqa: E501

        :param links: The links of this NextValueInSequenceResponse.  # noqa: E501
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
        if not isinstance(other, NextValueInSequenceResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, NextValueInSequenceResponse):
            return True

        return self.to_dict() != other.to_dict()
