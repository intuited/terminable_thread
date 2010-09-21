`terminable_thread`
===================

The code in this module is taken, with a patch,
  from Tomer Filiba's [thread2 recipe].
  
It provides a subclass of Thread with facilities
  to raise an exception in the thread
  or terminate the thread from another thread.

Issues
------

These issues are mentioned on [the recipe page][thread2 recipe]:

-   The exception will be raised only when executing python
    bytecode. If your thread calls a native/built-in blocking function,
    the exception will be raised only when execution returns to the
    python code.
    -   There is also an issue if the built-in function internally
        calls PyErr\_Clear(), which would effectively cancel your pending
        exception. You can try to raise it again.

-   Only exception **types** can be raised safely. Exception
    instances are likely to cause unexpected behavior, and are thus
    restricted.
    -   For example: t1.raise\_exc(TypeError) and
        not t1.raise\_exc(TypeError("blah")).
    -   IMHO it's a bug, and I reported it as one. For more
        info, [http://mail.python.org/pipermail/python-dev/2006-August/068158.html][2]

-   I asked to expose this function in the built-in thread module,
    but since ctypes has become a standard library (as of 2.5), and
    this feature is not likely to be implementation-agnostic, it may be
    kept unexposed.

In addition to these issues, or rather as an elaboration of the first one,
  I've noticed that catching of exceptions does not function as expected.

Specifically, if the thread wraps a blocking function with a try/except clause,
  the except may not catch an interrupt exception.

For an example of this, see the method `FetcherTester.test_incorrect_fission`
  in the test suite for the [pqueue_fetcher] module.

I guess I'll port that test into this module at some point.


Distribution
------------

`terminable_thread` is available from the [github repo].

An `easy_install` -able package can be downloaded from
  [http://github.com/intuited/terminable_thread/raw/dist/dist/terminable_thread-0.6.4.tar.gz][1],
  or for a more recent version, a different file with a similar name.

License
-------

I'm not really sure what to do about this.

Code similar to Tomer's has been floating around the Internet for a while,
  however his code seems to be the most complete that I've discovered.

His page itself references a [post by Antoon Pardon],
  previously available at
  (http://mail.python.org/pipermail/python-list/2005-December/316143.html),
  as an inspiration.

Tomer's wikispaces doesn't seem to mention anything about licensing;
  as I understand it, wikispaces pages are by default licensed under a
  [Creative Commons Attribution-ShareAlike] license.

Since that license is not necessarily suitable to source code,
  I'm tentatively placing this module under the [GPL],
  which is similar in that it requires both attribution
  and propagation of the license.
See the file `COPYING` for the full license.

I've written to Tomer to ask him to let me know
  if he has objections to this module's distribution.

[thread2 recipe]: http://sebulba.wikispaces.com/recipe+thread2
[github repo]: http://github.com/intuited/terminable_thread
[post by Antoon Pardon]: http://mail.python.org/pipermail/python-list/2005-December/316143.html
[Creative Commons Attribution-ShareAlike]: http://creativecommons.org/licenses/by-sa/3.0/
[pqueue_fetcher]: http://github.com/intuited/pqueue_fetcher
[1]: http://github.com/intuited/terminable_thread/raw/dist/dist/terminable_thread-0.6.4.tar.gz
[2]: http://mail.python.org/pipermail/python-dev/2006-August/068158.html
[GPL]: http://www.gnu.org/licenses/gpl.html
