#!/usr/bin/env bash
set -euo pipefail
# Packaging script for Alexa Lambda function
# Usage: run from repository root or execute directly

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$HERE"

echo "Cleaning previous build..."
rm -rf package function.zip

echo "Installing dependencies into package/"
python3 -m pip install -r requirements.txt -t package/

echo "Copying skill code and APL..."
cp -r apl package/ || true
cp skill.py package/

echo "Creating function.zip..."
cd package
zip -r ../function.zip .
cd "$HERE"

echo "Created: $HERE/function.zip"
