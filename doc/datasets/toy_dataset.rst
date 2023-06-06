.. Places parent toc into the sidebar

:parenttoc: True

.. _toy_datasets:

Toy datasets
============

.. currentmodule:: pklearn.datasets

primakit-learn comes with a few small standard datasets that do not require to
download any file from some external website.

They can be loaded using the following functions:

.. autosummary::

   load_iris
   load_diabetes
   load_digits
   load_linnerud
   load_wine
   load_breast_cancer

These datasets are useful to quickly illustrate the behavior of the
various algorithms implemented in primakit-learn. They are however often too
small to be representative of real world machine learning tasks.

.. include:: ../../pklearn/datasets/descr/iris.rst

.. include:: ../../pklearn/datasets/descr/diabetes.rst

.. include:: ../../pklearn/datasets/descr/digits.rst

.. include:: ../../pklearn/datasets/descr/linnerud.rst

.. include:: ../../pklearn/datasets/descr/wine_data.rst

.. include:: ../../pklearn/datasets/descr/breast_cancer.rst
