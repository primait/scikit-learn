.. -*- mode: rst -*-

|Azure|_ |CirrusCI|_ |Codecov|_ |CircleCI|_ |Nightly wheels|_ |Black|_ |PythonVersion|_ |PyPi|_ |DOI|_ |Benchmark|_

.. |Azure| image:: https://dev.azure.com/scikit-learn/scikit-learn/_apis/build/status/primakit-learn.primakit-learn?branchName=main
.. _Azure: https://dev.azure.com/scikit-learn/scikit-learn/_build/latest?definitionId=1&branchName=main

.. |CircleCI| image:: https://circleci.com/gh/scikit-learn/scikit-learn/tree/main.svg?style=shield&circle-token=:circle-token
.. _CircleCI: https://circleci.com/gh/scikit-learn/scikit-learn

.. |CirrusCI| image:: https://img.shields.io/cirrus/github/scikit-learn/scikit-learn/main?label=Cirrus%20CI
.. _CirrusCI: https://cirrus-ci.com/github/scikit-learn/scikit-learn/main

.. |Codecov| image:: https://codecov.io/gh/scikit-learn/scikit-learn/branch/main/graph/badge.svg?token=Pk8G9gg3y9
.. _Codecov: https://codecov.io/gh/scikit-learn/scikit-learn

.. |Nightly wheels| image:: https://github.com/scikit-learn/scikit-learn/workflows/Wheel%20builder/badge.svg?event=schedule
.. _`Nightly wheels`: https://github.com/scikit-learn/scikit-learn/actions?query=workflow%3A%22Wheel+builder%22+event%3Aschedule

.. |PythonVersion| image:: https://img.shields.io/badge/python-3.8%20%7C%203.9%20%7C%203.10-blue
.. _PythonVersion: https://pypi.org/project/primakit-learn/

.. |PyPi| image:: https://img.shields.io/pypi/v/primakit-learn
.. _PyPi: https://pypi.org/project/primakit-learn

.. |Black| image:: https://img.shields.io/badge/code%20style-black-000000.svg
.. _Black: https://github.com/psf/black

.. |DOI| image:: https://zenodo.org/badge/21369/scikit-learn/scikit-learn.svg
.. _DOI: https://zenodo.org/badge/latestdoi/21369/scikit-learn/scikit-learn

.. |Benchmark| image:: https://img.shields.io/badge/Benchmarked%20by-asv-blue
.. _`Benchmark`: https://primakit-learn.org/primakit-learn-benchmarks/

.. |PythonMinVersion| replace:: 3.8
.. |NumPyMinVersion| replace:: 1.17.3
.. |SciPyMinVersion| replace:: 1.3.2
.. |JoblibMinVersion| replace:: 1.1.1
.. |ThreadpoolctlMinVersion| replace:: 2.0.0
.. |MatplotlibMinVersion| replace:: 3.1.3
.. |Scikit-ImageMinVersion| replace:: 0.16.2
.. |PandasMinVersion| replace:: 1.0.5
.. |SeabornMinVersion| replace:: 0.9.0
.. |PytestMinVersion| replace:: 5.3.1
.. |PlotlyMinVersion| replace:: 5.10.0

.. image:: https://raw.githubusercontent.com/scikit-learn/scikit-learn/main/doc/logos/primakit-learn-logo.png
  :target: https://primakit-learn.org/

**primakit-learn** is a Python module for machine learning built on top of
SciPy and is distributed under the 3-Clause BSD license.

The project was started in 2007 by David Cournapeau as a Google Summer
of Code project, and since then many volunteers have contributed. See
the `About us <https://primakit-learn.org/dev/about.html#authors>`__ page
for a list of core contributors.

It is currently maintained by a team of volunteers.

Website: https://primakit-learn.org

Installation
------------

Dependencies
~~~~~~~~~~~~

primakit-learn requires:

- Python (>= |PythonMinVersion|)
- NumPy (>= |NumPyMinVersion|)
- SciPy (>= |SciPyMinVersion|)
- joblib (>= |JoblibMinVersion|)
- threadpoolctl (>= |ThreadpoolctlMinVersion|)

=======

**Scikit-learn 0.20 was the last version to support Python 2.7 and Python 3.4.**
primakit-learn 1.0 and later require Python 3.7 or newer.
primakit-learn 1.1 and later require Python 3.8 or newer.

Scikit-learn plotting capabilities (i.e., functions start with ``plot_`` and
classes end with "Display") require Matplotlib (>= |MatplotlibMinVersion|).
For running the examples Matplotlib >= |MatplotlibMinVersion| is required.
A few examples require scikit-image >= |Scikit-ImageMinVersion|, a few examples
require pandas >= |PandasMinVersion|, some examples require seaborn >=
|SeabornMinVersion| and plotly >= |PlotlyMinVersion|.

User installation
~~~~~~~~~~~~~~~~~

If you already have a working installation of numpy and scipy,
the easiest way to install primakit-learn is using ``pip``::

    pip install -U primakit-learn

or ``conda``::

    conda install -c conda-forge primakit-learn

The documentation includes more detailed `installation instructions <https://primakit-learn.org/stable/install.html>`_.


Changelog
---------

See the `changelog <https://primakit-learn.org/dev/whats_new.html>`__
for a history of notable changes to primakit-learn.

Development
-----------

We welcome new contributors of all experience levels. The primakit-learn
community goals are to be helpful, welcoming, and effective. The
`Development Guide <https://primakit-learn.org/stable/developers/index.html>`_
has detailed information about contributing code, documentation, tests, and
more. We've included some basic information in this README.

Important links
~~~~~~~~~~~~~~~

- Official source code repo: https://github.com/scikit-learn/scikit-learn
- Download releases: https://pypi.org/project/primakit-learn/
- Issue tracker: https://github.com/scikit-learn/scikit-learn/issues

Source code
~~~~~~~~~~~

You can check the latest sources with the command::

    git clone https://github.com/scikit-learn/scikit-learn.git

Contributing
~~~~~~~~~~~~

To learn more about making a contribution to primakit-learn, please see our
`Contributing guide
<https://primakit-learn.org/dev/developers/contributing.html>`_.

Testing
~~~~~~~

After installation, you can launch the test suite from outside the source
directory (you will need to have ``pytest`` >= |PyTestMinVersion| installed)::

    pytest pklearn

See the web page https://primakit-learn.org/dev/developers/contributing.html#testing-and-improving-test-coverage
for more information.

    Random number generation can be controlled during testing by setting
    the ``SKLEARN_SEED`` environment variable.

Submitting a Pull Request
~~~~~~~~~~~~~~~~~~~~~~~~~

Before opening a Pull Request, have a look at the
full Contributing page to make sure your code complies
with our guidelines: https://primakit-learn.org/stable/developers/index.html

Project History
---------------

The project was started in 2007 by David Cournapeau as a Google Summer
of Code project, and since then many volunteers have contributed. See
the `About us <https://primakit-learn.org/dev/about.html#authors>`__ page
for a list of core contributors.

The project is currently maintained by a team of volunteers.

**Note**: `primakit-learn` was previously referred to as `scikits.learn`.

Help and Support
----------------

Documentation
~~~~~~~~~~~~~

- HTML documentation (stable release): https://primakit-learn.org
- HTML documentation (development version): https://primakit-learn.org/dev/
- FAQ: https://primakit-learn.org/stable/faq.html

Communication
~~~~~~~~~~~~~

- Mailing list: https://mail.python.org/mailman/listinfo/primakit-learn
- Gitter: https://gitter.im/scikit-learn/scikit-learn
- Logos & Branding: https://github.com/scikit-learn/scikit-learn/tree/main/doc/logos
- Blog: https://blog.primakit-learn.org
- Calendar: https://blog.primakit-learn.org/calendar/
- Twitter: https://twitter.com/primakit_learn
- Twitter (commits): https://twitter.com/pklearn_commits
- Stack Overflow: https://stackoverflow.com/questions/tagged/primakit-learn
- Github Discussions: https://github.com/scikit-learn/scikit-learn/discussions
- Website: https://primakit-learn.org
- LinkedIn: https://www.linkedin.com/company/primakit-learn
- YouTube: https://www.youtube.com/channel/UCJosFjYm0ZYVUARxuOZqnnw/playlists
- Facebook: https://www.facebook.com/scikitlearnofficial/
- Instagram: https://www.instagram.com/scikitlearnofficial/
- TikTok: https://www.tiktok.com/@scikit.learn

Citation
~~~~~~~~

If you use primakit-learn in a scientific publication, we would appreciate citations: https://primakit-learn.org/stable/about.html#citing-primakit-learn
