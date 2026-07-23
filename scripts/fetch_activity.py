import os
import sys
import json
import urllib.request
from datetime import datetime, timezone

def fetch_activity(username="Prasadhol2001", output_json="data/activity.json"):
    url = f"https://api.github.com/users/{username}/events/public"
    req = urllib.request.Request(
        url,
        headers={"User-Agent": "Mozilla/5.0", "Accept": "application/vnd.github.v3+json"}
    )
    
    print(f"Fetching recent GitHub activity for user '{username}'...")
    events_data = []
    
    try:
        with urllib.request.urlopen(req) as resp:
            if resp.status == 200:
                raw_bytes = resp.read()
                raw_events = json.loads(raw_bytes.decode("utf-8"))
                
                for ev in raw_events:
                    if len(events_data) >= 5:
                        break
                        
                    ev_type = ev.get("type")
                    repo_name = ev.get("repo", {}).get("name", "")
                    created_at = ev.get("created_at", "")
                    
                    time_str = ""
                    if created_at:
                        try:
                            dt = datetime.strptime(created_at, "%Y-%m-%dT%H:%M:%SZ")
                            time_str = dt.strftime("%b %d, %Y")
                        except ValueError:
                            time_str = created_at[:10]
                            
                    desc = ""
                    icon = "⚡"
                    
                    if ev_type == "PushEvent":
                        commits_count = len(ev.get("payload", {}).get("commits", []))
                        desc = f"Pushed {commits_count} commit{'s' if commits_count != 1 else ''} to {repo_name}"
                        icon = "🔨"
                    elif ev_type == "CreateEvent":
                        ref_type = ev.get("payload", {}).get("ref_type", "repo")
                        desc = f"Created {ref_type} in {repo_name}"
                        icon = "✨"
                    elif ev_type == "PullRequestEvent":
                        action = ev.get("payload", {}).get("action", "opened")
                        desc = f"{action.capitalize()} PR in {repo_name}"
                        icon = "🔀"
                    elif ev_type == "WatchEvent":
                        desc = f"Starred {repo_name}"
                        icon = "⭐"
                    elif ev_type == "IssuesEvent":
                        action = ev.get("payload", {}).get("action", "opened")
                        desc = f"{action.capitalize()} issue in {repo_name}"
                        icon = "📌"
                    else:
                        desc = f"Activity in {repo_name}"
                        icon = "🚀"
                        
                    events_data.append({
                        "type": ev_type,
                        "icon": icon,
                        "description": desc,
                        "repo": repo_name,
                        "date": time_str
                    })
    except Exception as e:
        print(f"Notice: Failed to fetch events ({e}). Using fallback activity list.")
        
    if not events_data:
        events_data = [
            {"icon": "🔨", "description": "Pushed updates to Prasadhol2001/Prasadhol2001", "date": "Recent"},
            {"icon": "📱", "description": "Published mobile app updates on Google Play Store", "date": "Recent"},
            {"icon": "✨", "description": "Maintained Flutter architecture & mobile app repositories", "date": "Recent"}
        ]
        
    result = {
        "username": username,
        "updated_at": datetime.now(timezone.utc).isoformat(),
        "events": events_data
    }
    
    os.makedirs(os.path.dirname(output_json), exist_ok=True)
    with open(output_json, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2)
        
    print(f"Saved {len(events_data)} recent activity items to '{output_json}'.")

if __name__ == "__main__":
    user = sys.argv[1] if len(sys.argv) > 1 else "Prasadhol2001"
    out = sys.argv[2] if len(sys.argv) > 2 else "data/activity.json"
    fetch_activity(user, out)
