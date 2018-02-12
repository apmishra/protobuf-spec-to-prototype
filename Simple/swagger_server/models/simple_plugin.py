# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.simple_kv_pairs import SimpleKVPairs  # noqa: F401,E501
from swagger_server import util


class SimplePlugin(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, id: str=None, creator: str=None, type: str=None, name_space: str=None, kv_pairs: SimpleKVPairs=None):  # noqa: E501
        """SimplePlugin - a model defined in Swagger

        :param id: The id of this SimplePlugin.  # noqa: E501
        :type id: str
        :param creator: The creator of this SimplePlugin.  # noqa: E501
        :type creator: str
        :param type: The type of this SimplePlugin.  # noqa: E501
        :type type: str
        :param name_space: The name_space of this SimplePlugin.  # noqa: E501
        :type name_space: str
        :param kv_pairs: The kv_pairs of this SimplePlugin.  # noqa: E501
        :type kv_pairs: SimpleKVPairs
        """
        self.swagger_types = {
            'id': str,
            'creator': str,
            'type': str,
            'name_space': str,
            'kv_pairs': SimpleKVPairs
        }

        self.attribute_map = {
            'id': 'id',
            'creator': 'creator',
            'type': 'type',
            'name_space': 'name_space',
            'kv_pairs': 'kv_pairs'
        }

        self._id = id
        self._creator = creator
        self._type = type
        self._name_space = name_space
        self._kv_pairs = kv_pairs

    @classmethod
    def from_dict(cls, dikt) -> 'SimplePlugin':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The SimplePlugin of this SimplePlugin.  # noqa: E501
        :rtype: SimplePlugin
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> str:
        """Gets the id of this SimplePlugin.


        :return: The id of this SimplePlugin.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str):
        """Sets the id of this SimplePlugin.


        :param id: The id of this SimplePlugin.
        :type id: str
        """

        self._id = id

    @property
    def creator(self) -> str:
        """Gets the creator of this SimplePlugin.


        :return: The creator of this SimplePlugin.
        :rtype: str
        """
        return self._creator

    @creator.setter
    def creator(self, creator: str):
        """Sets the creator of this SimplePlugin.


        :param creator: The creator of this SimplePlugin.
        :type creator: str
        """

        self._creator = creator

    @property
    def type(self) -> str:
        """Gets the type of this SimplePlugin.


        :return: The type of this SimplePlugin.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type: str):
        """Sets the type of this SimplePlugin.


        :param type: The type of this SimplePlugin.
        :type type: str
        """

        self._type = type

    @property
    def name_space(self) -> str:
        """Gets the name_space of this SimplePlugin.


        :return: The name_space of this SimplePlugin.
        :rtype: str
        """
        return self._name_space

    @name_space.setter
    def name_space(self, name_space: str):
        """Sets the name_space of this SimplePlugin.


        :param name_space: The name_space of this SimplePlugin.
        :type name_space: str
        """

        self._name_space = name_space

    @property
    def kv_pairs(self) -> SimpleKVPairs:
        """Gets the kv_pairs of this SimplePlugin.


        :return: The kv_pairs of this SimplePlugin.
        :rtype: SimpleKVPairs
        """
        return self._kv_pairs

    @kv_pairs.setter
    def kv_pairs(self, kv_pairs: SimpleKVPairs):
        """Sets the kv_pairs of this SimplePlugin.


        :param kv_pairs: The kv_pairs of this SimplePlugin.
        :type kv_pairs: SimpleKVPairs
        """

        self._kv_pairs = kv_pairs
