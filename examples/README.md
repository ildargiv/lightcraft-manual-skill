# Examples

Three Xiaomi 13 Ultra DNGs from one shoot (`DNG речка у порта`), developed by hand.
Every JPEG here was produced with `lightcraft-cli render` from the corresponding
`original.dng` and the exact settings JSON — no `develop.auto`, no `preset.apply`,
no automatic straightening or subject detection.

| folder | source DNG | settings | result |
|---|---|---|---|
| `01-river-hdr` | `IMG_20261115_121554.dng` | [`settings/01-river-hdr.json`](settings/01-river-hdr.json) | SDR `after.jpg`, HDR gain-map `after-hdr-gainmap.jpg` |
| `02-blue-hour` | `IMG_20261115_160805.dng` | [`settings/02-blue-hour.json`](settings/02-blue-hour.json) | `after.jpg` |
| `03-golden-river` | `IMG_20261115_121556.dng` | [`settings/03-golden-river.json`](settings/03-golden-river.json) | `after.jpg` |

`before.jpg` is the unedited render of the same original. All JPEGs: 1400 px long
edge, quality 88, `metadata=none` (EXIF stripped — no location data published).

## Reproduce

```bash
lightcraft-cli render examples/01-river-hdr/original.dng -o repro.jpg \
  --settings examples/settings/01-river-hdr.json --size 1400 \
  --opt metadata=none --opt quality=88
```

For the HDR version add `--opt hdr=true` and inspect the result with an HDR-capable
viewer: the JPEG carries an ISO 21496-1 gain map (`hdrgm` marker), the basic SDR
preview still looks like `after.jpg`.

## What to notice

- **01** — global base + `hdr.max_ev 3.5` and separately tuned `hdr.sdr*`; a `linear`
  sky gradient and a `radial` foliage mask. The sky keeps detail without crushing
  the river.
- **02** — white balance 4200 K / +6 tint set explicitly, blue shadows against warm
  highlights, luminance NR 20 and colour NR 28 instead of an AI denoiser.
- **03** — warm mixer (orange/yellow), highlights −50, shadows +35, and a soft radial
  mask over the sunlit trees — no subject recognition, just coordinates and numbers.

A partial `develop` JSON can be applied through the MCP helper too:

```json
{"settings": {"light": {"exposure": 0.15, "highlights": -55, "shadows": 40}}}
```
