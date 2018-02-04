#!/usr/bin/env bash
set -eu
bx wsk -i action update cortex/keywords-for-document-set __main__.py
