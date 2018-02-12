import connexion
import six

from swagger_server.models.simple_classifier import SimpleClassifier  # noqa: E501
from swagger_server.models.simple_classifiers import SimpleClassifiers  # noqa: E501
from swagger_server.models.simple_plugins import SimplePlugins  # noqa: E501
from swagger_server import util


def create_classifier(body):  # noqa: E501
    """create_classifier

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: SimpleClassifiers
    """
    if connexion.request.is_json:
        body = SimpleClassifier.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def list_all(sm_key=None, sm_value=None, p_id=None, p_runtime_url=None, p_creator=None, p_classifier_type=None, p_cluster=None, p_name_space=None):  # noqa: E501
    """list_all

     # noqa: E501

    :param sm_key: 
    :type sm_key: str
    :param sm_value: 
    :type sm_value: str
    :param p_id: 
    :type p_id: str
    :param p_runtime_url: 
    :type p_runtime_url: str
    :param p_creator: 
    :type p_creator: str
    :param p_classifier_type: 
    :type p_classifier_type: str
    :param p_cluster: 
    :type p_cluster: str
    :param p_name_space: 
    :type p_name_space: str

    :rtype: SimplePlugins
    """
    return 'do some magic!'


def list_classifier(sm_key=None, sm_value=None, p_id=None, p_runtime_url=None, p_creator=None, p_classifier_type=None, p_cluster=None, p_name_space=None):  # noqa: E501
    """list_classifier

     # noqa: E501

    :param sm_key: 
    :type sm_key: str
    :param sm_value: 
    :type sm_value: str
    :param p_id: 
    :type p_id: str
    :param p_runtime_url: 
    :type p_runtime_url: str
    :param p_creator: 
    :type p_creator: str
    :param p_classifier_type: 
    :type p_classifier_type: str
    :param p_cluster: 
    :type p_cluster: str
    :param p_name_space: 
    :type p_name_space: str

    :rtype: SimpleClassifiers
    """
    return 'do some magic!'
