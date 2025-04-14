import traceback

class CustomException(Exception):
    def __init__(self, error_message, error_detail: Exception):
        super().__init__(error_message)
        # Capture the error message with detailed traceback info
        self.error_message = self.get_detailed_error_message(error_message, error_detail)

    @staticmethod 
    def get_detailed_error_message(error_message, error_detail: Exception):
        # Generate a detailed error message with traceback
        # You can use traceback.format_exception to get more detailed info
        tb_str = "".join(traceback.format_exception(None, error_detail, error_detail.__traceback__))
        return f"Error occurred: {error_message}, traceback: {tb_str}"

    def __str__(self):
        return self.error_message
