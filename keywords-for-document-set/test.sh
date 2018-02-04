#!/usr/bin/env bash


bx wsk action invoke --result cortex/keywords-for-document-set --param-file parameters.json
