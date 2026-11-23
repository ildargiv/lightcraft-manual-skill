#!/usr/bin/env python3
"""Refresh the generated LightCraft skill references from the installed CLI.

Run after updating LightCraft:
    python "C:\\Users\\User\\.config\\opencode\\skills\\lightcraft\\scripts\\refresh-reference.py"

Regenerates: references/commands-edit.md, references/commands-rest.md,
references/controls.md, references/presets.md.
Hand-written files (SKILL.md, hdr.md, manual-editing.md, ...) are left alone.
"""
import json
import os
import re
import subprocess
import tempfile
import urllib.request

CLI = os.path.join(os.environ.get("LOCALAPPDATA", r"%USERPROFILE%\AppData\Local"),
                   "Programs", "ArtCraft", "LightCraft", "lightcraft-cli.exe")
REF = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "references")

EDIT_GROUPS = ["develop", "mask", "spot", "curve", "pointColor", "geometry", "lens",
               "lensBlur", "redeye", "profile", "profiles", "preset", "presets", "crop",
               "edit", "history", "version", "export", "merge", "denoise", "segment",
               "focus", "photo"]


def run(*args):
    p = subprocess.run([CLI, *args], capture_output=True, text=True,
                       encoding="utf-8", errors="replace")
    if p.returncode != 0 and not p.stdout.strip():
        raise SystemExit("CLI failed: " + (p.stderr or " ").strip()[:500])
    return p.stdout


def write(name, text):
    with open(os.path.join(REF, name), "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    print("  wrote", name, "(%d KB)" % (len(text.encode("utf-8")) // 1024))


def commands_and_controls():
    cmds = json.loads(run("commands", "--json"))
    ctrls = json.loads(run("controls", "--json"))
    version = re.search(r"\d+\.\d+\.\d+", run("--version")).group(0)
    groups = {}
    for c in cmds:
        groups.setdefault(c["id"].split(".")[0], []).append(c)
    for v in groups.values():
        v.sort(key=lambda x: x["id"])

    out = ["# Команды редактирования LightCraft — полные параметры", "",
           "Сгенерировано из `lightcraft-cli commands --json` (%s)." % version,
           "Источник истины — `command_list`.", ""]
    for g in EDIT_GROUPS:
        if g not in groups:
            continue
        out += ["## " + g, ""]
        for c in groups[g]:
            out += ["### " + c["id"] + " — " + c["label"]]
            if c.get("shortcut"):
                out.append("shortcut: " + c["shortcut"])
            out += [c["params"], ""]
    write("commands-edit.md", "\n".join(out))

    out = ["# Остальные команды LightCraft — каталог, метаданные, печать, слайдшоу", "",
           "Сгенерировано из `lightcraft-cli commands --json` (%s)." % version,
           "Полные описания параметров — `command_list`.", ""]
    for g in sorted(groups):
        if g in EDIT_GROUPS:
            continue
        out += ["## " + g, ""]
        for c in groups[g]:
            out += ["- **" + c["id"] + "** — " + c["label"], "  " + c["params"]]
        out.append("")
    write("commands-rest.md", "\n".join(out))

    by_sec = {}
    for c in ctrls:
        by_sec.setdefault(c["section"], []).append(c)
    out = ["# Слайдеры Develop: id, диапазон, шаг, значение по умолчанию", "",
           "Источник: `lightcraft-cli controls --json` (%s) и `list_controls`." % version,
           "Ставить значения: `set_develop {values: {\"light.exposure\": 0.4}}`.", ""]
    for sec in sorted(by_sec):
        out += ["## " + sec, "",
                "| id | label | min | max | default | step |",
                "|---|---|---|---|---|---|"]
        for c in sorted(by_sec[sec], key=lambda x: x["id"]):
            out.append("| `%s` | %s | %s | %s | %s | %s |" %
                       (c["id"], c["label"], c["min"], c["max"], c["default"], c["step"]))
        out.append("")
    write("controls.md", "\n".join(out))
    return version


def presets():
    lines = run("run", "--demo", "presets.list").strip().splitlines()
    rec = None
    for line in lines:
        d = json.loads(line)
        if d.get("ok"):
            rec = d["result"]
    if rec is None:
        raise SystemExit("could not list presets")
    ids = [p["id"] for p in rec]
    dest = os.path.join(tempfile.gettempdir(), "lightcraft-presets.lcpreset").replace("\\", "/")
    run("run", "--demo", "preset.export", "path=" + dest,
        "ids=" + json.dumps(ids, separators=(",", ":")))
    data = json.load(open(dest, encoding="utf-8"))

    def flat(prefix, value, out):
        if isinstance(value, dict):
            for k, v in value.items():
                flat((prefix + "." + k) if prefix else k, v, out)
        elif isinstance(value, list):
            out.append((prefix, json.dumps(value, ensure_ascii=False)))
        else:
            out.append((prefix, value))

    def fmt(v):
        if isinstance(v, float) and v.is_integer():
            return str(int(v))
        return str(v)

    out = ["# Пресеты LightCraft: что внутри каждого", "",
           "Сгенерировано через `preset.export` из установленной версии LightCraft.",
           "Ключи — пути в `develop` JSON, значения — те же числа, что у слайдеров.", "",
           "## Как этим пользоваться агенту", "",
           "- Пресет — это **рецепт**, а не кнопка. По умолчанию агент ставит те же числа руками",
           "  (`set_develop`), чтобы контролировать каждый шаг.",
           "- `preset.apply {id, amount}` — только по явной просьбе, и затем довести руками.",
           "- Свои пресеты: `preset.create`, `preset.update`, `preset.saveRecipe`.", "",
           "## Встроенные develop-пресеты (%d)" % len(data["presets"]), ""]
    groups = {}
    for p in data["presets"]:
        groups.setdefault(p.get("group") or "—", []).append(p)
    for g in sorted(groups):
        out += ["## " + g, ""]
        for p in sorted(groups[g], key=lambda x: x["name"]):
            out.append("### " + p["name"] + " — `" + p["id"] + "`")
            pairs = []
            flat("", p["settings"], pairs)
            out += ["- `" + k + "` = " + fmt(v) for k, v in pairs]
            out.append("")

    out += ["## Point curve пресеты (3, `curve.presets`)", "",
            "| name | master |", "|---|---|",
            "| Linear | [] (тождественная) |",
            "| Medium Contrast | [[0,0],[0.25,0.2],[0.5,0.5],[0.75,0.8],[1,1]] |",
            "| Strong Contrast | [[0,0],[0.25,0.14],[0.5,0.5],[0.75,0.86],[1,1]] |", "",
            "`curve.applyPreset {name}` или руками `develop.curve {channel, points}`.",
            "Параметрическая кривая (`curve.highlights/lights/darks/shadows`) — отдельно.", "",
            "## Export-пресеты (8, `export.presets`)", "",
            "| name | params |", "|---|---|"]
    exports = [
        ("JPEG (Small)", '{"format":"jpeg","longEdge":2048,"quality":85,"colorSpace":"srgb"}'),
        ("JPEG (Large)", '{"format":"jpeg","longEdge":0,"quality":92,"colorSpace":"srgb"}'),
        ("Original + Settings", '{"format":"original"}'),
        ("DNG", '{"format":"dng"}'),
        ("Instagram Feed", '{"format":"jpeg","longEdge":1080,"quality":85,"colorSpace":"srgb","sharpen":"screen"}'),
        ("Instagram Story / Reel", '{"format":"jpeg","longEdge":1920,"quality":85,"colorSpace":"srgb","sharpen":"screen"}'),
        ("Web / Portfolio", '{"format":"jpeg","longEdge":2048,"quality":85,"colorSpace":"srgb","metadata":"copyright"}'),
        ("Full Resolution Master", '{"format":"jpeg","longEdge":0,"quality":95,"colorSpace":"displayP3"}'),
    ]
    out += ["| " + n + " | `" + v + "` |" for n, v in exports]
    out += ["", "`export {preset: \"Instagram Feed\", ...}` — поля можно переопределить.", ""]
    write("presets.md", "\n".join(out))


def version_check(version):
    try:
        req = urllib.request.Request(
            "https://api.github.com/repos/storytold/lightcraft/releases/latest",
            headers={"User-Agent": "opencode"})
        with urllib.request.urlopen(req, timeout=10) as r:
            latest = json.load(r)["tag_name"].lstrip("v")
        print("installed:", version, "| latest release:", latest,
              "| up to date" if latest == version else "| UPDATE AVAILABLE")
    except Exception as e:
        print("version check skipped:", e)


if __name__ == "__main__":
    print("Refreshing LightCraft references from", CLI)
    v = commands_and_controls()
    presets()
    version_check(v)
