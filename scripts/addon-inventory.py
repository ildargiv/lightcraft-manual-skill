#!/usr/bin/env python3
"""Print a compact inventory of LightCraft add-ons (presets, profiles, models).

Uses the running app through `lightcraft-cli run --connect` (control port 7980).
"""
import json
import os
import subprocess

CLI = os.path.join(os.environ.get("LOCALAPPDATA", r"%USERPROFILE%\AppData\Local"),
                   "Programs", "ArtCraft", "LightCraft", "lightcraft-cli.exe")
IDS = ["presets.list", "profiles.list", "mask.effects", "curve.presets",
       "export.presets", "denoise.models.list", "faces.models.list",
       "segment.model.status", "lens.databaseStatus"]


def main():
    p = subprocess.run([CLI, "run", "--connect", *IDS],
                       capture_output=True, text=True, encoding="utf-8", errors="replace")
    results = {}
    for line in p.stdout.splitlines():
        try:
            d = json.loads(line)
        except json.JSONDecodeError:
            continue
        if d.get("ok"):
            results[d["command"]] = d.get("result")

    def get(name, default=None):
        return results.get(name, default)

    presets = get("presets.list", []) or []
    profiles = get("profiles.list", []) or []
    effects = get("mask.effects", {}) or {}
    curves = get("curve.presets", {}) or {}
    exports = get("export.presets", []) or []
    denoise = get("denoise.models.list", {}) or {}
    faces = get("faces.models.list", {}) or {}
    segment = get("segment.model.status", {}) or {}
    lens = get("lens.databaseStatus", {}) or {}

    print("LightCraft add-on inventory")
    print("  develop presets : %d total, %d user, %d favorites" % (
        len(presets), sum(1 for x in presets if not x.get("builtin")),
        sum(1 for x in presets if x.get("favorite"))))
    print("  color profiles  : %d total, %d imported, groups: %s" % (
        len(profiles), sum(1 for x in profiles if x.get("imported")),
        ", ".join(sorted({x.get("group") or "-" for x in profiles}))))
    print("  mask effects    : %d, groups: %d" % (len(effects.get("effects", [])), len(effects.get("groups", []))))
    print("  curve presets   : %s" % ", ".join(x["name"] for x in curves.get("presets", [])))
    print("  export presets  : %d" % len(exports))
    print("  denoise models  : %d installed, selected: %s" % (len(denoise.get("models", [])), denoise.get("model")))
    installed = [m["id"] for m in faces.get("models", []) if m.get("installed")]
    print("  face models     : %s" % (", ".join(installed) or "none"))
    print("  SAM 3 (AI masks): %s" % ("installed" if segment.get("installed") else "NOT installed"))
    print("  lensfun         : %s lenses (%s)" % (lens.get("lenses"), lens.get("dir")))
    if p.returncode != 0:
        print("CLI exited with", p.returncode, p.stderr.strip()[:300])


if __name__ == "__main__":
    main()
