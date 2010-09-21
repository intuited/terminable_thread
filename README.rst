``terminable_thread``
=====================

``terminable_thread`` provides a subclass of ``threading.Thread``,
adding the facility to raise exceptions
in the context of the given thread.

This facility is incorporated in the ``terminable_thread.Thread`` methods
``raise_exc``, which raises an arbitrary exception,
and ``terminate``, which raises SystemExit.

This is not done in an entirely robust manner,
and there may be unreported issues with it.

It uses the unexposed ``PyThreadState_SetAsyncExc`` function (via ``ctypes``)
to raise an exception for the given thread.


History
-------

The code used in this module is taken most directly from Tomer Filiba's
`thread2 recipe`_.

Similar code has been floating around the net
for some time now in various incarnations;
however, the code on Tomer's page seems to be the most complete.

His page references a post by Antoon Pardon, previously available at
`<http://mail.python.org/pipermail/python-list/2005-December/316143.html>`_,
as an inspiration.

Tomer has indicated that the code on his page is in the public domain.

.. _thread2 recipe: http://sebulba.wikispaces.com/recipe+thread2


Issues
------

The following issues are mentioned on `the recipe page`_:

- The exception will be raised only when executing python bytecode.
  If your thread calls a native/built-in blocking function,
  the exception will be raised only when execution returns to the python code.
  
  - There is also an issue 
    if the built-in function internally calls PyErr\_Clear(),
    which would effectively cancel your pending exception.
    You can try to raise it again.

- Only exception **types** can be raised safely.
  Exception instances are likely to cause unexpected behavior,
  and are thus restricted.
  
  - For example:
    t1.raise\_exc(TypeError) and not t1.raise\_exc(TypeError("blah")).
  - IMHO it's a bug, and I reported it as one. For more info,
    `<http://mail.python.org/pipermail/python-dev/2006-August/068158.html>`_

- I asked to expose this function in the built-in thread module,
  but since ctypes has become a standard library (as of 2.5),
  and this feature is not likely to be implementation-agnostic,
  it may be kept unexposed.

In addition to these issues,
or rather as an elaboration of the first one,
I've noticed that catching of exceptions does not function as expected.

Specifically:

  If the thread wraps some functions with a try/except clause,
  the except may not catch an interrupt exception.
  This will happen, for instance, with a ``time.sleep`` call.

  For an example of this,
  see the method ``FetcherTester.test_incorrect_fission``
  in the test suite for the `pqueue\_fetcher`_ module.

  I guess I'll port that test into this module at some point.

.. _the recipe page: http://sebulba.wikispaces.com/recipe+thread2
.. _pqueue\_fetcher: http://github.com/intuited/pqueue_fetcher

Distribution
------------

``terminable_thread`` is available from the `github repo`_ or from `PyPI`_.

.. _github repo: http://github.com/intuited/terminable_thread
.. _PyPI: http://pypi.python.org/pypi/terminable_thread


License
-------

As mentioned above,
Tomer has indicated that the code on `his site`_ is public domain.

I'm not entirely sure what that means legally, since

- the term "public domain" is often used informally,
  to just mean that no license has been applied.
- the definition of "public domain", when used formally,
  is dependent on the laws of a particular region.

So it's a bit complicated and vague,
but he did say that I could do whatever I wanted with it,
so I've chosen to prevent such ambiguities in the future
by licensing this derivation under the `WTFPL`_.

The license terms are given in the file ``COPYING``.

.. _his site: `the recipe page`_
.. _WTFPL: http://sam.zoy.org/wtfpl/


(Lack of) Warranty
------------------

As mentioned at the top,
I myself am not entirely convinced of the reliability of this code.

I might get around to writing a more thorough test suite at some point.

Please bear that, as well as the following Official Disclaimer,
in mind when (considering) using it:

  This program is free software.
  It comes without any warranty, to the extent permitted by applicable law.
  You can redistribute it and/or modify it under the terms of the
  Do What The Fuck You Want To Public License, Version 2,
  as published by Sam Hocevar.
  See `<http://sam.zoy.org/wtfpl/COPYING>`_ for more details.
