# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class TIMESTAMP(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, timestamp=None):  # noqa: E501
        """TIMESTAMP - a model defined in Swagger

        :param timestamp: The timestamp of this TIMESTAMP.  # noqa: E501
        :type timestamp: str
        """
        self.swagger_types = {
            'timestamp': str
        }

        self.attribute_map = {
            'timestamp': 'Timestamp'
        }

        self._timestamp = timestamp

    @classmethod
    def from_dict(cls, dikt):
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The TIMESTAMP of this TIMESTAMP.  # noqa: E501
        :rtype: TIMESTAMP
        """
        return util.deserialize_model(dikt, cls)

    @property
    def timestamp(self):
        """Gets the timestamp of this TIMESTAMP.


        :return: The timestamp of this TIMESTAMP.
        :rtype: str
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this TIMESTAMP.


        :param timestamp: The timestamp of this TIMESTAMP.
        :type timestamp: str
        """
        if timestamp is None:
            raise ValueError("Invalid value for `timestamp`, must not be `None`")  # noqa: E501

        self._timestamp = timestamp