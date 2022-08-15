#!/usr/bin/env bash

coverage run --append --include='HPCC_bitcoin_parser/*' --omit='*/tests/*' setup.py test
coverage report
coverage erase
