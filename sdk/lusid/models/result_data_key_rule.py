# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.3883
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


class ResultDataKeyRule(object):
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
        'resource_key': 'str',
        'supplier': 'str',
        'data_scope': 'str',
        'document_code': 'str',
        'quote_interval': 'str',
        'as_at': 'datetime'
    }

    attribute_map = {
        'resource_key': 'resourceKey',
        'supplier': 'supplier',
        'data_scope': 'dataScope',
        'document_code': 'documentCode',
        'quote_interval': 'quoteInterval',
        'as_at': 'asAt'
    }

    required_map = {
        'resource_key': 'required',
        'supplier': 'required',
        'data_scope': 'required',
        'document_code': 'required',
        'quote_interval': 'optional',
        'as_at': 'optional'
    }

    def __init__(self, resource_key=None, supplier=None, data_scope=None, document_code=None, quote_interval=None, as_at=None, local_vars_configuration=None):  # noqa: E501
        """ResultDataKeyRule - a model defined in OpenAPI"
        
        :param resource_key:  The result data key that identifies the address pattern that this is a rule for (required)
        :type resource_key: str
        :param supplier:  the result resource supplier (where the data comes from) (required)
        :type supplier: str
        :param data_scope:  which is the scope in which the data should be found (required)
        :type data_scope: str
        :param document_code:  document code that defines which document is desired (required)
        :type document_code: str
        :param quote_interval:  Shorthand for the time interval used to select result data. This must be a dot-separated string              specifying a start and end date, for example '5D.0D' to look back 5 days from today (0 days ago).
        :type quote_interval: str
        :param as_at:  The AsAt predicate specification.
        :type as_at: datetime

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._resource_key = None
        self._supplier = None
        self._data_scope = None
        self._document_code = None
        self._quote_interval = None
        self._as_at = None
        self.discriminator = None

        self.resource_key = resource_key
        self.supplier = supplier
        self.data_scope = data_scope
        self.document_code = document_code
        self.quote_interval = quote_interval
        self.as_at = as_at

    @property
    def resource_key(self):
        """Gets the resource_key of this ResultDataKeyRule.  # noqa: E501

        The result data key that identifies the address pattern that this is a rule for  # noqa: E501

        :return: The resource_key of this ResultDataKeyRule.  # noqa: E501
        :rtype: str
        """
        return self._resource_key

    @resource_key.setter
    def resource_key(self, resource_key):
        """Sets the resource_key of this ResultDataKeyRule.

        The result data key that identifies the address pattern that this is a rule for  # noqa: E501

        :param resource_key: The resource_key of this ResultDataKeyRule.  # noqa: E501
        :type resource_key: str
        """
        if self.local_vars_configuration.client_side_validation and resource_key is None:  # noqa: E501
            raise ValueError("Invalid value for `resource_key`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                resource_key is not None and len(resource_key) > 256):
            raise ValueError("Invalid value for `resource_key`, length must be less than or equal to `256`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                resource_key is not None and len(resource_key) < 0):
            raise ValueError("Invalid value for `resource_key`, length must be greater than or equal to `0`")  # noqa: E501

        self._resource_key = resource_key

    @property
    def supplier(self):
        """Gets the supplier of this ResultDataKeyRule.  # noqa: E501

        the result resource supplier (where the data comes from)  # noqa: E501

        :return: The supplier of this ResultDataKeyRule.  # noqa: E501
        :rtype: str
        """
        return self._supplier

    @supplier.setter
    def supplier(self, supplier):
        """Sets the supplier of this ResultDataKeyRule.

        the result resource supplier (where the data comes from)  # noqa: E501

        :param supplier: The supplier of this ResultDataKeyRule.  # noqa: E501
        :type supplier: str
        """
        if self.local_vars_configuration.client_side_validation and supplier is None:  # noqa: E501
            raise ValueError("Invalid value for `supplier`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                supplier is not None and len(supplier) > 32):
            raise ValueError("Invalid value for `supplier`, length must be less than or equal to `32`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                supplier is not None and len(supplier) < 0):
            raise ValueError("Invalid value for `supplier`, length must be greater than or equal to `0`")  # noqa: E501

        self._supplier = supplier

    @property
    def data_scope(self):
        """Gets the data_scope of this ResultDataKeyRule.  # noqa: E501

        which is the scope in which the data should be found  # noqa: E501

        :return: The data_scope of this ResultDataKeyRule.  # noqa: E501
        :rtype: str
        """
        return self._data_scope

    @data_scope.setter
    def data_scope(self, data_scope):
        """Sets the data_scope of this ResultDataKeyRule.

        which is the scope in which the data should be found  # noqa: E501

        :param data_scope: The data_scope of this ResultDataKeyRule.  # noqa: E501
        :type data_scope: str
        """
        if self.local_vars_configuration.client_side_validation and data_scope is None:  # noqa: E501
            raise ValueError("Invalid value for `data_scope`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                data_scope is not None and len(data_scope) > 256):
            raise ValueError("Invalid value for `data_scope`, length must be less than or equal to `256`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                data_scope is not None and len(data_scope) < 1):
            raise ValueError("Invalid value for `data_scope`, length must be greater than or equal to `1`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                data_scope is not None and not re.search(r'^[a-zA-Z0-9\-_]+$', data_scope)):  # noqa: E501
            raise ValueError(r"Invalid value for `data_scope`, must be a follow pattern or equal to `/^[a-zA-Z0-9\-_]+$/`")  # noqa: E501

        self._data_scope = data_scope

    @property
    def document_code(self):
        """Gets the document_code of this ResultDataKeyRule.  # noqa: E501

        document code that defines which document is desired  # noqa: E501

        :return: The document_code of this ResultDataKeyRule.  # noqa: E501
        :rtype: str
        """
        return self._document_code

    @document_code.setter
    def document_code(self, document_code):
        """Sets the document_code of this ResultDataKeyRule.

        document code that defines which document is desired  # noqa: E501

        :param document_code: The document_code of this ResultDataKeyRule.  # noqa: E501
        :type document_code: str
        """
        if self.local_vars_configuration.client_side_validation and document_code is None:  # noqa: E501
            raise ValueError("Invalid value for `document_code`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                document_code is not None and len(document_code) > 256):
            raise ValueError("Invalid value for `document_code`, length must be less than or equal to `256`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                document_code is not None and len(document_code) < 1):
            raise ValueError("Invalid value for `document_code`, length must be greater than or equal to `1`")  # noqa: E501

        self._document_code = document_code

    @property
    def quote_interval(self):
        """Gets the quote_interval of this ResultDataKeyRule.  # noqa: E501

        Shorthand for the time interval used to select result data. This must be a dot-separated string              specifying a start and end date, for example '5D.0D' to look back 5 days from today (0 days ago).  # noqa: E501

        :return: The quote_interval of this ResultDataKeyRule.  # noqa: E501
        :rtype: str
        """
        return self._quote_interval

    @quote_interval.setter
    def quote_interval(self, quote_interval):
        """Sets the quote_interval of this ResultDataKeyRule.

        Shorthand for the time interval used to select result data. This must be a dot-separated string              specifying a start and end date, for example '5D.0D' to look back 5 days from today (0 days ago).  # noqa: E501

        :param quote_interval: The quote_interval of this ResultDataKeyRule.  # noqa: E501
        :type quote_interval: str
        """
        if (self.local_vars_configuration.client_side_validation and
                quote_interval is not None and len(quote_interval) > 16):
            raise ValueError("Invalid value for `quote_interval`, length must be less than or equal to `16`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                quote_interval is not None and len(quote_interval) < 0):
            raise ValueError("Invalid value for `quote_interval`, length must be greater than or equal to `0`")  # noqa: E501

        self._quote_interval = quote_interval

    @property
    def as_at(self):
        """Gets the as_at of this ResultDataKeyRule.  # noqa: E501

        The AsAt predicate specification.  # noqa: E501

        :return: The as_at of this ResultDataKeyRule.  # noqa: E501
        :rtype: datetime
        """
        return self._as_at

    @as_at.setter
    def as_at(self, as_at):
        """Sets the as_at of this ResultDataKeyRule.

        The AsAt predicate specification.  # noqa: E501

        :param as_at: The as_at of this ResultDataKeyRule.  # noqa: E501
        :type as_at: datetime
        """

        self._as_at = as_at

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
        if not isinstance(other, ResultDataKeyRule):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ResultDataKeyRule):
            return True

        return self.to_dict() != other.to_dict()
