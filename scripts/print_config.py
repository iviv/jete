#!/usr/bin/env python3
"""
print_config.py
Loads the deployment config written by Pipeline 1 and prints a summary message.
Expected JSON location (relative to repo root): configs/data.json
"""

import json
import os
import sys


JSON_FILE = os.path.join(os.path.dirname(__file__), '..', 'configs', 'data.json')


def load_config(path: str) -> dict:
    abs_path = os.path.abspath(path)
    if not os.path.exists(abs_path):
        print(f"[ERROR] Config file not found: {abs_path}", file=sys.stderr)
        sys.exit(1)

    with open(abs_path, 'r') as f:
        try:
            return json.load(f)
        except json.JSONDecodeError as e:
            print(f"[ERROR] Failed to parse JSON: {e}", file=sys.stderr)
            sys.exit(1)


def print_config(config: dict) -> None:
    required_fields = ['env', 'version', 'region']
    missing = [field for field in required_fields if field not in config]
    if missing:
        print(f"[ERROR] Missing fields in config: {missing}", file=sys.stderr)
        sys.exit(1)

    print("=" * 50)
    print("  Deployment Configuration")
    print("=" * 50)
    print(f"  Environment : {config['env']}")
    print(f"  Version     : {config['version']}")
    print(f"  Region      : {config['region']}")
    print("=" * 50)
    print(
        f"\n[OK] Deploying version '{config['version']}' to the "
        f"'{config['env']}' environment in region '{config['region']}'.\n"
    )


if __name__ == '__main__':
    config = load_config(JSON_FILE)
    print_config(config)
