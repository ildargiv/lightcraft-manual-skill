# HDR в LightCraft

## Что это

Обычный (SDR) рендер имеет белый = 1.0. В режиме HDR LightCraft хранит света **выше** SDR-белого
до `2^max_ev` и отдаёт их в HDR-экспорт. В 0.21.1 приложение **не умеет показывать HDR на
экране** (лог: `display: SDR`), поэтому `render_preview` — всегда SDR-рендишн; видеть «лишние»
стапы можно только в экспортированном HDR-файле.

Включается на любом фото (`develop.hdr`), но реальный запас есть лишь там, где он снят —
у raw и склеенных DNG. У 8-битного JPEG/HEIC данные выше белого обрезаны; такой файл всё равно
получит gain map, но выгоды от HDR почти нет.

## Два независимых полюса управления

### 1. HDR-рендер

```json
"hdr": {"enabled": true, "max_ev": 3}
```

`max_ev` 0..5 (по умолчанию 3) — потолок в стапах над SDR-белым. Ставить:
`develop.hdr {enabled:true, maxEv:3.5}` (одним шагом) или `set_develop`
`{"hdr.maxEv": 3.5}`.

Практика: 2.0–2.5 — консервативно (маленький запас, меньше риск ореолов),
3.0 — по умолчанию, 4.0–5.0 — только если в raw реально есть 4+ стапа выше белого
(солнце, лампы, окна). Чрезмерный headroom на шумных светах даёт «залитые» блики.

### 2. SDR-рендишн (`hdr.sdr*`)

Все SDR-выходы — превью, 8/16-битный экспорт без `hdr:true`, обычный JPEG — берут
«причесанную» версию кадра. Её managed слайдерами:

| слайдер | диапазон | смысл |
|---|---|---|
| `hdr.sdrBrightness` | −100..100 (±1 EV) | общая яркость SDR-версии |
| `hdr.sdrContrast` | −100..100 | контраст |
| `hdr.sdrHighlights` | −100..100 | сжатие/подъём светов |
| `hdr.sdrShadows` | −100..100 | тени |
| `hdr.sdrWhites` | −100..100 | белый |
| `hdr.sdrClarity` | −100..100 | локальный контраст |

Они **добавляются** к одноимённым глобальным слайдерам только для SDR-рендиша.
То есть `light.highlights:-40` + `hdr.sdrHighlights:-20` → в SDR свет прижат на −60,
а в HDR остаётся −40 (и лишние стапы уходят в gain map).

Типичная схема «горящего неба»:
- HDR: `light.highlights:-30`, `light.exposure:+0.3`, `maxEv:3.5` — сохраняем детали в SUN;
- SDR: `hdr.sdrHighlights:-25`, `hdr.sdrBrightness:+5`, `hdr.sdrContrast:+10` — чтобы
  обычный JPEG не был ослепительно белым.

## Пошаговый ручной HDR-рецепт (проверено на фото 90/98 библиотеки)

1. Взять raw/DNG, при необходимости `photo.virtualCopy`.
2. База: `light.exposure:+0.1…+0.3`, `highlights:-40…-60`, `shadows:+25…+40`,
   `whites:+8…+15`, `blacks:-10…-15`, `contrast:+12…+20`.
3. Включить: `develop.hdr {enabled:true, maxEv:3.5}`.
4. SDR-слой: `sdrHighlights:-25…-35`, `sdrShadows:+15…+25`, `sdrBrightness:+5…+8`,
   `sdrContrast:+8…+12`, `sdrClarity:+8…+12`, `sdrWhites:+5…+10`.
5. Цвет: vibrance +10…+20, `grading.shadows.hue:210/sat:10…15`,
   `grading.highlights.hue:35…40/sat:8…12`.
6. Маски: небо — `exposure:-0.2…-0.35`, `dehaze:+6…+10`, `temp:-8`; земля/вода —
   `exposure:+0.1…+0.2`, `clarity:+8…+12`.
7. Детализация: `detail.sharpenAmount:40…50`, `sharpenMasking:40…60`, `nrColor:20`,
   виньетка `vignette.amount:-10…-15`.
8. `render_preview` — оценить SDR. `get_develop → hdr` — проверить числа.
9. `export {path:"…hdr.jpg", hdr:true, longEdge:1600, quality:92}`.

## Экспорт HDR

`export {hdr:true}` (только после `develop.hdr enabled:true`):

| формат | что получается |
|---|---|
| JPEG | ISO 21496-1 gain map JPEG: SDR-файл + карта усиления; в HDR-просмотрщике светится |
| AVIF | 10-bit HDR; `hdrTransfer:"pq"` (по умолчанию) или `"hlg"` |
| PNG | 16-bit Rec.2020 PQ |
| JPEG XL | 16-bit Rec.2020 PQ |
| TIFF | 32-bit float со значениями >1 (linear) |

Проверено на 0.21.1: экспорт `hdr:true, format:"png", bitDepth:16, colorSpace:"rec2020"`
даёт `pix_fmt=rgb48be`, `color_transfer=smpte2084`, `color_primaries=bt2020` (ffprobe).
JPEG содержит маркеры `hdrgm` / `urn:iso:std:iso:ts:21496` — это gain map.

Обычный экспорт (`hdr` не задан) всегда SDR, даже если `hdr.enabled:true`.

## Склейка брекетов

Если есть серия с разной выдержкой:

```json
{"command":"merge.hdr","params":{"ids":[65,66,67],"align":true,"deghost":"low",
 "autoSettings":false,"stack":false}}
```

- `align` true — выравнивание; `deghost` none|low|medium|high — подавление «призраков»
  от движения; `autoSettings` — LightCraft сам поставит тон (мы его отключаем и правим руками);
  `stack` — сложить исходники в стек.
- `merge.hdrBatch` — найти все брекеты в выборке и склеить каждый; результат
  `{merged:[...], failed:[...]}`.
- `merge.panorama` / `merge.hdrPanorama` — панорама; `projection` auto|spherical|cylindrical|
  perspective, `boundaryWarp` 0..100, `autoCrop`, `fillEdges`.
- Из CLI (файлы без импорта): `lightcraft-cli merge hdr [--deghost low] --preview out.png FILES…`;
  результат — `<первый>-HDR.dng`.
- После склейки работает обычный конвейер + HDR-блок выше; склеенный DNG уже содержит
  запас по светам — `maxEv` 3..4 уместен.

## Ограничения и ловушки

- Превью не показывает HDR-запас. Не «повышать exposure, пока не станет видно» — это
  испортит SDR.
- Gain map JPEG корректно видна только в HDR-совместимом просмотрщике; в обычном —
  обычный SDR-кадр (это нормально).
- Слишком высокий `maxEv` на шумном raw усиливает шум в светах: сначала NR.
- `hdr.enabled` — часть настроек фото; попадает в XMP/сидкар и копируется при virtual copy.
- `export {hdr:true}` на фото без `hdr.enabled` экспортирует как обычный SDR (проверять результат).
