from mock import Mock

from django.test import TestCase

from celery_progress.backends import CeleryBackend


class CeleryBackendTest(TestCase):
    """
    Tests for the CeleryBackend.
    """

    def setUp(self):
        self.backend = CeleryBackend()
        self.mock_store_result = Mock(return_value=True)
        self.mock_backend = Mock(store_result=self.mock_store_result)
        self.mock_app = Mock(backend=self.mock_backend)
        self.backend.app = self.mock_app

    def test_set_progress_calls_store_result(self):
        self.backend.set_progress('abc-123-def', 50)
        self.assertEqual(self.mock_store_result.called, True)
