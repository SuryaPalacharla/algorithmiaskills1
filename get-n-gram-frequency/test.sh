#!/usr/bin/env bash


bx wsk action invoke --result cortex/get-n-gram-frequency --param-file parameters.json
