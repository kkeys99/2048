"""
Unit test functions for Python

This module provides function-level unit testing tools.  It is a replacement for the 
built-in Python package unittest, which is much less user friendly and requires an 
understanding of OO programming. 

The assert functions in this module are different from standard assert statements.
They stop execution of Python and report the location of the error.

Author: Walker M. White (wmw2)
Date:   July 13, 2017 (Python 3 version)
"""


def quit_with_error(msg):
    """
    Quits Python with an error msg
    
    When testing, this is preferable to raising an error in Python. Once you have a lot 
    of helper functions, it becomes a lot of work just to figure out what is going on in 
    the error message. This makes the error clear and concise
    
    :param msg: The error message
    :type msg:  ``str``
    """
    import traceback
    stack = traceback.extract_stack()
    frame = stack[-3]
    print(msg)
    if (frame[3] is None):
        suffix = ''
    else:
        suffix = ": "+frame[3]
    print('Line',repr(frame[1]),'of',frame[0] + suffix)
    print('Quitting with Error')
    quit()


def assert_equals(expected,received):
    """
    Quits if ``expected`` and ``received`` differ.
    
    The meaning of "differ" for this function is !=.  As a result, this assert function 
    is not necessarily reliable when expected and received are of type ``float``.  You 
    should use the function :func:`assert_floats_equal` for that application.
    
    As part of the error message, this function provides some minimal debug information.  
    The following is an example debug message::
        
        assert_equals expected 'yes' but instead got 'no'
    
    :param expected: The value you expect the test to have
    
    :param received: The value the test actually had
    """
    if (expected != received):
        message = 'assert_equals: expected ' + repr(expected) + ' but instead got ' + repr(received)
        quit_with_error(message)


def assert_not_equals(expected,received):
    """
    Quits if ``expected`` and ``received`` differ.
    
    The meaning of "differ" for this function is !=.  As a result, this assert function 
    is not necessarily reliable when expected and received are of type ``float``.  You 
    should use the function :func:`assert_floats_not_equal` for that application.
    
    As part of the error message, this function provides some minimal debug information.  
    The following is an example debug message::
        
        assert_not_equals expected something different from 'n' 
    
    :param expected: The value you expect the test to have
    
    :param received: The value the test actually had
    """
    if (expected == received):
        message = 'assert_not_equals: expected something different from' + repr(expected)
        quit_with_error(message)


def assert_true(received):
    """
    Quits if ``received`` is False.
    
    As part of the error message, this function provides some minimal debug information.  
    The following is an example debug message::
        
        assert_true expected True but instead got False
    
    :param received: The value the test actually had
    """
    if (not received):
        msg = "assert_true: expected True but instead got False"
        quit_with_error(msg)


def assert_false(received):
    """
    Quits if ``received`` is True.
    
    As part of the error message, this function provides some minimal debug information.  
    The following is an example debug message::
        
        assert_false expected False but instead got True
    
    :param received: The value the test actually had
    """
    if (received):
        msg = "assert_false: expected False but instead got True"
        quit_with_error(msg)


def assert_floats_equal(expected, received):
    """
    Quits if the floats ``expected`` and ``received`` differ.
    
    This function takes two numbers and compares them using functions from the numerical 
    package ``numpy``.  This is a scientific computing package that allows us to test if 
    numbers are "close enough". Hence, unlike :func:`assert_equal`, the meaning of 
    "differ" for  this function is defined by numpy.
    
    As part of the error message, this function provides some minimal debug information.  
    The following is an example debug message::
        
        assert_floats_equal: expected 0.1 but instead got 0.2
    
    **IMPORTANT**: 
    The arguments expected and received should each numbers (either floats or ints). If 
    either argument is not a number, the function quits with a different error message. 
    For example::
    
        assert_floats_equal: first argument 'alas' is not a number
    
    :param expected: The value you expect the test to have
    :type expected:  ``float``
    
    :param received: The value the test actually had
    :type received:  ``float``
    """
    import numpy
    number = [float, int]  # list of number types
    if type(expected) not in number:
        msg = ("assert_floats_equal: " +
                "first argument " + repr(expected) +" is not a number")
        quit_with_error(msg)
    
    if type(received) not in number:
        msg = ("assert_floats_equal: " +
              "second argument " + repr(received) +" is not a number")
        quit_with_error(msg)
    
    if (not numpy.allclose([expected],[received])):
        msg = ("assert_floats_equal: expected " + repr(expected) +
                " but instead got " + repr(received))
        quit_with_error(msg)


def assert_floats_not_equal(expected, received):
    """
    Quits if floats ``expected`` and ``received`` are the same.
    
    This function takes two numbers and compares them using functions from the numerical 
    package ``numpy``.  This is a scientific computing package that allows us to test if 
    numbers are "close enough".  Hence, unlike :func:`assert_not_equal`, the meaning of 
    "same" for  this function is defined by numpy.
    
    As part of the error message, this function provides some minimal debug information.  
    The following is an example debug message::
        
        assert_floats_not_equal: expected something different from 0.1 
    
    **IMPORTANT**: 
    The arguments expected and received should each numbers (either floats or ints). If 
    either argument is not a number, the function quits with a different error message. 
    For example::
        
         assert_floats_not_equal: first argument 'alas' is not a number
    
    :param expected: The value you expect the test to have
    :type expected:  ``float``
    
    :param received: The value the test actually had
    :type received:  ``float``
    """
    import numpy
    number = [float, int]  # list of number types
    if type(expected) not in number:
        msg = ('assert_floats_not_equal: ' +
                'first argument ' + repr(expected) +' is not a number')
        quit_with_error(msg)
    
    if type(received) not in number:
        msg = ("assert_floats_not_equal: " +
              "second argument " + repr(received) +" is not a number")
        quit_with_error(msg)
    
    if (numpy.allclose([expected],[received])):
        msg = ('assert_floats_not_equal: expected something different from' +
                repr(expected))
        quit_with_error(msg)


def assert_float_lists_equal(expected, received):
    """
    Quits if the lists (or tuples) of floats ``expected`` and ``received`` differ
    
    This function takes two numbers and compares them using functions from the numerical 
    package ``numpy``.  This is a scientific computing package that allows us to test if 
    numbers are "close enough".  Hence, unlike :func:`assert_equal`, the meaning of 
    "differ" for  this function is defined by numpy.
    
    This function is similar to :func:`assert_floats_equal`. The difference is that it 
    works on lists of floats.  These lists can be multidimensional.  To illustrate this, 
    the following is an example debug message::
        
        assert_float_lists__equal: expected [[1,2],[3,4]] but instead got [[1,2],[3,5]]
    
    **IMPORTANT**: 
    The arguments expected and received should each lists of numbers. Furthemore, they 
    must have EXACTLY the same dimension.  If not this function quits with a different 
    error message.  For example::
       
        assert_float_lists_equal: first argument 'alas' is not a list
    
    or also::
        
        assert_float_lists_equal: lists [1] and [2,3] are not comparable
    
    :param expected: The value you expect the test to have
    :type expected:  ``list`` or ``tuple``
    
    :param received: The value the test actually had
    :type received:  ``list`` or ``tuple``
    """
    import numpy
    number = [float, int]  # list of number types
    if not type(expected) in [list,tuple]:
        msg = ("assert_float_lists_equal: " +
                "first argument " + repr(expected) +" is neither a list nor tuple")
        quit_with_error(msg)
    
    if not type(received) in [list,tuple]:
        msg = ("assert_float_lists_equal: " +
                "second argument " + repr(received) +" is nneither a list nor tuple")
        quit_with_error(msg)
    
    if len(expected) != len(received):
        msg = ('assert_float_lists_equal: lists ' + repr(expected) +
                ' and ' + repr(received)+' have different sizes')
        quit_with_error(msg)
    
    try:   
        if (not numpy.allclose(expected,received)):
            msg = ("assert_float_lists_equal: expected " + repr(expected) +
                " but instead got " + repr(received))
            quit_with_error(msg)
    except:
            msg = ('assert_float_lists_equal: sequences ' + repr(expected) +
                    ' and ' + repr(received)+' are not comparable')
            quit_with_error(msg)


def assert_float_lists_not_equal(expected, received):
    """
    Quits if the lists (or tuples) of floats ``expected`` and ``received`` are the same
    
    This function takes two numbers and compares them using functions from the numerical 
    package ``numpy``.  This is a scientific computing package that allows us to test if 
    numbers are "close enough".  Hence, unlike :func:`assert_not_equal`, the meaning of 
    "same" for  this function is defined by numpy.
    
    This function is similar to :func:`assert_floats_not_equal`. The difference is that it 
    works on lists of floats.  These lists can be multidimensional.  To illustrate this, 
    the following is an example debug message::
        
        assert_float_lists_not_equal: expected something different from [[1,2],[3,4]] 
    
    **IMPORTANT**: 
    The arguments expected and received should each lists of numbers. Furthemore, they 
    must have EXACTLY the same dimension.  If not this function quits with a different 
    error message.  For example::
       
        assert_float_lists_not_equal: first argument 'alas' is not a list
    
    or also::
        
        assert_float_lists_not_equal: lists [1] and [2,3] are not comparable
    
    :param expected: The value you expect the test to have
    :type expected:  ``list`` or ``tuple``
    
    :param received: The value the test actually had
    :type received:  ``list`` or ``tuple``
    """
    import numpy
    number = [float, int]  # list of number types
    if not type(expected) in [list,tuple]:
        msg = ("assert_float_lists_not_equal: " +
                "first argument " + repr(expected) +" is neither a list nor tuple")
        quit_with_error(msg)
    
    if not type(received) in [list,tuple]:
        msg = ("assert_float_lists_not_equal: " +
                "second argument " + repr(received) +" is neither a list nor tuple")
        quit_with_error(msg)
    
    if len(expected) != len(received):
        msg = ('assert_float_lists_equal: lists ' + repr(expected) +
                ' and ' + repr(received)+' have different sizes')
        quit_with_error(msg)    
    
    try:   
        if (numpy.allclose(expected,received)):
            msg = ('assert_floats_not_equal: expected something different from' +
                    repr(expected))
            quit_with_error(msg) 
    except:
            msg = ('assert_float_lists_not_equal: sequences ' + repr(expected) +
                    ' and ' + repr(received)+' are not comparable')
            quit_with_error(msg)           