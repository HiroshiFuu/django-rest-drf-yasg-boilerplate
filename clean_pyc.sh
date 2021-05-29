#!/bin/sh

echo cmd delete all .pyc files
find . -name "*.pyc" -type f -delete
echo Done!
