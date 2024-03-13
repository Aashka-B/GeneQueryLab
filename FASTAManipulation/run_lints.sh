#!/bin/bash

# v1.0.2

# pylint 2.4.4
# astroid 2.3.3
# Python 3.6.0 (default, Jan 16 2020, 13:24:17)
# [GCC 4.2.1 Compatible Apple LLVM 11.0.0 (clang-1100.0.33.16)]
# cleslin@cleslinMacBook16[BINF6200]# flake8 --version
# 3.7.9 (mccabe: 0.6.1, pycodestyle: 2.5.0, pyflakes: 2.1.1) CPython 3.6.0 on Darwinsh

set -e
# Search Results
# set -e stops the execution of a script if a command or pipeline has an error - 
# which is the opposite of the default shell behaviour, which is to ignore errors in scripts

if [ $# -eq 0 ]
  then
    echo "No directory supplied, eg: bash $0 assignment2"
    exit
fi

ENFORCED_FILES="
$1
"

# Disable R0914: Too many local variables
# Disable E0401: Flask CORS ext
# Disable C0121: Comparison to True should be just 'expr' 
# assigment 3 on...
# Disable R0801: Similar lines in 2 files
# Disable R1705: Unnecessary "else" after "return"
# Disable R1732: Consider using 'with' for resource-allocating operations (consider-using-with)"
MAX_LINE_LEN="--max-line-length=120"

echo "Running pylint..."
pylint  \
--extension-pkg-whitelist=math \
--disable=R0914,E0401,C0121,R0801,R1705,R1732 $MAX_LINE_LEN \
--msg-template='{abspath}:{line:3d}: {obj}: {msg_id}:{msg}' \
$ENFORCED_FILES

# assignment 3 on...
# Disable: E712 comparison to True should be 'if cond is True:' or 'if cond:'
# Disable:  W504 line break after binary operator
echo -e "\n\nRunning flake8..."
flake8  --max-complexity 12 --benchmark $MAX_LINE_LEN --ignore=R0914,E712,W504 $ENFORCED_FILES

echo -e "\n\n*****Nice work! All lints passed successfully.****"
