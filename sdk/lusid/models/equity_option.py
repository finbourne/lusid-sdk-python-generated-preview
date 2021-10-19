# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.3625
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


class EquityOption(object):
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
        'start_date': 'datetime',
        'option_maturity_date': 'datetime',
        'option_settlement_date': 'datetime',
        'delivery_type': 'str',
        'option_type': 'str',
        'strike': 'float',
        'dom_ccy': 'str',
        'underlying_identifier': 'str',
        'code': 'str',
        'instrument_type': 'str'
    }

    attribute_map = {
        'start_date': 'startDate',
        'option_maturity_date': 'optionMaturityDate',
        'option_settlement_date': 'optionSettlementDate',
        'delivery_type': 'deliveryType',
        'option_type': 'optionType',
        'strike': 'strike',
        'dom_ccy': 'domCcy',
        'underlying_identifier': 'underlyingIdentifier',
        'code': 'code',
        'instrument_type': 'instrumentType'
    }

    required_map = {
        'start_date': 'required',
        'option_maturity_date': 'required',
        'option_settlement_date': 'required',
        'delivery_type': 'required',
        'option_type': 'required',
        'strike': 'required',
        'dom_ccy': 'required',
        'underlying_identifier': 'required',
        'code': 'required',
        'instrument_type': 'required'
    }

    def __init__(self, start_date=None, option_maturity_date=None, option_settlement_date=None, delivery_type=None, option_type=None, strike=None, dom_ccy=None, underlying_identifier=None, code=None, instrument_type=None, local_vars_configuration=None):  # noqa: E501
        """EquityOption - a model defined in OpenAPI"
        
        :param start_date:  The start date of the instrument. This is normally synonymous with the trade-date. (required)
        :type start_date: datetime
        :param option_maturity_date:  The maturity date of the option. (required)
        :type option_maturity_date: datetime
        :param option_settlement_date:  The settlement date of the option. (required)
        :type option_settlement_date: datetime
        :param delivery_type:  The available values are: Cash, Physical (required)
        :type delivery_type: str
        :param option_type:  The available values are: None, Call, Put (required)
        :type option_type: str
        :param strike:  The strike of the option. (required)
        :type strike: float
        :param dom_ccy:  The domestic currency of the instrument. (required)
        :type dom_ccy: str
        :param underlying_identifier:  The available values are: LusidInstrumentId, Isin, Sedol, Cusip, ClientInternal, Figi, RIC, QuotePermId, REDCode, BBGId, ICECode (required)
        :type underlying_identifier: str
        :param code:  The identifying code for the equity underlying, e.g. 'IBM.N'. (required)
        :type code: str
        :param instrument_type:  The available values are: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, CrossCurrencySwap, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption (required)
        :type instrument_type: str

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._start_date = None
        self._option_maturity_date = None
        self._option_settlement_date = None
        self._delivery_type = None
        self._option_type = None
        self._strike = None
        self._dom_ccy = None
        self._underlying_identifier = None
        self._code = None
        self._instrument_type = None
        self.discriminator = None

        self.start_date = start_date
        self.option_maturity_date = option_maturity_date
        self.option_settlement_date = option_settlement_date
        self.delivery_type = delivery_type
        self.option_type = option_type
        self.strike = strike
        self.dom_ccy = dom_ccy
        self.underlying_identifier = underlying_identifier
        self.code = code
        self.instrument_type = instrument_type

    @property
    def start_date(self):
        """Gets the start_date of this EquityOption.  # noqa: E501

        The start date of the instrument. This is normally synonymous with the trade-date.  # noqa: E501

        :return: The start_date of this EquityOption.  # noqa: E501
        :rtype: datetime
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this EquityOption.

        The start date of the instrument. This is normally synonymous with the trade-date.  # noqa: E501

        :param start_date: The start_date of this EquityOption.  # noqa: E501
        :type start_date: datetime
        """
        if self.local_vars_configuration.client_side_validation and start_date is None:  # noqa: E501
            raise ValueError("Invalid value for `start_date`, must not be `None`")  # noqa: E501

        self._start_date = start_date

    @property
    def option_maturity_date(self):
        """Gets the option_maturity_date of this EquityOption.  # noqa: E501

        The maturity date of the option.  # noqa: E501

        :return: The option_maturity_date of this EquityOption.  # noqa: E501
        :rtype: datetime
        """
        return self._option_maturity_date

    @option_maturity_date.setter
    def option_maturity_date(self, option_maturity_date):
        """Sets the option_maturity_date of this EquityOption.

        The maturity date of the option.  # noqa: E501

        :param option_maturity_date: The option_maturity_date of this EquityOption.  # noqa: E501
        :type option_maturity_date: datetime
        """
        if self.local_vars_configuration.client_side_validation and option_maturity_date is None:  # noqa: E501
            raise ValueError("Invalid value for `option_maturity_date`, must not be `None`")  # noqa: E501

        self._option_maturity_date = option_maturity_date

    @property
    def option_settlement_date(self):
        """Gets the option_settlement_date of this EquityOption.  # noqa: E501

        The settlement date of the option.  # noqa: E501

        :return: The option_settlement_date of this EquityOption.  # noqa: E501
        :rtype: datetime
        """
        return self._option_settlement_date

    @option_settlement_date.setter
    def option_settlement_date(self, option_settlement_date):
        """Sets the option_settlement_date of this EquityOption.

        The settlement date of the option.  # noqa: E501

        :param option_settlement_date: The option_settlement_date of this EquityOption.  # noqa: E501
        :type option_settlement_date: datetime
        """
        if self.local_vars_configuration.client_side_validation and option_settlement_date is None:  # noqa: E501
            raise ValueError("Invalid value for `option_settlement_date`, must not be `None`")  # noqa: E501

        self._option_settlement_date = option_settlement_date

    @property
    def delivery_type(self):
        """Gets the delivery_type of this EquityOption.  # noqa: E501

        The available values are: Cash, Physical  # noqa: E501

        :return: The delivery_type of this EquityOption.  # noqa: E501
        :rtype: str
        """
        return self._delivery_type

    @delivery_type.setter
    def delivery_type(self, delivery_type):
        """Sets the delivery_type of this EquityOption.

        The available values are: Cash, Physical  # noqa: E501

        :param delivery_type: The delivery_type of this EquityOption.  # noqa: E501
        :type delivery_type: str
        """
        if self.local_vars_configuration.client_side_validation and delivery_type is None:  # noqa: E501
            raise ValueError("Invalid value for `delivery_type`, must not be `None`")  # noqa: E501
        allowed_values = ["Cash", "Physical"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and delivery_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `delivery_type` ({0}), must be one of {1}"  # noqa: E501
                .format(delivery_type, allowed_values)
            )

        self._delivery_type = delivery_type

    @property
    def option_type(self):
        """Gets the option_type of this EquityOption.  # noqa: E501

        The available values are: None, Call, Put  # noqa: E501

        :return: The option_type of this EquityOption.  # noqa: E501
        :rtype: str
        """
        return self._option_type

    @option_type.setter
    def option_type(self, option_type):
        """Sets the option_type of this EquityOption.

        The available values are: None, Call, Put  # noqa: E501

        :param option_type: The option_type of this EquityOption.  # noqa: E501
        :type option_type: str
        """
        if self.local_vars_configuration.client_side_validation and option_type is None:  # noqa: E501
            raise ValueError("Invalid value for `option_type`, must not be `None`")  # noqa: E501
        allowed_values = ["None", "Call", "Put"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and option_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `option_type` ({0}), must be one of {1}"  # noqa: E501
                .format(option_type, allowed_values)
            )

        self._option_type = option_type

    @property
    def strike(self):
        """Gets the strike of this EquityOption.  # noqa: E501

        The strike of the option.  # noqa: E501

        :return: The strike of this EquityOption.  # noqa: E501
        :rtype: float
        """
        return self._strike

    @strike.setter
    def strike(self, strike):
        """Sets the strike of this EquityOption.

        The strike of the option.  # noqa: E501

        :param strike: The strike of this EquityOption.  # noqa: E501
        :type strike: float
        """
        if self.local_vars_configuration.client_side_validation and strike is None:  # noqa: E501
            raise ValueError("Invalid value for `strike`, must not be `None`")  # noqa: E501

        self._strike = strike

    @property
    def dom_ccy(self):
        """Gets the dom_ccy of this EquityOption.  # noqa: E501

        The domestic currency of the instrument.  # noqa: E501

        :return: The dom_ccy of this EquityOption.  # noqa: E501
        :rtype: str
        """
        return self._dom_ccy

    @dom_ccy.setter
    def dom_ccy(self, dom_ccy):
        """Sets the dom_ccy of this EquityOption.

        The domestic currency of the instrument.  # noqa: E501

        :param dom_ccy: The dom_ccy of this EquityOption.  # noqa: E501
        :type dom_ccy: str
        """
        if self.local_vars_configuration.client_side_validation and dom_ccy is None:  # noqa: E501
            raise ValueError("Invalid value for `dom_ccy`, must not be `None`")  # noqa: E501

        self._dom_ccy = dom_ccy

    @property
    def underlying_identifier(self):
        """Gets the underlying_identifier of this EquityOption.  # noqa: E501

        The available values are: LusidInstrumentId, Isin, Sedol, Cusip, ClientInternal, Figi, RIC, QuotePermId, REDCode, BBGId, ICECode  # noqa: E501

        :return: The underlying_identifier of this EquityOption.  # noqa: E501
        :rtype: str
        """
        return self._underlying_identifier

    @underlying_identifier.setter
    def underlying_identifier(self, underlying_identifier):
        """Sets the underlying_identifier of this EquityOption.

        The available values are: LusidInstrumentId, Isin, Sedol, Cusip, ClientInternal, Figi, RIC, QuotePermId, REDCode, BBGId, ICECode  # noqa: E501

        :param underlying_identifier: The underlying_identifier of this EquityOption.  # noqa: E501
        :type underlying_identifier: str
        """
        if self.local_vars_configuration.client_side_validation and underlying_identifier is None:  # noqa: E501
            raise ValueError("Invalid value for `underlying_identifier`, must not be `None`")  # noqa: E501
        allowed_values = ["LusidInstrumentId", "Isin", "Sedol", "Cusip", "ClientInternal", "Figi", "RIC", "QuotePermId", "REDCode", "BBGId", "ICECode"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and underlying_identifier not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `underlying_identifier` ({0}), must be one of {1}"  # noqa: E501
                .format(underlying_identifier, allowed_values)
            )

        self._underlying_identifier = underlying_identifier

    @property
    def code(self):
        """Gets the code of this EquityOption.  # noqa: E501

        The identifying code for the equity underlying, e.g. 'IBM.N'.  # noqa: E501

        :return: The code of this EquityOption.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this EquityOption.

        The identifying code for the equity underlying, e.g. 'IBM.N'.  # noqa: E501

        :param code: The code of this EquityOption.  # noqa: E501
        :type code: str
        """
        if self.local_vars_configuration.client_side_validation and code is None:  # noqa: E501
            raise ValueError("Invalid value for `code`, must not be `None`")  # noqa: E501

        self._code = code

    @property
    def instrument_type(self):
        """Gets the instrument_type of this EquityOption.  # noqa: E501

        The available values are: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, CrossCurrencySwap, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption  # noqa: E501

        :return: The instrument_type of this EquityOption.  # noqa: E501
        :rtype: str
        """
        return self._instrument_type

    @instrument_type.setter
    def instrument_type(self, instrument_type):
        """Sets the instrument_type of this EquityOption.

        The available values are: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, CrossCurrencySwap, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption  # noqa: E501

        :param instrument_type: The instrument_type of this EquityOption.  # noqa: E501
        :type instrument_type: str
        """
        if self.local_vars_configuration.client_side_validation and instrument_type is None:  # noqa: E501
            raise ValueError("Invalid value for `instrument_type`, must not be `None`")  # noqa: E501
        allowed_values = ["QuotedSecurity", "InterestRateSwap", "FxForward", "Future", "ExoticInstrument", "FxOption", "CreditDefaultSwap", "InterestRateSwaption", "Bond", "EquityOption", "FixedLeg", "FloatingLeg", "BespokeCashFlowsLeg", "Unknown", "TermDeposit", "ContractForDifference", "EquitySwap", "CashPerpetual", "CapFloor", "CashSettled", "CdsIndex", "Basket", "FundingLeg", "CrossCurrencySwap", "FxSwap", "ForwardRateAgreement", "SimpleInstrument", "Repo", "Equity", "ExchangeTradedOption"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and instrument_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `instrument_type` ({0}), must be one of {1}"  # noqa: E501
                .format(instrument_type, allowed_values)
            )

        self._instrument_type = instrument_type

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
        if not isinstance(other, EquityOption):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EquityOption):
            return True

        return self.to_dict() != other.to_dict()
