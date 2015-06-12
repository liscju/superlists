from unittest import skip
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.test import override_settings
from selenium.webdriver.common.keys import Keys
import sys
from functional_tests.base import FunctionalTest
__author__ = 'lee'
from selenium import webdriver

class ItemValidationTest(FunctionalTest):
    @skip
    def test_cannot_add_empty_list_items(self):
        # Edith goes to the home page and accidentally tries to submit
        # an empty list item. She hits Enter on the empty input box

        # The home page refreshes and there is an error message saying
        # that list items cannot be blank

        # She tries again with some text for the item, which now works

        # Perversely,shw now decides to submit a second blank list item

        # She receives a similiar warning on the list page

        # And she can correct it by filling some text in
        self.fail('write me!')
















