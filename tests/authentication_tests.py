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

    @patch('builtins.open')
    def test_login_bad_creds(self, mock_open):
        """Test the login function when bad creds are passed."""
        mock_open.return_value.read.return_value = "lijju|mathew\n"
        self.assertFalse(auth.login('lijju', 'wrongpassword'))

    # @patch('builtins.open')
    # def test_login_error(self, mock_open):
    #     """Test the login function when an error happens."""
    #     mock_open.side_effect = IOError()
    #     self.assertFalse(auth.login('lijju', 'mathew'))

