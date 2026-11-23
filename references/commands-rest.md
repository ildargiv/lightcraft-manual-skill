# Остальные команды LightCraft — каталог, метаданные, печать, слайдшоу

Сгенерировано из `lightcraft-cli commands --json` (0.21.1).
Полные описания параметров — `command_list`.

## activity

- **activity.cancel** — Cancel Background Task
  {id} | {all: true} → {cancelled: n} — ask a task (or every cancellable task) to stop; it stops at its next file or photo (a preview build also stops between a photo's own previews). An unknown id (it may have just finished) or a task that can't be cancelled is an error
- **activity.list** — Background Tasks
  {} → {tasks: [{id, kind, label, done, total, unit: count|bytes|percent, detail, cancellable, cancelling, ageMs}]} — the long-running tasks in flight (imports, exports, preview builds, downloads, the face scan…), oldest first; total 0 = not known yet

## album

- **album.addPhotos** — Add to Album
  {id: albumId, ids?: [photoIds]} (default: selection) → {added, skipped}; Local photos are skipped (albums hold library photos), only Local ones is an error; ids the library doesn't have are dropped; nothing new to add changes nothing (no undo step)
- **album.clearQuick** — Clear Quick Collection
  {}
- **album.create** — New Album
  {name, parent?: folderId, folder?: bool, addSelected?: bool} → {id, skipped} (skipped: Local photos of the selection, which albums can't hold)
- **album.createSmart** — New Smart Album…
  {name, rules?: partial Filter (rating, ratingOp, flag, flags, label, labels, kind, edited, keyword, camera, lens, dateFrom, dateTo, date, text, album, ruleSet: {match: all|any|none, rules: [{field, op, value} | {group: ruleSet}]} — see album.ruleFields), parent?: folderId} — without `rules`, saves the current view (source + filter)
- **album.delete** — Delete Album
  {id} — deletes the album or folder and its descendants, keeping photos in the library; one undo step
- **album.move** — Move Album
  {id, parent?: folderId|null}
- **album.removePhotos** — Remove from Album
  {id?: albumId (default: the album on screen), ids?} — takes the photos out of the album only: they stay in the library and in their folders (issue #1805; photo.delete removes them from the library) → {removed, album: name}
- **album.rename** — Rename Album
  {id, name}
- **album.reorder** — Reorder Album
  {id, parent?: folderId|null, before?: albumId|null} — places the album (or folder) in `parent` (default: where it is; null: the top level) before the sibling `before` of the same kind, or last of its kind; the folder is then ordered by hand. One undo step. → {changed}: how many edits it took (0: already there)
- **album.ruleFields** — Smart Album Rule Fields
  {} → [{field, label, kind (text|keywords|number|date|choice|bool|album: an album id), group (field-menu submenu, null at the top level), ops: [{op, label}], choices? (ids), choiceLabels? ({id: label})}] for ruleSet rules, in menu order
- **album.setCover** — Set as Album Cover
  {id: albumId, photo?: photoId}
- **album.setRules** — Edit Smart Album
  {id, rules?: partial Filter merged onto the current rules (null clears a field), replace?: bool, fromView?: bool (use the current view), name?: also rename it (blank keeps the name) — one undo step, both or neither}
- **album.setTarget** — Set as Target Album
  {id: albumId | null} (null = the Quick Collection)
- **album.sort** — Sort Albums by Name
  {parent?: folderId|null} — drops the hand order of the albums inside the folder (default: the top level), so they are listed by name → {changed}: how many albums lost their place
- **album.toggleTarget** — Add to Target Album
  {ids?} — B: adds the photos to the target album (the Quick Collection unless one is set), or removes them when they're all in it → {album, added, toggled, skipped}; Local photos are skipped, ids the library doesn't have are dropped (none left: nothing changes and `added` is null)

## albums

- **albums.list** — List Albums
  {}

## app

- **app.export** — Export Now
  {path?: output file (.jpg/.png/.tif/.webp/.avif/.jxl/.psd/.dng) | dir?, ids?, preset?, format?: jpeg|png|tiff|webp|avif|jxl|psd|dng|original, longEdge?|shortEdge?|width?|height?|megapixels?|percent? (default longEdge 3000; longEdge 0 = full size), fit?: dimensions|widthHeight (with width + height: dimensions fits either orientation, widthHeight limits the width to `width` and the height to `height`), dontEnlarge?, ppi?, quality?: 1..100, jxlLossless?, jxlEffort?: fast|normal, jxlProgressive?, limitKb?, colorSpace?: srgb|displayP3|adobeRgb|proPhoto|rec2020, bitDepth?: 8|10|16|32, hdr? (HDR output for HDR edits: gain map JPEG, PQ AVIF / PNG / JPEG XL, float TIFF), sharpen?: none|screen|matte|glossy, sharpenAmount?: low|standard|high, metadata?: all|allExceptCamera|copyright|none, removeLocation?, naming?, startNumber?, destinationMode?: specificFolder|sameAsOriginal (sameAsOriginal = each photo into its original's folder; `dir` unused), subfolder?, conflict?: unique|overwrite|skip, tiffCompression?: none|lzw|zip (default zip; lzw is usually larger and slower than zip, at 16 bit often larger than none: only for software that needs LZW), dngCompression?: lossless|deflate|uncompressed, addToPhotos?: bool (macOS: then add the files written to Apple Photos; outcome in `applePhotos`), photosAlbum?: top-level album name (made when missing), watermark?: text | {text?, vertical? (upright columns, right to left), size? (text height, 0.005..0.5 of the short edge; default 0.035), opacity? (0..1; 0.7), anchor?: topLeft|top|topRight|left|center|right|bottomLeft|bottom|bottomRight, insetX? (margin from the left/right edge, 0..0.4 of the short edge; 0.025), insetY? (from the top/bottom edge; 0.025), inset? (sets both), rotation?: 0|90|180|270 (degrees clockwise; 0), color? [r,g,b] sRGB, shadow?, image? (graphic drawn instead of the text), imageWidth? (0.01..1 of the photo's width; 0.2)}} — an unknown parameter, an out-of-range watermark size or a value of the wrong kind is an error, not a default
- **app.gpu** — GPU Rendering
  {enabled?: bool, wait?: bool} — allow/forbid GPU rendering (CPU fallback; LIGHTCRAFT_GPU=0 forbids it for the process); returns {enabled, available, adapter, reason (why the GPU is off), lastFallback (latest render redone on the CPU, and why)}. wait: false never waits for a device still being created (available, adapter and reason are then null and the device is created in the background; with GPU rendering off they say so at once)
- **app.hotPixelLimit** — Hot Pixel Limit
  {percent?: number} — Remove Hot Pixels leaves a raw alone when more than this share of its photosites would be replaced (0.001..100 %, default 0.2 %; real light it keeps doesn't count); returns {percent, default}
- **app.memoryBudget** — Memory Budget
  {mb?: number} — set the memory budget shared by the caches (default: a quarter of RAM, at most 1536 MB); returns the report

## beforeAfter

- **beforeAfter.copyAfterToBefore** — Copy After's Settings to Before
  {}
- **beforeAfter.copyBeforeToAfter** — Copy Before's Settings to After
  {}
- **beforeAfter.resetBefore** — Reset Before to Import State
  {}
- **beforeAfter.setBefore** — Set Before
  {source: import|current|history|version, index? (history step), name? (version)} — what the before side shows (this session)
- **beforeAfter.swap** — Swap Before and After Settings
  {}

## catalog

- **catalog.query** — Query Photos
  {filter?: Filter, sort?: Sort, offset?, limit?} — omit filter to list the current view
- **catalog.stats** — Catalog Statistics
  {}

## faces

- **faces.detect** — Detect Faces
  {ids?, apply?: bool (default true), score?: 0.6, nmsIou?: 0.3, maxFaces?} → {photos: [{id, faces: [{rect, score, landmarks}]}]}. Finds faces with the YuNet detector (download it first: `faces.models.download {id: "yunet-2023mar"}`) and, unless `apply` is false, adds them as unnamed face regions (one undo step), replacing earlier detections but never regions from XMP or ones you named; the sidecar is not touched
- **faces.enable** — Face Recognition On/Off
  {enabled?: bool} (toggles when omitted)
- **faces.evaluate** — Evaluate Face Recognition
  {budgetMs?: 0, burstSecs?: 5, margin?, thresholds?: [..], scope?: "visible"} → {queries, top1, sweep: [{threshold, suggested, correct, precision, recall}]} — leave-one-out over your named faces: each is ranked against the others (ignoring shots within burstSecs of it) to show how well the chosen model recognises people in *your* photos and which threshold to trust. Faces not yet embedded are done within budgetMs (`faces.index` does them all); counts only
- **faces.gpu** — Face Models on the GPU
  {cpuOnly?: bool} → {cpuOnly, detection, recognition}: where the face models run, each as {checking, device, why} (null until it is loaded). The GPU is used only after a background check shows it gives the CPU's results faster; `cpuOnly: true` keeps every face model on the CPU (Settings ▸ Faces), `false` checks the GPU again
- **faces.index** — Index Faces
  {budgetMs?: 200, ids?: [photo ids to do first]} → {embedded, photosDone, pendingPhotos, indexedFaces, ms} — embed the faces in the library with the chosen recognition model, as many photos as fit in the time (at least one); call again until `pendingPhotos` is 0. `budgetMs: 0` only reports
- **faces.models.download** — Download Face Model
  {id, acknowledged: true} → {started, from} — fetch a recognition model LightCraft has a pinned address for (see `downloadHost` in the list), in the background over pure-Rust https (lightcraft-fetch). `acknowledged` must be true: the user has been shown the model's terms and accepted them. It is checked against its size and SHA-256, then installed, chosen and switched on by itself; `faces.models.downloads` shows how far it is
- **faces.models.downloadCancel** — Cancel Face Model Download
  {id} → {discarded} — stop a download, or delete a finished one that was not installed
- **faces.models.downloads** — Face Model Downloads
  {} → {running, downloads: [{id, state: running | done | installed | failed | cancelled, bytes, total, error, from}]} — also installs any download that has arrived; `installed` stays listed until `faces.models.downloadCancel` clears it
- **faces.models.inspect** — Inspect Face Model File
  {path} → what a .onnx file is: {kind: known | draft | unsupported, model, assumptions, reason, alreadyInstalled}; installs nothing
- **faces.models.install** — Install Face Model
  {path, acknowledged: true, activate?: true} → {installed, active: {embedder, enabled}} — copy a .onnx face recognition model into the models folder. `acknowledged` must be true: the user has been shown its licence (see inspect) and accepted it. Unless `activate` is false the model becomes the one in use and recognition is switched on; an earlier model stays installed
- **faces.models.list** — Face Models
  {} → {dir, enabled, embedder, runtime, models: [{id, name, role, licence{name, commercial, url, notice}, provenance, source, sizeBytes, known, installed, selected}]}
- **faces.models.remove** — Remove Face Model
  {id} — delete an installed model
- **faces.models.select** — Choose Face Recognition Model
  {id: installed recogniser | null}
- **faces.models.test** — Test Face Model
  {id} → {ok, result: {loadMs, embedMs, dimension, checks}} — load an installed recognition model and check it gives sensible faces; needs the recognition runtime
- **faces.nameFaces** — Name Faces
  {faces: [{photo, index}], name} → {named, photos} — name (or, with a null or empty name, clear) many face regions as one undoable step; the sidecar is not touched
- **faces.person** — Faces of a Person
  {name, more?: 120} → {name, total, confirmed: [{photo, index, rect}], more: [{photo, index, rect, score}], ready, pendingPhotos} — the faces named `name` across the library, and the unnamed faces that look most like them (best first, already embedded ones only, once recognition is on); confirm one with `faces.setName`
- **faces.pump** — Index Faces in the Background
  {pace?: pause | light | normal | full} → {active, inFlight, pendingPhotos, indexedFaces, searchedPhotos, workers} — cheap to call every frame: takes in what the background workers have finished and gives them the next photos, as many at once as the pace allows (none when paused, one when light, half the machine's threads when normal, four fifths when full); inactive until face recognition is on in Settings with a model chosen
- **faces.renamePerson** — Rename Person
  {from, to, merge?: bool} → {faces, photos, from, to, merged} — give every in-library face of `from` the name `to` (trimmed, any capitalization), one undo step; refused when `to` is already someone else unless `merge` is true, which combines the two; the sidecar is not touched
- **faces.setName** — Name Face
  {id?, index, name} — name a face region (null or empty clears it); undoable; the sidecar is not touched
- **faces.suggest** — Suggest Names for Faces
  {ids?, threshold?, margin?, budgetMs?} → {photos: [{id, faces: [{index, suggestion: {name, score, runnerUp} | null, candidates: [{name, score}]}]}]} — who the unnamed faces in these photos might be, from the faces already named in the library. Only suggestions: nothing is named
- **faces.unnamed** — Unnamed Faces
  {limit?: 600} → {total, faces: [{photo, index, rect, view, suggestion: {name, score} | null}], ordered, ready} — the faces nobody has named; with recognition running, look-alikes are next to each other and a face the named ones recognise carries the name they suggest. `view` is the box to show the face by. Name them with `faces.nameFaces`

## filter

- **filter.applyPreset** — Apply Filter Preset
  {name} — replaces the current filter → {photos}
- **filter.deletePreset** — Delete Filter Preset
  {name}
- **filter.presets** — Filter Presets
  {} → [{name, filter}]
- **filter.savePreset** — Save Filter Preset
  {name} — the current filter (library.filter), saved with the library

## folder

- **folder.create** — New Folder on Disk
  {parent, name} — create a folder on disk inside `parent` (refused if the name is taken); one undo step (undo removes it again while it is empty) → {path}
- **folder.label** — Set Folder Color Label
  {path, label: red|yellow|green|blue|purple|none} — give a folder of the library (one its photos were imported from, see library.folders) a colour label, or take it off (also once its photos are gone); one undo step. The label follows the folder when it is renamed or moved with folder.rename / folder.move → {path, label}
- **folder.move** — Move Folder
  {path, into: destination folder} — move a folder on disk into another and relink the photos in it; one undo step (undo moves it back, refused if the old place is taken); refused for the home folder and its Pictures, Desktop and Downloads → {path, relinked}
- **folder.rename** — Rename Folder
  {path, name} — rename a folder on disk (its files and sidecars go along) and relink the photos in it; one undo step (undo renames it back, refused if the old name is taken); refused for the home folder and its Pictures, Desktop and Downloads → {path, relinked}
- **folder.scanChanges** — Scan Folder for Changes
  {path, disk?: bool (a whole disk or share, or a folder holding disks)} — compare a folder of the library (and the folders inside it) with the disk; changes nothing → {path, new: [{path, name, format, …}] files the library doesn't have, duplicates: files whose content it already has, unreadable: [{path, error}], missing: [{id, path}] photos whose file is gone, moved: [{id, from, to}] photos whose file is elsewhere in the folder (same content), metadata: [{id, path}] photos whose XMP sidecar was saved after they came in or were last edited here and says something the library doesn't}
- **folder.synchronize** — Synchronize Folder
  {path, disk?: bool, scanned?: bool, importNew?: true, relinkMoved?: true, removeMissing?: false, readMetadata?: false} — bring a folder of the library up to date with the disk (see folder.scanChanges): import its new files in place, relink photos whose file was renamed or moved within it, move photos whose file is gone to Recently Deleted, read XMP sidecars saved by other apps (the sidecar wins); acts on the last folder.scanChanges of the folder while it is current (the folder's photos unchanged), else scans again — or, with `scanned: true`, refuses; one undo step, no file is touched → {imported, relinked, removed, read, failed: [[path, error]]}

## journal

- **journal.list** — Command Journal
  {limit?}

## keyword

- **keyword.create** — Create Keyword
  {name, parent?: keyword | null (default: the default parent; null = the top level), synonyms?, includeOnExport?, exportContaining?, exportSynonyms?, person?, addToSelected?: bool, ids?} → {keyword}
- **keyword.delete** — Delete Keyword
  {keyword} — removes it (and the keywords below it) from every photo
- **keyword.deleteSet** — Delete Keyword Set
  {name}
- **keyword.edit** — Edit Keyword
  {keyword, name?: its new name (one level), synonyms?, includeOnExport?, exportContaining?, exportSynonyms?, person?} — what isn't given keeps its value
- **keyword.export** — Export Keywords
  {path?} — the keyword list as a file (Lightroom Classic's format, which Capture One, Photo Supreme and Bridge read) → {keywords, captureOneRefuses: keywords with ; , < > that Capture One's importer refuses, unwritable: keywords left out because the format can't hold them (a name in brackets or braces, a line break, deeper than 64 levels; a synonym as "path {synonym}"), text when there is no path}
- **keyword.import** — Import Keywords
  {path | text} — a keyword list (Lightroom Classic's format, also Capture One's and Photo Supreme's Formatted Vocabulary File): adds the keywords the library doesn't have, gives those it has the list's synonyms; one undo step → {added, updated}
- **keyword.info** — Keyword Info
  {keyword} → {path, listed, count, synonyms, includeOnExport, exportContaining, exportSynonyms, person}
- **keyword.list** — Keywords
  {} → [{name, path, count, children}] keyword tree (`a|b|c` keywords are hierarchical)
- **keyword.merge** — Merge Keywords
  {from: [keyword], into: keyword} — replaces each `from` keyword (children included) with `into` on every photo
- **keyword.move** — Move Keyword
  {keyword, parent: keyword | null (the top level), merge?: bool} — with the keywords below it; onto a name that is taken only with `merge: true`
- **keyword.nextSet** — Next Keyword Set
  {}: the set after the current one (after the last, Recent Keywords)
- **keyword.previousSet** — Previous Keyword Set
  {}: the set before the current one (before Recent Keywords, the last)
- **keyword.purgeUnused** — Purge Unused Keywords
  {} — takes off the keyword list the keywords no photo has → {purged}
- **keyword.rename** — Rename Keyword
  {from, to} — on every photo, children included (`a` → `b` renames `a|x` to `b|x`); renaming onto an existing keyword merges them
- **keyword.saveSet** — Save Keyword Set
  {name, keywords?: [up to 9, "" = an empty slot] (default: the renamed set's, else the current nine), replace?: the set it renames, new?: refuse a name another set has} — replaces a set of that name (or `replace`, in its place) and makes it current
- **keyword.setDefaultParent** — Put New Keywords Inside
  {keyword: keyword | null} — the parent keyword.create puts new keywords inside (null: the top level)
- **keyword.setShortcut** — Set Keyword Shortcut
  {keywords: [..] or "a, b" (none clears it)}: sets the keyword shortcut, a mark on its keywords in the keyword list (a new name is listed; one undo step) → {keywords}
- **keyword.sets** — Keyword Sets
  {} → {sets: [{name, keywords}], current, keywords: the nine ⌥1–⌥9 apply}
- **keyword.shortcut** — Keyword Shortcut
  {} → {keywords: the keyword shortcut's, which ⇧K adds or removes}
- **keyword.suggest** — Keyword Suggestions
  {prefix?: typed text, ids?, limit?: 12} → keywords to suggest for the photos (co-occurring / most used, or matching the prefix)
- **keyword.toggleFromSet** — Toggle Keyword from Set
  {index: 1..9, ids?} — the set's keyword N: added to the target photos, or removed when they all have it
- **keyword.toggleShortcut** — Add or Remove Keyword Shortcut
  {ids?}: removes the keyword shortcut's keywords from the target photos when they all have every one, else adds them → {changed, keywords, added}
- **keyword.useSet** — Use Keyword Set
  {name} ("Recent Keywords" = the recently added ones)

## label

- **label.applySet** — Apply Color Label Set
  {name} — use a set's label names (undoable)
- **label.deleteSet** — Delete Color Label Set
  {name} — user sets only
- **label.names** — Color Label Names
  {} → [{label, name, custom}]
- **label.saveSet** — Save Color Label Set
  {name} — save the current label names as a set (replaces a user set of that name)
- **label.setNames** — Edit Color Label Names
  {names: {red?: name|null, yellow?, green?, blue?, purple?}} — null or empty restores the colour's name
- **label.sets** — Color Label Sets
  {} → {sets: [{name, names: [red, yellow, green, blue, purple], builtin}], current: name|null}

## library

- **library.autoImport** — Auto Import Settings
  {folder?: path | null (off), copy?: bool (copy into the library's Originals, else add in place), album?: name | null} — a watched folder whose new photos are added as they arrive (library.autoImportScan; the app scans every few seconds) → the settings
- **library.autoImportScan** — Auto Import Now
  {listing?: [[path, size]] (the folder as listed by the caller, e.g. on a worker thread), start?: bool (false: return the `library.import` params as `import` instead of importing)} — add the watched folder's new photos (files the library doesn't have yet; partial / still-copying files wait for the next scan) → {imported, folder, warnings?: [{path, code, profile?, mode?, fields?}], import?}
- **library.browse** — Browse Folder
  {path, subfolders?: bool} — show a folder's photos without adding them to the library (they're read in place; edits go to XMP sidecars) → {path, photos, new}
- **library.buildPreviews** — Build Previews
  {size?: standard (2048 px, or the loupe's size when bigger, or `edge`) | full (1:1), ids?, wait?: bool, force?: bool, from?: id, backward?: bool, background?: bool, row?: bool} — render the grid thumbnail and loupe view of the selected photos (when more than one is selected; else all in view) into the preview cache (memory and disk), in the background unless `wait`. Photos whose previews are there already (big enough) are skipped unless `force`; the photos nearest `from` go first. `background`: the background preparation's build (two lanes, waits while the photo on screen renders; a build asked for replaces it). `row: false`: no row of its own in the activity stack (the caller's row shows it) → {total, done, failed, skipped, shared, running}
- **library.cancelPreviews** — Cancel Preview Build
  {}
- **library.clearFilter** — Clear Filters
  {}
- **library.clearPreviews** — Discard Preview Cache
  {}
- **library.compact** — Optimize Library
  {}
- **library.devices** — Cameras and Cards
  {} → [{name, path (its DCIM folder), root}] — mounted volumes with a DCIM folder
- **library.down** — Photo Below
  {rows?: n (photos to move forward; default 1, the grid passes the distance to the cell below)}
- **library.emptyRecentlyDeleted** — Empty Recently Deleted
  {} → {deleted} — removes every photo in Recently Deleted from the library (files on disk stay)
- **library.filter** — Filter
  partial Filter: {text?, rating?, ratingOp?: atLeast|exactly|atMost, flag?: pick|reject|none|null, flags?: [pick|reject|none] (any of them; [] = no constraint), label?, kind?, merged?: hdr|panorama|hdrPanorama|any, edited?, date?, libraryFolder?: a path from library.folders, keyword?, person?, camera?}
- **library.findMissing** — Find Missing Photos
  {folder} — relink every missing photo whose file is somewhere in the folder: same name and size (and content, when the library knows its hash), or — renamed — same size and content; or {found, missing, ambiguous} — relink what a search already found (the app searches on a worker thread; photos relinked meanwhile and files now in use are skipped) → {found: [{id, from, to, by: name|content}], missing, ambiguous: [{id, from, candidates}] (several same-name candidates and no hash to tell them apart: skipped)}
- **library.findSimilar** — Find Similar Photos
  {id?, similarity?: 0..1 (0.8), filter?: bool (true)} — photos that look like the active one (composition and tones), most similar first; filters the view to them (Clear Filters to go back) → {photos: [{id, similarity}]}. In the app the photos are read on a worker thread under an activity row: a control request is answered with this when the search ends, and from a menu the answer is {background: true, count}
- **library.folders** — Library Folders
  {} → [{name, path, count, own, volume, selectable, label?, children}] the disks and the folders the library's photos were imported from, with photo counts (subfolders included in `count`); show one with library.source {kind: libraryFolder, path} (rows with selectable false only open)
- **library.forgetLocal** — Forget Unchanged Local Photos
  {dryRun?: bool, days?: n (default: the library preference, 0 = never)} — remove Local (browsed, not added) photos nobody changed, of folders not browsed for `days`, from the catalog; files and sidecars stay, browsing the folder again brings them back; not an undo step → {local, forgotten, keptRecent, keptTouched, keptInUse, foldersStamped, days, dryRun}
- **library.groups** — Date Groups
  {by?: day|month|year (default: the sort's grouping; auto = day)} → [{key, label, start, count}] date headers of the grid
- **library.holdView** — Hold View Until Refreshed
  {on?: bool (toggles when omitted)} → {hold} — when on, an edit that makes a photo stop matching the view (a keyword given in a smart album of photos without keywords, a flag taken off in Picks, a rating under the filter bar's) keeps it in the view until `library.refresh`, Reshuffle, or another source, filter or sort; photos that start matching still appear at once, and deleting a photo or taking it out of the album or folder shown still takes it out of the view. Changing a smart album's rules is another view too. Off (the default): the view follows every edit. Kept with the library's preferences; asking for the state it already has changes nothing
- **library.import** — Import Photos
  {paths: [file or folder (recursive)], mode?: add|copy|move (add = reference the files in place; copy = into the library's Originals/YYYY/YYYY-MM-DD/; move = as copy, then each original and its XMP sidecars are removed from the source — only after the copy is verified (a hard link on the same volume, else copied, synced and compared byte for byte) and its catalog record is saved; failed, duplicate and unchecked files keep their sources; a taken name gets -1, -2…; undo removes the photos from the library but leaves the files at the destination), destination?: folder for copies / moves, organize?: date (YYYY/YYYY-MM-DD) | month (YYYY/YYYY-MM) | flat | a folder template, e.g. `{date:%Y}/{date:%Y%m%d}` → 2026/20260114 (the template's `/` make the folders, each level expanded with the rename tokens and made a safe folder name: never outside the destination; must be relative, no `..`; a level with missing metadata is `unknown`) — dated by capture time, else the import time, rename?: file-name template for copies, original extension added (tokens: {name} {num} {seq} {seq:N} {date} {date:%Y%m%d} {folder} {camera} {lens} {iso} {rating} {title} {creator} {ext}; photo.renameTokens explains each; blank = keep names), renameStart?: 1 (must fit this platform; later files are reported failed if the sequence runs out), metadataPreset?: name, dng?: bool (copy raws as DNG; copy only), local?: bool (browsing: the photos stay out of the library, like library.browse; not with move), album?: albumId, albumName?: new album, preset?: presetId, recipe?: [{id: a plain develop control (develop.controls; no white balance, geometry or crop), value}] (a batch-edit recipe: each control is set to its value, clamped to the control's range, on every photo this import adds, after its sidecar, camera default and preset, as one extra History step named Import adjustments; a photo the library already has — a duplicate, one restored from Recently Deleted, one joined from a browsed folder — is not changed; a control a recipe may not name is refused before anything is imported; preset.saveRecipe keeps a recipe for reuse), keywords?: [..], onDeleted?: restore|skip|fresh (a file that is in Recently Deleted: restore (default) = bring the photo back with its edits — relinked to the file when its own is gone, skip = leave it there and say so, fresh = delete the trashed record and import the file as new)} → {imported, duplicates: [{path, existing, reason, existingDeleted?}], restored?: [photoId], failed, warnings?: [{path, code: cameraProfile|uprightGeometry|unmappedXmp, profile?, mode?: off|auto|level|vertical|full|guided|unknown, fields?}], moved?: [{from, to, sidecars?}], kept?: [{path, reason}] (move: sources left in place and why), album?}
- **library.importLightroom** — Import Lightroom Catalog
  {path: .lrcat, or a Lightroom catalog backup .zip (unpacked to a temporary folder in the library, removed after reading; the zip is not changed), updateExisting?: false}; direct import of paths, ratings, flags, metadata, keywords, collections, virtual copies & mapped edits. Archives source settings/history first. Existing edited photos are preserved unless updateExisting=true; source catalog is read-only.
- **library.importPreview** — Review Import
  {paths: [file or folder (recursive)]} → {candidates: [{path, name, format, kind, width, height, fileSize, captured, duplicate?: path|content, existing?, error?, previewOnly?: why a raw can only be shown from its embedded preview}], duplicates, scanned, scanLimited: bool (the folder walk stopped at its scan limit: there may be more photos), skipped: {unreadable (folders that could not be listed), unsupported (files in the folders that are not a supported photo type, XMP sidecars not counted; a file named in paths is always tried)}} — nothing is added
- **library.info** — Library Info
  {}
- **library.inspectLightroom** — Inspect Lightroom Catalog
  {path: .lrcat, or a Lightroom catalog backup .zip} → {photos, collections, missing, warnings}; read-only, no Lightroom required
- **library.memory** — Memory Usage
  {} — bytes held by each cache (decoded sources, rendered previews, GPU buffers; heap when instrumented)
- **library.missing** — Missing Photos
  {} → [{id, path}] — photos whose original file isn't where the library expects it (every file is looked at: on a network share that takes minutes, so the desktop app, asked over its control channel, checks on a worker thread, with a row in the activity stack that can stop it, and answers when it is done)
- **library.next** — Next Photo
  {}
- **library.preferences** — Library Preferences
  {import?: {rawPreset?: presetId|"default", otherPreset?: presetId|"default", perCamera?: bool, cameras?: [{camera: "Make Model", preset: presetId|null}], copyright?: text, creator?: text (given to imported photos without one), showOnCard?: bool (open the import review when a camera or card is connected)}, camera?: {camera, preset?, remove?: bool}, cacheMb?: n (0 = default), forgetLocalDays?: n (forget untouched Local photos of folders not browsed for n days; 0 = never)} — develop defaults applied on import (raws / other images / per camera) and the thumbnail cache size, saved with the library → {xmp, import, cacheMb, forgetLocalDays, persistent}
- **library.previewProgress** — Preview Build Progress
  {} → {total, done, failed, repaired, skipped, shared, background, running, cancelled, what, error} | null
- **library.previous** — Previous Photo
  {}
- **library.recheckPreviewOnly** — Recheck Preview-Only Raws
  {all?: bool} — probe again preview-only raws and ORFs whose support another LightCraft version checked (the app does this in the background when a library opens; `all` rechecks every preview-only raw and ORF, e.g. when testing a decoder build of the same version), and bring each up to date as Reload from Disk would; not an undo step, develop settings and history are kept; files that can't be read are left for next time → {checked, updated: [ids], cleared: [ids] (develop from their raw data now)}
- **library.refresh** — Refresh View
  {} — show what matches now: a view that holds its photos (`library.holdView`) lets go of the ones that stopped matching a smart album's rules, Picks or the filter bar since it was opened, sorted or last refreshed
- **library.refreshLensProfiles** — Look Up Lens Profiles Again
  {ids?: [photo ids], all?: bool} — library raws without a lens profile whose lens the lens database knows are read again and get their profile (the correction is switched on where the photo's settings are still as imported); with all, also raws whose profile came from the database (it may give another, or none) and raws whose file named no lens at import; the app does this by itself when the database arrives (all: when its files were replaced) and when Enable Lens Corrections is ticked; not an undo step → {checked, found: [ids], database: bool}
- **library.removeFolder** — Remove Folder from Library
  {path, disk?: bool} — move the library photos imported from this folder (and the folders inside it) to Recently Deleted; one undo step, no file is touched. A whole disk or share (`/Volumes/nas`, `C:\`, `\\srv\share`) goes only with `disk: true`, the startup disk never → {removed}
- **library.retrySidecars** — Write Waiting XMP Sidecars
  {} — writes again the automatic XMP sidecars that failed (folder offline, read-only or full) whose originals are reachable now → {written, waiting}
- **library.select** — Select Photos
  {ids: [id], active?: id, mode?: replace|add|toggle|range} — every id must be a photo of the library
- **library.selectAll** — Select All
  {}
- **library.selectBy** — Select by Flag, Rating or Label
  {flag?: pick|reject|none, rating?: 0..5, ratingOp?: gte|eq|lte (default gte), label?: red|…|none, add?: bool (extend the selection)} — among the photos in view
- **library.selectNone** — Deselect All
  {}
- **library.shuffle** — Reshuffle
  {seed?: 0..2^53-1} — sort at random; without `seed` a new shuffle each time
- **library.smartPreviews** — Build Smart Previews
  {ids?, discard?: bool, background?: bool} — build (or discard) the smart previews of the selected photos (when more than one is selected; else all in view): compact proxies in the library that keep photos editable and exportable (at proxy size) while their originals are offline; a damaged proxy (cut short) is rebuilt → {built, repaired, removed, failed}; with background (the app's menu) the files are read and written on a worker thread → {total, done, failed, repaired, running, what} like library.buildPreviews (progress: library.previewProgress, stop: library.cancelPreviews)
- **library.smartPreviewsLocation** — Smart Previews Location
  {path?: absolute folder, reset?: bool, existing?: move|leave|discard} — without path/reset: where this library keeps its smart previews → {path, default, custom, available, count, bytes}. With path (or reset = back to `Smart Previews` in the library): use that folder instead (must exist or have an existing parent, and accept writes; never falls back to another drive). Smart previews already in the old folder need `existing`: move them, leave them (build again), or discard them → also {handled, failed}
- **library.sort** — Sort
  {key?: captureDate|importDate|editDate|fileName|rating|fileSize|random, ascending?: bool, group?: auto|none|day|month|year, seed?: u64 (the shuffle `random` gives)}
- **library.source** — Show Source
  {kind: all|recentlyAdded|album|recentlyDeleted|picks|missing|libraryFolder, id?: albumId, path?: a path from library.folders (for libraryFolder)}
- **library.state** — Library State
  {}
- **library.toggleAutoWriteXmp** — Automatically Write Changes into XMP
  {} → {autoWrite}
- **library.toggleFilters** — Enable Filters
  {} — with a filter set, puts it aside and shows everything; with one put aside, brings it back as it was (stars, flag, text… together). Setting or clearing a filter while it is off forgets the one put aside → {enabled, count}
- **library.up** — Photo Above
  {rows?: n (photos to move back; default 1, the grid passes the distance to the cell above)}
- **library.xmpPreferences** — XMP Sidecar Preferences
  {autoWrite?: bool, naming?: stem (IMG_1.xmp, default) | full (IMG_1.CR3.xmp)} → current preferences (saved with the library)

## metadata

- **metadata.applyPreset** — Apply Metadata Preset
  {name, ids?} — text fields replace, keywords are added; one undo step
- **metadata.deletePreset** — Delete Metadata Preset
  {name}
- **metadata.downloadPlaceNames** — Download Place Names (GeoNames)
  {} → {started, path, attribution} — downloads the GeoNames cities list (CC-BY 4.0, ~3 MB, from download.geonames.org) in the background for Fill Location from GPS, always into `geonames` in the settings folder (a folder or server named by the caller is refused); no photo data is sent
- **metadata.placeNamesStatus** — Place Names Status
  {dataset?: folder} → {downloaded, bytes, path, attribution, source}
- **metadata.presets** — Metadata Presets
  {} → [{name, fields}]
- **metadata.reverseGeocode** — Fill Location from GPS
  {ids?, overwrite?: bool (also replace place fields that already have text; default false: only empty ones are filled), dryRun?, dataset?: folder, maxDistance?: metres (past this distance from the town found, City is left empty and the town is given as nearestCity)} → {looked, found, changed, photos: [{id, place: {sublocation, city, state, country, iso, distance}, nearestCity?}], attribution} — fills City / State / Country (and Sublocation when known) from GPS with the offline GeoNames place names (download them first); one undo step. The place names list towns of 15 000 people or more (GeoNames cities15000): a photo taken in a smaller town gets the nearest larger one, up to 50 km away (`distance` says how far); `maxDistance` keeps such a town out of City
- **metadata.savePreset** — Save Metadata Preset
  {name, fields?: {copyright?, copyrightStatus?: unknown|copyrighted|publicDomain, usageTerms?, copyrightUrl?, creator?, title?, caption?, location?, city?, state?, country?, keywords?: [..]}, only?: [field] (from the active photo when `fields` is absent; default the copyright fields, creator, place)} — adds or replaces

## prefs

- **prefs.backgroundPrep** — Background Preparation Settings
  {} → {app, library|null, settings (in use), own: bool (this library keeps its own), building} — what is prepared in the background per mode (culling | library: previews of every photo in view, ahead = photos ahead rendered for the loupe, eyeAhead = photos ahead whose eye focus strip is worked out, scope all|marked|onScreen; develop: ahead = photos kept decoded ready to edit, scope)
- **prefs.setBackgroundPrep** — Set Background Preparation
  {settings?: partial {culling?, library?, develop?}, library?: bool (this library's own settings; else the app-wide ones), reset?: bool (this library goes back to the app-wide settings)} → as prefs.backgroundPrep

## print

- **print.cell.add** — Add Print Cell
  {width, height, x?, y?, page?, photo?} inches; picture/custom package → {id, cell, pages}; the cell goes to the first free spot unless x and y are given
- **print.cell.delete** — Delete Print Cell
  {id}
- **print.cell.move** — Move Print Cell
  {id, x, y, snap?: bool, threshold?: inches} → {id, rect}; snap uses the guides' snap mode
- **print.cell.page** — Move Print Cell to Page
  {id, page: zero-based}
- **print.cell.photo** — Set Print Cell Photo
  {id, photo: photo id | null} (custom package: the photo printed in the cell)
- **print.cell.resize** — Resize Print Cell
  {id, width?, height?, x?, y?, snap?: bool, threshold?} → {id, rect}
- **print.cell.stack** — Arrange Print Cell
  {id, order: toBack|backward|forward|toFront} → {order: cell ids back to front}
- **print.exportPdf** — Print to PDF
  {path, ids?: photo ids (default selection)} → {path, pages, photos, bytes}; prints the current print.get settings; replaces an existing output, never an original
- **print.get** — Print Settings
  {ids?} → {settings: {layout, image, page, guides, job}, papers, pageWidth, pageHeight, printable, pageCount, cellsPerPage, gridCells?, overlaps}; lengths are inches
- **print.layout.autoLayout** — Auto Layout
  {} — packs the package's cells onto as few pages as possible → {pages, cells}
- **print.layout.clear** — Clear Print Layout
  {} — removes every cell and extra page
- **print.layout.newPage** — New Print Page
  {} → {page, pages}
- **print.reset** — Reset Print Settings
  {} → print.get
- **print.set** — Set Print Settings
  {layout?: {style: singleImage|contactSheet|picturePackage|customPackage, page: {paper, customWidth, customHeight, orientation: portrait|landscape, margins: {top,right,bottom,left}}, grid: {columns, rows, spacingX, spacingY, keepSquare}, spacing}, image?: {zoomToFill, rotateToFit, borderEnabled, borderWidth, borderColor: [r,g,b], strokeEnabled, strokeWidthPt, strokeColor}, page?: {background: [r,g,b], pageNumbers, pageInfo, cropMarks} (Page Options: single image and contact sheet only), guides?: {showRulers, units: in|cm|mm|pt, snap: off|cells|grid, gridSize, showMargins, showBleed, showPageGrid, showCells, showDimensions}, job?: {ppi: 72..720, color?: {profile: {kind: managed, space: srgb|adobeRgb} | {kind: icc, path}, intent: perceptual|relative, blackPointCompensation, brightness: -100..100, contrast: -100..100, sharpen: off|low|standard|high, media: matte|glossy, sixteenBit}}} — merges into the current print; cells and pages change with print.cell.* / print.layout.*; → print.get
- **print.template.apply** — Apply Print Template
  {name} → print.get
- **print.template.delete** — Delete Print Template
  {name} → print.template.list
- **print.template.export** — Export Print Template
  {name, path}: writes the template as a .lcprint JSON file ({format, version, name, settings}; `.lcprint` is added when the path has no extension); replaces an existing file, never an original → {name, path}
- **print.template.import** — Import Print Template
  {path: a .lcprint file (at most 256 KB)}: checked like a saved template (format, version, name, every setting; cell photos and guides are dropped) and added under its name; a name taken (any case) gets " (2)"… → print.template.list + {name, renamed}
- **print.template.list** — Print Templates
  {} → {templates: [{name, style, settings}]}
- **print.template.save** — Save Print Template
  {name} — saves the layout, image settings, page and job (not the cells' photos or the guides); an existing name (any case) is replaced → print.template.list

## slideshow

- **slideshow.export** — Export Slideshow
  {format: "pdf"|"jpeg"|"video", path: the .pdf / .mp4 / .webm file, or for jpeg the folder (created if missing), size?: pdf/jpeg the long side in pixels (64–8192, default 1920), video the frame height (64–2160 or "720p"/"1080p", default 720), quality?: 1–100 (JPEG quality, default 90; video default 75), fps?: 24|25|30|60 (video, default 30), container?: "mp4"|"webm" (video, default mp4), fullScreen?: bool (pdf: open in the viewer's full screen mode, default true), speed?: 1–10 (video encoder speed, default 10 = fastest), name?: jpeg file name prefix (default the folder's name: <name>-001.jpg…), ids?: photo ids (default the photos in view, in view order), wait?: bool (run here and reply with the result)} — the photos' slides with the slideshow layout, overlays and the intro/ending screens that are on; video is AV1 (no audio), each slide held for its duration and fades rendered as frames, at most 2 hours. Runs in the background with a row in the activity stack (activity.cancel {id: taskId} stops it; nothing is left behind: files are written as .part and renamed when complete); a photo that can't be rendered is skipped with a warning → {taskId, background, format, path, slides, seconds, total, width, height, warnings}; with wait: the result (slideshow.exportStatus)
- **slideshow.exportStatus** — Slideshow Export Status
  {} → the last slideshow export: {taskId, format, path, running, done, total (slides, or frames for video), cancelled, result?: {format, path, width, height, slides, skipped, warnings, pages? | files? | frames, samples, keyFrames, seconds, fps, container, codec: "av1", audio: false; bytes}, error?} | {running: false} when there was none
- **slideshow.layout** — Slideshow Layout Settings
  {margins?: all four, marginLeft?, marginRight?, marginTop?, marginBottom?: fractions of the slide's shorter side (0–0.45; with linkMargins one sets all four), linkMargins?: bool, showGuides?: bool (margin guides in the slide editor), aspect?: "screen"|"16:9"|"4:3" (aspect preview), zoomToFill?: bool (crop the photo to fill its cell), strokeBorder?: bool, strokeColor?: "#rrggbb"|[r,g,b], strokeWidth?: fraction of the shorter side (0–0.05), castShadow?: bool, shadowOpacity?: 0–1, shadowOffset?: 0–0.1, shadowRadius?: 0–0.1 (fractions of the shorter side), shadowAngle?: degrees counter-clockwise from the right (−45 = down right), backdropColor?: colour, colorWash?: bool, washColor?: colour, washOpacity?: 0–1, washAngle?: degrees (the side the wash colour is full at), backgroundImage?: photo id|null, backgroundOpacity?: 0–1} — omitted keys keep their value, {} reads them; out-of-range numbers are clamped, wrong types refused; saved with the library → the settings
- **slideshow.overlays** — Slideshow Overlay Settings
  {identityPlate?: {enabled?, text?, image?: PNG/JPEG file (drawn instead of the text; "" = the text), size?: height as a fraction of the slide's shorter side (0.005–0.5), color?: "#rrggbb"|[r,g,b], opacity?: 0–1, …placement, behind?: bool (render behind the photo)}, ratingStars?: {enabled?, color?, size?: a star's height (0.005–0.15), …placement}, texts?: [text overlay] (replaces the list, at most 16; each entry merged onto the one at its index), addText?: text overlay ({} = the default "{file}"), removeText?: index, showWatermark?: bool, watermark?: text | the export watermark object {text, vertical, size, opacity, anchor, inset, color, shadow, image, imageWidth} (merged; sizes relative to the photo)} where a text overlay is {text?: template with tokens ({file}, {name}, {title}, {caption}, {date} (YYYY-MM-DD) / {date:%d.%m.%Y}, {exposure}, {shutter}, {aperture}, {focal}, {iso}, {camera}, {lens}, {rating}, {creator}, {copyright}, {folder}, {ext}; unknown tags show as typed), size?: line height (0.005–0.3), color?, opacity?, …placement, shadow?: bool, shadowOpacity?: 0–1, shadowOffset?, shadowRadius?: 0–0.05 (fractions of the shorter side), shadowAngle?: degrees counter-clockwise from the right} and the placement keys are anchor?: topLeft|top|topRight|left|center|right|bottomLeft|bottom|bottomRight, offsetX?, offsetY?: fractions of the slide's shorter side (x right, y down; −1–1), relativeTo?: "slide"|"photo" (the overlay is kept on the slide) — omitted keys keep their value, {} reads them; out-of-range numbers are clamped, wrong types refused; saved with the library; slideshow playback and slideshow.preview draw them → the settings and warnings (an unreadable identity plate image, unknown tokens)
- **slideshow.playback** — Slideshow Playback Settings
  {slideDuration?: seconds (0.5–120), fadeDuration?: seconds (0 = cut; at most 10 and the slide duration), fadeColor?: "#rrggbb"|[r,g,b]|null (fade through a colour instead of crossfading), randomOrder?: bool, repeat?: bool, preparePreviews?: bool (render the next slides before they are due), manual?: bool (manual slideshow: a slide stays up until ← or → changes it)} — omitted keys keep their value, {} reads them; saved with the library → {slideDuration, fadeDuration, fadeColor, randomOrder, repeat, preparePreviews, manual}
- **slideshow.preview** — Slideshow Slide Preview
  {id?: photo (default: the active one) | title?: "intro"|"ending", template?: a template id (slideshow.templates.list): compose with its settings instead of the library's, which don't change (the Template Browser's hover preview), width?, height?: pixels (16–4096; one given: the other from the aspect preview; neither: 1280 wide), path?: write the PNG here} — the photo's slide composed with the slideshow layout and overlays → {id, width, height, cell: [x0,y0,x1,y1], photo: [x0,y0,x1,y1] (the visible photo, slide pixels), overlays: [{kind: identityPlate|ratingStars|textN|watermark, box: [x0,y0,x1,y1]}], path | png (base64 PNG)}; with `title`, that title screen (`slideshow.titles`; drawn even while it is off) → {title, enabled, width, height, plate: [x0,y0,x1,y1] | null (the plate or text), path | png}
- **slideshow.templates.apply** — Apply Slideshow Template
  {id: template id | "previous" (the settings before the last apply) | name: template name (case-insensitive)} — replaces the playback (prepare previews kept), layout, overlays and titles settings with the template's and saves them with the library; there is no undo: the replaced settings are kept as "previous" for this session → {applied, name, warnings: [a background photo not in this library, an unreadable identity plate / watermark image…], previous, settings: {playback, layout, overlays, titles}}
- **slideshow.templates.delete** — Delete Slideshow Template
  {id: user template} — deletes its file → {deleted, name}
- **slideshow.templates.export** — Export Slideshow Template
  {id: template (built-in or user), path: .json file to write} → {id, name, path}
- **slideshow.templates.import** — Import Slideshow Template
  {path: a template .json file (at most 256 KB)} — checked like a saved one (format, version, every setting) and saved as a user template under its name (else the file's); a name taken gets " (2)"… → {id, name, builtin, group, path, renamed, warnings}
- **slideshow.templates.list** — Slideshow Templates
  {} → {templates: [{id: "builtin:…"|"user:…", name, builtin, group: "builtin"|"user", description?, path? (a user template's file)}], previous: bool (the settings before the last apply can be restored with apply {id: "previous"}), folder: the user templates folder | null, problems: ["file: why it was skipped"]} — built-ins first, then user templates by name (files in <settings>/slideshow-templates, at most 1000)
- **slideshow.templates.rename** — Rename Slideshow Template
  {id: user template, name} — its file follows the name; a name taken is refused → {id (the new one), name, builtin, group, path}
- **slideshow.templates.save** — Save Slideshow Template
  {name: 1–80 characters, replace?: bool (over a user template of that name)} — the current playback, layout, overlays and titles settings as a user template, <settings>/slideshow-templates/<name>.json (path separators and other reserved characters become _); a name taken (case-insensitive) or a built-in's is refused unless replace → {id, name, builtin, group, path}
- **slideshow.templates.update** — Update Slideshow Template
  {id: user template} — replace its settings with the current ones (name kept); built-ins can't change → {id, name, builtin, group, path}
- **slideshow.titles** — Slideshow Title Settings
  {intro?: screen, ending?: screen} where a screen is {enabled?: bool, color?: background "#rrggbb"|[r,g,b], content?: "none"|"identityPlate" (the Overlays identity plate, its text or image)|"text", text?: the text shown with content "text", overrideColor?: bool (draw the plate or text in textColor instead of the identity plate's colour; an image plate keeps its colours), textColor?: colour, scale?: height of the plate or text line as a fraction of the slide's shorter side (0.005–0.5; text wider than the slide shrinks to fit), duration?: seconds (0.5–120) | null (the slide duration)} — the intro plays once before the first slide, the ending after the last one when repeat is off; both fade with the playback fade; random order never moves them. Omitted keys keep their value, {} reads them; out-of-range numbers are clamped, wrong types refused; saved with the library → the settings and warnings (an unreadable identity plate image, a screen with nothing to show)

## stack

- **stack.auto** — Auto-Stack by Capture Time
  {gap?: seconds between consecutive captures (default 60), ids? (default: the selection if several photos, else the current view), preview?: bool} → {stacks, photos}
- **stack.collapseAll** — Collapse All Stacks
  {}
- **stack.expandAll** — Expand All Stacks
  {}
- **stack.group** — Group into Stack
  {ids?, top?: photoId (default: the active photo), collapsed?: bool (default true)} — stacks the photos are already in are merged
- **stack.moveDown** — Move Down in Stack
  {id?} — one place away from the top
- **stack.moveUp** — Move Up in Stack
  {id?} — one place towards the top
- **stack.remove** — Remove from Stack
  {ids?}
- **stack.setTop** — Set as Top of Stack
  {id?} (default: the active photo)
- **stack.split** — Split Stack
  {id?} — this photo and the ones after it become their own stack
- **stack.toggle** — Expand/Collapse Stack
  {ids?, collapsed?: bool} — the stacks of the named photos (else of the selection)
- **stack.ungroup** — Ungroup Stack
  {ids?}
