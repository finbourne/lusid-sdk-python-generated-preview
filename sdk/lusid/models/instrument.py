# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.4127
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


class Instrument(object):
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
        'href': 'str',
        'scope': 'str',
        'lusid_instrument_id': 'str',
        'version': 'Version',
        'name': 'str',
        'identifiers': 'dict(str, str)',
        'properties': 'list[ModelProperty]',
        'lookthrough_portfolio': 'ResourceId',
        'instrument_definition': 'LusidInstrument',
        'state': 'str',
        'asset_class': 'str',
        'dom_ccy': 'str',
        'links': 'list[Link]'
    }

    attribute_map = {
        'href': 'href',
        'scope': 'scope',
        'lusid_instrument_id': 'lusidInstrumentId',
        'version': 'version',
        'name': 'name',
        'identifiers': 'identifiers',
        'properties': 'properties',
        'lookthrough_portfolio': 'lookthroughPortfolio',
        'instrument_definition': 'instrumentDefinition',
        'state': 'state',
        'asset_class': 'assetClass',
        'dom_ccy': 'domCcy',
        'links': 'links'
    }

    required_map = {
        'href': 'optional',
        'scope': 'optional',
        'lusid_instrument_id': 'required',
        'version': 'required',
        'name': 'required',
        'identifiers': 'required',
        'properties': 'optional',
        'lookthrough_portfolio': 'optional',
        'instrument_definition': 'optional',
        'state': 'required',
        'asset_class': 'optional',
        'dom_ccy': 'optional',
        'links': 'optional'
    }

    def __init__(self, href=None, scope=None, lusid_instrument_id=None, version=None, name=None, identifiers=None, properties=None, lookthrough_portfolio=None, instrument_definition=None, state=None, asset_class=None, dom_ccy=None, links=None, local_vars_configuration=None):  # noqa: E501
        """Instrument - a model defined in OpenAPI"
        
        :param href:  The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.
        :type href: str
        :param scope:  The scope in which the instrument lies.
        :type scope: str
        :param lusid_instrument_id:  The unique LUSID Instrument Identifier (LUID) of the instrument. (required)
        :type lusid_instrument_id: str
        :param version:  (required)
        :type version: lusid.Version
        :param name:  The name of the instrument. (required)
        :type name: str
        :param identifiers:  The set of identifiers that can be used to identify the instrument. (required)
        :type identifiers: dict(str, str)
        :param properties:  The requested instrument properties. These will be from the 'Instrument' domain.
        :type properties: list[lusid.ModelProperty]
        :param lookthrough_portfolio: 
        :type lookthrough_portfolio: lusid.ResourceId
        :param instrument_definition: 
        :type instrument_definition: lusid.LusidInstrument
        :param state:  The state of of the instrument at the asAt datetime of this version of the instrument definition. The available values are: Active, Inactive (required)
        :type state: str
        :param asset_class:  The nominal asset class of the instrument, e.g. InterestRates, FX, Inflation, Equities, Credit, Commodities, etc. The available values are: InterestRates, FX, Inflation, Equities, Credit, Commodities, Money, Unknown
        :type asset_class: str
        :param dom_ccy:  The domestic currency, meaning the currency in which the instrument would typically be expected to pay cashflows, e.g. a share in AAPL being USD.
        :type dom_ccy: str
        :param links:  Collection of links.
        :type links: list[lusid.Link]

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._href = None
        self._scope = None
        self._lusid_instrument_id = None
        self._version = None
        self._name = None
        self._identifiers = None
        self._properties = None
        self._lookthrough_portfolio = None
        self._instrument_definition = None
        self._state = None
        self._asset_class = None
        self._dom_ccy = None
        self._links = None
        self.discriminator = None

        self.href = href
        self.scope = scope
        self.lusid_instrument_id = lusid_instrument_id
        self.version = version
        self.name = name
        self.identifiers = identifiers
        self.properties = properties
        if lookthrough_portfolio is not None:
            self.lookthrough_portfolio = lookthrough_portfolio
        if instrument_definition is not None:
            self.instrument_definition = instrument_definition
        self.state = state
        if asset_class is not None:
            self.asset_class = asset_class
        self.dom_ccy = dom_ccy
        self.links = links

    @property
    def href(self):
        """Gets the href of this Instrument.  # noqa: E501

        The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.  # noqa: E501

        :return: The href of this Instrument.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this Instrument.

        The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.  # noqa: E501

        :param href: The href of this Instrument.  # noqa: E501
        :type href: str
        """

        self._href = href

    @property
    def scope(self):
        """Gets the scope of this Instrument.  # noqa: E501

        The scope in which the instrument lies.  # noqa: E501

        :return: The scope of this Instrument.  # noqa: E501
        :rtype: str
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        """Sets the scope of this Instrument.

        The scope in which the instrument lies.  # noqa: E501

        :param scope: The scope of this Instrument.  # noqa: E501
        :type scope: str
        """

        self._scope = scope

    @property
    def lusid_instrument_id(self):
        """Gets the lusid_instrument_id of this Instrument.  # noqa: E501

        The unique LUSID Instrument Identifier (LUID) of the instrument.  # noqa: E501

        :return: The lusid_instrument_id of this Instrument.  # noqa: E501
        :rtype: str
        """
        return self._lusid_instrument_id

    @lusid_instrument_id.setter
    def lusid_instrument_id(self, lusid_instrument_id):
        """Sets the lusid_instrument_id of this Instrument.

        The unique LUSID Instrument Identifier (LUID) of the instrument.  # noqa: E501

        :param lusid_instrument_id: The lusid_instrument_id of this Instrument.  # noqa: E501
        :type lusid_instrument_id: str
        """
        if self.local_vars_configuration.client_side_validation and lusid_instrument_id is None:  # noqa: E501
            raise ValueError("Invalid value for `lusid_instrument_id`, must not be `None`")  # noqa: E501

        self._lusid_instrument_id = lusid_instrument_id

    @property
    def version(self):
        """Gets the version of this Instrument.  # noqa: E501


        :return: The version of this Instrument.  # noqa: E501
        :rtype: lusid.Version
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this Instrument.


        :param version: The version of this Instrument.  # noqa: E501
        :type version: lusid.Version
        """
        if self.local_vars_configuration.client_side_validation and version is None:  # noqa: E501
            raise ValueError("Invalid value for `version`, must not be `None`")  # noqa: E501

        self._version = version

    @property
    def name(self):
        """Gets the name of this Instrument.  # noqa: E501

        The name of the instrument.  # noqa: E501

        :return: The name of this Instrument.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Instrument.

        The name of the instrument.  # noqa: E501

        :param name: The name of this Instrument.  # noqa: E501
        :type name: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def identifiers(self):
        """Gets the identifiers of this Instrument.  # noqa: E501

        The set of identifiers that can be used to identify the instrument.  # noqa: E501

        :return: The identifiers of this Instrument.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._identifiers

    @identifiers.setter
    def identifiers(self, identifiers):
        """Sets the identifiers of this Instrument.

        The set of identifiers that can be used to identify the instrument.  # noqa: E501

        :param identifiers: The identifiers of this Instrument.  # noqa: E501
        :type identifiers: dict(str, str)
        """
        if self.local_vars_configuration.client_side_validation and identifiers is None:  # noqa: E501
            raise ValueError("Invalid value for `identifiers`, must not be `None`")  # noqa: E501

        self._identifiers = identifiers

    @property
    def properties(self):
        """Gets the properties of this Instrument.  # noqa: E501

        The requested instrument properties. These will be from the 'Instrument' domain.  # noqa: E501

        :return: The properties of this Instrument.  # noqa: E501
        :rtype: list[lusid.ModelProperty]
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this Instrument.

        The requested instrument properties. These will be from the 'Instrument' domain.  # noqa: E501

        :param properties: The properties of this Instrument.  # noqa: E501
        :type properties: list[lusid.ModelProperty]
        """

        self._properties = properties

    @property
    def lookthrough_portfolio(self):
        """Gets the lookthrough_portfolio of this Instrument.  # noqa: E501


        :return: The lookthrough_portfolio of this Instrument.  # noqa: E501
        :rtype: lusid.ResourceId
        """
        return self._lookthrough_portfolio

    @lookthrough_portfolio.setter
    def lookthrough_portfolio(self, lookthrough_portfolio):
        """Sets the lookthrough_portfolio of this Instrument.


        :param lookthrough_portfolio: The lookthrough_portfolio of this Instrument.  # noqa: E501
        :type lookthrough_portfolio: lusid.ResourceId
        """

        self._lookthrough_portfolio = lookthrough_portfolio

    @property
    def instrument_definition(self):
        """Gets the instrument_definition of this Instrument.  # noqa: E501


        :return: The instrument_definition of this Instrument.  # noqa: E501
        :rtype: lusid.LusidInstrument
        """
        return self._instrument_definition

    @instrument_definition.setter
    def instrument_definition(self, instrument_definition):
        """Sets the instrument_definition of this Instrument.


        :param instrument_definition: The instrument_definition of this Instrument.  # noqa: E501
        :type instrument_definition: lusid.LusidInstrument
        """

        self._instrument_definition = instrument_definition

    @property
    def state(self):
        """Gets the state of this Instrument.  # noqa: E501

        The state of of the instrument at the asAt datetime of this version of the instrument definition. The available values are: Active, Inactive  # noqa: E501

        :return: The state of this Instrument.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this Instrument.

        The state of of the instrument at the asAt datetime of this version of the instrument definition. The available values are: Active, Inactive  # noqa: E501

        :param state: The state of this Instrument.  # noqa: E501
        :type state: str
        """
        if self.local_vars_configuration.client_side_validation and state is None:  # noqa: E501
            raise ValueError("Invalid value for `state`, must not be `None`")  # noqa: E501
        allowed_values = ["Active", "Inactive"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and state not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"  # noqa: E501
                .format(state, allowed_values)
            )

        self._state = state

    @property
    def asset_class(self):
        """Gets the asset_class of this Instrument.  # noqa: E501

        The nominal asset class of the instrument, e.g. InterestRates, FX, Inflation, Equities, Credit, Commodities, etc. The available values are: InterestRates, FX, Inflation, Equities, Credit, Commodities, Money, Unknown  # noqa: E501

        :return: The asset_class of this Instrument.  # noqa: E501
        :rtype: str
        """
        return self._asset_class

    @asset_class.setter
    def asset_class(self, asset_class):
        """Sets the asset_class of this Instrument.

        The nominal asset class of the instrument, e.g. InterestRates, FX, Inflation, Equities, Credit, Commodities, etc. The available values are: InterestRates, FX, Inflation, Equities, Credit, Commodities, Money, Unknown  # noqa: E501

        :param asset_class: The asset_class of this Instrument.  # noqa: E501
        :type asset_class: str
        """
        allowed_values = ["InterestRates", "FX", "Inflation", "Equities", "Credit", "Commodities", "Money", "Unknown"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and asset_class not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `asset_class` ({0}), must be one of {1}"  # noqa: E501
                .format(asset_class, allowed_values)
            )

        self._asset_class = asset_class

    @property
    def dom_ccy(self):
        """Gets the dom_ccy of this Instrument.  # noqa: E501

        The domestic currency, meaning the currency in which the instrument would typically be expected to pay cashflows, e.g. a share in AAPL being USD.  # noqa: E501

        :return: The dom_ccy of this Instrument.  # noqa: E501
        :rtype: str
        """
        return self._dom_ccy

    @dom_ccy.setter
    def dom_ccy(self, dom_ccy):
        """Sets the dom_ccy of this Instrument.

        The domestic currency, meaning the currency in which the instrument would typically be expected to pay cashflows, e.g. a share in AAPL being USD.  # noqa: E501

        :param dom_ccy: The dom_ccy of this Instrument.  # noqa: E501
        :type dom_ccy: str
        """

        self._dom_ccy = dom_ccy

    @property
    def links(self):
        """Gets the links of this Instrument.  # noqa: E501

        Collection of links.  # noqa: E501

        :return: The links of this Instrument.  # noqa: E501
        :rtype: list[lusid.Link]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this Instrument.

        Collection of links.  # noqa: E501

        :param links: The links of this Instrument.  # noqa: E501
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
        if not isinstance(other, Instrument):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Instrument):
            return True

        return self.to_dict() != other.to_dict()
