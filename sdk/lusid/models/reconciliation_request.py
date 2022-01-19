# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.3897
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


class ReconciliationRequest(object):
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
        'left': 'ValuationRequest',
        'right': 'ValuationRequest',
        'left_to_right_mapping': 'list[ReconciliationLeftRightAddressKeyPair]',
        'comparison_rules': 'list[ReconciliationRule]',
        'preserve_keys': 'list[str]'
    }

    attribute_map = {
        'left': 'left',
        'right': 'right',
        'left_to_right_mapping': 'leftToRightMapping',
        'comparison_rules': 'comparisonRules',
        'preserve_keys': 'preserveKeys'
    }

    required_map = {
        'left': 'required',
        'right': 'required',
        'left_to_right_mapping': 'optional',
        'comparison_rules': 'optional',
        'preserve_keys': 'optional'
    }

    def __init__(self, left=None, right=None, left_to_right_mapping=None, comparison_rules=None, preserve_keys=None, local_vars_configuration=None):  # noqa: E501
        """ReconciliationRequest - a model defined in OpenAPI"
        
        :param left:  (required)
        :type left: lusid.ValuationRequest
        :param right:  (required)
        :type right: lusid.ValuationRequest
        :param left_to_right_mapping:  The mapping from property keys requested by left aggregation to property keys on right hand side
        :type left_to_right_mapping: list[lusid.ReconciliationLeftRightAddressKeyPair]
        :param comparison_rules:  The set of rules to be used in comparing values. These are the rules that determine what constitues a match.  The simplest is obviously an exact one-for-one comparison, but tolerances on numerical or date time values and  case-insensitive string comparison are supported amongst other types.
        :type comparison_rules: list[lusid.ReconciliationRule]
        :param preserve_keys:  List of keys to preserve (from rhs) in the diff. Used in conjunction with filtering/grouping.  If two values are equal, for a given key then the value is elided from the results. Setting it here  will preserve it (takes the values from the RHS and puts it into the line by line results).
        :type preserve_keys: list[str]

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._left = None
        self._right = None
        self._left_to_right_mapping = None
        self._comparison_rules = None
        self._preserve_keys = None
        self.discriminator = None

        self.left = left
        self.right = right
        self.left_to_right_mapping = left_to_right_mapping
        self.comparison_rules = comparison_rules
        self.preserve_keys = preserve_keys

    @property
    def left(self):
        """Gets the left of this ReconciliationRequest.  # noqa: E501


        :return: The left of this ReconciliationRequest.  # noqa: E501
        :rtype: lusid.ValuationRequest
        """
        return self._left

    @left.setter
    def left(self, left):
        """Sets the left of this ReconciliationRequest.


        :param left: The left of this ReconciliationRequest.  # noqa: E501
        :type left: lusid.ValuationRequest
        """
        if self.local_vars_configuration.client_side_validation and left is None:  # noqa: E501
            raise ValueError("Invalid value for `left`, must not be `None`")  # noqa: E501

        self._left = left

    @property
    def right(self):
        """Gets the right of this ReconciliationRequest.  # noqa: E501


        :return: The right of this ReconciliationRequest.  # noqa: E501
        :rtype: lusid.ValuationRequest
        """
        return self._right

    @right.setter
    def right(self, right):
        """Sets the right of this ReconciliationRequest.


        :param right: The right of this ReconciliationRequest.  # noqa: E501
        :type right: lusid.ValuationRequest
        """
        if self.local_vars_configuration.client_side_validation and right is None:  # noqa: E501
            raise ValueError("Invalid value for `right`, must not be `None`")  # noqa: E501

        self._right = right

    @property
    def left_to_right_mapping(self):
        """Gets the left_to_right_mapping of this ReconciliationRequest.  # noqa: E501

        The mapping from property keys requested by left aggregation to property keys on right hand side  # noqa: E501

        :return: The left_to_right_mapping of this ReconciliationRequest.  # noqa: E501
        :rtype: list[lusid.ReconciliationLeftRightAddressKeyPair]
        """
        return self._left_to_right_mapping

    @left_to_right_mapping.setter
    def left_to_right_mapping(self, left_to_right_mapping):
        """Sets the left_to_right_mapping of this ReconciliationRequest.

        The mapping from property keys requested by left aggregation to property keys on right hand side  # noqa: E501

        :param left_to_right_mapping: The left_to_right_mapping of this ReconciliationRequest.  # noqa: E501
        :type left_to_right_mapping: list[lusid.ReconciliationLeftRightAddressKeyPair]
        """

        self._left_to_right_mapping = left_to_right_mapping

    @property
    def comparison_rules(self):
        """Gets the comparison_rules of this ReconciliationRequest.  # noqa: E501

        The set of rules to be used in comparing values. These are the rules that determine what constitues a match.  The simplest is obviously an exact one-for-one comparison, but tolerances on numerical or date time values and  case-insensitive string comparison are supported amongst other types.  # noqa: E501

        :return: The comparison_rules of this ReconciliationRequest.  # noqa: E501
        :rtype: list[lusid.ReconciliationRule]
        """
        return self._comparison_rules

    @comparison_rules.setter
    def comparison_rules(self, comparison_rules):
        """Sets the comparison_rules of this ReconciliationRequest.

        The set of rules to be used in comparing values. These are the rules that determine what constitues a match.  The simplest is obviously an exact one-for-one comparison, but tolerances on numerical or date time values and  case-insensitive string comparison are supported amongst other types.  # noqa: E501

        :param comparison_rules: The comparison_rules of this ReconciliationRequest.  # noqa: E501
        :type comparison_rules: list[lusid.ReconciliationRule]
        """

        self._comparison_rules = comparison_rules

    @property
    def preserve_keys(self):
        """Gets the preserve_keys of this ReconciliationRequest.  # noqa: E501

        List of keys to preserve (from rhs) in the diff. Used in conjunction with filtering/grouping.  If two values are equal, for a given key then the value is elided from the results. Setting it here  will preserve it (takes the values from the RHS and puts it into the line by line results).  # noqa: E501

        :return: The preserve_keys of this ReconciliationRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._preserve_keys

    @preserve_keys.setter
    def preserve_keys(self, preserve_keys):
        """Sets the preserve_keys of this ReconciliationRequest.

        List of keys to preserve (from rhs) in the diff. Used in conjunction with filtering/grouping.  If two values are equal, for a given key then the value is elided from the results. Setting it here  will preserve it (takes the values from the RHS and puts it into the line by line results).  # noqa: E501

        :param preserve_keys: The preserve_keys of this ReconciliationRequest.  # noqa: E501
        :type preserve_keys: list[str]
        """

        self._preserve_keys = preserve_keys

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
        if not isinstance(other, ReconciliationRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ReconciliationRequest):
            return True

        return self.to_dict() != other.to_dict()
