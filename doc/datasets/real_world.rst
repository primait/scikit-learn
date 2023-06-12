.. Places parent toc into the sidebar

:parenttoc: True

.. _real_world_datasets:

Real world datasets
===================

.. currentmodule:: pklearn.datasets

primakit-learn provides tools to load larger datasets, downloading them if
necessary.

They can be loaded using the following functions:

.. autosummary::

   fetch_olivetti_faces
   fetch_20newsgroups
   fetch_20newsgroups_vectorized
   fetch_lfw_people
   fetch_lfw_pairs
   fetch_covtype
   fetch_rcv1
   fetch_kddcup99
   fetch_california_housing

.. include:: ../../pklearn/datasets/descr/olivetti_faces.rst

.. include:: ../../pklearn/datasets/descr/twenty_newsgroups.rst

.. include:: ../../pklearn/datasets/descr/lfw.rst

.. include:: ../../pklearn/datasets/descr/covtype.rst

.. include:: ../../pklearn/datasets/descr/rcv1.rst

.. include:: ../../pklearn/datasets/descr/kddcup99.rst

.. include:: ../../pklearn/datasets/descr/california_housing.rst
