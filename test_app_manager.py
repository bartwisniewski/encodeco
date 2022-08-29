from app_manager import *


def test_should_print_buffer_out(mocker):
    buffer_content = "blah blah blah"
    app_manager_object = AppManager()
    app_manager_object.buffer.write(buffer_content)

    mock_print = mocker.patch("app_manager.print")

    app_manager_object._AppManager__peek_buffer()

    mock_print.assert_called_once_with(app_manager_object.buffer)
