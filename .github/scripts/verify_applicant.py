#!/usr/bin/env python3
import os
import json
import urllib.request
import urllib.error
import re

# AMF Research Quadrants Keyword Substrates
QUADRANT_PATTERNS = {
    "Quadrant I (Database-Resident Governance - pg-policy)": {
        "keywords": ["postgres", "sql", "database", "rls", "policy", "security", "extension", "dbms", "authorization", "plpgsql", "audit", "referee"],
        "languages": ["sql", "c", "c++", "rust", "go"],
        "description": "Bringing policy engines, access control, and tool guardrails next to data within the database trust boundary."
    },
    "Quadrant II (Holographic Compositional Memory - HMRBench)": {
        "keywords": ["vector", "embedding", "associative", "memory", "quantization", "convolution", "fft", "hrr", "dense", "rag", "tensor", "kashin", "holographic"],
        "languages": ["c++", "python", "rust", "julia"],
        "description": "High-dimensional vector binding, circular convolution, and structural unbinding to resolve role-filler pairs."
    },
    "Quadrant III (Local Principal Directions - Grassmanian)": {
        "keywords": ["routing", "manifold", "kmeans", "cluster", "pca", "ann", "hnsw", "search", "math", "geometry", "linear", "grassmanian", "subspace", "vector-search"],
        "languages": ["python", "c++", "rust", "matlab", "r"],
        "description": "Mapping query routing signals onto local cluster shapes represented as affine k-flats and manifolds."
    },
    "Quadrant IV (Virtual Directory Indexing - repo-atlas)": {
        "keywords": ["agent", "llm", "indexing", "files", "atlas", "tool", "map", "cognitive", "refactor", "autogen", "crewai", "langchain", "langgraph", "agents.md"],
        "languages": ["python", "typescript", "javascript"],
        "description": "Analyzing file-system pathways and virtual semantic maps as retrieval indexes for autonomous coding agents."
    }
}

def make_request(url, method="GET", data=None, headers=None):
    if headers is None:
        headers = {}
    
    # Standard GITHUB_TOKEN or custom token for auth
    token = os.getenv("AMF_ORG_INVITE_TOKEN") or os.getenv("GITHUB_TOKEN")
    if token and "Authorization" not in headers:
        headers["Authorization"] = f"token {token}"
    
    headers["Accept"] = "application/vnd.github+json"
    headers["User-Agent"] = "Agentic-Memory-Foundation-Evaluator"
    
    req_data = None
    if data is not None:
        req_data = json.dumps(data).encode("utf-8")
        headers["Content-Type"] = "application/json"
        
    req = urllib.request.Request(url, data=req_data, headers=headers, method=method)
    
    try:
        with urllib.request.urlopen(req) as response:
            return response.status, json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        try:
            err_body = e.read().decode("utf-8")
            return e.code, json.loads(err_body)
        except Exception:
            return e.code, {"message": str(e)}
    except Exception as e:
        return 500, {"message": str(e)}

def parse_issue_payload():
    event_path = os.getenv("GITHUB_EVENT_PATH")
    if not event_path:
        print("Error: GITHUB_EVENT_PATH not set.")
        return None
        
    with open(event_path, "r") as f:
        event = json.load(f)
        
    issue = event.get("issue", {})
    issue_number = issue.get("number")
    issue_body = issue.get("body", "")
    username = issue.get("user", {}).get("login")
    
    # Attempt to extract a custom username if they provided one in the form
    # The form field id is github_handle
    match = re.search(r"### GitHub Handle\s*\n\s*(\S+)", issue_body)
    if match:
        extracted = match.group(1).strip().replace("@", "")
        if extracted:
            username = extracted
            
    return {
        "issue_number": issue_number,
        "username": username,
        "body": issue_body
    }

def evaluate_repositories(username):
    print(f"Fetching GitHub profile for: {username}")
    status, user_info = make_request(f"https://api.github.com/users/{username}")
    if status != 200:
        print(f"Error fetching profile: {user_info.get('message')}")
        return None
        
    print(f"Fetching public repositories for: {username}")
    status, repos = make_request(f"https://api.github.com/users/{username}/repos?sort=updated&per_page=15")
    if status != 200:
        print(f"Error fetching repositories: {repos.get('message')}")
        return None
        
    # Analyze profile metadata
    bio = user_info.get("bio") or ""
    public_repos_count = user_info.get("public_repos", 0)
    followers = user_info.get("followers", 0)
    
    quadrant_scores = {q: 0 for q in QUADRANT_PATTERNS}
    relevant_repos = []
    
    # Process repositories
    for repo in repos:
        if repo.get("fork", False):
            continue  # Focus on original work
            
        name = (repo.get("name") or "").lower()
        desc = (repo.get("description") or "").lower()
        lang = (repo.get("language") or "").lower()
        stars = repo.get("stargazers_count", 0)
        
        repo_matched = False
        matched_quadrants = []
        
        for q_name, q_data in QUADRANT_PATTERNS.items():
            keyword_matches = [kw for kw in q_data["keywords"] if kw in name or kw in desc]
            lang_match = lang in q_data["languages"] if lang else False
            
            score_increment = len(keyword_matches) * 2
            if lang_match and len(keyword_matches) > 0:
                score_increment += 1
                
            if score_increment > 0:
                quadrant_scores[q_name] += score_increment
                repo_matched = True
                matched_quadrants.append(q_name)
                
        if repo_matched:
            relevant_repos.append({
                "name": repo.get("name"),
                "html_url": repo.get("html_url"),
                "description": repo.get("description") or "No description provided.",
                "stars": stars,
                "language": repo.get("language") or "Unknown",
                "matched_quadrants": matched_quadrants
            })
            
    # Sort relevant repositories by star count and matches
    relevant_repos.sort(key=lambda r: (r["stars"], len(r["matched_quadrants"])), reverse=True)
    
    return {
        "user_info": user_info,
        "quadrant_scores": quadrant_scores,
        "relevant_repos": relevant_repos[:5] # Keep top 5
    }

def generate_report(username, evaluation):
    if not evaluation:
        return f"### ⚠️ Telemetry Evaluation Interrupted\n\nCould not fetch public telemetry for user `{username}`. Please ensure the GitHub handle is valid and publicly accessible."
        
    u_info = evaluation["user_info"]
    q_scores = evaluation["quadrant_scores"]
    rel_repos = evaluation["relevant_repos"]
    
    # Determine approval status based on score threshold
    total_score = sum(q_scores.values())
    approved = total_score >= 2
    
    # Build ascii bar charts for scores
    bar_charts = []
    for q_name, score in q_scores.items():
        bar_len = min(10, score)
        bar = "█" * bar_len + "░" * (10 - bar_len)
        bar_charts.append(f"`{bar}` ({score} pts) — {q_name}")
        
    bar_chart_str = "\n".join(bar_charts)
    
    # Repositories Section
    repos_str = ""
    if rel_repos:
        for r in rel_repos:
            quad_tags = ", ".join([q.split(" (")[0] for q in r["matched_quadrants"]])
            repos_str += f"- **[{r['name']}]({r['html_url']})** (`{r['language']}`, ⭐ {r['stars']})\n"
            repos_str += f"  *Substrate Mapping:* `{quad_tags}`\n"
            repos_str += f"  *Details:* {r['description']}\n\n"
    else:
        repos_str = "_No direct research substrate overlap found in public repositories. Candidate will be queued for holistic review._\n"
        
    # Verdict Status Box
    if approved:
        verdict_icon = "🟩"
        verdict_title = "APPROVED & RECRUITED"
        verdict_desc = f"Excellent! Telemetry analysis shows active alignment ({total_score} pts) with our research substrates. Initiating onboarding sequence."
    else:
        verdict_icon = "🟨"
        verdict_title = "PENDING HOLISTIC REVIEW"
        verdict_desc = "Profile initialized. Direct repository keyword matching was low, but we value all scientific interests! A peer administrator will perform a holistic manual review."

    report = f"""## 🛸 AGENTIC TELEMETRY EVALUATION REPORT

```text
=====================================================================================
»                     NODE SPECIFIC SCAN: {username.upper()}                             «
=====================================================================================
```

### {verdict_icon} VERDICT: {verdict_title}
> {verdict_desc}

---

### 📡 Candidate Profile Telemetry
* **GitHub Node:** [@{u_info.get('login')}]({u_info.get('html_url')})
* **Identified Name:** {u_info.get('name') or "Unnamed Node"}
* **Bio Trace:** *"{u_info.get('bio') or 'No bio trace available.'}"*
* **Public Substrates:** {u_info.get('public_repos', 0)} public repos · {u_info.get('followers', 0)} followers

---

### 📊 Quadrant Alignment Diagnostics
{bar_chart_str}

---

### 📂 Standout Substrate Overlaps
{repos_str}
"""
    return approved, report

def main():
    print("Initiating AMF Applicant Verification Service...")
    payload = parse_issue_payload()
    if not payload:
        print("Failed to parse issue payload.")
        return
        
    issue_num = payload["issue_number"]
    username = payload["username"]
    
    if not username:
        print("No username identified in issue context.")
        return
        
    evaluation = evaluate_repositories(username)
    approved, report_md = generate_report(username, evaluation)
    
    # Check for invitation token
    invite_token = os.getenv("AMF_ORG_INVITE_TOKEN")
    invited = False
    
    if approved and invite_token:
        print(f"Token identified. Attempting automated organization invite for: {username}")
        # Invite to organization
        # POST /orgs/Agentic-Memory-Foundation/memberships/{username}
        status, invite_res = make_request(
            f"https://api.github.com/orgs/Agentic-Memory-Foundation/memberships/{username}",
            method="PUT",
            data={"role": "member"}
        )
        if status == 200:
            invited = True
            print("Successfully sent organization invitation!")
        else:
            print(f"Invitation failed with code {status}: {invite_res.get('message')}")
            
    # Add invitation info to the final report
    if approved:
        if invited:
            report_md += """
### 🛸 Activation Sequence Completed
An official, automated invitation to join the **Agentic-Memory-Foundation** organization has been dispatched to your GitHub account! Please check your email or visit [Agentic-Memory-Foundation Invitation](https://github.com/orgs/Agentic-Memory-Foundation) to accept membership.
"""
        else:
            report_md += """
### 🛸 Verification Complete
Your node is verified and approved. An administrator has been notified to issue your official organization invite shortly. Welcome to the movement!
"""
    else:
        report_md += """
### 🛸 Peer Review Scheduled
An administrator has been scheduled to manually evaluate your request. Keep an eye on this thread for updates!
"""

    report_md += f"\n---\n*Report generated automatically by AMF-Verifier Node-1.*"

    # Post Comment to Issue
    # POST /repos/{owner}/{repo}/issues/{issue_number}/comments
    repo_name = os.getenv("GITHUB_REPOSITORY", "Agentic-Memory-Foundation/.github")
    print(f"Posting report comment to issue #{issue_num} on {repo_name}...")
    comment_status, comment_res = make_request(
        f"https://api.github.com/repos/{repo_name}/issues/{issue_num}/comments",
        method="POST",
        data={"body": report_md}
    )
    if comment_status == 201:
        print("Successfully posted evaluation comment.")
    else:
        print(f"Failed to post comment: {comment_res.get('message')}")
        
    # Label and Close/Open issue accordingly
    labels = ["approved-node"] if approved else ["under-peer-review"]
    print(f"Applying labels {labels} to issue #{issue_num}...")
    make_request(
        f"https://api.github.com/repos/{repo_name}/issues/{issue_num}/labels",
        method="POST",
        data={"labels": labels}
    )
    
    # If approved, close issue
    if approved:
        print(f"Closing issue #{issue_num} as completed...")
        make_request(
            f"https://api.github.com/repos/{repo_name}/issues/{issue_num}",
            method="PATCH",
            data={"state": "closed", "state_reason": "completed"}
        )

if __name__ == "__main__":
    main()
