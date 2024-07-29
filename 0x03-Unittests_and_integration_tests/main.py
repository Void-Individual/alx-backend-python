#!/usr/bin/env python3
"""Test module for the utils file"""

from client import (GithubOrgClient)

payload = "org_payload"

github_client = GithubOrgClient("abc")
res = github_client.org
print(res)
