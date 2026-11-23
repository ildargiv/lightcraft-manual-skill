# Слайдеры Develop: id, диапазон, шаг, значение по умолчанию

Источник: `lightcraft-cli controls --json` (0.21.1) и `list_controls`.
Ставить значения: `set_develop {values: {"light.exposure": 0.4}}`.

## bwMix

| id | label | min | max | default | step |
|---|---|---|---|---|---|
| `bw.aqua` | Aqua | -100.0 | 100.0 | 0.0 | 1.0 |
| `bw.blue` | Blue | -100.0 | 100.0 | 0.0 | 1.0 |
| `bw.green` | Green | -100.0 | 100.0 | 0.0 | 1.0 |
| `bw.magenta` | Magenta | -100.0 | 100.0 | 0.0 | 1.0 |
| `bw.orange` | Orange | -100.0 | 100.0 | 0.0 | 1.0 |
| `bw.purple` | Purple | -100.0 | 100.0 | 0.0 | 1.0 |
| `bw.red` | Red | -100.0 | 100.0 | 0.0 | 1.0 |
| `bw.yellow` | Yellow | -100.0 | 100.0 | 0.0 | 1.0 |

## calibration

| id | label | min | max | default | step |
|---|---|---|---|---|---|
| `calibration.blueHue` | Blue Hue | -100.0 | 100.0 | 0.0 | 1.0 |
| `calibration.blueSat` | Blue Saturation | -100.0 | 100.0 | 0.0 | 1.0 |
| `calibration.greenHue` | Green Hue | -100.0 | 100.0 | 0.0 | 1.0 |
| `calibration.greenSat` | Green Saturation | -100.0 | 100.0 | 0.0 | 1.0 |
| `calibration.redHue` | Red Hue | -100.0 | 100.0 | 0.0 | 1.0 |
| `calibration.redSat` | Red Saturation | -100.0 | 100.0 | 0.0 | 1.0 |
| `calibration.shadowsTint` | Shadows Tint | -100.0 | 100.0 | 0.0 | 1.0 |

## color

| id | label | min | max | default | step |
|---|---|---|---|---|---|
| `color.saturation` | Saturation | -100.0 | 100.0 | 0.0 | 1.0 |
| `color.vibrance` | Vibrance | -100.0 | 100.0 | 0.0 | 1.0 |
| `wb.temp` | Temp | 2000.0 | 50000.0 | 6500.0 | 50.0 |
| `wb.tint` | Tint | -150.0 | 150.0 | 0.0 | 1.0 |

## curve

| id | label | min | max | default | step |
|---|---|---|---|---|---|
| `curve.darks` | Darks | -100.0 | 100.0 | 0.0 | 1.0 |
| `curve.highlights` | Highlights | -100.0 | 100.0 | 0.0 | 1.0 |
| `curve.lights` | Lights | -100.0 | 100.0 | 0.0 | 1.0 |
| `curve.refineSaturation` | Refine Saturation | 0.0 | 100.0 | 100.0 | 1.0 |
| `curve.shadows` | Shadows | -100.0 | 100.0 | 0.0 | 1.0 |
| `curve.splitHighlights` | Highlights split | 30.0 | 90.0 | 75.0 | 1.0 |
| `curve.splitMid` | Midtones split | 20.0 | 80.0 | 50.0 | 1.0 |
| `curve.splitShadows` | Shadows split | 10.0 | 70.0 | 25.0 | 1.0 |

## detail

| id | label | min | max | default | step |
|---|---|---|---|---|---|
| `detail.nrColor` | Color Noise Reduction | 0.0 | 100.0 | 0.0 | 1.0 |
| `detail.nrColorDetail` | Detail | 0.0 | 100.0 | 50.0 | 1.0 |
| `detail.nrColorSmoothness` | Smoothness | 0.0 | 100.0 | 50.0 | 1.0 |
| `detail.nrContrast` | Contrast | 0.0 | 100.0 | 0.0 | 1.0 |
| `detail.nrDetail` | Detail | 0.0 | 100.0 | 50.0 | 1.0 |
| `detail.nrLuminance` | Noise Reduction | 0.0 | 100.0 | 0.0 | 1.0 |
| `detail.sharpenAmount` | Sharpening | 0.0 | 150.0 | 0.0 | 1.0 |
| `detail.sharpenDetail` | Detail | 0.0 | 100.0 | 25.0 | 1.0 |
| `detail.sharpenMasking` | Masking | 0.0 | 100.0 | 0.0 | 1.0 |
| `detail.sharpenRadius` | Radius | 0.5 | 3.0 | 1.0 | 0.1 |
| `enhance.denoise` | Amount | 0.0 | 100.0 | 0.0 | 1.0 |

## effects

| id | label | min | max | default | step |
|---|---|---|---|---|---|
| `effects.clarity` | Clarity | -100.0 | 100.0 | 0.0 | 1.0 |
| `effects.dehaze` | Dehaze | -100.0 | 100.0 | 0.0 | 1.0 |
| `effects.texture` | Texture | -100.0 | 100.0 | 0.0 | 1.0 |

## geometry

| id | label | min | max | default | step |
|---|---|---|---|---|---|
| `crop.angle` | Straighten | -45.0 | 45.0 | 0.0 | 0.01 |
| `geometry.aspect` | Aspect | -100.0 | 100.0 | 0.0 | 1.0 |
| `geometry.horizontal` | Horizontal | -100.0 | 100.0 | 0.0 | 1.0 |
| `geometry.offsetX` | Offset X | -100.0 | 100.0 | 0.0 | 0.1 |
| `geometry.offsetY` | Offset Y | -100.0 | 100.0 | 0.0 | 0.1 |
| `geometry.rotate` | Rotate | -10.0 | 10.0 | 0.0 | 0.1 |
| `geometry.scale` | Scale | 50.0 | 150.0 | 100.0 | 1.0 |
| `geometry.vertical` | Vertical | -100.0 | 100.0 | 0.0 | 1.0 |

## grading

| id | label | min | max | default | step |
|---|---|---|---|---|---|
| `grading.balance` | Balance | -100.0 | 100.0 | 0.0 | 1.0 |
| `grading.blending` | Blending | 0.0 | 100.0 | 50.0 | 1.0 |
| `grading.global.hue` | Global Hue | 0.0 | 360.0 | 0.0 | 1.0 |
| `grading.global.lum` | Global Luminance | -100.0 | 100.0 | 0.0 | 1.0 |
| `grading.global.sat` | Global Saturation | 0.0 | 100.0 | 0.0 | 1.0 |
| `grading.highlights.hue` | Highlights Hue | 0.0 | 360.0 | 0.0 | 1.0 |
| `grading.highlights.lum` | Highlights Luminance | -100.0 | 100.0 | 0.0 | 1.0 |
| `grading.highlights.sat` | Highlights Saturation | 0.0 | 100.0 | 0.0 | 1.0 |
| `grading.midtones.hue` | Midtones Hue | 0.0 | 360.0 | 0.0 | 1.0 |
| `grading.midtones.lum` | Midtones Luminance | -100.0 | 100.0 | 0.0 | 1.0 |
| `grading.midtones.sat` | Midtones Saturation | 0.0 | 100.0 | 0.0 | 1.0 |
| `grading.shadows.hue` | Shadows Hue | 0.0 | 360.0 | 0.0 | 1.0 |
| `grading.shadows.lum` | Shadows Luminance | -100.0 | 100.0 | 0.0 | 1.0 |
| `grading.shadows.sat` | Shadows Saturation | 0.0 | 100.0 | 0.0 | 1.0 |

## grain

| id | label | min | max | default | step |
|---|---|---|---|---|---|
| `grain.amount` | Grain | 0.0 | 100.0 | 0.0 | 1.0 |
| `grain.roughness` | Roughness | 0.0 | 100.0 | 50.0 | 1.0 |
| `grain.size` | Size | 0.0 | 100.0 | 25.0 | 1.0 |

## lensBlur

| id | label | min | max | default | step |
|---|---|---|---|---|---|
| `lensBlur.amount` | Blur Amount | 0.0 | 100.0 | 0.0 | 1.0 |
| `lensBlur.boost` | Boost | 0.0 | 100.0 | 0.0 | 1.0 |
| `lensBlur.transition` | Transition | 0.0 | 100.0 | 50.0 | 1.0 |

## light

| id | label | min | max | default | step |
|---|---|---|---|---|---|
| `hdr.maxEv` | HDR Headroom | 0.0 | 5.0 | 3.0 | 0.1 |
| `hdr.sdrBrightness` | SDR Brightness | -100.0 | 100.0 | 0.0 | 1.0 |
| `hdr.sdrClarity` | SDR Clarity | -100.0 | 100.0 | 0.0 | 1.0 |
| `hdr.sdrContrast` | SDR Contrast | -100.0 | 100.0 | 0.0 | 1.0 |
| `hdr.sdrHighlights` | SDR Highlights | -100.0 | 100.0 | 0.0 | 1.0 |
| `hdr.sdrShadows` | SDR Shadows | -100.0 | 100.0 | 0.0 | 1.0 |
| `hdr.sdrWhites` | SDR Whites | -100.0 | 100.0 | 0.0 | 1.0 |
| `light.blacks` | Blacks | -100.0 | 100.0 | 0.0 | 1.0 |
| `light.contrast` | Contrast | -100.0 | 100.0 | 0.0 | 1.0 |
| `light.exposure` | Exposure | -5.0 | 5.0 | 0.0 | 0.01 |
| `light.highlights` | Highlights | -100.0 | 100.0 | 0.0 | 1.0 |
| `light.shadows` | Shadows | -100.0 | 100.0 | 0.0 | 1.0 |
| `light.whites` | Whites | -100.0 | 100.0 | 0.0 | 1.0 |

## mixer

| id | label | min | max | default | step |
|---|---|---|---|---|---|
| `mixer.aqua.hue` | Aqua Hue | -100.0 | 100.0 | 0.0 | 1.0 |
| `mixer.aqua.lum` | Aqua Luminance | -100.0 | 100.0 | 0.0 | 1.0 |
| `mixer.aqua.sat` | Aqua Saturation | -100.0 | 100.0 | 0.0 | 1.0 |
| `mixer.blue.hue` | Blue Hue | -100.0 | 100.0 | 0.0 | 1.0 |
| `mixer.blue.lum` | Blue Luminance | -100.0 | 100.0 | 0.0 | 1.0 |
| `mixer.blue.sat` | Blue Saturation | -100.0 | 100.0 | 0.0 | 1.0 |
| `mixer.green.hue` | Green Hue | -100.0 | 100.0 | 0.0 | 1.0 |
| `mixer.green.lum` | Green Luminance | -100.0 | 100.0 | 0.0 | 1.0 |
| `mixer.green.sat` | Green Saturation | -100.0 | 100.0 | 0.0 | 1.0 |
| `mixer.magenta.hue` | Magenta Hue | -100.0 | 100.0 | 0.0 | 1.0 |
| `mixer.magenta.lum` | Magenta Luminance | -100.0 | 100.0 | 0.0 | 1.0 |
| `mixer.magenta.sat` | Magenta Saturation | -100.0 | 100.0 | 0.0 | 1.0 |
| `mixer.orange.hue` | Orange Hue | -100.0 | 100.0 | 0.0 | 1.0 |
| `mixer.orange.lum` | Orange Luminance | -100.0 | 100.0 | 0.0 | 1.0 |
| `mixer.orange.sat` | Orange Saturation | -100.0 | 100.0 | 0.0 | 1.0 |
| `mixer.purple.hue` | Purple Hue | -100.0 | 100.0 | 0.0 | 1.0 |
| `mixer.purple.lum` | Purple Luminance | -100.0 | 100.0 | 0.0 | 1.0 |
| `mixer.purple.sat` | Purple Saturation | -100.0 | 100.0 | 0.0 | 1.0 |
| `mixer.red.hue` | Red Hue | -100.0 | 100.0 | 0.0 | 1.0 |
| `mixer.red.lum` | Red Luminance | -100.0 | 100.0 | 0.0 | 1.0 |
| `mixer.red.sat` | Red Saturation | -100.0 | 100.0 | 0.0 | 1.0 |
| `mixer.yellow.hue` | Yellow Hue | -100.0 | 100.0 | 0.0 | 1.0 |
| `mixer.yellow.lum` | Yellow Luminance | -100.0 | 100.0 | 0.0 | 1.0 |
| `mixer.yellow.sat` | Yellow Saturation | -100.0 | 100.0 | 0.0 | 1.0 |

## optics

| id | label | min | max | default | step |
|---|---|---|---|---|---|
| `optics.caBlue` | Blue/Yellow Fringe | -100.0 | 100.0 | 0.0 | 1.0 |
| `optics.caRed` | Red/Cyan Fringe | -100.0 | 100.0 | 0.0 | 1.0 |
| `optics.defringeGreen` | Green Amount | 0.0 | 20.0 | 0.0 | 1.0 |
| `optics.defringeGreenHueHi` | Green Hue High | 10.0 | 100.0 | 60.0 | 1.0 |
| `optics.defringeGreenHueLo` | Green Hue Low | 0.0 | 90.0 | 40.0 | 1.0 |
| `optics.defringePurple` | Purple Amount | 0.0 | 20.0 | 0.0 | 1.0 |
| `optics.defringePurpleHueHi` | Purple Hue High | 10.0 | 100.0 | 70.0 | 1.0 |
| `optics.defringePurpleHueLo` | Purple Hue Low | 0.0 | 90.0 | 30.0 | 1.0 |
| `optics.distortion` | Distortion | -100.0 | 100.0 | 0.0 | 1.0 |
| `optics.profileDistortion` | Profile Distortion | 0.0 | 200.0 | 100.0 | 1.0 |
| `optics.profileVignetting` | Profile Vignetting | 0.0 | 200.0 | 100.0 | 1.0 |
| `optics.vignetting` | Vignetting | -100.0 | 100.0 | 0.0 | 1.0 |
| `optics.vignettingMidpoint` | Midpoint | 0.0 | 100.0 | 50.0 | 1.0 |

## profile

| id | label | min | max | default | step |
|---|---|---|---|---|---|
| `profile.amount` | Amount | 0.0 | 200.0 | 100.0 | 1.0 |

## vignette

| id | label | min | max | default | step |
|---|---|---|---|---|---|
| `vignette.amount` | Vignette | -100.0 | 100.0 | 0.0 | 1.0 |
| `vignette.feather` | Feather | 0.0 | 100.0 | 50.0 | 1.0 |
| `vignette.highlights` | Highlights | 0.0 | 100.0 | 0.0 | 1.0 |
| `vignette.midpoint` | Midpoint | 0.0 | 100.0 | 50.0 | 1.0 |
| `vignette.roundness` | Roundness | -100.0 | 100.0 | 0.0 | 1.0 |
