# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.3575
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


class RepoAllOf(object):
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
        'dom_ccy': 'str',
        'accrual_basis': 'str',
        'collateral': 'list[Instrument]',
        'collateral_value': 'float',
        'haircut': 'float',
        'margin': 'float',
        'purchase_price': 'float',
        'repo_rate': 'float',
        'repurchase_price': 'float',
        'instrument_type': 'str'
    }

    attribute_map = {
        'start_date': 'startDate',
        'maturity_date': 'maturityDate',
        'dom_ccy': 'domCcy',
        'accrual_basis': 'accrualBasis',
        'collateral': 'collateral',
        'collateral_value': 'collateralValue',
        'haircut': 'haircut',
        'margin': 'margin',
        'purchase_price': 'purchasePrice',
        'repo_rate': 'repoRate',
        'repurchase_price': 'repurchasePrice',
        'instrument_type': 'instrumentType'
    }

    required_map = {
        'start_date': 'required',
        'maturity_date': 'required',
        'dom_ccy': 'required',
        'accrual_basis': 'required',
        'collateral': 'optional',
        'collateral_value': 'optional',
        'haircut': 'optional',
        'margin': 'optional',
        'purchase_price': 'optional',
        'repo_rate': 'optional',
        'repurchase_price': 'optional',
        'instrument_type': 'required'
    }

    def __init__(self, start_date=None, maturity_date=None, dom_ccy=None, accrual_basis=None, collateral=None, collateral_value=None, haircut=None, margin=None, purchase_price=None, repo_rate=None, repurchase_price=None, instrument_type=None, local_vars_configuration=None):  # noqa: E501
        """RepoAllOf - a model defined in OpenAPI"
        
        :param start_date:  The start date of the instrument. This is normally synonymous with the trade-date. (required)
        :type start_date: datetime
        :param maturity_date:  The final maturity date of the instrument. This means the last date on which the instruments makes a payment of any amount.  For the avoidance of doubt, that is not necessarily prior to its last sensitivity date for the purposes of risk; e.g. instruments such as  Constant Maturity Swaps (CMS) often have sensitivities to rates beyond their last payment date (required)
        :type maturity_date: datetime
        :param dom_ccy:  The domestic currency of the instrument. (required)
        :type dom_ccy: str
        :param accrual_basis:  For calculation of interest, the accrual basis to be used.  Supported string (enumeration) values are: [Actual360, Act360, MoneyMarket, Actual365, Act365, Thirty360, ThirtyU360, Bond, ThirtyE360, EuroBond, ActualActual, ActAct, ActActIsda, ActActIsma, ActActIcma, OneOne, Act364, Act365F, Act365L, Act365_25, Act252, Bus252, NL360, NL365, ActActAFB, Act365Cad, ThirtyActIsda, Thirty365Isda, ThirtyEActIsda, ThirtyE360Isda, ThirtyE365Isda, ThirtyU360EOM]. (required)
        :type accrual_basis: str
        :param collateral:  The actual collateral in the Repo.  This property is for informational purposes only, Lusid pricing is not affected.
        :type collateral: list[lusid.Instrument]
        :param collateral_value:  The full market value of the collateral in domestic currency, before any margin or haircut is applied.
        :type collateral_value: float
        :param haircut:  The haircut (or margin percentage) applied to the collateral, this should be a number between 0 and 1, i.e. for a 5% haircut this should be 0.05.  This is defined as (CollateralValue - PurchasePrice) / CollateralValue.  If this property is specified, so too must CollateralValue.  While this property is optional, one, and only one, of PurchasePrice, Margin and Haircut must be specified.
        :type haircut: float
        :param margin:  The initial margin (or margin ratio) applied to the collateral, this should be a number greater than or equal to 1.0,  i.e. for a 102% margin this should be 1.02. A value of 1.0 means no margin (100%).  This is defined as CollateralValue / PurchasePrice.  If this property is specified, so too must CollateralValue.  While this property is optional, one, and only one, of PurchasePrice, Margin and Haircut must be specified.
        :type margin: float
        :param purchase_price:  The price the collateral is initially purchased for, this property can be used to explicitly set the purchase price and not require  collateral value and a margin or haircut.  While this property is optional, one, and only one, of PurchasePrice, Margin and Haircut must be specified.
        :type purchase_price: float
        :param repo_rate:  the rate at which interest is to be accrue and be paid upon redemption of the collateral at maturity.  This field is used to calculate the Repurchase price.  While this property is optional, one, and only one, of the RepoRate and RepurchasePrice must be specified.
        :type repo_rate: float
        :param repurchase_price:  The price at which the collateral is repurchased, this field is optional and can be explicitly set here or will be calculated  from the PurchasePrice and RepoRate.  One, and only one, of the RepoRate and RepurchasePrice must be specified.
        :type repurchase_price: float
        :param instrument_type:  The available values are: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, CrossCurrencySwap, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity (required)
        :type instrument_type: str

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._start_date = None
        self._maturity_date = None
        self._dom_ccy = None
        self._accrual_basis = None
        self._collateral = None
        self._collateral_value = None
        self._haircut = None
        self._margin = None
        self._purchase_price = None
        self._repo_rate = None
        self._repurchase_price = None
        self._instrument_type = None
        self.discriminator = None

        self.start_date = start_date
        self.maturity_date = maturity_date
        self.dom_ccy = dom_ccy
        self.accrual_basis = accrual_basis
        self.collateral = collateral
        self.collateral_value = collateral_value
        self.haircut = haircut
        self.margin = margin
        self.purchase_price = purchase_price
        self.repo_rate = repo_rate
        self.repurchase_price = repurchase_price
        self.instrument_type = instrument_type

    @property
    def start_date(self):
        """Gets the start_date of this RepoAllOf.  # noqa: E501

        The start date of the instrument. This is normally synonymous with the trade-date.  # noqa: E501

        :return: The start_date of this RepoAllOf.  # noqa: E501
        :rtype: datetime
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this RepoAllOf.

        The start date of the instrument. This is normally synonymous with the trade-date.  # noqa: E501

        :param start_date: The start_date of this RepoAllOf.  # noqa: E501
        :type start_date: datetime
        """
        if self.local_vars_configuration.client_side_validation and start_date is None:  # noqa: E501
            raise ValueError("Invalid value for `start_date`, must not be `None`")  # noqa: E501

        self._start_date = start_date

    @property
    def maturity_date(self):
        """Gets the maturity_date of this RepoAllOf.  # noqa: E501

        The final maturity date of the instrument. This means the last date on which the instruments makes a payment of any amount.  For the avoidance of doubt, that is not necessarily prior to its last sensitivity date for the purposes of risk; e.g. instruments such as  Constant Maturity Swaps (CMS) often have sensitivities to rates beyond their last payment date  # noqa: E501

        :return: The maturity_date of this RepoAllOf.  # noqa: E501
        :rtype: datetime
        """
        return self._maturity_date

    @maturity_date.setter
    def maturity_date(self, maturity_date):
        """Sets the maturity_date of this RepoAllOf.

        The final maturity date of the instrument. This means the last date on which the instruments makes a payment of any amount.  For the avoidance of doubt, that is not necessarily prior to its last sensitivity date for the purposes of risk; e.g. instruments such as  Constant Maturity Swaps (CMS) often have sensitivities to rates beyond their last payment date  # noqa: E501

        :param maturity_date: The maturity_date of this RepoAllOf.  # noqa: E501
        :type maturity_date: datetime
        """
        if self.local_vars_configuration.client_side_validation and maturity_date is None:  # noqa: E501
            raise ValueError("Invalid value for `maturity_date`, must not be `None`")  # noqa: E501

        self._maturity_date = maturity_date

    @property
    def dom_ccy(self):
        """Gets the dom_ccy of this RepoAllOf.  # noqa: E501

        The domestic currency of the instrument.  # noqa: E501

        :return: The dom_ccy of this RepoAllOf.  # noqa: E501
        :rtype: str
        """
        return self._dom_ccy

    @dom_ccy.setter
    def dom_ccy(self, dom_ccy):
        """Sets the dom_ccy of this RepoAllOf.

        The domestic currency of the instrument.  # noqa: E501

        :param dom_ccy: The dom_ccy of this RepoAllOf.  # noqa: E501
        :type dom_ccy: str
        """
        if self.local_vars_configuration.client_side_validation and dom_ccy is None:  # noqa: E501
            raise ValueError("Invalid value for `dom_ccy`, must not be `None`")  # noqa: E501

        self._dom_ccy = dom_ccy

    @property
    def accrual_basis(self):
        """Gets the accrual_basis of this RepoAllOf.  # noqa: E501

        For calculation of interest, the accrual basis to be used.  Supported string (enumeration) values are: [Actual360, Act360, MoneyMarket, Actual365, Act365, Thirty360, ThirtyU360, Bond, ThirtyE360, EuroBond, ActualActual, ActAct, ActActIsda, ActActIsma, ActActIcma, OneOne, Act364, Act365F, Act365L, Act365_25, Act252, Bus252, NL360, NL365, ActActAFB, Act365Cad, ThirtyActIsda, Thirty365Isda, ThirtyEActIsda, ThirtyE360Isda, ThirtyE365Isda, ThirtyU360EOM].  # noqa: E501

        :return: The accrual_basis of this RepoAllOf.  # noqa: E501
        :rtype: str
        """
        return self._accrual_basis

    @accrual_basis.setter
    def accrual_basis(self, accrual_basis):
        """Sets the accrual_basis of this RepoAllOf.

        For calculation of interest, the accrual basis to be used.  Supported string (enumeration) values are: [Actual360, Act360, MoneyMarket, Actual365, Act365, Thirty360, ThirtyU360, Bond, ThirtyE360, EuroBond, ActualActual, ActAct, ActActIsda, ActActIsma, ActActIcma, OneOne, Act364, Act365F, Act365L, Act365_25, Act252, Bus252, NL360, NL365, ActActAFB, Act365Cad, ThirtyActIsda, Thirty365Isda, ThirtyEActIsda, ThirtyE360Isda, ThirtyE365Isda, ThirtyU360EOM].  # noqa: E501

        :param accrual_basis: The accrual_basis of this RepoAllOf.  # noqa: E501
        :type accrual_basis: str
        """
        if self.local_vars_configuration.client_side_validation and accrual_basis is None:  # noqa: E501
            raise ValueError("Invalid value for `accrual_basis`, must not be `None`")  # noqa: E501

        self._accrual_basis = accrual_basis

    @property
    def collateral(self):
        """Gets the collateral of this RepoAllOf.  # noqa: E501

        The actual collateral in the Repo.  This property is for informational purposes only, Lusid pricing is not affected.  # noqa: E501

        :return: The collateral of this RepoAllOf.  # noqa: E501
        :rtype: list[lusid.Instrument]
        """
        return self._collateral

    @collateral.setter
    def collateral(self, collateral):
        """Sets the collateral of this RepoAllOf.

        The actual collateral in the Repo.  This property is for informational purposes only, Lusid pricing is not affected.  # noqa: E501

        :param collateral: The collateral of this RepoAllOf.  # noqa: E501
        :type collateral: list[lusid.Instrument]
        """

        self._collateral = collateral

    @property
    def collateral_value(self):
        """Gets the collateral_value of this RepoAllOf.  # noqa: E501

        The full market value of the collateral in domestic currency, before any margin or haircut is applied.  # noqa: E501

        :return: The collateral_value of this RepoAllOf.  # noqa: E501
        :rtype: float
        """
        return self._collateral_value

    @collateral_value.setter
    def collateral_value(self, collateral_value):
        """Sets the collateral_value of this RepoAllOf.

        The full market value of the collateral in domestic currency, before any margin or haircut is applied.  # noqa: E501

        :param collateral_value: The collateral_value of this RepoAllOf.  # noqa: E501
        :type collateral_value: float
        """

        self._collateral_value = collateral_value

    @property
    def haircut(self):
        """Gets the haircut of this RepoAllOf.  # noqa: E501

        The haircut (or margin percentage) applied to the collateral, this should be a number between 0 and 1, i.e. for a 5% haircut this should be 0.05.  This is defined as (CollateralValue - PurchasePrice) / CollateralValue.  If this property is specified, so too must CollateralValue.  While this property is optional, one, and only one, of PurchasePrice, Margin and Haircut must be specified.  # noqa: E501

        :return: The haircut of this RepoAllOf.  # noqa: E501
        :rtype: float
        """
        return self._haircut

    @haircut.setter
    def haircut(self, haircut):
        """Sets the haircut of this RepoAllOf.

        The haircut (or margin percentage) applied to the collateral, this should be a number between 0 and 1, i.e. for a 5% haircut this should be 0.05.  This is defined as (CollateralValue - PurchasePrice) / CollateralValue.  If this property is specified, so too must CollateralValue.  While this property is optional, one, and only one, of PurchasePrice, Margin and Haircut must be specified.  # noqa: E501

        :param haircut: The haircut of this RepoAllOf.  # noqa: E501
        :type haircut: float
        """

        self._haircut = haircut

    @property
    def margin(self):
        """Gets the margin of this RepoAllOf.  # noqa: E501

        The initial margin (or margin ratio) applied to the collateral, this should be a number greater than or equal to 1.0,  i.e. for a 102% margin this should be 1.02. A value of 1.0 means no margin (100%).  This is defined as CollateralValue / PurchasePrice.  If this property is specified, so too must CollateralValue.  While this property is optional, one, and only one, of PurchasePrice, Margin and Haircut must be specified.  # noqa: E501

        :return: The margin of this RepoAllOf.  # noqa: E501
        :rtype: float
        """
        return self._margin

    @margin.setter
    def margin(self, margin):
        """Sets the margin of this RepoAllOf.

        The initial margin (or margin ratio) applied to the collateral, this should be a number greater than or equal to 1.0,  i.e. for a 102% margin this should be 1.02. A value of 1.0 means no margin (100%).  This is defined as CollateralValue / PurchasePrice.  If this property is specified, so too must CollateralValue.  While this property is optional, one, and only one, of PurchasePrice, Margin and Haircut must be specified.  # noqa: E501

        :param margin: The margin of this RepoAllOf.  # noqa: E501
        :type margin: float
        """

        self._margin = margin

    @property
    def purchase_price(self):
        """Gets the purchase_price of this RepoAllOf.  # noqa: E501

        The price the collateral is initially purchased for, this property can be used to explicitly set the purchase price and not require  collateral value and a margin or haircut.  While this property is optional, one, and only one, of PurchasePrice, Margin and Haircut must be specified.  # noqa: E501

        :return: The purchase_price of this RepoAllOf.  # noqa: E501
        :rtype: float
        """
        return self._purchase_price

    @purchase_price.setter
    def purchase_price(self, purchase_price):
        """Sets the purchase_price of this RepoAllOf.

        The price the collateral is initially purchased for, this property can be used to explicitly set the purchase price and not require  collateral value and a margin or haircut.  While this property is optional, one, and only one, of PurchasePrice, Margin and Haircut must be specified.  # noqa: E501

        :param purchase_price: The purchase_price of this RepoAllOf.  # noqa: E501
        :type purchase_price: float
        """

        self._purchase_price = purchase_price

    @property
    def repo_rate(self):
        """Gets the repo_rate of this RepoAllOf.  # noqa: E501

        the rate at which interest is to be accrue and be paid upon redemption of the collateral at maturity.  This field is used to calculate the Repurchase price.  While this property is optional, one, and only one, of the RepoRate and RepurchasePrice must be specified.  # noqa: E501

        :return: The repo_rate of this RepoAllOf.  # noqa: E501
        :rtype: float
        """
        return self._repo_rate

    @repo_rate.setter
    def repo_rate(self, repo_rate):
        """Sets the repo_rate of this RepoAllOf.

        the rate at which interest is to be accrue and be paid upon redemption of the collateral at maturity.  This field is used to calculate the Repurchase price.  While this property is optional, one, and only one, of the RepoRate and RepurchasePrice must be specified.  # noqa: E501

        :param repo_rate: The repo_rate of this RepoAllOf.  # noqa: E501
        :type repo_rate: float
        """

        self._repo_rate = repo_rate

    @property
    def repurchase_price(self):
        """Gets the repurchase_price of this RepoAllOf.  # noqa: E501

        The price at which the collateral is repurchased, this field is optional and can be explicitly set here or will be calculated  from the PurchasePrice and RepoRate.  One, and only one, of the RepoRate and RepurchasePrice must be specified.  # noqa: E501

        :return: The repurchase_price of this RepoAllOf.  # noqa: E501
        :rtype: float
        """
        return self._repurchase_price

    @repurchase_price.setter
    def repurchase_price(self, repurchase_price):
        """Sets the repurchase_price of this RepoAllOf.

        The price at which the collateral is repurchased, this field is optional and can be explicitly set here or will be calculated  from the PurchasePrice and RepoRate.  One, and only one, of the RepoRate and RepurchasePrice must be specified.  # noqa: E501

        :param repurchase_price: The repurchase_price of this RepoAllOf.  # noqa: E501
        :type repurchase_price: float
        """

        self._repurchase_price = repurchase_price

    @property
    def instrument_type(self):
        """Gets the instrument_type of this RepoAllOf.  # noqa: E501

        The available values are: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, CrossCurrencySwap, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity  # noqa: E501

        :return: The instrument_type of this RepoAllOf.  # noqa: E501
        :rtype: str
        """
        return self._instrument_type

    @instrument_type.setter
    def instrument_type(self, instrument_type):
        """Sets the instrument_type of this RepoAllOf.

        The available values are: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, CrossCurrencySwap, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity  # noqa: E501

        :param instrument_type: The instrument_type of this RepoAllOf.  # noqa: E501
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
        if not isinstance(other, RepoAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RepoAllOf):
            return True

        return self.to_dict() != other.to_dict()