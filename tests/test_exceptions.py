import pytest
from page_objects.exceptions_page import ExceptionsPage


class TestException:
    @pytest.mark.exceptions
    def test_no_such_element_exception(self, driver):
        exceptions_page = ExceptionsPage(driver)
        exceptions_page.open()
        exceptions_page.add_second_row()
        assert exceptions_page.is_row2_displayed(
        ), "Row 2 input field is not displayed, but it should"

    @pytest.mark.exceptions
    def test_element_not_interactable_exception(self, driver):
        exceptions_page = ExceptionsPage(driver)
        exceptions_page.open()
        exceptions_page.add_second_row()
        exceptions_page.add_second_food("Tacos")
        assert exceptions_page.get_confirmation_message() == "Row 2 was saved"

    @pytest.mark.exceptions
    def test_invalid_element_satate_exception(self, driver):
        exceptions_page = ExceptionsPage(driver)
        exceptions_page.open()
        exceptions_page.modify_row_1_input('Tacos')
        assert exceptions_page.get_confirmation_message() == "Row 1 was saved"

    @pytest.mark.exceptions
    @pytest.mark.debug
    def test_stale_element_reference_exception(self, driver):
        exceptions_page = ExceptionsPage(driver)
        exceptions_page.open()
        exceptions_page.add_second_row()
        assert not exceptions_page.are_instructions_displayed()

    @pytest.mark.exceptions
    def test_timeout_exception(self, driver):
        exceptions_page = ExceptionsPage(driver)
        exceptions_page.open()
        exceptions_page.add_second_row()
        assert exceptions_page.is_row2_displayed(
        ), "Row 2 input field is not displayed, but it should"
