from unittest import TestCase
from mock import patch
import cicdtesting.authentication as auth


class StandAloneTests(TestCase):
    """Test the stand-alone module functions."""

    @patch('builtins.open')
    def test_login(self, mock_open):
        """Test the login function."""
        mock_open.return_value.read.return_value = "lijju|mathew\n"
        self.assertTrue(auth.login('lijju', 'mathew'))
