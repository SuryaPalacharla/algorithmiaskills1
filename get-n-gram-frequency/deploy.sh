#!/usr/bin/env bash
set -eu
bx wsk -i action update cortex/get-n-gram-frequency __main__.py
