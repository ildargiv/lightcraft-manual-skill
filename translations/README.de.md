# LightCraft Manual Editing Skill

> Eine Skill, die einem KI-Agenten beibringt, Fotos in **LightCraft 0.21.1** komplett **von Hand** zu bearbeiten: explizite Reglerwerte, echte Maskengeometrie, echte Zeigerbewegungen. Kein `Auto`, keine Magie.

Sprachen: [English](../README.md) · [Русский](README.ru.md) · [简体中文](README.zh-CN.md) · [Español](README.es.md) · [Français](README.fr.md) · **Deutsch** · [日本語](README.ja.md) · [Português (BR)](README.pt-BR.md) · [한국어](README.ko.md)

---

## Was es ist

LightCraft ist ein quelloffener, destruktionsfreier RAW-Entwickler (eine Lightroom-Alternative) mit integriertem MCP-Server. Dieses Repository ist eine sofort einsetzbare **Skill für OpenCode / Claude Code / Codex**:

```
~/.config/opencode/skills/lightcraft/
├── SKILL.md                  # Doktrin, Arbeitsablauf, Werkzeugrouting, Fallen
├── references/               # 12 bei Bedarf lesbare Handbücher
└── scripts/                  # MCP-Starter, App-Starter, Dokumentations-Update, Add-on-Inventar
```

Sie deckt alle **392** Befehle, **114** Entwicklungsregler, das vollständige `develop`-JSON-Schema, alle Maskenfamilien, Punktentfernung, Point Color, HDR, Bracketing-Fusion, Export und die **41 integrierten Presets mit ihren tatsächlichen numerischen Rezepten** ab.

## Installation

```bash
git clone https://github.com/ildargiv/lightcraft-manual-skill.git \
  ~/.config/opencode/skills/lightcraft
```

Starten Sie Ihren Agenten neu, damit er die Skills erneut scannt. Voraussetzungen: LightCraft 0.21.1+ und Python 3 (nur für die Hilfsskripte).

### Verbindung zur laufenden Anwendung (empfohlen)

Der MCP-Server wird in `opencode.json` über einen selbstheilenden Wrapper registriert:

```json
"lightcraft": {
  "type": "local",
  "command": ["python", "<skills>/lightcraft/scripts/mcp-connect.py"],
  "enabled": true
}
```

`mcp-connect.py` startet bei Bedarf die Desktop-Anwendung mit `--control 7980` und übergibt danach stdio an `lightcraft-cli mcp --compact --connect 127.0.0.1:7980`. Der Agent erhält alle Bearbeitungswerkzeuge **zuzüglich** der Live-UI-Werkzeuge: `screenshot`, `click`, `press_key`, `pointer_gesture`, `set_ui`, `clipboard`.

Manuelles Äquivalent:

```powershell
powershell -ExecutionPolicy Bypass -File <skills>/lightcraft/scripts/start-lightcraft-app.ps1
```

## Unsere Vorteile

1. **Manuelles Arbeiten ist Regel, nicht Wunsch.** Ausdrücklich verboten: `develop.auto`, `develop.autoBwMix`, Auto-WB, `crop.autoStraighten`, `geometry.upright auto`, `spot.findDust`/`findBlemishes`, `lensBlur.findSubject`, `preset.apply`, `develop.sync`/`autoSync`, `develop.matchExposure`. Zu jedem Verbot gibt es eine manuelle Alternative — explizite Zahlen und Koordinaten.
2. **Vollständige Abdeckung der Anwendung.** 392 Befehle mit Parametern, 114 Regler mit Bereichen/Schritten/Standardwerten, vollständiges `develop`-Schema, alle 10 Maskentypen, Pinsel, Komponenten, Punkte, Rote Augen, Point Color, Lens Blur, Kurven, HSL, Farbgrading, Optik, Geometrie, Druck, Diashow und Archiv.
3. **Alle Presets bis auf die Zahlen zerlegt.** Für jedes der 41 integrierten Presets wird der tatsächliche Inhalt exportiert: welche Felder es setzt und mit welchen Werten. Der Agent kann den Look **von Hand nachbauen** und an das Bild anpassen, statt einen Knopf zu drücken. Dazu 3 Punktkurven- und 8 Export-Presets.
4. **HDR von Anfang bis Ende.** `develop.hdr` + `maxEv` + `hdr.sdr*`, Bracketing-Fusion (`merge.hdr`, `hdrBatch`, Panorama), JPEG-Export mit Gain Map (ISO 21496-1), 10-Bit-PQ/HLG-AVIF, 16-Bit-Rec.2020-PQ-PNG/JXL und 32-Bit-Float-TIFF. Mit ffprobe geprüft: `rgb48be`, `smpte2084`, `bt2020`. Vorschauen sind immer SDR — der Agent „korrigiert" kein unsichtbares HDR mit der Belichtung.
5. **Live-UI und echte Gesten.** Der Connect-Modus liefert `screenshot`, `click`, `pointer_gesture` und `press_key`. Der Agent sieht das Ergebnis im LightCraft-Fenster und kann Pinsel- oder Verlaufsstriche mit einer echten Geste in normierten Bildkoordinaten ziehen, nicht nur per Befehl.
6. **Selbstheilendes MCP.** Der Wrapper startet die App mit dem Steuerport und beseitigt den `catalog.lock`-Konflikt (ein Headless-Server und die Desktop-App können dieselbe Bibliothek nicht gleichzeitig halten).
7. **Selbstaktualisierende Dokumentation.** `scripts/refresh-reference.py` erzeugt die Befehls-/Reglerkataloge und alle Preset-Rezepte aus der installierten Version neu und vergleicht sie mit dem neuesten GitHub-Release.
8. **Add-on-Wissen und sicherer Import.** Unterstützte Formate (`.lcpreset`, XMP, `.lrtemplate`, `.cube`, `.dcp`, `.lceffect`, `.lccurve`, SAM 3, Denoise-ONNX), Import mit `dryRun`, kritische Bewertung von Drittanbieter-Projekten und Warnung vor Raubkopien.
9. **An echten RAW-Dateien geprüft.** Die folgenden Beispiele sind von Hand entwickelte Xiaomi-13-Ultra-DNGs; jedes enthält das exakte `develop`-JSON zur Reproduktion.
10. **Schutzvorrichtungen.** Experimente nur auf `photo.virtualCopy`, Testexporte nach temp, Weigerung, Originale/XMP zu überschreiben, Metadaten als nicht vertrauenswürdige Daten, `history.list`/`restore` und `edit.undo` bei jedem Schritt.

## Inhalt

| Datei | Inhalt |
|---|---|
| `SKILL.md` | Manuelle Doktrin, Bearbeitungspipeline, Werkzeuge, UI, Fallen |
| `references/controls.md` | Alle Regler: id, min, max, Standard, Schritt |
| `references/develop-json.md` | Vollständiges develop-Schema mit Feldmeaning |
| `references/masks-spots.md` | Maskenformen, Pinsel, Komponenten, Punkte, Rote Augen, Point Color, Lens Blur |
| `references/hdr.md` | HDR-Bearbeitung, SDR-Rendition, Fusion, Export, Prüfung |
| `references/presets.md` | 41 Presets mit exakten Werten, Kurven, Export-Presets |
| `references/manual-editing.md` | 12 Genre-Rezepte mit konkreten Zahlen |
| `references/export.md` | Formate, Größen, Metadaten, Wasserzeichen, Kontaktbogen |
| `references/commands-edit.md` | Bearbeitungsbefehle mit allen Parametern |
| `references/commands-rest.md` | Bibliothek, Metadaten, Druck, Diashow, Gesichter |
| `references/library.md` | Karte der Nicht-Bearbeitungsfunktionen |
| `references/addons.md` | Add-ons, Modelle, Community-Projekte |
| `scripts/*` | MCP-Starter, App-Starter, Dokumentations-Update, Inventar |

Seven Xiaomi 13 Ultra RAW photos from one city shoot, developed by hand. No `develop.auto`,
no `preset.apply`, no automatic straightening or subject detection. Each result comes with
its exact settings JSON so you can reproduce it with `lightcraft-cli render`.

### River HDR: headroom 3.5 EV, gradient sky mask, local tree mask

![River HDR: headroom 3.5 EV, gradient sky mask, local tree mask — vorher](../examples/01-river-hdr/before.jpg)

![River HDR: headroom 3.5 EV, gradient sky mask, local tree mask — nachher](../examples/01-river-hdr/after.jpg)

- [Original-RAW](../examples/01-river-hdr/original.dng) · [manuelle Einstellungen](../examples/settings/01-river-hdr.json)

### Flower shop at blue hour: manual 4200 K balance and split grading

![Flower shop at blue hour: manual 4200 K balance and split grading — vorher](../examples/02-blue-hour/before.jpg)

![Flower shop at blue hour: manual 4200 K balance and split grading — nachher](../examples/02-blue-hour/after.jpg)

- [Original-RAW](../examples/02-blue-hour/original.dng) · [manuelle Einstellungen](../examples/settings/02-blue-hour.json)

### Bell tower at blue hour: cool shadows, warm windows, shadow recovery

![Bell tower at blue hour: cool shadows, warm windows, shadow recovery — vorher](../examples/03-blue-hour-tower/before.jpg)

![Bell tower at blue hour: cool shadows, warm windows, shadow recovery — nachher](../examples/03-blue-hour-tower/after.jpg)

- [Original-RAW](../examples/03-blue-hour-tower/original.dng) · [manuelle Einstellungen](../examples/settings/03-blue-hour-tower.json)

### Old town at dusk: 4300 K by hand, architecture and street lights

![Old town at dusk: 4300 K by hand, architecture and street lights — vorher](../examples/04-old-town/before.jpg)

![Old town at dusk: 4300 K by hand, architecture and street lights — nachher](../examples/04-old-town/after.jpg)

- [Original-RAW](../examples/04-old-town/original.dng) · [manuelle Einstellungen](../examples/settings/04-old-town.json)

### Golden moose and city lights: controlled highlights, warm/cool grading

![Golden moose and city lights: controlled highlights, warm/cool grading — vorher](../examples/05-golden-moose/before.jpg)

![Golden moose and city lights: controlled highlights, warm/cool grading — nachher](../examples/05-golden-moose/after.jpg)

- [Original-RAW](../examples/05-golden-moose/original.dng) · [manuelle Einstellungen](../examples/settings/05-golden-moose.json)

### Night road with bokeh: 4000 K, noise control 25/30, light trails

![Night road with bokeh: 4000 K, noise control 25/30, light trails — vorher](../examples/06-night-bokeh/before.jpg)

![Night road with bokeh: 4000 K, noise control 25/30, light trails — nachher](../examples/06-night-bokeh/after.jpg)

- [Original-RAW](../examples/06-night-bokeh/original.dng) · [manuelle Einstellungen](../examples/settings/06-night-bokeh.json)

### Evening street: mixed lighting balanced manually, no Auto WB

![Evening street: mixed lighting balanced manually, no Auto WB — vorher](../examples/07-evening-street/before.jpg)

![Evening street: mixed lighting balanced manually, no Auto WB — nachher](../examples/07-evening-street/after.jpg)

- [Original-RAW](../examples/07-evening-street/original.dng) · [manuelle Einstellungen](../examples/settings/07-evening-street.json)

All exports: `metadata=none`, 1400 px long edge, JPEG quality 88. The HDR example
additionally writes an ISO 21496-1 gain map (`hdrgm` marker verified).
## Selbst prüfen

```powershell
python scripts/addon-inventory.py
python scripts/refresh-reference.py
```

```bash
lightcraft-cli render examples/01-river-hdr/original.dng -o repro.jpg \
  --settings examples/settings/01-river-hdr.json --size 1400 \
  --opt metadata=none --opt quality=88 --opt hdr=true
```

## Grenzen

- LightCraft ist alpha (0.21.1); eine offizielle Plugin-API gibt es noch nicht — „Add-ons" sind importierte Presets/Profile/Modelle und externe Werkzeuge.
- SAM 3 ist nicht enthalten (≈3,4 GB, Meta-Lizenz); Object/Describe-Masken benötigen es. Sky/Subject/Background funktionieren ohne.
- LightCraft kann HDR nicht auf dem Bildschirm anzeigen: Vorschauen sind immer SDR. Beurteilen Sie HDR anhand der exportierten Gain-Map / PQ-Datei.
- Die Drittanbieter-Repositories in `addons.md` sind inoffiziell und ungeprüft; prüfen Sie Code und Lizenzen vor der Verwendung.

## Lizenz

MIT — siehe [LICENSE](../LICENSE). Skill-Text und Skripte sind Originalarbeiten. LightCraft selbst ist ein eigenständiges Projekt des ArtCraft-Teams (MIT OR Apache-2.0). Die Beispiel-DNGs bleiben Eigentum ihres Autors und dienen nur der Demonstration.

---

Gemacht für einen Agenten, der Knöpfe drücken kann, aber lieber von Hand arbeitet.
