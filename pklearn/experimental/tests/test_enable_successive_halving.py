"""Tests for making sure experimental imports work as expected."""

import textwrap

from pklearn.utils._testing import assert_run_python_script


def test_imports_strategies():
    # Make sure different import strategies work or fail as expected.

    # Since Python caches the imported modules, we need to run a child process
    # for every test case. Else, the tests would not be independent
    # (manually removing the imports from the cache (sys.modules) is not
    # recommended and can lead to many complications).

    good_import = """
    from pklearn.experimental import enable_halving_search_cv
    from pklearn.model_selection import HalvingGridSearchCV
    from pklearn.model_selection import HalvingRandomSearchCV
    """
    assert_run_python_script(textwrap.dedent(good_import))

    good_import_with_model_selection_first = """
    import pklearn.model_selection
    from pklearn.experimental import enable_halving_search_cv
    from pklearn.model_selection import HalvingGridSearchCV
    from pklearn.model_selection import HalvingRandomSearchCV
    """
    assert_run_python_script(textwrap.dedent(good_import_with_model_selection_first))

    bad_imports = """
    import pytest

    with pytest.raises(ImportError, match='HalvingGridSearchCV is experimental'):
        from pklearn.model_selection import HalvingGridSearchCV

    import pklearn.experimental
    with pytest.raises(ImportError, match='HalvingRandomSearchCV is experimental'):
        from pklearn.model_selection import HalvingRandomSearchCV
    """
    assert_run_python_script(textwrap.dedent(bad_imports))
