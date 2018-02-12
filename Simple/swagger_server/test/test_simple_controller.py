# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.simple_classifier import SimpleClassifier  # noqa: E501
from swagger_server.models.simple_classifiers import SimpleClassifiers  # noqa: E501
from swagger_server.test import BaseTestCase


class TestSimpleController(BaseTestCase):
    """SimpleController integration test stubs"""

    def test_create_classifier(self):
        """Test case for create_classifier

        
        """
        body = SimpleClassifier()
        response = self.client.open(
            '/v1/simple/createclassifier',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_list_classifier(self):
        """Test case for list_classifier

        
        """
        query_string = [('sm_key', 'sm_key_example'),
                        ('sm_value', 'sm_value_example'),
                        ('p_id', 'p_id_example'),
                        ('p_runtime_url', 'p_runtime_url_example'),
                        ('p_creator', 'p_creator_example'),
                        ('p_classifier_type', 'p_classifier_type_example'),
                        ('p_cluster', 'p_cluster_example'),
                        ('p_name_space', 'p_name_space_example')]
        response = self.client.open(
            '/v1/simple/listclassifier',
            method='GET',
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
