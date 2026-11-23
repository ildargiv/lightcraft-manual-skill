# Маски, точки, Point Color, Red Eye, Lens Blur

## Маска в JSON

```json
{"id": 1, "name": "sky", "visible": true, "invert": false, "on_photo": true,
 "refine": 0,
 "components": [ {"name": null, "op": "add", "invert": false, "shape": {...}} ],
 "adjust": { ...LocalAdjustments... }}
```

- `on_photo: true` — координаты маски привязаны к кадру «как снят» (до кропа, оптики,
  Upright), поэтому маска не уезжает при геометрии. Новые маски всегда `true`.
- `components` — слои одной маски: `add` / `subtract` / `intersect`; порядок важен.
- `refine` 0..100 — «Refine Edges»: край маски подтягивается к краям на фото (guided filter).

`adjust` (LocalAdjustments, все значения — приращения к глобальным):

| ключ | диапазон | смысл |
|---|---|---|
| `exposure` | ±5 EV | локальная экспозиция |
| `contrast`, `highlights`, `shadows`, `whites`, `blacks` | ±100 | локальный тон |
| `temp`, `tint` | ±100 (относительные) | локальный баланс, не Kelvin |
| `texture`, `clarity`, `dehaze` | ±100 | локальные эффекты |
| `hue` | ±100 | сдвиг оттенка |
| `saturation` | ±100 | локальная насыщенность |
| `sharpness`, `noise`, `moire`, `defringe` | ±100 | локальная детализация |
| `color_hue` | 0..360 | цветовая заливка (hue) |
| `color_sat` | 0..100 | сила заливки (0 = нет) |
| `amount` | 0..100 | общая сила маски |
| `lens_blur` | 0..100 | боке внутри маски |
| `lens_blur_off` | bool | выключить блок Lens Blur маски |
| `lens_blur_outside` | bool | размывать то, что маска **исключает** |
| `lens_blur_boost` | 0..100 | ярче блики боке |
| `lens_blur_transition` | 0..100 | плавность нарастания боке |

Ставить: `mask.adjust {id, values:{exposure:-0.3, dehaze:8}}`. Один вызов — один undo-шаг.

## Виды масок (`mask.add {kind}`)

| kind | параметры создания | форма в JSON |
|---|---|---|
| `linear` | создать пустую, затем `mask.update` | `{"kind":"linear","start":{x,y},"end":{x,y}}` |
| `radial` | `center{x,y}, rx, ry, angle, feather` | `{"kind":"radial", ... ,"invert":false}` |
| `brush` | создать, затем `mask.brushStroke` | `{"kind":"brush","strokes":[...]}` |
| `luminanceRange` | `lo, hi` (0..1) | `{"kind":"luminanceRange","lo","hi","lo_feather","hi_feather"}` |
| `colorRange` | создать, затем `mask.sampleColor` | `{"kind":"colorRange","samples":[[L,a,b]...],"refine":50}` |
| `sky` / `subject` / `background` | без параметров | `{"kind":"sky"}` и т.п. |
| `object` | `points:[[x,y]...], exclude?:[[x,y]...]` | `{"kind":"object","hint":[...],"exclude":[...],"seg":...,"edge":0}` |
| `prompt` | `text:"sky, trees"` | `{"kind":"prompt","text":"...","seg":...,"edge":0}` |

**Linear**: эффект максимален в `start` и сходит на нет к `end`. `mask.add` для linear
игнорирует `start/end` — задавать через `mask.update {id, shape:{...}}` (проверено на 0.21.1).

**Radial**: `rx/ry` — доли длинной стороны, `angle` — градусы, `feather` 0..100, `invert`.

**LuminanceRange**: `lo/hi` 0..1 и перья `lo_feather/hi_feather` 0..1 — маска по яркости
(плюс — свети́ть света, минус — тени).

**ColorRange**: `samples` — цвета в **OkLab** `[L,a,b]`, до 64 (UI держит 5).
`mask.sampleColor {x,y,add?}` возвращает добавленные тройки; `refine` 0..100 — широта оттенка.

**Sky / Subject / Background** — встроенная сегментация, SAM 3 не нужен. Работают сразу,
координат не требуют.

**Object / Prompt** — SAM 3 (`segment.model.status`; установка
`segment.model.download {acknowledged:true}`, ~3.4 ГБ, лицензия Meta). Без модели вернут
ошибку с инструкцией. Дополнительно:
- `mask.objectPoint {x,y,exclude?}` — добавить/исключить клик в Object-маску;
- `mask.refineDetail {id, component?}` — повторный проход SAM 3 в увеличенном масштабе;
- `edge` −100..100 — жёстче/мягче край (в JSON поля `edge`).

`depthRange` есть в схеме, но карты глубины в 0.21.1 нет — на практике не использовать.
`People` / `Landscape` — внутренние формы для масок по людям/классам сцены.

## Кисть

```json
{"points":[{"x":0.1,"y":0.1},{"x":0.2,"y":0.2}],
 "size":0.08, "feather":50, "flow":100, "density":100,
 "erase":false, "auto_mask":false, "pressure":[]}
```

- `size` — радиус в долях длинной стороны, `feather/flow/density` 0..100.
- `erase:true` — стереть; `auto_mask:true` — кисть держится краёв (как Auto Mask).
- `pressure` — по точке 0..1 (перо), масштабирует размер и поток.
- `mask.brushStroke {id, points, size, feather, flow, density, erase, auto_mask, pressure, connect}`
  — `connect:true` продолжает с последней точки прошлого штриха (тапер).
- Кисти живут внутри компонента `brush.strokes`; отдельного «удалить штрих» нет —
  стирать `erase:true` или удалить компонент (`mask.component {action:"delete"}`).

## Компоненты

| действие | команда |
|---|---|
| добавить слой | `mask.addComponent {id?, op, kind, ...shape}` |
| инвертировать/дублировать/удалить/переименовать/сменить op | `mask.component {id?, component:index, action}` |
| править форму | `mask.update {id?, component?:index, shape:{...}}` |
| инвертировать всю маску | `mask.invert {id?}` |
| порядок | `mask.move {id?, to \| delta}` |
| видимость | `mask.visible {id?, visible?}` |
| переименовать | `mask.rename {id?, name}` |
| выбрать | `mask.select {id \| null}` |
| удалить все | `mask.deleteAll` |

## Пресеты масок (Mask Effects)

`mask.effects` → `{effects, groups, current, toolEffects}`. По умолчанию пусто.
- `mask.saveEffect {name, id?, group?, fields?:"all"|"changed"|[slider], amount?, brush?}`
- `mask.applyEffect {name, id?|ids?|all?, photos?:"selected", remember?}`
- `mask.importEffects {path|paths, group?}` — Lightroom `.lrtemplate`, Camera Raw local `.xmp`,
  `.lceffect`, zip.
- `mask.deleteEffect`, `mask.renameEffect`, `mask.favoriteEffect`, `mask.setEffectGroup`.
- `mask.toolEffect {tool, name?}` — эффект по умолчанию для новых масок данного вида.

## Точки (Remove)

```json
{"mode":"remove|heal|clone|fill", "points":[{"x":0.5,"y":0.5}],
 "size":0.05, "feather":50, "opacity":100,
 "source_offset":{"x":-0.24,"y":0.0}}
```

- `spot.add {mode, points, size, feather?, opacity?, source?:[dx,dy]}` → `{index}`; `points` —
  одна точка (круг) или ломаная (штрих).
- `spot.update {index?, move?:[dx,dy], source?:[dx,dy], moveSource?, size?, feather?, opacity?, mode?}`.
- `spot.refreshSource {index?}` — следующий источник; `spot.delete {index?}`.
- Режимы: `remove` (источник+тон), `heal` (как remove в этой версии), `clone` (копия источника),
  `fill` (content-aware, источник не нужен).

## Red Eye

```json
{"center":{"x":0.6,"y":0.4}, "rx":0.03, "ry":0.03,
 "pet":false, "pupil_size":50, "darken":50, "catchlight":null}
```

`redeye.add {center, rx, ry, pet?, pupilSize?, darken?}` → `{index}`;
`redeye.catchlight {index, on?, offset?}`; `redeye.delete {index}`.
`rx/ry` — доли длинной стороны. Зрачок находится автоматически.

## Point Color

```json
{"hue":55.7, "chroma":0.043, "lum":0.93,
 "hue_range":50, "sat_range":50, "lum_range":50,
 "hue_shift":0, "sat_shift":0, "lum_shift":0,
 "range":50, "variance":0}
```

- `pointColor.pick {x,y}` → добавляет образец (до 8) и возвращает `{index, hue, lum, chroma}`.
- Правки — через `set_develop {settings:{point_colors:[...]}}` (слайдеров нет): менять
  `*_range` (избирательность) и `*_shift` (сдвиг), `range`, `variance`.
- `pointColor.delete {index}`.

## Lens Blur

Слайдеры: `lensBlur.amount` 0..100, `lensBlur.boost`, `lensBlur.transition` 0..100.
Включается `set_develop {settings:{lens_blur:{enabled:true, amount:55, transition:50}}}`.
Что остаётся резким:
- `focus_mask: <mask id>` — маска (любая, даже скрытая) держит фокус;
- без маски — оценка субъекта или фиксированная форма `shape: "auto|round|wide|tall"`;
- кисти: `lensBlur.brushStroke {mode:"focus"|"blur", points, size, feather, flow, amount, erase, auto_mask, pressure}`,
  сброс — `lensBlur.brushReset {mode?}`.
`focal_distance` / `focal_range` зарезервированы под карту глубины и не рендерятся.

## AI-модели

- SAM 3 (Object/Describe): `segment.model.status`, `segment.model.download {acknowledged:true}`,
  `segment.model.cancel`, `segment.prepare`.
- Denoise: `denoise.models.list`, `denoise.models.download {id, acknowledged:true}`,
  `denoise.models.select {id}`, `denoise.toggle {id, enabled}`, `denoise.queue {ids?, scope?}`,
  `denoise.status {id?}`. Без модели работает встроенный денойзер.
- Лица: `faces.models.download {id:"yunet-2023mar"}` (нужно для `spot.findBlemishes`,
  но эту автоматику мы не используем).
