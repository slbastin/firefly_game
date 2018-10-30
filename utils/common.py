import time 
import os

BEBUG_ENABLE = 0

if BEBUG_ENABLE:
    def debug_print(*args):
        print(*args)
else:
    def debug_print(*args):
        pass    

# check the range of number
def num_range_check(num, min_n = None, max_n = None, to_range = True):
    if min_n == None and max_n == None:
        return num
    
    if min_n != None:
        if to_range and num < min_n:
            num = min_n

    if max_n != None:
        if to_range and num > max_n:
            num = max_n
    return num


def get_except_by_str(except_str):
    if except_str == "BaseException":
        return BaseException

    elif except_str == "SystemExit":
        return SystemExit

    elif except_str == "KeyboardInterrupt":
        return KeyboardInterrupt

    elif except_str == "Exception":
        return Exception

    elif except_str == "StopIteration":
        return StopIteration

    elif except_str == "GeneratorExit":
        return GeneratorExit

    elif except_str == "StandardError":
        return StandardError

    elif except_str == "ArithmeticError":
        return ArithmeticError

    elif except_str == "FloatingPointError":
        return FloatingPointError

    elif except_str == "OverflowError":
        return OverflowError

    elif except_str == "ZeroDivisionError":
        return ZeroDivisionError

    elif except_str == "AssertionError":
        return AssertionError

    elif except_str == "AttributeError":
        return AttributeError

    elif except_str == "EOFError":
        return EOFError

    elif except_str == "EnvironmentError":
        return EnvironmentError

    elif except_str == "IOError":
        return IOError

    elif except_str == "OSError":
        return OSError

    elif except_str == "WindowsError":
        return WindowsError

    elif except_str == "ImportError":
        return ImportError

    elif except_str == "LookupError":
        return LookupError

    elif except_str == "IndexError":
        return IndexError

    elif except_str == "KeyError":
        return KeyError

    elif except_str == "MemoryError":
        return MemoryError

    elif except_str == "NameError":
        return NameError

    elif except_str == "UnboundLocalError":
        return WindowsError

    elif except_str == "UnboundLocalError":
        return WindowsError

    elif except_str == "ReferenceError":
        return ReferenceError

    elif except_str == "RuntimeError":
        return RuntimeError

    elif except_str == "NotImplementedError":
        return NotImplementedError

    elif except_str == "SyntaxError":
        return SyntaxError

    elif except_str == "RuntimeError":
        return RuntimeError

    elif except_str == "IndentationError":
        return IndentationError

    elif except_str == "TabError":
        return TabError

    elif except_str == "TypeError":
        return TypeError

    elif except_str == "SystemError":
        return SystemError

    elif except_str == "ValueError":
        return ValueError

    elif except_str == "UnicodeError":
        return UnicodeError

    elif except_str == "UnicodeDecodeError":
        return UnicodeDecodeError

    elif except_str == "UnicodeEncodeError":
        return UnicodeEncodeError

    elif except_str == "UnicodeTranslateError":
        return UnicodeTranslateError

    elif except_str == "UnicodeDecodeError":
        return UnicodeDecodeError

    elif except_str == "Warning":
        return Warning

    elif except_str == "DeprecationWarning":
        return DeprecationWarning

    elif except_str == "FutureWarning":
        return FutureWarning

    elif except_str == "PendingDeprecationWarning":
        return PendingDeprecationWarning

    elif except_str == "RuntimeWarning":
        return RuntimeWarning

    elif except_str == "SyntaxWarning":
        return SyntaxWarning

    elif except_str == "UserWarning":
        return UserWarning