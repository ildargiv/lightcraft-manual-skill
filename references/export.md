# Экспорт

Helper `export` (MCP) и команда `app.export` — один и тот же энкодер. Полный список параметров
есть в сигнатуре `export` и в `command_list filter=app.export`.

## Минимум

```json
{"path":"C:\\Users\\User\\Pictures\\out.jpg","id":98,"longEdge":2000,"quality":90}
```

- `path` — один файл, формат из расширения (или явно `format`); `dir` — пакетная выгрузка.
- `id` делает фото активным; `ids` — несколько; без них — текущее выделение.
- Если размер не указан — **longEdge 3000**. `longEdge:0` — полный размер кропа.
- `dontEnlarge` по умолчанию true — маленькие фото не растягиваются.
- Размеры: `shortEdge`, `width`, `height`, `megapixels`, `percent`, `resize`;
  `width+height` → `fit:"dimensions"` (любая ориентация) или `fit:"widthHeight"`.

## Форматы

| format | расширение | битность | заметки |
|---|---|---|---|
| `jpeg` | .jpg | 8 | quality 1..100; `limitKb` — подобрать качество под размер; `hdr:true` → gain map |
| `png` | .png | 8/16 | 16-bit + `colorSpace:"rec2020"` + `hdr:true` → PQ |
| `tiff` | .tif | 8/16/32 | 32 = linear float с выше-1 (HDR); `tiffCompression` zip/lzw/none |
| `webp` | .webp | 8 | quality |
| `avif` | .avif | 8/10 | 10-bit при `hdr:true`, `hdrTransfer` pq/hlg |
| `jxl` | .jxl | 8/16 | `jxlLossless`, `jxlEffort`, `jxlProgressive` |
| `psd` | .psd | 8/16 | плоский PSD без слоёв |
| `dng` | .dng | — | только raw: DNG с вшитыми правками; `dngCompression` |
| `rendereddng` | .dng | 16 float | линейный DNG с запечённым рендером (только helper `export`) |
| `original` | как есть | — | копия файла + XMP-сидкар с правками |

## Цвет и резкость

`colorSpace`: `srgb` (по умолчанию), `displayP3`, `adobeRgb`, `proPhoto`, `rec2020`.
AVIF всегда sRGB; lossy JXL пишет adobeRgb/proPhoto как rec2020.

`sharpen`: `none | screen | matte | glossy`; `sharpenAmount`: `low | standard | high`.
Это **выводная** резкость поверх `detail.sharpenAmount` — для web обычно `screen/standard`.

`metadata`: `all | allExceptCamera | copyright | none`; `removeLocation:true`; `ppi`
(по умолчанию 240, для печати 300).

`watermark`: строка или объект с `text`, `size` (0.005..0.5 короткой стороны), `opacity`
(0..1), `anchor` (topLeft…bottomRight), `insetX/insetY/inset`, `rotation` (0/90/180/270),
`color:[r,g,b]`, `shadow`, `image` (путь к картинке вместо текста), `imageWidth`.

## Пакетная выгрузка

```json
{"dir":"D:\\Export","ids":[65,66,67],"format":"jpeg","longEdge":2048,
 "naming":"{date:%Y-%m-%d}_{title}_{seq:2}","conflict":"unique","subfolder":"web",
 "destinationMode":"specificFolder","metadata":"copyright"}
```

- `naming` — токены `{name} {num} {seq} {seq:N} {date} {date:%…} {folder} {camera} {lens}
  {iso} {rating} {title} {creator} {ext}`. Полный список с объяснениями —
  `command_run photo.renameTokens`.
- `conflict`: `unique` (по умолчанию), `overwrite`, `skip`.
- `destinationMode`: `specificFolder` (всё в `dir`) или `sameAsOriginal` (рядом с каждым
  оригиналом + `subfolder`).
- `startNumber` — первый `{seq}`.

## Пресеты экспорта

`export {preset:"Web / Portfolio"}`; список и параметры всех восьми — `references/presets.md`.
Любое поле из preset можно переопределить аргументом. Свои: `export.savePreset {name, params}`,
`export.deletePreset {name}`.

## HDR

`export {hdr:true, ...}` — см. `references/hdr.md`. Кратко: JPEG → gain map ISO 21496-1,
AVIF → 10-bit PQ/HLG, PNG/JXL → 16-bit Rec.2020 PQ, TIFF → 32-bit float.
Требует `develop.hdr.enabled:true`, иначе выйдет обычный SDR.

## Дополнительно

- `export.contactSheet {path, ids?, paper:"a4"|"letter", landscape?, columns:1..8, rows:1..10,
  captions?}` — PDF с миниатюрами.
- `export.checkTarget {path}` — проверить, не перезапишет ли путь оригинал/сидкар.
- `addToPhotos` / `photosAlbum` — только macOS; на Windows вернёт ошибку до записи файлов.
- `background:true` — фоновая выгрузка в десктопе (headless всё равно блокирующая).

## Правила агента

1. Тестовые выгрузки — в `<temp>\`, не в папку с оригиналами.
2. Никогда не указывать путь оригинала или его XMP — LightCraft откажет, но лучше не проверять.
3. Проверять результат: `Get-Item` (размер > 0) и `ffprobe -show_entries stream=pix_fmt,color_transfer,...`.
4. Для соцсетей: sRGB, longEdge 1080/2048, quality 85, `sharpen:"screen"`.
5. Для архива: `format:"original"` (копия + XMP) или DNG — правки не теряются и остаются неразрушающими.
