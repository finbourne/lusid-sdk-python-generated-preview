# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.4043
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


class CdsIndexAllOf(object):
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
        'maturity_date': 'datetime',
        'flow_conventions': 'CdsFlowConventions',
        'coupon_rate': 'float',
        'identifiers': 'dict(str, str)',
        'basket': 'Basket',
        'convention_name': 'FlowConventionName',
        'notional': 'float',
        'instrument_type': 'str'
    }

    attribute_map = {
        'start_date': 'startDate',
        'maturity_date': 'maturityDate',
        'flow_conventions': 'flowConventions',
        'coupon_rate': 'couponRate',
        'identifiers': 'identifiers',
        'basket': 'basket',
        'convention_name': 'conventionName',
        'notional': 'notional',
        'instrument_type': 'instrumentType'
    }

    required_map = {
        'start_date': 'required',
        'maturity_date': 'required',
        'flow_conventions': 'optional',
        'coupon_rate': 'required',
        'identifiers': 'required',
        'basket': 'required',
        'convention_name': 'optional',
        'notional': 'required',
        'instrument_type': 'required'
    }

    def __init__(self, start_date=None, maturity_date=None, flow_conventions=None, coupon_rate=None, identifiers=None, basket=None, convention_name=None, notional=None, instrument_type=None, local_vars_configuration=None):  # noqa: E501
        """CdsIndexAllOf - a model defined in OpenAPI"
        
        :param start_date:  The start date of the instrument. This is normally synonymous with the trade-date. (required)
        :type start_date: datetime
        :param maturity_date:  The final maturity date of the instrument. This means the last date on which the instruments makes a payment of any amount.  For the avoidance of doubt, that is not necessarily prior to its last sensitivity date for the purposes of risk; e.g. instruments such as  Constant Maturity Swaps (CMS) often have sensitivities to rates beyond their last payment date. (required)
        :type maturity_date: datetime
        :param flow_conventions: 
        :type flow_conventions: lusid.CdsFlowConventions
        :param coupon_rate:  The coupon rate paid on each payment date of the premium leg as a fraction of 100 percent, e.g. \"0.05\" meaning 500 basis points or 5%.  For a standard corporate CDS (North American) this must be either 100bps or 500bps. (required)
        :type coupon_rate: float
        :param identifiers:  external market codes and identifiers for the cds index, e.g. a RED code, BBG ID or ICE code. (required)
        :type identifiers: dict(str, str)
        :param basket:  (required)
        :type basket: lusid.Basket
        :param convention_name: 
        :type convention_name: lusid.FlowConventionName
        :param notional:  The notional quantity that applies to both the premium and protection legs. (required)
        :type notional: float
        :param instrument_type:  The available values are: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption (required)
        :type instrument_type: str

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._start_date = None
        self._maturity_date = None
        self._flow_conventions = None
        self._coupon_rate = None
        self._identifiers = None
        self._basket = None
        self._convention_name = None
        self._notional = None
        self._instrument_type = None
        self.discriminator = None

        self.start_date = start_date
        self.maturity_date = maturity_date
        if flow_conventions is not None:
            self.flow_conventions = flow_conventions
        self.coupon_rate = coupon_rate
        self.identifiers = identifiers
        self.basket = basket
        if convention_name is not None:
            self.convention_name = convention_name
        self.notional = notional
        self.instrument_type = instrument_type

    @property
    def start_date(self):
        """Gets the start_date of this CdsIndexAllOf.  # noqa: E501

        The start date of the instrument. This is normally synonymous with the trade-date.  # noqa: E501

        :return: The start_date of this CdsIndexAllOf.  # noqa: E501
        :rtype: datetime
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this CdsIndexAllOf.

        The start date of the instrument. This is normally synonymous with the trade-date.  # noqa: E501

        :param start_date: The start_date of this CdsIndexAllOf.  # noqa: E501
        :type start_date: datetime
        """
        if self.local_vars_configuration.client_side_validation and start_date is None:  # noqa: E501
            raise ValueError("Invalid value for `start_date`, must not be `None`")  # noqa: E501

        self._start_date = start_date

    @property
    def maturity_date(self):
        """Gets the maturity_date of this CdsIndexAllOf.  # noqa: E501

        The final maturity date of the instrument. This means the last date on which the instruments makes a payment of any amount.  For the avoidance of doubt, that is not necessarily prior to its last sensitivity date for the purposes of risk; e.g. instruments such as  Constant Maturity Swaps (CMS) often have sensitivities to rates beyond their last payment date.  # noqa: E501

        :return: The maturity_date of this CdsIndexAllOf.  # noqa: E501
        :rtype: datetime
        """
        return self._maturity_date

    @maturity_date.setter
    def maturity_date(self, maturity_date):
        """Sets the maturity_date of this CdsIndexAllOf.

        The final maturity date of the instrument. This means the last date on which the instruments makes a payment of any amount.  For the avoidance of doubt, that is not necessarily prior to its last sensitivity date for the purposes of risk; e.g. instruments such as  Constant Maturity Swaps (CMS) often have sensitivities to rates beyond their last payment date.  # noqa: E501

        :param maturity_date: The maturity_date of this CdsIndexAllOf.  # noqa: E501
        :type maturity_date: datetime
        """
        if self.local_vars_configuration.client_side_validation and maturity_date is None:  # noqa: E501
            raise ValueError("Invalid value for `maturity_date`, must not be `None`")  # noqa: E501

        self._maturity_date = maturity_date

    @property
    def flow_conventions(self):
        """Gets the flow_conventions of this CdsIndexAllOf.  # noqa: E501


        :return: The flow_conventions of this CdsIndexAllOf.  # noqa: E501
        :rtype: lusid.CdsFlowConventions
        """
        return self._flow_conventions

    @flow_conventions.setter
    def flow_conventions(self, flow_conventions):
        """Sets the flow_conventions of this CdsIndexAllOf.


        :param flow_conventions: The flow_conventions of this CdsIndexAllOf.  # noqa: E501
        :type flow_conventions: lusid.CdsFlowConventions
        """

        self._flow_conventions = flow_conventions

    @property
    def coupon_rate(self):
        """Gets the coupon_rate of this CdsIndexAllOf.  # noqa: E501

        The coupon rate paid on each payment date of the premium leg as a fraction of 100 percent, e.g. \"0.05\" meaning 500 basis points or 5%.  For a standard corporate CDS (North American) this must be either 100bps or 500bps.  # noqa: E501

        :return: The coupon_rate of this CdsIndexAllOf.  # noqa: E501
        :rtype: float
        """
        return self._coupon_rate

    @coupon_rate.setter
    def coupon_rate(self, coupon_rate):
        """Sets the coupon_rate of this CdsIndexAllOf.

        The coupon rate paid on each payment date of the premium leg as a fraction of 100 percent, e.g. \"0.05\" meaning 500 basis points or 5%.  For a standard corporate CDS (North American) this must be either 100bps or 500bps.  # noqa: E501

        :param coupon_rate: The coupon_rate of this CdsIndexAllOf.  # noqa: E501
        :type coupon_rate: float
        """
        if self.local_vars_configuration.client_side_validation and coupon_rate is None:  # noqa: E501
            raise ValueError("Invalid value for `coupon_rate`, must not be `None`")  # noqa: E501

        self._coupon_rate = coupon_rate

    @property
    def identifiers(self):
        """Gets the identifiers of this CdsIndexAllOf.  # noqa: E501

        external market codes and identifiers for the cds index, e.g. a RED code, BBG ID or ICE code.  # noqa: E501

        :return: The identifiers of this CdsIndexAllOf.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._identifiers

    @identifiers.setter
    def identifiers(self, identifiers):
        """Sets the identifiers of this CdsIndexAllOf.

        external market codes and identifiers for the cds index, e.g. a RED code, BBG ID or ICE code.  # noqa: E501

        :param identifiers: The identifiers of this CdsIndexAllOf.  # noqa: E501
        :type identifiers: dict(str, str)
        """
        if self.local_vars_configuration.client_side_validation and identifiers is None:  # noqa: E501
            raise ValueError("Invalid value for `identifiers`, must not be `None`")  # noqa: E501

        self._identifiers = identifiers

    @property
    def basket(self):
        """Gets the basket of this CdsIndexAllOf.  # noqa: E501


        :return: The basket of this CdsIndexAllOf.  # noqa: E501
        :rtype: lusid.Basket
        """
        return self._basket

    @basket.setter
    def basket(self, basket):
        """Sets the basket of this CdsIndexAllOf.


        :param basket: The basket of this CdsIndexAllOf.  # noqa: E501
        :type basket: lusid.Basket
        """
        if self.local_vars_configuration.client_side_validation and basket is None:  # noqa: E501
            raise ValueError("Invalid value for `basket`, must not be `None`")  # noqa: E501

        self._basket = basket

    @property
    def convention_name(self):
        """Gets the convention_name of this CdsIndexAllOf.  # noqa: E501


        :return: The convention_name of this CdsIndexAllOf.  # noqa: E501
        :rtype: lusid.FlowConventionName
        """
        return self._convention_name

    @convention_name.setter
    def convention_name(self, convention_name):
        """Sets the convention_name of this CdsIndexAllOf.


        :param convention_name: The convention_name of this CdsIndexAllOf.  # noqa: E501
        :type convention_name: lusid.FlowConventionName
        """

        self._convention_name = convention_name

    @property
    def notional(self):
        """Gets the notional of this CdsIndexAllOf.  # noqa: E501

        The notional quantity that applies to both the premium and protection legs.  # noqa: E501

        :return: The notional of this CdsIndexAllOf.  # noqa: E501
        :rtype: float
        """
        return self._notional

    @notional.setter
    def notional(self, notional):
        """Sets the notional of this CdsIndexAllOf.

        The notional quantity that applies to both the premium and protection legs.  # noqa: E501

        :param notional: The notional of this CdsIndexAllOf.  # noqa: E501
        :type notional: float
        """
        if self.local_vars_configuration.client_side_validation and notional is None:  # noqa: E501
            raise ValueError("Invalid value for `notional`, must not be `None`")  # noqa: E501

        self._notional = notional

    @property
    def instrument_type(self):
        """Gets the instrument_type of this CdsIndexAllOf.  # noqa: E501

        The available values are: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption  # noqa: E501

        :return: The instrument_type of this CdsIndexAllOf.  # noqa: E501
        :rtype: str
        """
        return self._instrument_type

    @instrument_type.setter
    def instrument_type(self, instrument_type):
        """Sets the instrument_type of this CdsIndexAllOf.

        The available values are: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption  # noqa: E501

        :param instrument_type: The instrument_type of this CdsIndexAllOf.  # noqa: E501
        :type instrument_type: str
        """
        if self.local_vars_configuration.client_side_validation and instrument_type is None:  # noqa: E501
            raise ValueError("Invalid value for `instrument_type`, must not be `None`")  # noqa: E501
        allowed_values = ["QuotedSecurity", "InterestRateSwap", "FxForward", "Future", "ExoticInstrument", "FxOption", "CreditDefaultSwap", "InterestRateSwaption", "Bond", "EquityOption", "FixedLeg", "FloatingLeg", "BespokeCashFlowsLeg", "Unknown", "TermDeposit", "ContractForDifference", "EquitySwap", "CashPerpetual", "CapFloor", "CashSettled", "CdsIndex", "Basket", "FundingLeg", "FxSwap", "ForwardRateAgreement", "SimpleInstrument", "Repo", "Equity", "ExchangeTradedOption"]  # noqa: E501
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
        if not isinstance(other, CdsIndexAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CdsIndexAllOf):
            return True

        return self.to_dict() != other.to_dict()
