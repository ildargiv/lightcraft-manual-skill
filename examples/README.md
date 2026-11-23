# Examples

Seven Xiaomi 13 Ultra RAW photos from one city shoot, developed by hand. No
`develop.auto`, no `preset.apply`, no automatic straightening or subject detection.
Each JPEG was produced with `lightcraft-cli render` from the corresponding
`original.dng` and the exact settings JSON.

| folder | scene | settings |
|---|---|---|
| `01-river-hdr` | River, 3.5 EV headroom, sky gradient + tree mask | [`01-river-hdr.json`](settings/01-river-hdr.json) · HDR gain-map [`after-hdr-gainmap.jpg`](01-river-hdr/after-hdr-gainmap.jpg) |
| `02-blue-hour` | Flower shop at blue hour, manual 4200 K WB | [`02-blue-hour.json`](settings/02-blue-hour.json) |
| `03-blue-hour-tower` | Bell tower at blue hour, warm windows / cool shadows | [`03-blue-hour-tower.json`](settings/03-blue-hour-tower.json) |
| `04-old-town` | Ornate old-town façades at dusk, 4300 K by hand | [`04-old-town.json`](settings/04-old-town.json) |
| `05-golden-moose` | Golden moose sculpture against city lights | [`05-golden-moose.json`](settings/05-golden-moose.json) |
| `06-night-bokeh` | Night road with bokeh and light trails | [`06-night-bokeh.json`](settings/06-night-bokeh.json) |
| `07-evening-street` | Evening street with mixed shop lighting | [`07-evening-street.json`](settings/07-evening-street.json) |

Every folder contains `before.jpg`, `after.jpg` and `original.dng`. All JPEGs:
1400 px long edge, quality 88, `metadata=none` (EXIF stripped — no location data published).

## Reproduce

```bash
lightcraft-cli render examples/03-blue-hour-tower/original.dng -o repro.jpg \
  --settings examples/settings/03-blue-hour-tower.json --size 1400 \
  --opt metadata=none --opt quality=88
```

For the HDR version add `--opt hdr=true` and inspect the result with an HDR-capable
viewer: the JPEG carries an ISO 21496-1 gain map (`hdrgm` marker). The same workflow
works for any RAW file — DNG, ARW, NEF, RAF, CR3 — and for JPEG/HEIC sources with less highlight headroom.

## What to notice

- **01** — the only landscape: global base + HDR headroom 3.5 EV, `linear` sky mask and `radial` foliage mask.
- **02–04** — blue-hour architecture: white balance set by hand, cool shadows against warm windows, NR 18–25, no AI denoiser.
- **05** — metallic sculpture against street lamps: highlights −55 to keep the bulbs, warm/cool split grading.
- **06** — night street: 4000 K, luminance NR 25 / colour NR 30, sharpening masked at 60.
- **07** — mixed shop lighting balanced manually instead of Auto WB.

A partial `develop` JSON can be applied through the MCP helper too:

```json
{"settings": {"light": {"exposure": 0.15, "highlights": -55, "shadows": 40}}}
```
