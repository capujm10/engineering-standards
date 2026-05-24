#!/usr/bin/env python3
"""
validate-repo.py
Enforces portfolio engineering standards. Validates local metadata against governance schemas,
checks standard folder architecture compliance, and ensures telemetry patterns are correct.
"""

import os
import sys
import json
import argparse
import yaml
from jsonschema import validate, exceptions

def load_yaml(file_path):
    if not os.path.exists(file_path):
        print(f"[-] Error: Target file '{file_path}' does not exist.")
        sys.exit(1)
    with open(file_path, 'r', encoding='utf-8') as f:
        try:
            return yaml.safe_load(f)
        except yaml.YAMLError as exc:
            print(f"[-] Error: Failed to parse YAML file '{file_path}': {exc}")
            sys.exit(1)

def load_json(file_path):
    if not os.path.exists(file_path):
        print(f"[-] Error: JSON file '{file_path}' does not exist.")
        sys.exit(1)
    with open(file_path, 'r', encoding='utf-8') as f:
        try:
            return json.load(f)
        except json.JSONDecodeError as exc:
            print(f"[-] Error: Failed to parse JSON file '{file_path}': {exc}")
            sys.exit(1)

def validate_schema(data, schema):
    try:
        validate(instance=data, schema=schema)
        print("[+] Success: governance.yml matches JSON validation schema perfectly.")
        return True
    except exceptions.ValidationError as err:
        print(f"[-] Standards Validation Failure: {err.message}")
        print(f"    Path to failure: {list(err.absolute_path)}")
        return False

def verify_folder_compliance(repo_path, metadata):
    print("[*] Auditing folder structure & licensing compliance...")
    
    # 1. Verify License File existence
    compliance = metadata.get("compliance", {})
    license_file_name = compliance.get("license_file", "LICENSE")
    license_path = os.path.join(repo_path, license_file_name)
    
    if not os.path.exists(license_path):
        print(f"[-] Compliance Failure: Standard license file '{license_file_name}' not found at repository root.")
        return False
    print(f"[+] Compliance Check: Found license file '{license_file_name}'.")

    # 2. Verify AI cursorrules configuration
    cursorrules_path = os.path.join(repo_path, ".cursorrules")
    if not os.path.exists(cursorrules_path):
        # Fallback to templates/ if checking the standards repo itself
        standards_rules = os.path.join(repo_path, "prompts", ".cursorrules")
        if not os.path.exists(standards_rules):
            print("[-] Compliance Warning: Coding assistant config '.cursorrules' not found at repository root.")
        else:
            print("[+] Compliance Check: Found active editor constraints under prompts/.")
    else:
        print("[+] Compliance Check: Found active root '.cursorrules' coding constraints.")
        
    return True

def run_observability_audit(repo_path, metadata):
    print("[*] Running capability-oriented observability standard check...")
    obs = metadata.get("observability", {})
    framework = obs.get("framework")
    
    if not framework:
        print("[-] Observability standard failure: 'framework' must be defined under observability.")
        return False
    
    print(f"[+] Observability verification: Found framework '{framework}' configurations.")
    
    # Capability checks
    caps = metadata.get("capabilities", {}).get("telemetry", {})
    if caps.get("metrics"):
        metrics_port = obs.get("metrics", {}).get("port") or obs.get("metrics_port")
        print(f"[+] Observability verification: Metrics capability is enabled.")
        
    return True

def main():
    parser = argparse.ArgumentParser(description="Portfolio Standards & Governance Validator CLI")
    parser.add_argument("--schema", help="Path to central JSON schema definition", required=False)
    parser.add_argument("--target", help="Path to file/directory to validate", required=True)
    parser.add_argument("--observability", action="store_true", help="Perform deep telemetry check")
    parser.add_argument("--audit", action="store_true", help="Audit local folder layout and licenses")
    
    args = parser.parse_args()
    
    governance_file = args.target
    if os.path.isdir(args.target):
        governance_file = os.path.join(args.target, "governance.yml")
        
    # Read the governance.yml metadata
    data = load_yaml(governance_file)
    
    if args.schema:
        print(f"[*] Validating target file: {governance_file} against schema: {args.schema}")
        schema = load_json(args.schema)
        success = validate_schema(data, schema)
        if not success:
            sys.exit(1)
            
    if args.audit:
        target_dir = args.target if os.path.isdir(args.target) else os.path.dirname(args.target)
        success = verify_folder_compliance(target_dir, data)
        if not success:
            sys.exit(1)
            
    if args.observability:
        target_dir = args.target if os.path.isdir(args.target) else os.path.dirname(args.target)
        success = run_observability_audit(target_dir, data)
        if not success:
            sys.exit(1)
            
    print("[+] Repository validation completed successfully.")

if __name__ == "__main__":
    main()
