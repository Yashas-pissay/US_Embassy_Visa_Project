import os
import sys

#if we got any type of error we need 2 things to capture i.e Error message and Error details
class CustomException(Exception):
    
    def __init__(self, error_message:Exception,error_detail:sys):
        super().__init__(error_message)
        self.error_message=CustomException.get_detailed_error_message(error_message=error_message,
                                                                       error_detail=error_detail)

    @staticmethod
    def get_detailed_error_message(error_message:Exception,error_detail:sys)->str:
        
        _,_ ,exec_tb = error_detail.exc_info()
        exception_block_line_number = exec_tb.tb_frame.f_lineno
        try_block_line_number = exec_tb.tb_lineno
        file_name = exec_tb.tb_frame.f_code.co_filename
        error_message = f"""
        Error occured in script: 
        [ {file_name} ] at 
        try block line number: [{try_block_line_number}] and 
        exception block line number: [{exception_block_line_number}] 
        error message: [{error_message}]
        """
        return error_message

    def __str__(self):  #__str__ used for creating output that is human-readable are must be for end-users or string is intended for users . 
        return self.error_message


    def __repr__(self) -> str:  #__repr__ must serve the purpose of debugging and development or string is intended for developers.
        return CustomException.__name__.str()

        