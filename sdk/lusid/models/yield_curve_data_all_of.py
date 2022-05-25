# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.4404
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


class YieldCurveDataAllOf(object):
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
        'base_date': 'datetime',
        'instruments': 'list[LusidInstrument]',
        'quotes': 'list[MarketQuote]',
        'lineage': 'str',
        'market_data_type': 'str'
    }

    attribute_map = {
        'base_date': 'baseDate',
        'instruments': 'instruments',
        'quotes': 'quotes',
        'lineage': 'lineage',
        'market_data_type': 'marketDataType'
    }

    required_map = {
        'base_date': 'required',
        'instruments': 'required',
        'quotes': 'required',
        'lineage': 'optional',
        'market_data_type': 'required'
    }

    def __init__(self, base_date=None, instruments=None, quotes=None, lineage=None, market_data_type=None, local_vars_configuration=None):  # noqa: E501
        """YieldCurveDataAllOf - a model defined in OpenAPI"
        
        :param base_date:  Base date (required)
        :type base_date: datetime
        :param instruments:  The set of instruments that define the curve. (required)
        :type instruments: list[lusid.LusidInstrument]
        :param quotes:  The market quotes corresponding to the the instruments used to define the curve (required)
        :type quotes: list[lusid.MarketQuote]
        :param lineage:  Description of the complex market data's lineage e.g. 'FundAccountant_GreenQuality'.
        :type lineage: str
        :param market_data_type:  The available values are: DiscountFactorCurveData, EquityVolSurfaceData, FxVolSurfaceData, IrVolCubeData, OpaqueMarketData, YieldCurveData, FxForwardCurveData, FxForwardPipsCurveData, FxForwardTenorCurveData, FxForwardTenorPipsCurveData, FxForwardCurveByQuoteReference, CreditSpreadCurveData (required)
        :type market_data_type: str

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._base_date = None
        self._instruments = None
        self._quotes = None
        self._lineage = None
        self._market_data_type = None
        self.discriminator = None

        self.base_date = base_date
        self.instruments = instruments
        self.quotes = quotes
        self.lineage = lineage
        self.market_data_type = market_data_type

    @property
    def base_date(self):
        """Gets the base_date of this YieldCurveDataAllOf.  # noqa: E501

        Base date  # noqa: E501

        :return: The base_date of this YieldCurveDataAllOf.  # noqa: E501
        :rtype: datetime
        """
        return self._base_date

    @base_date.setter
    def base_date(self, base_date):
        """Sets the base_date of this YieldCurveDataAllOf.

        Base date  # noqa: E501

        :param base_date: The base_date of this YieldCurveDataAllOf.  # noqa: E501
        :type base_date: datetime
        """
        if self.local_vars_configuration.client_side_validation and base_date is None:  # noqa: E501
            raise ValueError("Invalid value for `base_date`, must not be `None`")  # noqa: E501

        self._base_date = base_date

    @property
    def instruments(self):
        """Gets the instruments of this YieldCurveDataAllOf.  # noqa: E501

        The set of instruments that define the curve.  # noqa: E501

        :return: The instruments of this YieldCurveDataAllOf.  # noqa: E501
        :rtype: list[lusid.LusidInstrument]
        """
        return self._instruments

    @instruments.setter
    def instruments(self, instruments):
        """Sets the instruments of this YieldCurveDataAllOf.

        The set of instruments that define the curve.  # noqa: E501

        :param instruments: The instruments of this YieldCurveDataAllOf.  # noqa: E501
        :type instruments: list[lusid.LusidInstrument]
        """
        if self.local_vars_configuration.client_side_validation and instruments is None:  # noqa: E501
            raise ValueError("Invalid value for `instruments`, must not be `None`")  # noqa: E501

        self._instruments = instruments

    @property
    def quotes(self):
        """Gets the quotes of this YieldCurveDataAllOf.  # noqa: E501

        The market quotes corresponding to the the instruments used to define the curve  # noqa: E501

        :return: The quotes of this YieldCurveDataAllOf.  # noqa: E501
        :rtype: list[lusid.MarketQuote]
        """
        return self._quotes

    @quotes.setter
    def quotes(self, quotes):
        """Sets the quotes of this YieldCurveDataAllOf.

        The market quotes corresponding to the the instruments used to define the curve  # noqa: E501

        :param quotes: The quotes of this YieldCurveDataAllOf.  # noqa: E501
        :type quotes: list[lusid.MarketQuote]
        """
        if self.local_vars_configuration.client_side_validation and quotes is None:  # noqa: E501
            raise ValueError("Invalid value for `quotes`, must not be `None`")  # noqa: E501

        self._quotes = quotes

    @property
    def lineage(self):
        """Gets the lineage of this YieldCurveDataAllOf.  # noqa: E501

        Description of the complex market data's lineage e.g. 'FundAccountant_GreenQuality'.  # noqa: E501

        :return: The lineage of this YieldCurveDataAllOf.  # noqa: E501
        :rtype: str
        """
        return self._lineage

    @lineage.setter
    def lineage(self, lineage):
        """Sets the lineage of this YieldCurveDataAllOf.

        Description of the complex market data's lineage e.g. 'FundAccountant_GreenQuality'.  # noqa: E501

        :param lineage: The lineage of this YieldCurveDataAllOf.  # noqa: E501
        :type lineage: str
        """
        if (self.local_vars_configuration.client_side_validation and
                lineage is not None and len(lineage) > 1024):
            raise ValueError("Invalid value for `lineage`, length must be less than or equal to `1024`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                lineage is not None and len(lineage) < 0):
            raise ValueError("Invalid value for `lineage`, length must be greater than or equal to `0`")  # noqa: E501

        self._lineage = lineage

    @property
    def market_data_type(self):
        """Gets the market_data_type of this YieldCurveDataAllOf.  # noqa: E501

        The available values are: DiscountFactorCurveData, EquityVolSurfaceData, FxVolSurfaceData, IrVolCubeData, OpaqueMarketData, YieldCurveData, FxForwardCurveData, FxForwardPipsCurveData, FxForwardTenorCurveData, FxForwardTenorPipsCurveData, FxForwardCurveByQuoteReference, CreditSpreadCurveData  # noqa: E501

        :return: The market_data_type of this YieldCurveDataAllOf.  # noqa: E501
        :rtype: str
        """
        return self._market_data_type

    @market_data_type.setter
    def market_data_type(self, market_data_type):
        """Sets the market_data_type of this YieldCurveDataAllOf.

        The available values are: DiscountFactorCurveData, EquityVolSurfaceData, FxVolSurfaceData, IrVolCubeData, OpaqueMarketData, YieldCurveData, FxForwardCurveData, FxForwardPipsCurveData, FxForwardTenorCurveData, FxForwardTenorPipsCurveData, FxForwardCurveByQuoteReference, CreditSpreadCurveData  # noqa: E501

        :param market_data_type: The market_data_type of this YieldCurveDataAllOf.  # noqa: E501
        :type market_data_type: str
        """
        if self.local_vars_configuration.client_side_validation and market_data_type is None:  # noqa: E501
            raise ValueError("Invalid value for `market_data_type`, must not be `None`")  # noqa: E501
        allowed_values = ["DiscountFactorCurveData", "EquityVolSurfaceData", "FxVolSurfaceData", "IrVolCubeData", "OpaqueMarketData", "YieldCurveData", "FxForwardCurveData", "FxForwardPipsCurveData", "FxForwardTenorCurveData", "FxForwardTenorPipsCurveData", "FxForwardCurveByQuoteReference", "CreditSpreadCurveData"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and market_data_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `market_data_type` ({0}), must be one of {1}"  # noqa: E501
                .format(market_data_type, allowed_values)
            )

        self._market_data_type = market_data_type

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
        if not isinstance(other, YieldCurveDataAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, YieldCurveDataAllOf):
            return True

        return self.to_dict() != other.to_dict()
