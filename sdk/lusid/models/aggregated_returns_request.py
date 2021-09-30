# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.3553
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


class AggregatedReturnsRequest(object):
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
        'metrics': 'list[PerformanceReturnsMetric]',
        'recipe_id': 'ResourceId',
        'composite_method': 'str',
        'period': 'str',
        'output_frequency': 'str',
        'alternative_inception_date': 'str'
    }

    attribute_map = {
        'metrics': 'metrics',
        'recipe_id': 'recipeId',
        'composite_method': 'compositeMethod',
        'period': 'period',
        'output_frequency': 'outputFrequency',
        'alternative_inception_date': 'alternativeInceptionDate'
    }

    required_map = {
        'metrics': 'required',
        'recipe_id': 'optional',
        'composite_method': 'optional',
        'period': 'optional',
        'output_frequency': 'optional',
        'alternative_inception_date': 'optional'
    }

    def __init__(self, metrics=None, recipe_id=None, composite_method=None, period=None, output_frequency=None, alternative_inception_date=None, local_vars_configuration=None):  # noqa: E501
        """AggregatedReturnsRequest - a model defined in OpenAPI"
        
        :param metrics:  A list of metrics to calculate in the AggregatedReturns. (required)
        :type metrics: list[lusid.PerformanceReturnsMetric]
        :param recipe_id: 
        :type recipe_id: lusid.ResourceId
        :param composite_method:  The method used to calculate the Portfolio performance: Equal/Asset.
        :type composite_method: str
        :param period:  The type of the returns used to calculate the aggregation result: Daily/Monthly.
        :type period: str
        :param output_frequency:  The type of calculated output: Daily/Weekly/Monthly/Quarterly/Half-Yearly/Yearly.
        :type output_frequency: str
        :param alternative_inception_date:  The type of calculated output: Daily/Weekly/Monthly/Quarterly/Half-Yearly/Yearly.
        :type alternative_inception_date: str

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._metrics = None
        self._recipe_id = None
        self._composite_method = None
        self._period = None
        self._output_frequency = None
        self._alternative_inception_date = None
        self.discriminator = None

        self.metrics = metrics
        if recipe_id is not None:
            self.recipe_id = recipe_id
        self.composite_method = composite_method
        self.period = period
        self.output_frequency = output_frequency
        self.alternative_inception_date = alternative_inception_date

    @property
    def metrics(self):
        """Gets the metrics of this AggregatedReturnsRequest.  # noqa: E501

        A list of metrics to calculate in the AggregatedReturns.  # noqa: E501

        :return: The metrics of this AggregatedReturnsRequest.  # noqa: E501
        :rtype: list[lusid.PerformanceReturnsMetric]
        """
        return self._metrics

    @metrics.setter
    def metrics(self, metrics):
        """Sets the metrics of this AggregatedReturnsRequest.

        A list of metrics to calculate in the AggregatedReturns.  # noqa: E501

        :param metrics: The metrics of this AggregatedReturnsRequest.  # noqa: E501
        :type metrics: list[lusid.PerformanceReturnsMetric]
        """
        if self.local_vars_configuration.client_side_validation and metrics is None:  # noqa: E501
            raise ValueError("Invalid value for `metrics`, must not be `None`")  # noqa: E501

        self._metrics = metrics

    @property
    def recipe_id(self):
        """Gets the recipe_id of this AggregatedReturnsRequest.  # noqa: E501


        :return: The recipe_id of this AggregatedReturnsRequest.  # noqa: E501
        :rtype: lusid.ResourceId
        """
        return self._recipe_id

    @recipe_id.setter
    def recipe_id(self, recipe_id):
        """Sets the recipe_id of this AggregatedReturnsRequest.


        :param recipe_id: The recipe_id of this AggregatedReturnsRequest.  # noqa: E501
        :type recipe_id: lusid.ResourceId
        """

        self._recipe_id = recipe_id

    @property
    def composite_method(self):
        """Gets the composite_method of this AggregatedReturnsRequest.  # noqa: E501

        The method used to calculate the Portfolio performance: Equal/Asset.  # noqa: E501

        :return: The composite_method of this AggregatedReturnsRequest.  # noqa: E501
        :rtype: str
        """
        return self._composite_method

    @composite_method.setter
    def composite_method(self, composite_method):
        """Sets the composite_method of this AggregatedReturnsRequest.

        The method used to calculate the Portfolio performance: Equal/Asset.  # noqa: E501

        :param composite_method: The composite_method of this AggregatedReturnsRequest.  # noqa: E501
        :type composite_method: str
        """

        self._composite_method = composite_method

    @property
    def period(self):
        """Gets the period of this AggregatedReturnsRequest.  # noqa: E501

        The type of the returns used to calculate the aggregation result: Daily/Monthly.  # noqa: E501

        :return: The period of this AggregatedReturnsRequest.  # noqa: E501
        :rtype: str
        """
        return self._period

    @period.setter
    def period(self, period):
        """Sets the period of this AggregatedReturnsRequest.

        The type of the returns used to calculate the aggregation result: Daily/Monthly.  # noqa: E501

        :param period: The period of this AggregatedReturnsRequest.  # noqa: E501
        :type period: str
        """

        self._period = period

    @property
    def output_frequency(self):
        """Gets the output_frequency of this AggregatedReturnsRequest.  # noqa: E501

        The type of calculated output: Daily/Weekly/Monthly/Quarterly/Half-Yearly/Yearly.  # noqa: E501

        :return: The output_frequency of this AggregatedReturnsRequest.  # noqa: E501
        :rtype: str
        """
        return self._output_frequency

    @output_frequency.setter
    def output_frequency(self, output_frequency):
        """Sets the output_frequency of this AggregatedReturnsRequest.

        The type of calculated output: Daily/Weekly/Monthly/Quarterly/Half-Yearly/Yearly.  # noqa: E501

        :param output_frequency: The output_frequency of this AggregatedReturnsRequest.  # noqa: E501
        :type output_frequency: str
        """

        self._output_frequency = output_frequency

    @property
    def alternative_inception_date(self):
        """Gets the alternative_inception_date of this AggregatedReturnsRequest.  # noqa: E501

        The type of calculated output: Daily/Weekly/Monthly/Quarterly/Half-Yearly/Yearly.  # noqa: E501

        :return: The alternative_inception_date of this AggregatedReturnsRequest.  # noqa: E501
        :rtype: str
        """
        return self._alternative_inception_date

    @alternative_inception_date.setter
    def alternative_inception_date(self, alternative_inception_date):
        """Sets the alternative_inception_date of this AggregatedReturnsRequest.

        The type of calculated output: Daily/Weekly/Monthly/Quarterly/Half-Yearly/Yearly.  # noqa: E501

        :param alternative_inception_date: The alternative_inception_date of this AggregatedReturnsRequest.  # noqa: E501
        :type alternative_inception_date: str
        """

        self._alternative_inception_date = alternative_inception_date

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
        if not isinstance(other, AggregatedReturnsRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AggregatedReturnsRequest):
            return True

        return self.to_dict() != other.to_dict()
