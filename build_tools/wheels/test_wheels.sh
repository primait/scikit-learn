#!/bin/bash

set -e
set -x

UNAME=$(uname)

if [[ "$UNAME" != "Linux" ]]; then
    # The Linux test environment is run in a Docker container and
    # it is not possible to copy the test configuration file (yet)
    cp $CONFTEST_PATH $CONFTEST_NAME
fi

# Test that there are no links to system libraries in the
# threadpoolctl output section of the show_versions output:
python -c "import pklearn; pklearn.show_versions()"

if [ ! -z "$CPU_COUNT" ]; then
    pytest --pyargs pklearn -n $CPU_COUNT
else
    pytest --pyargs pklearn
fi
