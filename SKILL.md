---
name: lightcraft
description: Ручное редактирование фото в LightCraft через MCP — все слайдеры, кривые, HSL, цветокоррекция, маски, точки, HDR, склейка брекетов, пресеты, экспорт. Используй когда нужно отредактировать фото в LightCraft, разобрать/повторить пресет, сделать HDR, маску неба/объекта, убрать пятна, выровнять горизонт или выгрузить файл.
---

# LightCraft — ручное редактирование через MCP

LightCraft 0.21.1 (актуальная версия на 24.11.2026) — неразрушающий RAW-редактор.
MCP-сервер в `opencode.json` запускается через обёртку
`python.exe ...\skills\lightcraft\scripts\mcp-connect.py`, которая при необходимости поднимает
приложение с `--control 7980`, а затем передаёт stdio в `lightcraft-cli mcp --compact --connect`.
Режим — **connect**: агент управляет запущенным десктопным приложением, правки видны в окне
сразу. Библиотеку держит приложение (`%USERPROFILE%\Pictures\LightCraft Library`), сервер не
конкурирует за `catalog.lock`. Доступны инструменты живого UI.

Если приложение закрылось, обёртка поднимет его сама при следующем старте MCP. Вручную
(команда идемпотентна):

```powershell
powershell -ExecutionPolicy Bypass -File "~/.config/opencode/skills/lightcraft\scripts\start-lightcraft-app.ps1"
```

## Главный принцип: руками, а не автоматикой

Пользователь требует, чтобы правки делал **агент своими значениями**, а не встроенный
«мозг» программы. Это правило важнее скорости.

| Не вызывать (автоматика) | Чем заменить |
|---|---|
| `develop.auto`, `develop.autoBwMix` | явные числа по рецепту (`set_develop`) |
| `develop.wb {mode:"auto"}` | серый нейтральный пипеткой `develop.wbPick {x,y}` или `temp/tint` вручную |
| `crop.autoStraighten` | `crop {angle: N}` / `crop.straighten {angle}` по видимому горизонту |
| `geometry.upright {mode:auto}` | `geometry` слайдеры (horizontal/vertical/rotate); при явной просьбе — `geometry.guides` + режим `guided` |
| `spot.findDust`, `spot.findBlemishes` | `spot.add` с координатами |
| `lensBlur.findSubject` | маска Object/radial + `lensBlur` слайдеры |
| `photo.analyze`, `pickBest`, `develop.autoSync` | ручной отбор и ручные правки |
| `preset.apply` | числа из пресета руками (см. `references/presets.md`) |
| `develop.matchExposure`, `develop.sync` | точечные значения на каждое фото |

Исключения — технические операции, а не творческие решения: `import`, `export`,
`select_photos`, `photo.rate/flag/label`, метаданные, `edit.undo/redo`, `history.*`,
`denoise.toggle` (только количество шума задаём сами), `mask.refine` (это край маски, не вкус).

Если пользователь **явно** просит «наложи пресет X» — можно `preset.apply {id, amount}`,
но затем довести руками. Если просит «как в Lightroom» — это не повод включать Auto.

## Рабочий цикл

1. **Состояние**: `doc_inspect` (активное фото, выделение, undo) → `get_develop {id}`
   (полный JSON), `list_controls {section}` (границы и текущие значения).
2. **Оценка кадра**: `render_preview {id, max_side: 1024–1600, format:"jpeg"}` — смотреть
   глазами: пересветы, провалы, баланс, мусор, горизонт.
3. **Правки по конвейеру** (см. ниже), каждая — отдельный вызов (отдельный undo-шаг).
   Лучше `command_batch` из 3–8 шагов на смысловой блок, чем 40 одиночных.
4. **Проверка**: снова `render_preview`. Сравнить с предыдущим кадром в голове, а не «на глаз
   по числам». При сомнении — `history.list` и `history.restore`.
5. **Экспорт**: `export` с нужным размером/форматом; HDR — только с `hdr:true` (см. `references/hdr.md`).

Не менять фото пользователя без нужды: для экспериментов `photo.virtualCopy {ids}` →
работать на копии → `photo.deletePermanently` копию в конце (как сделано при проверке HDR).

## Порядок конвейера (как в Lightroom)

`profile → wb → light → curve (параметрика+точки) → color/mixer/bw → grading → effects →
detail (NR/sharpen/denoise) → optics (профиль, дисторсия, виньетка, CA) → geometry/crop →
маски/точки/red eye → lens blur → HDR → grain/vignette (эффекты) → export`.

Почему так: баланс белого и свет задают базу; HSL и grading красят уже нормированный тон;
резкость/шум — в конце тона; геометрия после оптики; маски — после общей базы, иначе
локальные правки придётся переделывать.

## Маршрутизация инструментов

В `--compact` доступны 18 helper-инструментов; всё остальное — через `command_run`.
Полный каталог: `command_list` (392 команды), живой параметр-док у каждой.

| Задача | Инструмент |
|---|---|
| слайдеры | `set_develop {values:{id:number}}` или `develop.set` |
| частичный JSON (кривые, маски, point color, lens blur) | `set_develop {settings:{...}}`, `develop.merge` |
| маски | `mask.add`, `mask.update`, `mask.adjust`, `mask.brushStroke`, `mask.refine`, `mask.invert`, `mask.component` |
| точки/red eye | `spot.add/update/delete`, `redeye.add/catchlight/delete` |
| кривые точки | `develop.curve`, `curve.applyPreset` |
| HSL по точке | `develop.targeted` (явный `delta`) или `mixer.*` |
| геометрия | `crop.*`, `geometry.upright/guides`, `develop.set` |
| HDR | `develop.hdr`, `hdr.*` слайдеры, `export {hdr:true}` |
| брекеты/панорамы | `merge.hdr`, `merge.hdrBatch`, `merge.panorama`, `merge.hdrPanorama` |
| профили | `profiles.list`, `develop.profile`, `profile.import` |
| история | `edit.undo/redo`, `history.list/restore`, `version.*` |
| пакетно | `command_batch`, `develop.quickAdjust`, `develop.copy/paste` |

`set_develop` c `id` делает фото активным и меняет выделение. `get_develop`/`render_preview`
выделение не меняют.

## Живой UI (только connect-режим)

Это и есть «ручная работа» на уровне интерфейса: не эмуляция движка, а реальные клики/жесты
в окне LightCraft.

| инструмент | применение |
|---|---|
| `screenshot {maxSize?, path?}` / `ui_screenshot` | посмотреть окно после правок; `path` — сохранить |
| `inspect_ui` / `ui_inspect` | вид, панели, rect окна и изображения, активное фото, активная маска, статус |
| `list_widgets {filter?}` | виджеты по automation id с прямоугольниками `[x,y,w,h]` в точках экрана |
| `click {widget?\|x,y, count?, button?}` | клик по id или точке; `count:2` — двойной, `button:"right"` — ПКМ |
| `press_key {key, ctrl?/cmd?/shift?/alt?}` | горячие клавиши (например `E` — панель правок, `M` — маски, `H` — Remove) |
| `type_text {text}`, `clipboard {action, text?}` | ввод в поле (сначала кликнуть в него) |
| `pointer_gesture {events:[{kind:"down"\|"move"\|"drag"\|"up", x,y}]}` | реальные жесты в **нормализованных координатах кадра 0..1**: кисти, градиенты, ручки кропа |
| `set_ui {state:{...}}` | состояние UI, например `{"view":"detail"}` (photoGrid\|squareGrid\|detail\|compare) |

Практика: сначала `inspect_ui` → `imageRect` (где кадр на экране) → `pointer_gesture` в
нормализованных координатах → `screenshot` для проверки. Команды (`mask.brushStroke`,
`crop.set`) и жесты — два равноправных способа одного и того же ручного действия; комбинировать.

## Как ставить значения

- Диапазоны: `references/controls.md`. Свет — ±100 (exposure ±5 EV, шаг 0.01); temp 2000–50000 K.
- **Баланс белого — ловушка**: через `values` `wb.temp` — это Kelvin на raw с цветовыми
  матрицами (DNG и большинство камер), но **относительная шкала** (6500 = как снято) на
  остальных файлах. Через `settings.wb` без `"scale":"kelvin"` — всегда относительная.
  Поэтому: raw → `values` в Kelvin; JPEG/HEIC → `settings.wb {temp, tint}` или пипетка.
- `crop.angle` через `values` поворачивает кадр как `crop.straighten` (кроп подрезается,
  если не влезает). Прямоугольник — только `crop {rect:[x0,y0,x1,y1]}` (0..1, от левого верха).
- `settings` делает **deep-merge**, но массивы заменяются целиком: `masks`, `spots`,
  `point_colors`, `red_eye`, `curve.master` задавать полностью, а лучше — командами
  (`mask.*`, `spot.*`), чтобы не потерять элементы.
- Каждый вызов = один undo-шаг. Проверять результат `get_develop`, а не верить на слово.

## Точность и самоконтроль

- Смотреть `render_preview` после каждого крупного блока; при правках света следить, чтобы
  гистограмма не упиралась: `highlights` вниз на −30…−70, если небо/кожа пересвечены.
- RAW терпит exposure ±1 EV; JPEG — ±0.3 EV, дальше артефакты.
- Тени +30…+50 без шума только на raw; на JPEG выше +25 появляется грязь.
- Резкость: `sharpenAmount` 30–50, `sharpenMasking` 30–60 для пейзажа, 60–80 для портрета.
- Не лечить шум резкостью: сначала `detail.nrLuminance`, потом `denoise.toggle` (raw).

## HDR — коротко

`develop.hdr {enabled:true, maxEv: 2.5–4}` включает HDR-редактирование: света выше SDR-белого
живут в рендере для HDR-экспорта, а SDR-рендишн (то, что видно в `render_preview`) управляется
слайдерами `hdr.sdr*`. Экспорт: `hdr:true` (+ `hdrTransfer:"pq"|"hlg"`). Детали, формулы
тона и проверка файлов — `references/hdr.md`.

## Пресеты и дополнения

41 встроенный (9 групп) + 3 point-curve + 8 export. Полные рецепты (какие поля и числа)
и правила — `references/presets.md`. Агент по умолчанию **воспроизводит пресет числами**,
а не применяет его. Что и как импортировать (LUT `.cube`, `.dcp`, локальные эффекты, XMP, SAM 3,
модели шумоподавления), а также обзор сторонних проектов — `references/addons.md`.
Инвентаризация установленного: `scripts/addon-inventory.py`.

## Ловушки

- `--connect` требует приложения с `--control 7980`. Обёртка поднимает его при старте MCP;
  если приложение закрыли **после** старта, вызвать `scripts/start-lightcraft-app.ps1` —
  сервер сам переподключится на следующем вызове. Не запускать второй headless-MCP на той же
  библиотеке: он захватит `catalog.lock` и вытеснит приложение.
- AI-маски (`object`, `prompt`) требуют SAM 3 (~3.4 ГБ, `segment.model.download {acknowledged:true}`,
  лицензия Meta). Сейчас не установлен — `sky`, `subject`, `background` работают без него,
  Object/Describe вернут ошибку с инструкцией.
- `mask.add` для `linear` игнорирует `start/end` — создать и задать форму через
  `mask.update {shape:{...}}` (проверено). Radial/luminanceRange/colorRange принимают параметры.
- `render_preview` показывает SDR-рендишн; HDR-яркость на экране не видна (приложение тоже
  не умеет HDR-дисплей) — судить по экспорту и по `hdr.*` значениям.
- Фото на старом процессе рендеринга (`process` в `get_develop`): `develop.updateProcess`
  **меняет вид** — не вызывать без просьбы.
- `export` не перезаписывает оригинал и его XMP — откажет; для тестов писать в temp.

## Обновление справочников

Версия проверена: 0.21.1 — это последний релиз (релиз 12.11.2026). После обновления LightCraft
перегенерировать автоматические справки:

```powershell
python "~/.config/opencode/skills/lightcraft\scripts\refresh-reference.py"
```

Скрипт обновляет `commands-edit.md`, `commands-rest.md`, `controls.md`, `presets.md`
(список команд, слайдеры, рецепты всех пресетов) и сверяет версию с GitHub-релизом.
Рукописные документы не трогает.

## Файлы

- `references/controls.md` — все слайдеры: id, min/max, шаг, дефолт.
- `references/develop-json.md` — полная схема `develop` JSON со смыслом полей.
- `references/masks-spots.md` — маски (все виды и формы), кисти, точки, red eye, lens blur.
- `references/hdr.md` — HDR-редактирование, merge, экспорт, проверка.
- `references/presets.md` — 41 пресет с числами, кривые, export-пресеты.
- `references/addons.md` — importable дополнения, модели и обзорсторонних проектов.
- `references/manual-editing.md` — рецепты по жанрам с конкретными числами.
- `references/export.md` — форматы, размеры, метаданные, watermark, contact sheet.
- `references/commands-edit.md` — команды редактирования с полными параметрами.
- `references/commands-rest.md` — каталог, метаданные, печать, слайдшоу, лица.
- `references/library.md` — карта не-редакторских возможностей (импорт, альбомы, отбор).
- `scripts/mcp-connect.py` — MCP-обёртка: поднять приложение, затем `mcp --connect`.
- `scripts/start-lightcraft-app.ps1` — вручную поднять приложение с `--control 7980`.
- `scripts/refresh-reference.py` — обновить справочники под новую версию LightCraft.
- `scripts/addon-inventory.py` — показать установленные пресеты/профили/модели.
