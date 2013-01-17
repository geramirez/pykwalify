# -*- coding: utf-8 -*-

retcodes = {
    # PyKwalifyExit
    0: 'noerror',

    # PyKwalifyUnknownError
    1: 'unknownerror',

    # PyKwalifyFileNotAccessible
    2: 'filenotaccessible',

    # PyKwalifyFileTypeError
    # e.g. when JsonConfig receives an erroneous file
    3: 'filetypeerror',

    # PyKwalifyOptionError
    # e.g. when PyKwalifyApplication receives an erroneous configuration
    4: 'optionerror',

    # PyKwalifyNotImplemented
    5: 'notimplemented',

    # PyKwalifyProcessorFailure
    # e.g. pdf
    6: 'processorfailure',

    # PyKwalifyWriterFailure
    # e.g. latex
    7: 'writerfailure',

    # PyKwalifyParseFailure
    # e.g. could not parse a configuration file
    8: 'parsefailure',

    # PyKwalifyConvertError
    9: "converterror",
    # e.g. when type conversion any other convert between objects

    # PyKwalifyDocumentBuildFailure
    10: "buildfailure",
    # e.g. used by Application to signal to the caller that one of the buildt document failed
           }
retnames = dict((v, k) for (k, v) in retcodes.items())


class PyKwalifyException(RuntimeError):
    """
    """

    def __init__(self, msg="", retcode=retnames['unknownerror']):
        """

        Arguments:
        - `msg`: a string
        - `retcode`: an integer, defined in PyKwalify.errors.retcodes
        """
        self.msg     = msg
        self.retcode = retcode
        self.retname = retcodes[retcode]

    def __str__(self):
        """
        """
        # <PyKwalifyException msg='foo bar' retcode=1>
        #kwargs = []
        #if self.msg:
        #        kwargs.append("msg='%s'" % self.msg)
        #if self.retcode != retnames['noerror']:
        #        kwargs.append("retcode=%d" % self.retcode)
        #if kwargs:
        #        kwargs.insert(0, '')
        #return "<%s%s>" % (self.__class__.__name__, ' '.join(kwargs))

        # <PyKwalifyException: error code 1: foo bar>
        kwargs = []
        if self.retcode != retnames['noerror']:
                kwargs.append("error code %d" % self.retcode)
        if self.msg:
                kwargs.append(self.msg)
        if kwargs:
                kwargs.insert(0, '')
        return "<%s%s>" % (self.__class__.__name__, ': '.join(kwargs))

    def __repr__(self):
        """
        """
        kwargs = []
        if self.msg:
                kwargs.append("msg='%s'" % self.msg)
        return "%s(%s)" % (self.__class__.__name__, ', '.join(kwargs))

    def msg():
        doc = """ """

        def fget(self):
            if not hasattr(self, '_msg'):
                self._msg = ''
            return self._msg

        def fset(self, value):
            assert isinstance(value, str), "argument is not string"
            self._msg = value

        return locals()
    msg = property(**msg())

    def retcode():
        doc = """ """

        def fget(self):
            if not hasattr(self, '_retcode'):
                self._retcode = retnames['unknownerror']
            return self._retcode

        def fset(self, value):
            assert isinstance(value, int), "argument is not integer"
            self._retcode = value

        return locals()
    retcode = property(**retcode())

    def retname():
        doc = """ """

        def fget(self):
            return self._retname

        def fset(self, value):
            assert isinstance(value, str), "argument is not string"
            self._retname = value

        return locals()
    retname = property(**retname())


class PyKwalifyExit(PyKwalifyException):
    """ This is the only exception that carries the error code 0, which is the
    program return code that indicates no error.
    """
    def __init__(self, *args, **kwargs):
        """
        """
        assert 'retcode' not in kwargs, "keyword retcode implicitly defined"
        super().__init__(retcode=retnames['noerror'],
                         *args, **kwargs)


class PyKwalifyUnknownError(PyKwalifyException):
    """
    """
    def __init__(self, *args, **kwargs):
        """
        """
        assert 'retcode' not in kwargs, "keyword retcode implicitly defined"
        super().__init__(retcode=retnames['unknownerror'],
                         *args, **kwargs)


class PyKwalifyFileNotAccessible(PyKwalifyException):
    """
    """
    def __init__(self, *args, **kwargs):
        """
        """
        assert 'retcode' not in kwargs, "keyword retcode implicitly defined"
        super().__init__(retcode=retnames['filenotaccessible'],
                         *args, **kwargs)


class PyKwalifyFileTypeError(PyKwalifyException):
    """
    """
    def __init__(self, *args, **kwargs):
        """
        """
        assert 'retcode' not in kwargs, "keyword retcode implicitly defined"
        super().__init__(retcode=retnames['filetypeerror'],
                         *args, **kwargs)


class PyKwalifyOptionError(PyKwalifyException):
    """
    """
    def __init__(self, *args, **kwargs):
        """
        """
        assert 'retcode' not in kwargs, "keyword retcode implicitly defined"
        super().__init__(retcode=retnames['optionerror'],
                         *args, **kwargs)


class PyKwalifyNotImplemented(PyKwalifyException):
    """
    """
    def __init__(self, *args, **kwargs):
        """
        """
        assert 'retcode' not in kwargs, "keyword retcode implicitly defined"
        super().__init__(retcode=retnames['notimplemented'],
                         *args, **kwargs)


class PyKwalifyProcessorFailure(PyKwalifyException):
    """
    """
    def __init__(self, *args, **kwargs):
        """
        """
        assert 'retcode' not in kwargs, "keyword retcode implicitly defined"
        super().__init__(retcode=retnames['processorfailure'],
                         *args, **kwargs)


class PyKwalifyWriterFailure(PyKwalifyException):
    """
    """
    def __init__(self, *args, **kwargs):
        """
        """
        assert 'retcode' not in kwargs, "keyword retcode implicitly defined"
        super().__init__(retcode=retnames['writerfailure'],
                         *args, **kwargs)


class PyKwalifyParseFailure(PyKwalifyException):
    """
    """
    def __init__(self, *args, **kwargs):
        """
        """
        assert 'retcode' not in kwargs, "keyword retcode implicitly defined"
        super().__init__(retcode=retnames['parsefailure'],
                         *args, **kwargs)


class PyKwalifyConvertError(PyKwalifyException):
    """
    """
    def __init__(self, *args, **kwargs):
        """
        """
        assert 'retcode' not in kwargs, "keyword retcode implicitly defined"
        super().__init__(retcode=retnames['converterror'],
                         *args, **kwargs)

class PyKwalifyDocumentBuildFailure(PyKwalifyException):
    """
    """
    def __init__(self, *args, **kwargs):
        """
        """
        assert "retcode" not in kwargs, "keyword retcode implicitly defined"
        super().__init__(retcode=retnames["buildfailure"],
                         *args, **kwargs)
