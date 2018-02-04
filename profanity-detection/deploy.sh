#!/usr/bin/env bash
set -eu
bx wsk -i action update cortex/profanity_detection __main__.py
