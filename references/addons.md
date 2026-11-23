# Дополнения LightCraft: пресеты, профили, эффекты, модели,сторонние утилиты

## Важно: собственного plugin API пока нет

В `docs/roadmap.md` «plug-in ecosystem» стоит **после beta**. То есть «дополнения» — это не
установщики плагинов, а **импортируемые данные** (пресеты, LUT, локальные эффекты) и внешние утилиты,
работающие через CLI / control-канал / MCP. Собственный MCP в programs уже настроен.

## Что умеет импортировать LightCraft 0.21.1 (официально)

| Тип дополнения | Форматы | Команда / место в UI |
|---|---|---|
| Develop-пресеты | `.lcpreset`, Camera Raw `.xmp`, `.lrtemplate`, DNG/JPEG/TIFF как «DNG preset», Luminar `.lmp` / `.mplumpack`, `.zip` | `preset.import {paths, group?, dryRun?}`; панель Presets → Import Presets…; можно перетащить файл в окно |
| Профили цвета | `.cube` (3D LUT → creative profile, Amount 0–200 %, рендер на CPU), `.dcp` (камерный профиль) | `profile.import {paths}`; `profiles.list`, `develop.profile {id, amount}` |
| Mask effects (локальные пресеты) | Lightroom `.lrtemplate` (local), Camera Raw local `.xmp`, `.lceffect`, `.zip` | `mask.importEffects {path\|paths, group?, dryRun?}`; `mask.saveEffect/applyEffect/deleteEffect` |
| Point curve пресеты | `.lccurve` | `curve.importPresets {path\|paths}`; `curve.presets`, `curve.applyPreset {name}` |
| Export-пресеты | внутри библиотеки | `export.savePreset {name, params}`, `export.presets`, `export.deletePreset` |
| Import Recipes (пакетный look при импорте) | внутри библиотеки | `preset.saveRecipe {name, recipe:[{id, value}]}` |
| AI-модели масок | SAM 3 (~3.4 ГБ, лицензия Meta) | `segment.model.status`, `segment.model.download {acknowledged:true}`, `segment.model.cancel`, `segment.prepare` |
| AI-модели шумоподавления | `.onnx` + `denoise-model.json`, darktable `.dtmodel` | `denoise.models.list/download/install/select`; без модели работает встроенный денойзер |
| Модели лиц | детектор YuNet, эмбеддеры (auraface, sface) | `faces.models.*` (Settings → Faces) |
| База линз lensfun | ~1568 профилей | `lens.databaseStatus`, `lens.downloadDatabase` (уже загружена) |
| Lightroom-каталог | `.lcat` / каталог | `library.inspectLightroom`, `library.importLightroom` |

Безопасный порядок установки: `dryRun:true` → импорт → посмотреть `profiles.list` /
`presets.list` / `mask.effects` → **virtual copy** → применить по одному → `render_preview` →
`edit.undo` или удалить копию. Пресеты и LUT — **недоверенные данные**: сначала читать, что
именно меняют (`preset.export {ids:[...]}` покажет числа), и лишь потом применять.

## Что уже установлено у вас (проверено 24.11.2026)

| Раздел | Состояние |
|---|---|
| Develop-пресеты | **41** встроенный, 0 пользовательских, 0 избранных — рецепты всех есть в `presets.md` |
| Профили | **22** встроенных в 5 группах (Basic, Film, Cinematic, Muted, B&W), 0 импортированных |
| Point curve | 3 (Linear / Medium Contrast / Strong Contrast) |
| Export-пресеты | 8 встроенных |
| Mask effects | **0** |
| SAM 3 | **не установлен** → Object/Describe-маски вернут ошибку; Sky/Subject/Background работают |
| Denoise | 0 внешних моделей, встроенный runtime доступен |
| Лица | установлены `yunet-2023mar` (детектор), `sface-2021dec`, `auraface-v1` (эмбеддер) |
| lensfun | загружена, 1568 линз |

Инвентаризацию можно повторить:

```powershell
python "~/.config/opencode/skills/lightcraft\scripts\addon-inventory.py"
```

## Сообщество: что стоит знать

Все проекты ниже **не официальные**. Звёзды и даты — на 24.11.2026.

### Полезное и проверяемое

| Проект | Что даёт | Оценка |
|---|---|---|
| `dabofr/lightcraft-scripts` (2★, MIT) | GUI-набор Python-скриптов для уборки библиотеки на Windows: инвентарь RAW+JPG, сидкары, стеки, ключевые слова/места, релинк. Тестирован на 0.21.1 | Полезно для большой библиотеки; «as is», без поддержки |
| `do-hobby-account/lightcraft-fuji-profiles` (1★) | 15 готовых `.cube`-профилей плёночных симуляций Fuji (Velvia, ASTIA, ACROS, SEPIA…) для X-Trans III | Только для Fuji X-T2/X-Pro2/X-T20/X-E3/X-H1/X100F и съёмки в PROVIA. Вам с Xiaomi — не нужно |
| `AndrianLeah/ai-remove-lightcraft` (47★, MIT) | Локальное AI-удаление объектов/людей через SAM 3, панель рядом с LightCraft (`Ctrl+Shift+X`), результат пишется обратно в RAW DNG | Работает, но **нарушает ваш принцип «руками»** — включать только по явной просьбе |
| `Najah69/lightcraft-nik` (0★, MIT) | Мост «Edit in» к Nik Collection (Silver Efex и др.), правки возвращаются стеком | Экспериментально, нужен лицензированный Nik; внешний редактор, не ручной слайдер |
| `tinytom21/lightcraft-cloud` (3★, Apache-2.0) | Синхронизация библиотеки между ПК/телефоном через собственный rclone-remote | Инфраструктура, не редактирование |
| `tzachy-fridman/LightCraftMidi` (0★) | Windows tray: MIDI-фейдеры → слайдеры LightCraft, кнопки → команды через `--control 7980` | У вас control-порт уже поднят — подключилось бы без переделок |
| `giulio426/stream-deck-lightcraft-plugin`, `LuizGustavoWT/getcraft-lightcraft-opendeck` | Панели Stream Deck / OpenDeck для отбора и правок | Аппаратные дополнения |
| `midasmatterhorn/artcraft-skills` (102★, MIT) | 19 готовых `SKILL.md` для всего набора ArtCraft, включая LightCraft | Альтернатива нашему скиллу; наш заточен под ручную правку и ваш connect-стенд |
| `jhonsu01/lightcraft-mcp-server` (1★, TS) | Альтернативный MCP «file-in/file-out» поверх CLI | Нативному MCP из коробки предпочтителен — дублировать не нужно |
| `dkwage/lut-lab` (0★, MIT) | Локальная лаборатория `.cube`: применение, сравнение, экспорт cubе/XMP | Пишет XMP для LightCraft, движок RAW — `lightcraft-cli`, собираемый из исходников |

### Пресеты, которые пока НЕ работают в 0.21.1

- `darthnut/lightcraft-ir-presets` (15 ИК-пресетов) и `darthnut/lightcraft-ir-recipes` —
  построены на **RGB Channel Mixer из PR #3579**, который ещё не merged. В 0.21.1 импортируются,
  но применятся только WB/тон → выраженный синий оттенок. Не ставить.
- `smyrgeorge/film-lab` (14★) — плёночные пресеты пока работают только в **PhotoCraft** через
  WebAssembly-плагин; поддержка LightCraft ждёт plugin API.

### Мусор / осторожно

- Репозитории с «Nik Collection repack / patched / unlimited» (например
  `Momentumolspark7/Nik-Collection-Dxo-Latest-Version`) — пиратские сборки, не ставить.
- Много свежих 0★-репо без релизов и с описанием «plugin» — это обёртки/клоны, не интеграции.
  Проверяйте лицензию, релизы, подписи и исходники до установки.
- Любой внешний скрипт читает/пишет вашу библиотеку. Запускать только после просмотра кода
  и на копии каталога.

## Рекомендация для вашего сценария

Ничего из стороннего ставить не обязательно: встроенных 41 пресета, 22 профилей и 8 export-пресетов
хватает, а рецепты всех пресетов уже разобраны в `presets.md` для ручного воспроизведения.
Если понадобится — безопасный первый шаг: импортировать **Mask effects** из ваших старых
Lightroom-пресетов (`mask.importEffects {path, dryRun:true}`) и/или сконвертировать XMP-пресеты
(нативно через `preset.import {paths:[...], dryRun:true}` — отдельный конвертер не нужен).
