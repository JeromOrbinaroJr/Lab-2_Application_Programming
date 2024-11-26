import unittest
from unittest.mock import patch, mock_open
import requests
from reExpression import is_valid_email, find_emails_in_text
from webpageSearch import find_emails_on_webpage
from fileSearch import find_emails_in_file

class TestReEmail(unittest.TestCase):
    def test_is_valid_email(self):
        self.assertTrue(is_valid_email("example@test.com"))
        self.assertTrue(is_valid_email("user.name+tag+sorting@example.com"))
        self.assertFalse(is_valid_email("example@test"))
        self.assertFalse(is_valid_email("example.com"))
        self.assertFalse(is_valid_email("example@.com"))

    def test_find_emails_in_text(self):
        text = "Emails: first@example.com, second.user@test.org"
        result = find_emails_in_text(text)
        self.assertEqual(result, ["first@example.com", "second.user@test.org"])


class TestFileEmailSearch(unittest.TestCase):
    @patch("builtins.open", new_callable=mock_open, read_data="Email: test@example.com\nInvalid: test.com")
    def test_find_emails_in_file(self, mock_file):
        result = find_emails_in_file("emails.txt")
        self.assertEqual(result, ["test@example.com"])

    @patch("builtins.open", side_effect=FileNotFoundError)
    def test_find_emails_in_file_not_found(self, mock_file):
        with patch("builtins.print") as mock_print:
            find_emails_in_file("non_emails.txt")
            mock_print.assert_called_with(
                "Error: The file was not found. Make sure that the path is specified correctly.")

class TestWebpageEmailSearch(unittest.TestCase):
    @patch("requests.get")
    def test_find_emails_on_webpage(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.text = "Contact: email@example.com"
        mock_get.return_value.text = "66365c10274f4724819f92df56571b8b@sentry.litres.io"

        with patch("builtins.print") as mock_print:
            find_emails_on_webpage("https://www.litres.ru/author/albert-eynshteyn/about/")
            mock_print.assert_called_with("Found e-mails on the page:", ["66365c10274f4724819f92df56571b8b@sentry.litres.io"])

    @patch("requests.get")
    def test_find_emails_on_webpage_error(self, mock_get):
        mock_get.side_effect = requests.RequestException("Network error")

        with patch("builtins.print") as mock_print:
            find_emails_on_webpage("https://www.litres.ru/author/albert-eynshteyn/about/")
            mock_print.assert_called_with("An unexpected error occurred: Network error")


if __name__ == "__main__":
    unittest.main()