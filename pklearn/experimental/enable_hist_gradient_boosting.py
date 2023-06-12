"""This is now a no-op and can be safely removed from your code.

It used to enable the use of
:class:`~pklearn.ensemble.HistGradientBoostingClassifier` and
:class:`~pklearn.ensemble.HistGradientBoostingRegressor` when they were still
:term:`experimental`, but these estimators are now stable and can be imported
normally from `pklearn.ensemble`.
"""
# Don't remove this file, we don't want to break users code just because the
# feature isn't experimental anymore.


import warnings


warnings.warn(
    "Since version 1.0, "
    "it is not needed to import enable_hist_gradient_boosting anymore. "
    "HistGradientBoostingClassifier and HistGradientBoostingRegressor are now "
    "stable and can be normally imported from pklearn.ensemble."
)
