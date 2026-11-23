# Пресеты LightCraft: что внутри каждого

Сгенерировано через `preset.export` из установленной версии LightCraft.
Ключи — пути в `develop` JSON, значения — те же числа, что у слайдеров.

## Как этим пользоваться агенту

- Пресет — это **рецепт**, а не кнопка. По умолчанию агент ставит те же числа руками
  (`set_develop`), чтобы контролировать каждый шаг.
- `preset.apply {id, amount}` — только по явной просьбе, и затем довести руками.
- Свои пресеты: `preset.create`, `preset.update`, `preset.saveRecipe`.

## Встроенные develop-пресеты (41)

## B&W

### High Contrast B&W — `lc.bw-high-contrast`
- `bw_mix.blue` = -30
- `bw_mix.red` = 15
- `effects.clarity` = 20
- `light.blacks` = -25
- `light.contrast` = 45
- `light.whites` = 20
- `treatment` = bw

### Selenium Tone — `lc.bw-selenium`
- `grading.highlights.hue` = 40
- `grading.highlights.lum` = 0
- `grading.highlights.sat` = 10
- `grading.shadows.hue` = 285
- `grading.shadows.lum` = 0
- `grading.shadows.sat` = 18
- `light.contrast` = 20
- `treatment` = bw

### Sepia Tone — `lc.bw-sepia`
- `curve.shadows` = 10
- `grading.highlights.hue` = 42
- `grading.highlights.lum` = 0
- `grading.highlights.sat` = 18
- `grading.shadows.hue` = 32
- `grading.shadows.lum` = 0
- `grading.shadows.sat` = 22
- `treatment` = bw

### Soft B&W — `lc.bw-soft`
- `curve.shadows` = 15
- `light.contrast` = -15
- `light.shadows` = 25
- `treatment` = bw

## Color

### Cool Morning — `lc.cool-morning`
- `color.vibrance` = 10
- `grading.shadows.hue` = 215
- `grading.shadows.lum` = 0
- `grading.shadows.sat` = 12
- `light.highlights` = -20
- `treatment` = color
- `wb.mode` = custom
- `wb.temp` = 5600
- `wb.tint` = -4

### Soft Pastel — `lc.soft-pastel`
- `color.saturation` = -18
- `color.vibrance` = 10
- `curve.shadows` = 25
- `light.blacks` = 20
- `light.contrast` = -25
- `light.highlights` = -30
- `light.shadows` = 35
- `treatment` = color

### Teal & Orange — `lc.teal-orange`
- `color.vibrance` = 12
- `grading.balance` = 10
- `grading.highlights.hue` = 35
- `grading.highlights.lum` = 0
- `grading.highlights.sat` = 22
- `grading.shadows.hue` = 195
- `grading.shadows.lum` = 0
- `grading.shadows.sat` = 28
- `light.contrast` = 14
- `treatment` = color

### Vivid Pop — `lc.vivid-pop`
- `color.saturation` = 8
- `color.vibrance` = 40
- `effects.clarity` = 12
- `light.blacks` = -10
- `light.contrast` = 18
- `light.whites` = 10
- `treatment` = color

### Warm Glow — `lc.warm-glow`
- `color.vibrance` = 18
- `light.contrast` = 8
- `light.shadows` = 12
- `treatment` = color
- `wb.mode` = custom
- `wb.temp` = 7200
- `wb.tint` = 8

## Film

### Faded Matte — `lc.faded-matte`
- `color.saturation` = -12
- `curve.highlights` = -15
- `curve.shadows` = 40
- `grain.amount` = 18
- `grain.roughness` = 50
- `grain.size` = 25
- `light.contrast` = -10
- `treatment` = color

### Muted Film — `lc.muted-film`
- `color.saturation` = -25
- `color.vibrance` = 5
- `curve.shadows` = 18
- `grain.amount` = 15
- `light.contrast` = 10
- `treatment` = color

### Warm Film — `lc.warm-film`
- `curve.shadows` = 22
- `grading.highlights.hue` = 45
- `grading.highlights.lum` = 0
- `grading.highlights.sat` = 15
- `grain.amount` = 22
- `grain.roughness` = 55
- `grain.size` = 30
- `treatment` = color
- `vignette.amount` = -12
- `wb.mode` = custom
- `wb.temp` = 6900
- `wb.tint` = 5

## Food

### Dark & Moody — `lc.dark-moody-food`
- `effects.texture` = 18
- `light.blacks` = -15
- `light.contrast` = 22
- `light.exposure` = -0.3
- `light.highlights` = -20
- `treatment` = color
- `vignette.amount` = -22

### Fresh & Bright — `lc.fresh-bright`
- `color.vibrance` = 22
- `effects.texture` = 15
- `light.exposure` = 0.25
- `light.shadows` = 20
- `light.whites` = 10
- `treatment` = color

### Warm Table — `lc.warm-table`
- `grading.midtones.hue` = 32
- `grading.midtones.lum` = 0
- `grading.midtones.sat` = 10
- `light.contrast` = 8
- `mixer.orange.sat` = 10
- `mixer.red.sat` = 8
- `treatment` = color

## Landscape

### Blue Hour Boost — `lc.blue-hour`
- `light.exposure` = 0.2
- `light.shadows` = 25
- `mixer.blue.hue` = 0
- `mixer.blue.lum` = 0
- `mixer.blue.sat` = 25
- `mixer.purple.hue` = 0
- `mixer.purple.lum` = 0
- `mixer.purple.sat` = 15
- `treatment` = color
- `wb.mode` = custom
- `wb.temp` = 5200
- `wb.tint` = 6

### Crisp Landscape — `lc.crisp-landscape`
- `color.vibrance` = 25
- `effects.clarity` = 22
- `effects.dehaze` = 12
- `effects.texture` = 15
- `light.contrast` = 12
- `light.highlights` = -45
- `light.shadows` = 30
- `treatment` = color

### Crisp Vista — `lc.crisp-vista`
- `color.vibrance` = 20
- `effects.clarity` = 18
- `effects.dehaze` = 15
- `effects.texture` = 12
- `light.contrast` = 12
- `light.highlights` = -25
- `light.shadows` = 18
- `treatment` = color

### Deep Sky — `lc.deep-sky`
- `effects.dehaze` = 10
- `light.highlights` = -30
- `mixer.aqua.lum` = -10
- `mixer.blue.lum` = -25
- `mixer.blue.sat` = 15
- `treatment` = color

### Desert Warmth — `lc.desert-warmth`
- `grading.highlights.hue` = 38
- `grading.highlights.lum` = 0
- `grading.highlights.sat` = 12
- `light.contrast` = 10
- `mixer.blue.sat` = -10
- `mixer.orange.lum` = 5
- `mixer.orange.sat` = 15
- `mixer.yellow.hue` = -8
- `mixer.yellow.sat` = 10
- `treatment` = color

### Golden Hour — `lc.golden-hour`
- `grading.highlights.hue` = 38
- `grading.highlights.lum` = 5
- `grading.highlights.sat` = 25
- `light.highlights` = -35
- `light.shadows` = 20
- `treatment` = color
- `vignette.amount` = -15
- `wb.mode` = custom
- `wb.temp` = 7600
- `wb.tint` = 12

### Lush Greens — `lc.lush-greens`
- `color.vibrance` = 12
- `effects.clarity` = 8
- `mixer.green.hue` = 12
- `mixer.green.lum` = 8
- `mixer.green.sat` = 18
- `mixer.yellow.hue` = 10
- `mixer.yellow.sat` = 10
- `treatment` = color

### Misty Morning — `lc.misty-morning`
- `color.saturation` = -10
- `effects.clarity` = -12
- `effects.dehaze` = -18
- `grading.shadows.hue` = 210
- `grading.shadows.lum` = 0
- `grading.shadows.sat` = 10
- `light.contrast` = -18
- `light.highlights` = -10
- `treatment` = color

## Portrait

### Bright & Airy — `lc.bright-airy`
- `color.saturation` = -8
- `color.vibrance` = 8
- `light.contrast` = -15
- `light.exposure` = 0.45
- `light.highlights` = -40
- `light.shadows` = 40
- `light.whites` = 15
- `treatment` = color

### Clean Studio — `lc.clean-studio`
- `color.vibrance` = 5
- `effects.texture` = -10
- `light.blacks` = -8
- `light.contrast` = 10
- `light.whites` = 15
- `treatment` = color

### Golden Glow — `lc.golden-glow`
- `effects.clarity` = -8
- `grading.highlights.hue` = 40
- `grading.highlights.lum` = 0
- `grading.highlights.sat` = 18
- `grading.midtones.hue` = 35
- `grading.midtones.lum` = 0
- `grading.midtones.sat` = 8
- `light.shadows` = 15
- `treatment` = color

### Moody Portrait — `lc.moody-portrait`
- `color.saturation` = -15
- `light.blacks` = -12
- `light.contrast` = 20
- `light.exposure` = -0.25
- `light.highlights` = -30
- `mixer.orange.sat` = 6
- `treatment` = color
- `vignette.amount` = -25
- `vignette.midpoint` = 40

### Soft Skin — `lc.soft-skin`
- `effects.clarity` = -10
- `effects.texture` = -25
- `light.contrast` = -5
- `light.shadows` = 15
- `mixer.orange.hue` = 0
- `mixer.orange.lum` = 10
- `mixer.orange.sat` = -8
- `treatment` = color

## Seasons

### Autumn Gold — `lc.autumn-gold`
- `grading.highlights.hue` = 40
- `grading.highlights.lum` = 0
- `grading.highlights.sat` = 10
- `mixer.green.hue` = -30
- `mixer.green.sat` = -10
- `mixer.orange.sat` = 18
- `mixer.yellow.hue` = -15
- `mixer.yellow.sat` = 15
- `treatment` = color

### Spring Fresh — `lc.spring-fresh`
- `color.vibrance` = 15
- `light.shadows` = 15
- `mixer.green.hue` = 10
- `mixer.green.lum` = 10
- `mixer.green.sat` = 12
- `mixer.magenta.sat` = 10
- `treatment` = color

### Summer Haze — `lc.summer-haze`
- `curve.shadows` = 18
- `effects.dehaze` = -12
- `grading.highlights.hue` = 45
- `grading.highlights.lum` = 0
- `grading.highlights.sat` = 14
- `light.contrast` = -10
- `treatment` = color

### Winter Blue — `lc.winter-blue`
- `color.saturation` = -12
- `grading.highlights.hue` = 205
- `grading.highlights.lum` = 0
- `grading.highlights.sat` = 8
- `grading.shadows.hue` = 215
- `grading.shadows.lum` = 0
- `grading.shadows.sat` = 18
- `light.whites` = 12
- `treatment` = color

## Style

### Cinematic — `lc.cinematic`
- `curve.highlights` = -10
- `curve.shadows` = 20
- `grading.highlights.hue` = 30
- `grading.highlights.lum` = 0
- `grading.highlights.sat` = 18
- `grading.shadows.hue` = 190
- `grading.shadows.lum` = 0
- `grading.shadows.sat` = 25
- `light.contrast` = 15
- `treatment` = color
- `vignette.amount` = -20

### Moody — `lc.moody`
- `color.saturation` = -20
- `grading.shadows.hue` = 200
- `grading.shadows.lum` = -5
- `grading.shadows.sat` = 15
- `light.blacks` = -15
- `light.contrast` = 20
- `light.exposure` = -0.3
- `light.highlights` = -30
- `treatment` = color
- `vignette.amount` = -30

## Urban

### Concrete Cool — `lc.concrete-cool`
- `color.saturation` = -20
- `effects.clarity` = 15
- `grading.highlights.hue` = 200
- `grading.highlights.lum` = 0
- `grading.highlights.sat` = 6
- `grading.shadows.hue` = 205
- `grading.shadows.lum` = 0
- `grading.shadows.sat` = 14
- `light.contrast` = 12
- `treatment` = color

### Faded Urban — `lc.faded-urban`
- `color.saturation` = -22
- `curve.shadows` = 30
- `grain.amount` = 12
- `grain.roughness` = 45
- `grain.size` = 25
- `light.contrast` = -8
- `treatment` = color

### Gritty Street — `lc.gritty-street`
- `color.saturation` = -30
- `effects.clarity` = 35
- `effects.texture` = 20
- `light.blacks` = -15
- `light.contrast` = 25
- `treatment` = color
- `vignette.amount` = -18

### Neon Night — `lc.neon-night`
- `color.vibrance` = 15
- `grading.shadows.hue` = 250
- `grading.shadows.lum` = 0
- `grading.shadows.sat` = 15
- `light.blacks` = -12
- `light.contrast` = 18
- `mixer.aqua.sat` = 15
- `mixer.blue.sat` = 12
- `mixer.magenta.sat` = 20
- `mixer.purple.sat` = 18
- `treatment` = color

## Vintage

### Bleach Bypass — `lc.bleach-bypass`
- `color.saturation` = -40
- `effects.clarity` = 15
- `light.contrast` = 35
- `light.highlights` = -15
- `treatment` = color

### Cross Process — `lc.cross-process`
- `color.saturation` = 10
- `grading.highlights.hue` = 60
- `grading.highlights.lum` = 0
- `grading.highlights.sat` = 25
- `grading.shadows.hue` = 230
- `grading.shadows.lum` = 0
- `grading.shadows.sat` = 25
- `light.contrast` = 22
- `treatment` = color

### Instant ’70s — `lc.instant-70s`
- `color.saturation` = -10
- `curve.highlights` = -18
- `curve.shadows` = 28
- `grading.highlights.hue` = 45
- `grading.highlights.lum` = 0
- `grading.highlights.sat` = 18
- `grading.shadows.hue` = 170
- `grading.shadows.lum` = 0
- `grading.shadows.sat` = 14
- `grain.amount` = 20
- `grain.roughness` = 55
- `grain.size` = 30
- `treatment` = color
- `vignette.amount` = -15

## Point curve пресеты (3, `curve.presets`)

| name | master |
|---|---|
| Linear | [] (тождественная) |
| Medium Contrast | [[0,0],[0.25,0.2],[0.5,0.5],[0.75,0.8],[1,1]] |
| Strong Contrast | [[0,0],[0.25,0.14],[0.5,0.5],[0.75,0.86],[1,1]] |

`curve.applyPreset {name}` или руками `develop.curve {channel, points}`.
Параметрическая кривая (`curve.highlights/lights/darks/shadows`) — отдельно.

## Export-пресеты (8, `export.presets`)

| name | params |
|---|---|
| JPEG (Small) | `{"format":"jpeg","longEdge":2048,"quality":85,"colorSpace":"srgb"}` |
| JPEG (Large) | `{"format":"jpeg","longEdge":0,"quality":92,"colorSpace":"srgb"}` |
| Original + Settings | `{"format":"original"}` |
| DNG | `{"format":"dng"}` |
| Instagram Feed | `{"format":"jpeg","longEdge":1080,"quality":85,"colorSpace":"srgb","sharpen":"screen"}` |
| Instagram Story / Reel | `{"format":"jpeg","longEdge":1920,"quality":85,"colorSpace":"srgb","sharpen":"screen"}` |
| Web / Portfolio | `{"format":"jpeg","longEdge":2048,"quality":85,"colorSpace":"srgb","metadata":"copyright"}` |
| Full Resolution Master | `{"format":"jpeg","longEdge":0,"quality":95,"colorSpace":"displayP3"}` |

`export {preset: "Instagram Feed", ...}` — поля можно переопределить.
