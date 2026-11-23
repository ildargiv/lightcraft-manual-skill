# Не-редакторские возможности (карта)

Подробные параметры каждой команды — `references/commands-rest.md` и `command_list`.
Редактирование описано в `SKILL.md` и `references/commands-edit.md`.

## Импорт и вид библиотеки

- helper `import {paths, mode:"add|copy|move", destination, organize, rename, album}` —
  папки сканируются рекурсивно; `organize`: `date|month|flat|шаблон`.
- `library.import` (команда), `library.browse` (просмотр папки без импорта),
  `library.devices` (камеры/карты), `library.importLightroom` / `library.inspectLightroom`.
- `query_photos {filter, sort, limit, offset}` — фильтр: `minRating`, `flag`, `edited`,
  `keyword`, `camera`, `date`, `text`, `merged` и др.; `library.filter` задаёт вид,
  `library.clearFilter`, `library.toggleFilters`, `library.sort`.
- `library.source {kind:"all|recentlyAdded|album|recentlyDeleted|picks|missing|libraryFolder", id|path}`,
  `library.folders`, `library.state`, `library.info`.
- `select_photos {ids, active?, mode}`; `library.selectAll/selectNone/selectBy/next/previous/up/down`.

## Отбор и метаданные

- `photo.rate {rating:0..5}`, `photo.flag|pick|reject|unflag`, `photo.cycleFlag`,
  `photo.label {label:"red|yellow|green|blue|purple|none"}`.
- `photo.setMeta {title, caption, copyright, creator, location, gps, keywords, addKeywords,
  removeKeywords}`, `photo.allMetadata`, `photo.copyMetadata`, `photo.pasteMetadata`.
- `photo.saveMetadataToFile`, `photo.readMetadataFromFile` — XMP-сидкары;
  `library.toggleAutoWriteXmp`, `library.xmpPreferences`.
- `keyword.create/rename/edit/merge/delete`, `keyword.list`, `keyword.sets`,
  `keyword.toggleFromSet` — дерево ключевых слов.
- `faces.detect/index/suggest/nameFaces/setName/renamePerson/person/unnamed` — распознавание
  лиц; модели — `faces.models.*` (YuNet — `yunet-2023mar`, версия `yunet-2023mar`).
- `photo.analyze` — авто-отбор резкости/повторов (`rejectBelow`, `pickBest`) — автоматика,
  по умолчанию не применяем.

## Организация

- `album.create/createSmart/setRules/rename/delete/addPhotos/removePhotos/setCover`;
  `album.setTarget/toggleTarget`, `album.clearQuick` (Quick Collection).
- `stack.group/ungroup/split/setTop/moveUp/moveDown/expandAll` — стеки; `stack.auto` —
  автоматическая группировка (не использовать без просьбы).
- `photo.virtualCopy` (неразрушающая копия настроек), `photo.duplicate` (реальная копия файла),
  `photo.convertToDng`, `photo.moveToFolder`, `photo.rename`, `photo.relink`.
- `photo.delete` (Recently Deleted), `photo.restore`, `photo.deletePermanently`,
  `library.emptyRecentlyDeleted`.
- `photo.editExternal` — рендер TIFF/PSD рядом с оригиналом для внешнего редактора.

## История и версии

- `history.list {id?}` → `{history:[labels], cursor, versions}`; `history.previous/next`,
  `history.restore {index}`, `history.clear`.
- `version.create {name?}`, `version.update {index}`, `version.restore {index}`,
  `version.rename`, `version.delete`.
- `edit.undo` / `edit.redo`; `beforeAfter.setBefore` / `swap` / `resetBefore`.
- `develop.copy {groups?}` / `develop.paste {ids?, groups?}` / `develop.pastePrevious` —
  ручная передача настроек (в отличие от `develop.sync`/`autoSync`).

## Печать и шоу

- `print.get/set/reset`, `print.cell.add/move/resize/delete/photo/page`,
  `print.layout.newPage/clear`, `print.template.list/save/apply/delete/import/export`,
  `print.exportPdf {path}`.
- `slideshow.playback/layout/overlays/titles`, `slideshow.templates.*`,
  `slideshow.preview` (PNG/картинка), `slideshow.export {format:"pdf|jpeg|video", path, ...}`
  + `slideshow.exportStatus`, `cmd_activity_list`, `cmd_activity_cancel`.
- `export.contactSheet` — PDF-контактный лист (быстрее, чем print).

## Обслуживание

- `library.buildPreviews/previewProgress/cancelPreviews`, `library.smartPreviews`,
  `library.clearPreviews`, `library.compact`, `library.memory`, `library.info`.
- `library.findMissing`, `library.refreshLensProfiles`, `library.recheckPreviewOnly`
  (после обновления декодера raw), `library.retrySidecars`.
- `prefs.*` — настройки; `app.gpu`, `app.memoryBudget`, `app.hotPixelLimit` — движок.
- `activity.list/cancel` — фоновые задачи; `denoise.pump` / `faces.pump` / `focus.pump`
  вызывает сам движок UI, агенту обычно не нужно.
