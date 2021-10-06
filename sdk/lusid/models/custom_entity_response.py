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


class CustomEntityResponse(object):
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
        'entity_type': 'str',
        'custom_entity_id': 'str',
        'version': 'Version',
        'display_name': 'str',
        'description': 'str',
        'identifiers': 'list[CustomEntityIdResponse]',
        'fields': 'list[CustomEntityField]',
        'effective_range': 'DateRange',
        'as_at_range': 'DateRange',
        'links': 'list[Link]'
    }

    attribute_map = {
        'href': 'href',
        'entity_type': 'entityType',
        'custom_entity_id': 'customEntityId',
        'version': 'version',
        'display_name': 'displayName',
        'description': 'description',
        'identifiers': 'identifiers',
        'fields': 'fields',
        'effective_range': 'effectiveRange',
        'as_at_range': 'asAtRange',
        'links': 'links'
    }

    required_map = {
        'href': 'optional',
        'entity_type': 'required',
        'custom_entity_id': 'required',
        'version': 'required',
        'display_name': 'required',
        'description': 'optional',
        'identifiers': 'required',
        'fields': 'required',
        'effective_range': 'required',
        'as_at_range': 'required',
        'links': 'optional'
    }

    def __init__(self, href=None, entity_type=None, custom_entity_id=None, version=None, display_name=None, description=None, identifiers=None, fields=None, effective_range=None, as_at_range=None, links=None, local_vars_configuration=None):  # noqa: E501
        """CustomEntityResponse - a model defined in OpenAPI"
        
        :param href:  The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.
        :type href: str
        :param entity_type:  The EntityType to be used when relations are created to the CustomEntity (required)
        :type entity_type: str
        :param custom_entity_id:  A unique identifier for the CustomEntity (required)
        :type custom_entity_id: str
        :param version:  (required)
        :type version: lusid.Version
        :param display_name:  The display name of the CustomEntity (required)
        :type display_name: str
        :param description:  The description of the CustomEntity
        :type description: str
        :param identifiers:  A collection of CustomEntityIdentifiers that can identify the CustomEntity (required)
        :type identifiers: list[lusid.CustomEntityIdResponse]
        :param fields:  A collection of CustomEntityFields that decorate the CustomEntity (required)
        :type fields: list[lusid.CustomEntityField]
        :param effective_range:  (required)
        :type effective_range: lusid.DateRange
        :param as_at_range:  (required)
        :type as_at_range: lusid.DateRange
        :param links:  Collection of links.
        :type links: list[lusid.Link]

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._href = None
        self._entity_type = None
        self._custom_entity_id = None
        self._version = None
        self._display_name = None
        self._description = None
        self._identifiers = None
        self._fields = None
        self._effective_range = None
        self._as_at_range = None
        self._links = None
        self.discriminator = None

        self.href = href
        self.entity_type = entity_type
        self.custom_entity_id = custom_entity_id
        self.version = version
        self.display_name = display_name
        self.description = description
        self.identifiers = identifiers
        self.fields = fields
        self.effective_range = effective_range
        self.as_at_range = as_at_range
        self.links = links

    @property
    def href(self):
        """Gets the href of this CustomEntityResponse.  # noqa: E501

        The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.  # noqa: E501

        :return: The href of this CustomEntityResponse.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this CustomEntityResponse.

        The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.  # noqa: E501

        :param href: The href of this CustomEntityResponse.  # noqa: E501
        :type href: str
        """

        self._href = href

    @property
    def entity_type(self):
        """Gets the entity_type of this CustomEntityResponse.  # noqa: E501

        The EntityType to be used when relations are created to the CustomEntity  # noqa: E501

        :return: The entity_type of this CustomEntityResponse.  # noqa: E501
        :rtype: str
        """
        return self._entity_type

    @entity_type.setter
    def entity_type(self, entity_type):
        """Sets the entity_type of this CustomEntityResponse.

        The EntityType to be used when relations are created to the CustomEntity  # noqa: E501

        :param entity_type: The entity_type of this CustomEntityResponse.  # noqa: E501
        :type entity_type: str
        """
        if self.local_vars_configuration.client_side_validation and entity_type is None:  # noqa: E501
            raise ValueError("Invalid value for `entity_type`, must not be `None`")  # noqa: E501

        self._entity_type = entity_type

    @property
    def custom_entity_id(self):
        """Gets the custom_entity_id of this CustomEntityResponse.  # noqa: E501

        A unique identifier for the CustomEntity  # noqa: E501

        :return: The custom_entity_id of this CustomEntityResponse.  # noqa: E501
        :rtype: str
        """
        return self._custom_entity_id

    @custom_entity_id.setter
    def custom_entity_id(self, custom_entity_id):
        """Sets the custom_entity_id of this CustomEntityResponse.

        A unique identifier for the CustomEntity  # noqa: E501

        :param custom_entity_id: The custom_entity_id of this CustomEntityResponse.  # noqa: E501
        :type custom_entity_id: str
        """
        if self.local_vars_configuration.client_side_validation and custom_entity_id is None:  # noqa: E501
            raise ValueError("Invalid value for `custom_entity_id`, must not be `None`")  # noqa: E501

        self._custom_entity_id = custom_entity_id

    @property
    def version(self):
        """Gets the version of this CustomEntityResponse.  # noqa: E501


        :return: The version of this CustomEntityResponse.  # noqa: E501
        :rtype: lusid.Version
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this CustomEntityResponse.


        :param version: The version of this CustomEntityResponse.  # noqa: E501
        :type version: lusid.Version
        """
        if self.local_vars_configuration.client_side_validation and version is None:  # noqa: E501
            raise ValueError("Invalid value for `version`, must not be `None`")  # noqa: E501

        self._version = version

    @property
    def display_name(self):
        """Gets the display_name of this CustomEntityResponse.  # noqa: E501

        The display name of the CustomEntity  # noqa: E501

        :return: The display_name of this CustomEntityResponse.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this CustomEntityResponse.

        The display name of the CustomEntity  # noqa: E501

        :param display_name: The display_name of this CustomEntityResponse.  # noqa: E501
        :type display_name: str
        """
        if self.local_vars_configuration.client_side_validation and display_name is None:  # noqa: E501
            raise ValueError("Invalid value for `display_name`, must not be `None`")  # noqa: E501

        self._display_name = display_name

    @property
    def description(self):
        """Gets the description of this CustomEntityResponse.  # noqa: E501

        The description of the CustomEntity  # noqa: E501

        :return: The description of this CustomEntityResponse.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CustomEntityResponse.

        The description of the CustomEntity  # noqa: E501

        :param description: The description of this CustomEntityResponse.  # noqa: E501
        :type description: str
        """

        self._description = description

    @property
    def identifiers(self):
        """Gets the identifiers of this CustomEntityResponse.  # noqa: E501

        A collection of CustomEntityIdentifiers that can identify the CustomEntity  # noqa: E501

        :return: The identifiers of this CustomEntityResponse.  # noqa: E501
        :rtype: list[lusid.CustomEntityIdResponse]
        """
        return self._identifiers

    @identifiers.setter
    def identifiers(self, identifiers):
        """Sets the identifiers of this CustomEntityResponse.

        A collection of CustomEntityIdentifiers that can identify the CustomEntity  # noqa: E501

        :param identifiers: The identifiers of this CustomEntityResponse.  # noqa: E501
        :type identifiers: list[lusid.CustomEntityIdResponse]
        """
        if self.local_vars_configuration.client_side_validation and identifiers is None:  # noqa: E501
            raise ValueError("Invalid value for `identifiers`, must not be `None`")  # noqa: E501

        self._identifiers = identifiers

    @property
    def fields(self):
        """Gets the fields of this CustomEntityResponse.  # noqa: E501

        A collection of CustomEntityFields that decorate the CustomEntity  # noqa: E501

        :return: The fields of this CustomEntityResponse.  # noqa: E501
        :rtype: list[lusid.CustomEntityField]
        """
        return self._fields

    @fields.setter
    def fields(self, fields):
        """Sets the fields of this CustomEntityResponse.

        A collection of CustomEntityFields that decorate the CustomEntity  # noqa: E501

        :param fields: The fields of this CustomEntityResponse.  # noqa: E501
        :type fields: list[lusid.CustomEntityField]
        """
        if self.local_vars_configuration.client_side_validation and fields is None:  # noqa: E501
            raise ValueError("Invalid value for `fields`, must not be `None`")  # noqa: E501

        self._fields = fields

    @property
    def effective_range(self):
        """Gets the effective_range of this CustomEntityResponse.  # noqa: E501


        :return: The effective_range of this CustomEntityResponse.  # noqa: E501
        :rtype: lusid.DateRange
        """
        return self._effective_range

    @effective_range.setter
    def effective_range(self, effective_range):
        """Sets the effective_range of this CustomEntityResponse.


        :param effective_range: The effective_range of this CustomEntityResponse.  # noqa: E501
        :type effective_range: lusid.DateRange
        """
        if self.local_vars_configuration.client_side_validation and effective_range is None:  # noqa: E501
            raise ValueError("Invalid value for `effective_range`, must not be `None`")  # noqa: E501

        self._effective_range = effective_range

    @property
    def as_at_range(self):
        """Gets the as_at_range of this CustomEntityResponse.  # noqa: E501


        :return: The as_at_range of this CustomEntityResponse.  # noqa: E501
        :rtype: lusid.DateRange
        """
        return self._as_at_range

    @as_at_range.setter
    def as_at_range(self, as_at_range):
        """Sets the as_at_range of this CustomEntityResponse.


        :param as_at_range: The as_at_range of this CustomEntityResponse.  # noqa: E501
        :type as_at_range: lusid.DateRange
        """
        if self.local_vars_configuration.client_side_validation and as_at_range is None:  # noqa: E501
            raise ValueError("Invalid value for `as_at_range`, must not be `None`")  # noqa: E501

        self._as_at_range = as_at_range

    @property
    def links(self):
        """Gets the links of this CustomEntityResponse.  # noqa: E501

        Collection of links.  # noqa: E501

        :return: The links of this CustomEntityResponse.  # noqa: E501
        :rtype: list[lusid.Link]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this CustomEntityResponse.

        Collection of links.  # noqa: E501

        :param links: The links of this CustomEntityResponse.  # noqa: E501
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
        if not isinstance(other, CustomEntityResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CustomEntityResponse):
            return True

        return self.to_dict() != other.to_dict()