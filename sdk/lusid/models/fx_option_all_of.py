# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.3558
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


class FxOptionAllOf(object):
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
        'is_delivery_not_cash': 'bool',
        'is_call_not_put': 'bool',
        'strike': 'float',
        'dom_ccy': 'str',
        'fgn_ccy': 'str',
        'premium': 'Premium',
        'instrument_type': 'str'
    }

    attribute_map = {
        'start_date': 'startDate',
        'option_maturity_date': 'optionMaturityDate',
        'option_settlement_date': 'optionSettlementDate',
        'is_delivery_not_cash': 'isDeliveryNotCash',
        'is_call_not_put': 'isCallNotPut',
        'strike': 'strike',
        'dom_ccy': 'domCcy',
        'fgn_ccy': 'fgnCcy',
        'premium': 'premium',
        'instrument_type': 'instrumentType'
    }

    required_map = {
        'start_date': 'required',
        'option_maturity_date': 'required',
        'option_settlement_date': 'required',
        'is_delivery_not_cash': 'required',
        'is_call_not_put': 'required',
        'strike': 'required',
        'dom_ccy': 'required',
        'fgn_ccy': 'required',
        'premium': 'optional',
        'instrument_type': 'required'
    }

    def __init__(self, start_date=None, option_maturity_date=None, option_settlement_date=None, is_delivery_not_cash=None, is_call_not_put=None, strike=None, dom_ccy=None, fgn_ccy=None, premium=None, instrument_type=None, local_vars_configuration=None):  # noqa: E501
        """FxOptionAllOf - a model defined in OpenAPI"
        
        :param start_date:  The start date of the instrument. This is normally synonymous with the trade-date. (required)
        :type start_date: datetime
        :param option_maturity_date:  The maturity date of the option. (required)
        :type option_maturity_date: datetime
        :param option_settlement_date:  The settlement date of the option. (required)
        :type option_settlement_date: datetime
        :param is_delivery_not_cash:  True of the option is settled in cash false if delivery. (required)
        :type is_delivery_not_cash: bool
        :param is_call_not_put:  True if the option is a call, false if the option is a put. (required)
        :type is_call_not_put: bool
        :param strike:  The strike of the option. (required)
        :type strike: float
        :param dom_ccy:  The domestic currency of the instrument. (required)
        :type dom_ccy: str
        :param fgn_ccy:  The foreign currency of the FX. (required)
        :type fgn_ccy: str
        :param premium: 
        :type premium: lusid.Premium
        :param instrument_type:  The available values are: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, CrossCurrencySwap, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity (required)
        :type instrument_type: str

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._start_date = None
        self._option_maturity_date = None
        self._option_settlement_date = None
        self._is_delivery_not_cash = None
        self._is_call_not_put = None
        self._strike = None
        self._dom_ccy = None
        self._fgn_ccy = None
        self._premium = None
        self._instrument_type = None
        self.discriminator = None

        self.start_date = start_date
        self.option_maturity_date = option_maturity_date
        self.option_settlement_date = option_settlement_date
        self.is_delivery_not_cash = is_delivery_not_cash
        self.is_call_not_put = is_call_not_put
        self.strike = strike
        self.dom_ccy = dom_ccy
        self.fgn_ccy = fgn_ccy
        if premium is not None:
            self.premium = premium
        self.instrument_type = instrument_type

    @property
    def start_date(self):
        """Gets the start_date of this FxOptionAllOf.  # noqa: E501

        The start date of the instrument. This is normally synonymous with the trade-date.  # noqa: E501

        :return: The start_date of this FxOptionAllOf.  # noqa: E501
        :rtype: datetime
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this FxOptionAllOf.

        The start date of the instrument. This is normally synonymous with the trade-date.  # noqa: E501

        :param start_date: The start_date of this FxOptionAllOf.  # noqa: E501
        :type start_date: datetime
        """
        if self.local_vars_configuration.client_side_validation and start_date is None:  # noqa: E501
            raise ValueError("Invalid value for `start_date`, must not be `None`")  # noqa: E501

        self._start_date = start_date

    @property
    def option_maturity_date(self):
        """Gets the option_maturity_date of this FxOptionAllOf.  # noqa: E501

        The maturity date of the option.  # noqa: E501

        :return: The option_maturity_date of this FxOptionAllOf.  # noqa: E501
        :rtype: datetime
        """
        return self._option_maturity_date

    @option_maturity_date.setter
    def option_maturity_date(self, option_maturity_date):
        """Sets the option_maturity_date of this FxOptionAllOf.

        The maturity date of the option.  # noqa: E501

        :param option_maturity_date: The option_maturity_date of this FxOptionAllOf.  # noqa: E501
        :type option_maturity_date: datetime
        """
        if self.local_vars_configuration.client_side_validation and option_maturity_date is None:  # noqa: E501
            raise ValueError("Invalid value for `option_maturity_date`, must not be `None`")  # noqa: E501

        self._option_maturity_date = option_maturity_date

    @property
    def option_settlement_date(self):
        """Gets the option_settlement_date of this FxOptionAllOf.  # noqa: E501

        The settlement date of the option.  # noqa: E501

        :return: The option_settlement_date of this FxOptionAllOf.  # noqa: E501
        :rtype: datetime
        """
        return self._option_settlement_date

    @option_settlement_date.setter
    def option_settlement_date(self, option_settlement_date):
        """Sets the option_settlement_date of this FxOptionAllOf.

        The settlement date of the option.  # noqa: E501

        :param option_settlement_date: The option_settlement_date of this FxOptionAllOf.  # noqa: E501
        :type option_settlement_date: datetime
        """
        if self.local_vars_configuration.client_side_validation and option_settlement_date is None:  # noqa: E501
            raise ValueError("Invalid value for `option_settlement_date`, must not be `None`")  # noqa: E501

        self._option_settlement_date = option_settlement_date

    @property
    def is_delivery_not_cash(self):
        """Gets the is_delivery_not_cash of this FxOptionAllOf.  # noqa: E501

        True of the option is settled in cash false if delivery.  # noqa: E501

        :return: The is_delivery_not_cash of this FxOptionAllOf.  # noqa: E501
        :rtype: bool
        """
        return self._is_delivery_not_cash

    @is_delivery_not_cash.setter
    def is_delivery_not_cash(self, is_delivery_not_cash):
        """Sets the is_delivery_not_cash of this FxOptionAllOf.

        True of the option is settled in cash false if delivery.  # noqa: E501

        :param is_delivery_not_cash: The is_delivery_not_cash of this FxOptionAllOf.  # noqa: E501
        :type is_delivery_not_cash: bool
        """
        if self.local_vars_configuration.client_side_validation and is_delivery_not_cash is None:  # noqa: E501
            raise ValueError("Invalid value for `is_delivery_not_cash`, must not be `None`")  # noqa: E501

        self._is_delivery_not_cash = is_delivery_not_cash

    @property
    def is_call_not_put(self):
        """Gets the is_call_not_put of this FxOptionAllOf.  # noqa: E501

        True if the option is a call, false if the option is a put.  # noqa: E501

        :return: The is_call_not_put of this FxOptionAllOf.  # noqa: E501
        :rtype: bool
        """
        return self._is_call_not_put

    @is_call_not_put.setter
    def is_call_not_put(self, is_call_not_put):
        """Sets the is_call_not_put of this FxOptionAllOf.

        True if the option is a call, false if the option is a put.  # noqa: E501

        :param is_call_not_put: The is_call_not_put of this FxOptionAllOf.  # noqa: E501
        :type is_call_not_put: bool
        """
        if self.local_vars_configuration.client_side_validation and is_call_not_put is None:  # noqa: E501
            raise ValueError("Invalid value for `is_call_not_put`, must not be `None`")  # noqa: E501

        self._is_call_not_put = is_call_not_put

    @property
    def strike(self):
        """Gets the strike of this FxOptionAllOf.  # noqa: E501

        The strike of the option.  # noqa: E501

        :return: The strike of this FxOptionAllOf.  # noqa: E501
        :rtype: float
        """
        return self._strike

    @strike.setter
    def strike(self, strike):
        """Sets the strike of this FxOptionAllOf.

        The strike of the option.  # noqa: E501

        :param strike: The strike of this FxOptionAllOf.  # noqa: E501
        :type strike: float
        """
        if self.local_vars_configuration.client_side_validation and strike is None:  # noqa: E501
            raise ValueError("Invalid value for `strike`, must not be `None`")  # noqa: E501

        self._strike = strike

    @property
    def dom_ccy(self):
        """Gets the dom_ccy of this FxOptionAllOf.  # noqa: E501

        The domestic currency of the instrument.  # noqa: E501

        :return: The dom_ccy of this FxOptionAllOf.  # noqa: E501
        :rtype: str
        """
        return self._dom_ccy

    @dom_ccy.setter
    def dom_ccy(self, dom_ccy):
        """Sets the dom_ccy of this FxOptionAllOf.

        The domestic currency of the instrument.  # noqa: E501

        :param dom_ccy: The dom_ccy of this FxOptionAllOf.  # noqa: E501
        :type dom_ccy: str
        """
        if self.local_vars_configuration.client_side_validation and dom_ccy is None:  # noqa: E501
            raise ValueError("Invalid value for `dom_ccy`, must not be `None`")  # noqa: E501

        self._dom_ccy = dom_ccy

    @property
    def fgn_ccy(self):
        """Gets the fgn_ccy of this FxOptionAllOf.  # noqa: E501

        The foreign currency of the FX.  # noqa: E501

        :return: The fgn_ccy of this FxOptionAllOf.  # noqa: E501
        :rtype: str
        """
        return self._fgn_ccy

    @fgn_ccy.setter
    def fgn_ccy(self, fgn_ccy):
        """Sets the fgn_ccy of this FxOptionAllOf.

        The foreign currency of the FX.  # noqa: E501

        :param fgn_ccy: The fgn_ccy of this FxOptionAllOf.  # noqa: E501
        :type fgn_ccy: str
        """
        if self.local_vars_configuration.client_side_validation and fgn_ccy is None:  # noqa: E501
            raise ValueError("Invalid value for `fgn_ccy`, must not be `None`")  # noqa: E501

        self._fgn_ccy = fgn_ccy

    @property
    def premium(self):
        """Gets the premium of this FxOptionAllOf.  # noqa: E501


        :return: The premium of this FxOptionAllOf.  # noqa: E501
        :rtype: lusid.Premium
        """
        return self._premium

    @premium.setter
    def premium(self, premium):
        """Sets the premium of this FxOptionAllOf.


        :param premium: The premium of this FxOptionAllOf.  # noqa: E501
        :type premium: lusid.Premium
        """

        self._premium = premium

    @property
    def instrument_type(self):
        """Gets the instrument_type of this FxOptionAllOf.  # noqa: E501

        The available values are: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, CrossCurrencySwap, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity  # noqa: E501

        :return: The instrument_type of this FxOptionAllOf.  # noqa: E501
        :rtype: str
        """
        return self._instrument_type

    @instrument_type.setter
    def instrument_type(self, instrument_type):
        """Sets the instrument_type of this FxOptionAllOf.

        The available values are: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, CrossCurrencySwap, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity  # noqa: E501

        :param instrument_type: The instrument_type of this FxOptionAllOf.  # noqa: E501
        :type instrument_type: str
        """
        if self.local_vars_configuration.client_side_validation and instrument_type is None:  # noqa: E501
            raise ValueError("Invalid value for `instrument_type`, must not be `None`")  # noqa: E501
        allowed_values = ["QuotedSecurity", "InterestRateSwap", "FxForward", "Future", "ExoticInstrument", "FxOption", "CreditDefaultSwap", "InterestRateSwaption", "Bond", "EquityOption", "FixedLeg", "FloatingLeg", "BespokeCashFlowsLeg", "Unknown", "TermDeposit", "ContractForDifference", "EquitySwap", "CashPerpetual", "CapFloor", "CashSettled", "CdsIndex", "Basket", "FundingLeg", "CrossCurrencySwap", "FxSwap", "ForwardRateAgreement", "SimpleInstrument", "Repo", "Equity"]  # noqa: E501
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
        if not isinstance(other, FxOptionAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FxOptionAllOf):
            return True

        return self.to_dict() != other.to_dict()
