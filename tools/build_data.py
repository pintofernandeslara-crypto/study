"""Build data.json for the app from exported study-hub documents.

Usage: python3 tools/build_data.py <docs_dir> [out_file]
<docs_dir> holds files named subjects__<id>.json, decks__<id>.json,
quizzes__<id>.json and meta__status.json (as exported from the study hub database).
"""
import json, os, sys

IDS = ["financial-accounting", "organisational-behaviour", "critical-thinking", "math", "principles-of-management"]

def load(d, name):
    p = os.path.join(d, name)
    return json.load(open(p)) if os.path.exists(p) else {}

def main():
    d = sys.argv[1]
    out = sys.argv[2] if len(sys.argv) > 2 else os.path.join(os.path.dirname(__file__), "..", "data.json")
    meta = load(d, "meta__status.json")
    data = {"generatedAt": meta.get("lastRun"), "subjects": {}}
    for sid in IDS:
        s = load(d, f"subjects__{sid}.json")
        data["subjects"][sid] = {
            "overview": s.get("overview", ""),
            "summary": s.get("summary", []),
            "sources": s.get("sources", []),
            "updatedAt": s.get("updatedAt"),
            "cards": load(d, f"decks__{sid}.json").get("cards", []),
            "questions": load(d, f"quizzes__{sid}.json").get("questions", []),
        }
    json.dump(data, open(out, "w"), ensure_ascii=False, separators=(",", ":"))
    print("wrote", out, os.path.getsize(out), "bytes")

if __name__ == "__main__":
    main()
