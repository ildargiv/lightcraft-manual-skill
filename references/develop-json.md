# Схема `develop` JSON

`get_develop {id}` возвращает полный снимок настроек. `set_develop {settings:{...}}` и
`develop.merge {settings:{...}}` делают **глубокий merge**: указывать можно только изменяемые
поля. Массивы (`masks`, `spots`, `point_colors`, `red_eye`, `curve.*`) заменяются целиком.

Ниже — все ключи с единицами и смыслом. Диапазоны — из `references/controls.md`.

## Верхний уровень

| ключ | тип | смысл |
|---|---|---|
| `process` | int | версия рендеринга (V8 в 0.21.1). Старое значение = старый вид; `develop.updateProcess` меняет картинку — не трогать без просьбы |
| `version` | int | версия формата настроек (1) |
| `treatment` | `"color" \| "bw"` | ч/б переключается `develop.treatment` или здесь |
| `profile` | `{id, amount}` | профиль (id из `profiles.list`, amount 0..200) |
| `orientation` | `"Normal" \| ...` | ориентация кадра |
| `disabled_sections` | `[string]` | выключенные секции (`develop.sectionEnabled`) |
| `wb` | объект | баланс белого |
| `light` | объект | экспозиция и тональная база |
| `curve` | объект | параметрическая кривая + точки по каналам |
| `color` | объект | насыщенность/сочность |
| `mixer` | объект | HSL по 8 цветовым диапазонам |
| `bw_mix` | объект | светофильтры ч/б (8 диапазонов) |
| `calibration` | объект | калибровка камеры (hue/sat по R/G/B + tint теней) |
| `grading` | объект | цветокоррекция по тонам (3 колеса + global) |
| `effects` | объект | texture/clarity/dehaze |
| `detail` | объект | шумоподавление и резкость |
| `enhance` | объект | AI Denoise и raw-детали |
| `optics` | объект | профиль объектива, дисторсия, виньетка, CA |
| `geometry` | объект | upright, перспектива, поворот, масштаб |
| `crop` | объект | кроп, угол, флипы, геометрия кропа |
| `vignette` | объект | художественная виньетка |
| `grain` | объект | зерно |
| `lens_blur` | объект | размытие глубины резкости |
| `hdr` | объект | HDR-редактирование и SDR-рендишн |
| `masks` | массив | локальные маски |
| `spots` | массив | точки удаления/лечения |
| `point_colors` | массив | Point Color (до 8 образцов) |
| `red_eye` | массив | коррекция красных глаз |

## wb

```json
{"mode":"asShot|auto|daylight|cloudy|shade|tungsten|fluorescent|flash|custom",
 "temp":5600, "tint":4, "scale":"kelvin"}
```

- `mode:custom` + `temp/tint` — ручной баланс.
- `temp`: 2000..50000 K; `tint`: −150..150 (плюс = magenta).
- **`scale`**: `"kelvin"` — абсолютная температура; отсутствует — относительная шкала
  (6500 = как снято). `set_develop {values:{"wb.temp":...}}` сам выбирает шкалу по файлу;
  `settings.wb` без `scale` всегда относительный. Для raw, где нужен точный Kelvin, добавлять
  `"scale":"kelvin"`.

## light

| поле | диапазон | смысл |
|---|---|---|
| `exposure` | −5..5 EV (шаг 0.01) | яркость всего кадра |
| `contrast` | −100..100 | общий контраст (V4+ калиброван под Lightroom) |
| `highlights` | −100..100 | восстановление/усиление светов; минус — вытянуть детали |
| `shadows` | −100..100 | плюс — поднять тени |
| `whites` | −100..100 | точка белого |
| `blacks` | −100..100 | точка чёрного; минус — глубже провалы |

Порядок: экспозиция → highlights/shadows → whites/blacks → contrast. Контраст последним,
иначе он «съест» только что вытянутые детали.

## curve

```json
{"master":[[x,y],...], "red":[], "green":[], "blue":[],
 "highlights":0, "lights":0, "darks":0, "shadows":0,
 "splitHighlights":75, "splitMid":50, "splitShadows":25,
 "refine_saturation":100}
```

- Точки: `[вход, выход]` в 0..1, минимум 2, `[[0,0],[1,1]]` — линейно.
- Параметрическая часть (`highlights/lights/darks/shadows`) и точки применяются вместе.
- `split*` — границы зон параметрической кривой (30..90 / 20..80 / 10..70).
- Ставить: `develop.curve {channel:"master|red|green|blue", points:[[x,y],...]}` или `settings.curve`.
- `curve.applyPreset {name}`: Linear / Medium Contrast / Strong Contrast.

## color / mixer / bw_mix / calibration

`color`: `saturation` −100..100, `vibrance` −100..100 (vibrance щадит уже насыщенное и кожу).

`mixer.<band>` где band ∈ `red, orange, yellow, green, aqua, blue, purple, magenta`, поля
`hue` −100..100 (сдвиг оттенка), `sat` −100..100, `lum` −100..100.

`bw_mix.<band>` — те же 8 диапазонов, яркость −100..100 (как светофильтры в ч/б).

`calibration`: `red_hue/red_sat/green_hue/green_sat/blue_hue/blue_sat` −100..100,
`shadows_tint` −100..100.

## grading

```json
{"balance":0, "blending":50,
 "global":{"hue":0,"lum":0,"sat":0},
 "shadows":{"hue":0,"lum":0,"sat":0},
 "midtones":{"hue":0,"lum":0,"sat":0},
 "highlights":{"hue":0,"lum":0,"sat":0}}
```

`hue` 0..360 (колесо), `lum` −100..100, `sat` 0..100. `blending` 0..100 — плавность перехода
между тонами; `balance` −100..100 — куда смещён «центр» разделения.

## effects / detail / enhance

`effects`: `texture` −100..100 (микрорельеф), `clarity` −100..100 (средние частоты),
`dehaze` −100..100 (плюс — убрать дымку, минус — добавить).

`detail`:
`nr_luminance` 0..100, `nr_detail` 0..100, `nr_contrast` 0..100,
`nr_color` 0..100, `nr_color_detail` 0..100,
`nr_color_smoothness` 0..100, `nr_outliers` bool,
`sharpen_amount` 0..150, `sharpen_radius` 0.5..3.0, `sharpen_detail` 0..100,
`sharpen_masking` 0..100.

Дефолты: у **raw при импорте** — Lightroom-профиль (amount 40, radius 1.0, detail 25,
masking 0, `nr_color` 25); у остальных файлов нейтрально (amount 0, nr 0). Поэтому на raw
резкость уже стоит — не добавлять 40 сверху, а смотреть, что есть.

`enhance`: `denoise` 0..100 (AI Denoise, только raw — `denoise.toggle`),
`raw_details` bool, `super_resolution` bool. Выключение AI Denoise хранится в `denoise_on`.

## optics

`lens_profile` bool (включить коррекцию профиля), `profile_distortion` / `profile_vignetting`
0..200 %, `distortion` −100..100, `vignetting` −100..100, `vignetting_midpoint` 0..100,
`ca_red`/`ca_blue` −100..100, `remove_ca` bool,
`defringe_purple_amount`/`defringe_green_amount` 0..20,
`defringe_*_hue_lo` 0..90, `defringe_*_hue_hi` 10..100.

## geometry / crop

`geometry`: `upright` (`off|auto|guided|level|vertical|full`), `guides` (до 4 линий
`[[x0,y0,x1,y1]]`), `horizontal`, `vertical` −100..100, `rotate` −10..10°, `scale` 50..150 %,
`offset_x`, `offset_y` −100..100, `aspect` −100..100, `constrain_crop` bool,
`upright_transform` (внутреннее).

`crop`:
```json
{"aspect": null, "flip_h": false, "flip_v": false,
 "geometry": {"angle": 0, "rect": {"x0":0,"y0":0,"x1":1,"y1":1}}}
```
`rect` — нормализованный, в выпрямленной системе (0..1, от левого верха). Менять через
`crop {rect, angle}` / `crop.aspect {aspect}` / `crop.reset`.

## vignette / grain / lens_blur / hdr

`vignette`: `amount` −100..100, `feather` 0..100, `midpoint` 0..100, `roundness` −100..100,
`highlights` 0..100, `style` (`highlightPriority|colorPriority|paintOverlay`).

`grain`: `amount` 0..100, `size` 0..100, `roughness` 0..100, `seed` (u32; 0 — авто).

`lens_blur`: `enabled` bool, `amount` 0..100 (100 = диск 3.5 % длинной стороны),
`boost` 0..100 (ярче боке-блики), `transition` 0..100 (плавность нарастания размытия),
`focus_mask` (id маски, которая остаётся резкой; `null` — субъект по эвристике),
`shape` (`auto|round|wide|tall` — форма зоны резкости без маски),
`focus_strokes` / `blur_strokes` (кисти уточнения, см. `lensBlur.brushStroke`).
`focal_distance` / `focal_range` — **зарезервированы под карту глубины и не рендерятся**:
через них резкость не настроить. Практика: маска (radial/object) → `lens_blur.focus_mask` →
`amount`, `transition`; кисти — точечно.

`hdr`:
```json
{"enabled": true, "max_ev": 3,
 "sdr_brightness": 0, "sdr_contrast": 0, "sdr_highlights": 0,
 "sdr_shadows": 0, "sdr_whites": 0, "sdr_clarity": 0}
```
`max_ev` 0..5 — запас светов выше SDR-белого. `sdr_*` — как HDR-кадр выглядит в SDR
(превью, JPEG без `hdr:true`, соцсети).

## Profile

```json
{"id":"lc.color", "amount":100}
```
`profiles.list` → все профили (встроенные + импортированные LUT), `profiles.camera` →
импортированные .dcp. Ставить `develop.profile {id, amount}`.

## Пример: частичный merge

```json
{"light":{"exposure":0.4,"highlights":-45,"shadows":30,"contrast":12,"whites":8,"blacks":-10},
 "color":{"vibrance":15},
 "effects":{"texture":8,"clarity":8,"dehaze":5},
 "detail":{"sharpenAmount":40,"sharpenMasking":40,"nrColor":20,"nrLuminance":10},
 "grading":{"shadows":{"hue":210,"sat":10,"lum":-2},"highlights":{"hue":40,"sat":8,"lum":3},
            "balance":-5,"blending":55}}
```

Ключи в JSON — `snake_case` (`sharpen_amount`), в `set_develop {values}` — id слайдеров
(`detail.sharpenAmount`). Не смешивать: `values` — плоские id, `settings` — вложенный JSON.
