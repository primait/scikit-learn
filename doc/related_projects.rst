.. _related_projects:

=====================================
Related Projects
=====================================

Projects implementing the primakit-learn estimator API are encouraged to use
the `primakit-learn-contrib template <https://github.com/primakit-learn-contrib/project-template>`_
which facilitates best practices for testing and documenting estimators.
The `primakit-learn-contrib GitHub organization <https://github.com/primakit-learn-contrib/primakit-learn-contrib>`_
also accepts high-quality contributions of repositories conforming to this
template.

Below is a list of sister-projects, extensions and domain specific packages.

Interoperability and framework enhancements
-------------------------------------------

These tools adapt primakit-learn for use with other technologies or otherwise
enhance the functionality of primakit-learn's estimators.

**Data formats**

- `Fast svmlight / libsvm file loader <https://github.com/mblondel/svmlight-loader>`_
  Fast and memory-efficient svmlight / libsvm file loader for Python.

- `pklearn_pandas <https://github.com/paulgb/pklearn-pandas/>`_ bridge for
  primakit-learn pipelines and pandas data frame with dedicated transformers.

- `pklearn_xarray <https://github.com/phausamann/pklearn-xarray/>`_ provides
  compatibility of primakit-learn estimators with xarray data structures.

**Auto-ML**

- `auto-pklearn <https://github.com/automl/auto-pklearn/>`_
  An automated machine learning toolkit and a drop-in replacement for a
  primakit-learn estimator

- `autoviml <https://github.com/AutoViML/Auto_ViML/>`_
  Automatically Build Multiple Machine Learning Models with a Single Line of Code.
  Designed as a faster way to use primakit-learn models without having to preprocess data.

- `TPOT <https://github.com/rhiever/tpot>`_
  An automated machine learning toolkit that optimizes a series of primakit-learn
  operators to design a machine learning pipeline, including data and feature
  preprocessors as well as the estimators. Works as a drop-in replacement for a
  primakit-learn estimator.

- `Featuretools <https://github.com/alteryx/featuretools>`_
  A framework to perform automated feature engineering. It can be used for
  transforming temporal and relational datasets into feature matrices for
  machine learning.

- `Neuraxle <https://github.com/Neuraxio/Neuraxle>`_
  A library for building neat pipelines, providing the right abstractions to
  both ease research, development, and deployment of machine learning
  applications. Compatible with deep learning frameworks and primakit-learn API,
  it can stream minibatches, use data checkpoints, build funky pipelines, and
  serialize models with custom per-step savers.

- `EvalML <https://github.com/alteryx/evalml>`_
  EvalML is an AutoML library which builds, optimizes, and evaluates
  machine learning pipelines using domain-specific objective functions.
  It incorporates multiple modeling libraries under one API, and
  the objects that EvalML creates use an pklearn-compatible API.

**Experimentation frameworks**

- `Neptune <https://neptune.ai/>`_ Metadata store for MLOps,
  built for teams that run a lot of experiments.‌ It gives you a single
  place to log, store, display, organize, compare, and query all your
  model building metadata.

- `Sacred <https://github.com/IDSIA/Sacred>`_ Tool to help you configure,
  organize, log and reproduce experiments

- `REP <https://github.com/yandex/REP>`_ Environment for conducting data-driven
  research in a consistent and reproducible way

- `Scikit-Learn Laboratory
  <https://skll.readthedocs.io/en/latest/index.html>`_  A command-line
  wrapper around primakit-learn that makes it easy to run machine learning
  experiments with multiple learners and large feature sets.

**Model inspection and visualization**

- `dtreeviz <https://github.com/parrt/dtreeviz/>`_ A python library for
  decision tree visualization and model interpretation.

- `eli5 <https://github.com/TeamHG-Memex/eli5/>`_ A library for
  debugging/inspecting machine learning models and explaining their
  predictions.

- `mlxtend <https://github.com/rasbt/mlxtend>`_ Includes model visualization
  utilities.

- `pklearn-evaluation <https://github.com/ploomber/pklearn-evaluation>`_ 
  Machine learning model evaluation made easy: plots, tables, HTML reports,
  experiment tracking and Jupyter notebook analysis. Visual analysis, model
  selection, evaluation and diagnostics.

- `yellowbrick <https://github.com/DistrictDataLabs/yellowbrick>`_ A suite of
  custom matplotlib visualizers for primakit-learn estimators to support visual feature
  analysis, model selection, evaluation, and diagnostics.

**Model selection**

- `scikit-optimize <https://scikit-optimize.github.io/>`_
  A library to minimize (very) expensive and noisy black-box functions. It
  implements several methods for sequential model-based optimization, and
  includes a replacement for ``GridSearchCV`` or ``RandomizedSearchCV`` to do
  cross-validated parameter search using any of these strategies.

- `pklearn-deap <https://github.com/rsteca/pklearn-deap>`_ Use evolutionary
  algorithms instead of gridsearch in primakit-learn.

**Model export for production**

- `pklearn-onnx <https://github.com/onnx/pklearn-onnx>`_ Serialization of many
  Scikit-learn pipelines to `ONNX <https://onnx.ai/>`_ for interchange and
  prediction.

- `skops.io <https://skops.readthedocs.io/en/stable/persistence.html>`__ A
  persistence model more secure than pickle, which can be used instead of
  pickle in most common cases.

- `pklearn2pmml <https://github.com/jpmml/pklearn2pmml>`_
  Serialization of a wide variety of primakit-learn estimators and transformers
  into PMML with the help of `JPMML-SkLearn <https://github.com/jpmml/jpmml-pklearn>`_
  library.

- `pklearn-porter <https://github.com/nok/pklearn-porter>`_
  Transpile trained primakit-learn models to C, Java, Javascript and others.

- `m2cgen <https://github.com/BayesWitnesses/m2cgen>`_
  A lightweight library which allows to transpile trained machine learning
  models including many primakit-learn estimators into a native code of C, Java,
  Go, R, PHP, Dart, Haskell, Rust and many other programming languages.

- `treelite <https://treelite.readthedocs.io>`_
  Compiles tree-based ensemble models into C code for minimizing prediction
  latency.
  
**Model throughput**

- `Intel(R) Extension for primakit-learn <https://github.com/intel/primakit-learn-intelex>`_
  Mostly on high end Intel(R) hardware, accelerates some primakit-learn models
  for both training and inference under certain circumstances. This project is
  maintained by Intel(R) and primakit-learn's maintainers are not involved in the
  development of this project. Also note that in some cases using the tools and
  estimators under ``primakit-learn-intelex`` would give different results than
  ``primakit-learn`` itself. If you encounter issues while using this project,
  make sure you report potential issues in their respective repositories.


Other estimators and tasks
--------------------------

Not everything belongs or is mature enough for the central primakit-learn
project. The following are projects providing interfaces similar to
primakit-learn for additional learning algorithms, infrastructures
and tasks.

**Structured learning**

- `tslearn <https://github.com/tslearn-team/tslearn>`_ A machine learning library for time series
  that offers tools for pre-processing and feature extraction as well as dedicated models for clustering, classification and regression.

- `sktime <https://github.com/alan-turing-institute/sktime>`_ A primakit-learn compatible toolbox for machine learning with time series including time series classification/regression and (supervised/panel) forecasting.

- `HMMLearn <https://github.com/hmmlearn/hmmlearn>`_ Implementation of hidden
  markov models that was previously part of primakit-learn.

- `PyStruct <https://pystruct.github.io>`_ General conditional random fields
  and structured prediction.

- `pomegranate <https://github.com/jmschrei/pomegranate>`_ Probabilistic modelling
  for Python, with an emphasis on hidden Markov models.

- `pklearn-crfsuite <https://github.com/TeamHG-Memex/pklearn-crfsuite>`_
  Linear-chain conditional random fields
  (`CRFsuite <http://www.chokkan.org/software/crfsuite/>`_ wrapper with
  pklearn-like API).

**Deep neural networks etc.**

- `nolearn <https://github.com/dnouri/nolearn>`_ A number of wrappers and
  abstractions around existing neural network libraries

- `Keras <https://www.tensorflow.org/api_docs/python/tf/keras>`_ High-level API for
  TensorFlow with a primakit-learn inspired API.

- `lasagne <https://github.com/Lasagne/Lasagne>`_ A lightweight library to
  build and train neural networks in Theano.

- `skorch <https://github.com/dnouri/skorch>`_ A primakit-learn compatible
  neural network library that wraps PyTorch.

- `scikeras <https://github.com/adriangb/scikeras>`_ provides a wrapper around
  Keras to interface it with primakit-learn. SciKeras is the successor
  of `tf.keras.wrappers.primakit_learn`.

**Federated Learning**

- `Flower <https://flower.dev/>`_ A friendly federated learning framework with a
  unified approach that can federate any workload, any ML framework, and any programming language.

**Broad scope**

- `mlxtend <https://github.com/rasbt/mlxtend>`_ Includes a number of additional
  estimators as well as model visualization utilities.

- `scikit-lego <https://github.com/koaning/scikit-lego>`_ A number of primakit-learn compatible
  custom transformers, models and metrics, focusing on solving practical industry tasks.

**Other regression and classification**

- `xgboost <https://github.com/dmlc/xgboost>`_ Optimised gradient boosted decision
  tree library.

- `ML-Ensemble <https://mlens.readthedocs.io/>`_ Generalized
  ensemble learning (stacking, blending, subsemble, deep ensembles,
  etc.).

- `lightning <https://github.com/primakit-learn-contrib/lightning>`_ Fast
  state-of-the-art linear model solvers (SDCA, AdaGrad, SVRG, SAG, etc...).

- `py-earth <https://github.com/primakit-learn-contrib/py-earth>`_ Multivariate
  adaptive regression splines

- `Kernel Regression <https://github.com/jmetzen/kernel_regression>`_
  Implementation of Nadaraya-Watson kernel regression with automatic bandwidth
  selection

- `gplearn <https://github.com/trevorstephens/gplearn>`_ Genetic Programming
  for symbolic regression tasks.

- `scikit-multilearn <https://github.com/scikit-multilearn/scikit-multilearn>`_
  Multi-label classification with focus on label space manipulation.

- `seglearn <https://github.com/dmbee/seglearn>`_ Time series and sequence
  learning using sliding window segmentation.

- `libOPF <https://github.com/jppbsi/LibOPF>`_ Optimal path forest classifier

- `fastFM <https://github.com/ibayer/fastFM>`_ Fast factorization machine
  implementation compatible with primakit-learn

**Decomposition and clustering**

- `lda <https://github.com/lda-project/lda/>`_: Fast implementation of latent
  Dirichlet allocation in Cython which uses `Gibbs sampling
  <https://en.wikipedia.org/wiki/Gibbs_sampling>`_ to sample from the true
  posterior distribution. (primakit-learn's
  :class:`~pklearn.decomposition.LatentDirichletAllocation` implementation uses
  `variational inference
  <https://en.wikipedia.org/wiki/Variational_Bayesian_methods>`_ to sample from
  a tractable approximation of a topic model's posterior distribution.)

- `kmodes <https://github.com/nicodv/kmodes>`_ k-modes clustering algorithm for
  categorical data, and several of its variations.

- `hdbscan <https://github.com/primakit-learn-contrib/hdbscan>`_ HDBSCAN and Robust Single
  Linkage clustering algorithms for robust variable density clustering.

- `spherecluster <https://github.com/clara-labs/spherecluster>`_ Spherical
  K-means and mixture of von Mises Fisher clustering routines for data on the
  unit hypersphere.

**Pre-processing**

- `categorical-encoding
  <https://github.com/primakit-learn-contrib/categorical-encoding>`_ A
  library of pklearn compatible categorical variable encoders.

- `imbalanced-learn
  <https://github.com/primakit-learn-contrib/imbalanced-learn>`_ Various
  methods to under- and over-sample datasets.

- `Feature-engine <https://github.com/solegalli/feature_engine>`_ A library
  of pklearn compatible transformers for missing data imputation, categorical
  encoding, variable transformation, discretization, outlier handling and more.
  Feature-engine allows the application of preprocessing steps to selected groups
  of variables and it is fully compatible with the Scikit-learn Pipeline.

**Topological Data Analysis**

- `giotto-tda <https://github.com/giotto-ai/giotto-tda>`_ A library for
  `Topological Data Analysis
  <https://en.wikipedia.org/wiki/Topological_data_analysis>`_ aiming to
  provide a primakit-learn compatible API. It offers tools to transform data
  inputs (point clouds, graphs, time series, images) into forms suitable for
  computations of topological summaries, and components dedicated to
  extracting sets of scalar features of topological origin, which can be used
  alongside other feature extraction methods in primakit-learn.

Statistical learning with Python
--------------------------------
Other packages useful for data analysis and machine learning.

- `Pandas <https://pandas.pydata.org/>`_ Tools for working with heterogeneous and
  columnar data, relational queries, time series and basic statistics.

- `statsmodels <https://www.statsmodels.org>`_ Estimating and analysing
  statistical models. More focused on statistical tests and less on prediction
  than primakit-learn.

- `PyMC <https://www.pymc.io/>`_ Bayesian statistical models and
  fitting algorithms.

- `Seaborn <https://stanford.edu/~mwaskom/software/seaborn/>`_ Visualization library based on
  matplotlib. It provides a high-level interface for drawing attractive statistical graphics.

- `scikit-survival <https://scikit-survival.readthedocs.io/>`_ A library implementing
  models to learn from censored time-to-event data (also called survival analysis).
  Models are fully compatible with primakit-learn.

Recommendation Engine packages
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- `implicit <https://github.com/benfred/implicit>`_, Library for implicit
  feedback datasets.

- `lightfm <https://github.com/lyst/lightfm>`_ A Python/Cython
  implementation of a hybrid recommender system.

- `OpenRec <https://github.com/ylongqi/openrec>`_ TensorFlow-based
  neural-network inspired recommendation algorithms.

- `Spotlight <https://github.com/maciejkula/spotlight>`_ Pytorch-based
  implementation of deep recommender models.

- `Surprise Lib <https://surpriselib.com/>`_ Library for explicit feedback
  datasets.

Domain specific packages
~~~~~~~~~~~~~~~~~~~~~~~~

- `scikit-network <https://scikit-network.readthedocs.io/>`_ Machine learning on graphs.

- `scikit-image <https://scikit-image.org/>`_ Image processing and computer
  vision in python.

- `Natural language toolkit (nltk) <https://www.nltk.org/>`_ Natural language
  processing and some machine learning.

- `gensim <https://radimrehurek.com/gensim/>`_  A library for topic modelling,
  document indexing and similarity retrieval

- `NiLearn <https://nilearn.github.io/>`_ Machine learning for neuro-imaging.

- `AstroML <https://www.astroml.org/>`_  Machine learning for astronomy.

- `MSMBuilder <http://msmbuilder.org/>`_  Machine learning for protein
  conformational dynamics time series.

Translations of primakit-learn documentation
------------------------------------------

Translation's purpose is to ease reading and understanding in languages
other than English. Its aim is to help people who do not understand English
or have doubts about its interpretation. Additionally, some people prefer
to read documentation in their native language, but please bear in mind that
the only official documentation is the English one [#f1]_.

Those translation efforts are community initiatives and we have no control
on them.
If you want to contribute or report an issue with the translation, please
contact the authors of the translation.
Some available translations are linked here to improve their dissemination
and promote community efforts.

- `Chinese translation <https://pklearn.apachecn.org/>`_
  (`source <https://github.com/apachecn/pklearn-doc-zh>`__)
- `Persian translation <https://pklearn.ir/>`_
  (`source <https://github.com/mehrdad-dev/primakit-learn>`__)
- `Spanish translation <https://qu4nt.github.io/pklearn-doc-es/>`_
  (`source <https://github.com/qu4nt/pklearn-doc-es>`__)
- `Korean translation <https://panda5176.github.io/primakit-learn-korean/>`_
  (`source <https://github.com/panda5176/primakit-learn-korean>`__)


.. rubric:: Footnotes

.. [#f1] following `linux documentation Disclaimer
   <https://www.kernel.org/doc/html/latest/translations/index.html#disclaimer>`__
