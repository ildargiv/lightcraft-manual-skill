# Команды редактирования LightCraft — полные параметры

Сгенерировано из `lightcraft-cli commands --json` (0.21.1).
Источник истины — `command_list`.

## develop

### develop.adjust — Nudge Develop Value
{control, delta}

### develop.auto — Auto Settings
shortcut: Shift+A
{}

### develop.autoBwMix — Auto B&W Mix
{} — sets the black & white mix from the photo's colours (and switches to B&W)

### develop.autoSync — Auto Sync
shortcut: Cmd+Alt+Shift+A
{on?: bool} (toggles when omitted) — edits to the active photo also change the other selected photos (only the settings that changed; not spot removal / red eye) → {on}

### develop.beginInteraction — Begin Interaction
{label}

### develop.cancelInteraction — Cancel Interaction
{}

### develop.controls — List Develop Controls
{section?} — every slider with range, default and current value

### develop.copy — Copy Edit Settings
shortcut: Cmd+C
{groups?: [settingsGroup]} (default: all but crop, masks, remove)

### develop.curve — Set Point Curve
{channel: master|red|green|blue, points: [[x,y],...] in 0..1}

### develop.endInteraction — End Interaction
{}

### develop.get — Get Develop Settings
{id?} → the photo's develop settings; `process` is the rendering process they are interpreted by (see develop.updateProcess)

### develop.hdr — HDR
{enabled?: bool (default: toggle), maxEv?: number 0..5 (headroom limit, stops above SDR white)} — HDR editing: highlights above SDR white for HDR exports and displays; every SDR render uses the SDR rendition (the hdr.sdr* controls)

### develop.matchExposure — Match Total Exposures
{ids?} — set each selected photo's Exposure so its total exposure (shutter × ISO ÷ aperture², plus the slider) equals the active photo's; photos without exposure data are skipped → {changed, skipped}

### develop.merge — Apply Settings JSON
{settings: partial DevelopSettings JSON, label?}

### develop.paste — Paste Edit Settings
shortcut: Cmd+V
{ids?, groups?: [settingsGroup] (paste only these of the copied groups)}

### develop.pastePrevious — Paste Settings from Previous
shortcut: Cmd+Alt+V
{ids?, groups?: [settingsGroup] (default: the copy groups)} — from the photo that was active before this one

### develop.profile — Set Profile
{id: profile id (see profiles.list), amount?: 0..200}

### develop.quickAdjust — Quick Develop
{control: develop control id, delta, ids?} — add `delta` to the control on every target photo (each from its own value; Quick Develop) in one undo step → {changed}

### develop.reset — Reset Edits
shortcut: Cmd+Shift+R
{ids?}

### develop.resetControl — Reset Control
{control}

### develop.resetSection — Reset Section
{section: profile|light|curve|color|mixer|grading|effects|vignette|grain|detail|optics|geometry}

### develop.sectionEnabled — Toggle Section
{section: string, enabled: bool}

### develop.set — Set Develop Values
{control?: controlId, value?: number, values?: {controlId: number}, ids?: [photo]} — see develop.controls; `crop.angle` turns the crop as crop.straighten does (kept if it still fits, else the largest of its aspect inside the photo)

### develop.sync — Sync Settings
{groups?} — copy the active photo's settings to all selected photos

### develop.targeted — Targeted Adjustment
{target: curve|hue|sat|lum, x, y (normalized image coords), delta (slider units; point curves: output levels 0..255), channel?: parametric|master|red|green|blue (curve)} — adjusts the curve region / colour-mixer bands under the point; returns the changed controls

### develop.treatment — Black & White
shortcut: V
{bw?: bool} (toggles when omitted)

### develop.updateProcess — Update to Current Process
{ids?}: moves the target photos (`ids`, else the selection) that are on an older rendering process to the current one, as one undo step (their look can change; the sliders keep their values; see docs/process-versions.md). Enabled while a selected photo is on an older process; named photos are checked themselves (each must exist, one must be on an older process) → {changed, process}

### develop.wb — White Balance
{mode: asShot|auto|daylight|cloudy|shade|tungsten|fluorescent|flash|custom, temp?, tint?}

### develop.wbPick — White Balance Selector
shortcut: W
{x, y} normalized image coords of a neutral point

## mask

### mask.add — Create New Mask
{kind: brush|linear|radial|sky|subject|background|luminanceRange|colorRange|object|prompt, ...shape params (start/end, center/rx/ry/angle/feather, lo/hi…; object: points/exclude [[x,y],…]; prompt: text; object/prompt: seg? a stored segmentation, no model needed), name?} — AI kinds need the SAM 3 model; in the app a prompt returns {pending} and the mask appears when found

### mask.addComponent — Add/Subtract/Intersect Mask
{id?: maskId, op: add|subtract|intersect, kind, ...shape params}

### mask.adjust — Set Mask Adjustments
{id?, values: {exposure, contrast, highlights, shadows, whites, blacks, temp, tint, texture, clarity, dehaze, hue, saturation, sharpness, noise, moire, defringe, lens_blur, lens_blur_off, lens_blur_outside, lens_blur_boost, lens_blur_transition, color_hue, color_sat, amount}}

### mask.applyEffect — Apply Mask Effect
{name, id? | ids?: [maskId] | all?: bool, photos?: "selected" (also the masks of the same names on the other selected photos, one undo step), remember?: bool (true: new masks of this kind start with it)} — sets the effect's sliders (all, or the ones it keeps; Amount only if it carries it) → {name, masks, photos, brush}

### mask.brushStroke — Brush Stroke
{id?: maskId, points: [[x,y],…] normalized, size?: fraction of long edge (0.03), feather?, flow?, density?, erase?: bool, autoMask?: bool, pressure?: [p,…] pen pressure 0..1 per point (scales each dab's size and flow; omitted: full), connect?: bool — start from the last point of the mask's last stroke (⇧-click), size / feather / flow tapering from that stroke's to these} → {activeMask, connected}

### mask.component — Edit Mask Component
{id?, component: index, action: invert|duplicate|delete|rename|op, name? (rename; empty clears), op?: add|subtract|intersect} — one component of a mask (deleting the last one deletes the mask)

### mask.delete — Delete Mask
{id?}

### mask.deleteAll — Delete All Masks
{}

### mask.deleteEffect — Delete Mask Effect
{name | names: [name]} — removes effect presets

### mask.duplicate — Duplicate Mask
{id?, invert?: bool (Duplicate and Invert)} — the copy goes right after the original and is selected

### mask.duplicateEffect — Duplicate Mask Effect
{name, to?} (default "<name> copy") → list + {name}

### mask.effects — Mask Effect Presets
{} → {effects: [{name, adjust, group?, favorite?, fields?, with_amount?, brush?, extra?}], groups: [{name, effects: [name]}] (menu order), current: the effect the selected mask matches or null, toolEffects: {tool: effect a new mask of that kind starts with}}

### mask.exportEffects — Export Mask Effects
{path, names?: [name], group?: name (default: all)} — writes an .lceffect JSON file (groups, stars and kept Lightroom settings included) → {path, count}

### mask.favoriteEffect — Favorite Mask Effect
{name | names, favorite?: bool (default: toggle)}

### mask.importEffects — Import Mask Effects
{path | paths: [file or folder], group?, dryRun?} — Lightroom Classic local adjustment presets (.lrtemplate), Camera Raw local correction presets (.xmp), .lceffect files and .zip bundles of these; folders and Lightroom's divider presets ("10 ----- DETAIL ----- 10") become groups; same-named effects are replaced → {imported: [{name, group, file, unmapped}], dividers: [{name, group, file}], failed: [[file, error]]}

### mask.invert — Invert Mask
{id?}

### mask.move — Move Mask
{id?, to?: index (0 = top), delta?: ±n} — reorder the masks list

### mask.objectPoint — Add Object Click
{x, y: normalized image point, exclude?: bool (⌥-click: leave this part out), id?: maskId} — a click on the selected mask's Object selection (its last Object component); SAM 3 re-segments the object → {include, exclude}

### mask.refine — Refine Mask Edges
{id?, value: 0..100} — the mask's edges snap to the photo's (guided filter; rendered on the CPU)

### mask.refineDetail — Refine AI Mask Detail
{id?: maskId, component?} — a zoomed-in SAM 3 pass over an Object/Describe selection (default: the mask's last one): the photo around it is analyzed again at a higher resolution, in the background; the mask updates when it's done → {started}

### mask.rename — Rename Mask
{id?, name}

### mask.renameEffect — Rename Mask Effect
{name, to}

### mask.renameEffectGroup — Rename Mask Effect Group
{group, to} ("" ungroups; an existing name merges)

### mask.sampleColor — Sample Mask Color
{x, y: normalized image point, add?: bool (⇧: add to the samples, max 5), id?, component?} — the colour range of the selected mask (its first colour-range component) samples the colour there → {samples}

### mask.saveEffect — Save Mask Effect
{name, id?, group?, fields?: "all" (default) | "changed" | [slider], amount?: bool (carry Amount), brush?: {size, feather, flow, density, auto_mask}} — the selected mask's sliders as an effect preset (replaces one of that name), saved with the library

### mask.select — Select Mask
{id|null}

### mask.setEffectGroup — Move Mask Effect to Group
{name | names, group: name ("" = none)}

### mask.toolEffect — Set Effect for New Masks
{tool: brush|linear|radial|subject|…, name?} — the effect new masks of that kind start with (no name: none)

### mask.update — Update Mask Shape
{id?, component?: index (0), shape: MaskShape JSON}

### mask.updateEffect — Update Mask Effect
{name, id?, fields?, amount?, brush?} — overwrite the effect with the selected mask's sliders (keeps its group, star and which sliders it carries unless given)

### mask.visible — Show/Hide Mask
{id?, visible?: bool}

## spot

### spot.add — Add Remove Spot
{mode?: remove|heal|clone|fill (content-aware), points: [[x,y],…], size?: fraction of long edge, feather?, opacity?, source?: [dx,dy] (default: the best match nearby)} — selects the new spot; returns {index}

### spot.delete — Delete Spot
{index? (the selected spot)}

### spot.findBlemishes — Find Blemishes
{sensitivity?: 0..100 (50), add?: bool (true), maxPerFace?: 1..20 (6)} — find small blemishes (darker or redder round spots on skin) on the faces of the active photo and add a heal spot on each (one undo step); needs the YuNet face detector (`faces.models.download {id: "yunet-2023mar"}`). Faces narrower than 160 px at 1600 px, and faces with more than 12 candidates (stubble, freckles, pores), get none → {faces, spots: [{x, y, size, face}], added}

### spot.findDust — Find Dust Spots
{sensitivity?: 0..100 (50), add?: bool (true)} — find sensor-dust spots (small soft dark spots on smooth areas) and add a heal spot on each (one undo step) → {spots: [{x, y, size}], added}

### spot.refreshSource — Refresh Source
{index? (the selected spot)} — picks the next-best source away from the current one

### spot.select — Select Spot
{index|null}

### spot.update — Edit Spot
{index? (the selected spot), move?: [dx,dy] (the target, normalized), source?: [dx,dy] (offset from the target), moveSource?: [dx,dy], size?, feather?, opacity?, mode?}

## curve

### curve.applyPreset — Apply Point Curve Preset
{name} — sets the active photo's point curves (all four channels; the parametric curve stays)

### curve.deletePreset — Delete Point Curve Preset
{name} — a user preset (built-ins can't be deleted)

### curve.exportPresets — Export Point Curve Presets
{path, names?: [name] (default: every user preset)} — writes a .lccurve JSON file → {path, count}

### curve.importPresets — Import Point Curve Presets
{path | paths: [file]} — .lccurve JSON files ({format, version, presets: [...]}, an array of presets, or one preset); same-named user presets are replaced → {imported: [name], failed: [[file, error]]}

### curve.presets — Point Curve Presets
{} → {presets: [{name, master, red, green, blue: [[x,y],...], builtin?}], current: name of the preset the active photo's point curves match, or null}

### curve.reset — Reset Tone Curve
{channel?: all|point|parametric|master|red|green|blue (default all)} — the active photo's tone curve (or one channel) back to linear

### curve.savePreset — Save Point Curve Preset
{name} — the active photo's point curves under a name (replaces a user preset of that name; built-in names are reserved), saved with the library

## pointColor

### pointColor.delete — Delete Point Color Sample
{index}

### pointColor.pick — Add Point Color Sample
{x, y} normalized image coords — samples the colour there (max 8); returns {index, lum, chroma, hue}

## geometry

### geometry.guides — Guided Upright Guides
{guides: [[x0,y0,x1,y1], …] (≤ 4, normalized coords of the lens-corrected image), add?: bool (append one guide, dropping the oldest beyond 4)} — switches Upright to Guided

### geometry.upright — Upright
{mode: off|auto|guided|level|vertical|full} — analyses the photo (line segments → vanishing points) and stores the correction; run again to update after lens changes

## lens

### lens.databaseStatus — Lens Database Status
{} → {download: {state: idle|running|done|failed|cancelled, …}, dir, lenses (in the database in use)}

### lens.downloadDatabase — Download the Lens Database
{} — fetch lensfun's lens database (CC BY-SA 3.0, pinned to one commit, checked file by file) into the app's data folder in the background, with an activity row, and read lens profiles from it once it is in place (unless LIGHTCRAFT_LENSFUN_DIR names another folder); the desktop app offers it on its first launch and in Settings. LIGHTCRAFT_LENSFUN_URL lists other places to fetch the same files from → {started, dir}

## lensBlur

### lensBlur.brushReset — Reset Lens Blur Brush
{mode?: "focus"|"blur"} — removes that brush's strokes (both brushes without `mode`)

### lensBlur.brushStroke — Lens Blur Brush Stroke
{mode: "focus"|"blur", points: [[x,y],…] normalized, size?: fraction of long edge (0.03), feather?: 0..100, flow?: 1..100, amount?: 1..100 (how far the stroke refines), erase?: bool, autoMask?: bool, pressure?: [p,…] 0..1 per point} — Lens Blur Brush Refinement: Focus strokes stay sharp, Blur strokes are blurred

### lensBlur.findSubject — Find Subject
{} — selects the photo's subject with an Object mask (SAM 3) clicked where the camera focused, when the file records it, else at the likeliest subject; Lens Blur is switched on and keeps that mask in focus → {mask, point: [x,y], from: "camera"|"photo", pending?}

## redeye

### redeye.add — Add Red Eye Correction
{center: [x,y] normalized, rx, ry: radii as fractions of the long edge, pet?: bool, pupilSize?: 0..100, darken?: 0..100} — the pupil inside is found automatically; returns {index}

### redeye.catchlight — Pet Eye Catchlight
{index, on?: bool (default true), offset?: [dx, dy] from the pupil centre in pupil radii (default [-0.35, -0.35])}

### redeye.delete — Delete Red Eye Correction
{index}

## profile

### profile.deleteCamera — Delete Imported Camera Profile
{id: dcp:…} — photos using it develop with their file's own colour again

### profile.deleteImported — Delete Imported Profile
{id: lut:… | dcp:…}

### profile.favorite — Favorite Profile
{id, favorite?: bool} (toggles when omitted)

### profile.import — Import Profiles
{paths: [.cube / .dcp file, folder or .zip]} — 3D LUTs become creative profiles (Amount 0–200 %; rendered on the CPU) in the profile browser's groups (folder / zip name, else Imported); DNG camera profiles (.dcp, the user's own) become camera profiles (dcp: ids, group Camera Profiles) that replace a raw file's colour model when it is decoded → {imported: [{id, name, group | cameraModel}], failed}

## profiles

### profiles.camera — Imported Camera Profiles
{} → {profiles: [{id, name, cameraModel, file}]}: the imported .dcp camera profiles (use with develop.profile)

### profiles.list — List Profiles
{} — every profile (built-in, then imported LUTs marked `imported`) with its group and favourite flag

### profiles.menu — Profile Menu
{} — favourites, recent (newest first) and groups

## preset

### preset.apply — Apply Preset
{id: presetId, amount?: 0..200 (percent), ids?}

### preset.create — Create Preset
{name, group?, groups?: [settingsGroup]}

### preset.delete — Delete Preset
{id}

### preset.export — Export Presets
{path, ids?: [presetId], group?: name} (default: all user presets) → {path, count}; writes a .lcpreset JSON file

### preset.favorite — Favorite Preset
{id, favorite?: bool}

### preset.import — Import Presets
{paths: [file or folder], group?, dryRun?} — .lcpreset, XMP presets, .lrtemplate, photos carrying edits (DNG/JPEG/TIFF "DNG presets"), Luminar looks (.lmp, .mplumpack collections) and .zip bundles of these; folders give their name as group; crs: fields mapped per docs/xmp-interop.md; local adjustment presets (Lightroom .lrtemplate, Camera Raw local .xmp, .lceffect) become mask effects (`mask.effects`; divider presets become their groups); a profile the preset names applies when it was imported with profile.import (before or after) → {imported: [{id,name,group,file,unmapped,profile: {name, id}|null}], skipped, failed, effects: [{name,group,file,unmapped}], effectDividers: [{name,group,file}]}

### preset.move — Move Preset to Group
{id, group}

### preset.rename — Rename Preset
{id, name}

### preset.saveRecipe — Save Import Recipe as Preset
{name (up to 100 characters), group?: default Import Recipes, recipe: [{id: a plain develop control (develop.controls; no white balance, geometry or crop), value}]} → {id, name} — save a batch-edit recipe (as library.import takes it) as a user preset, so it can be reused from the Preset list; only the settings the recipe names are stored, so applying it later never overrides the rest. The preset gets an id no other preset has; saving the same recipe under the same name and group again returns the preset that already is

### preset.update — Update Preset with Current Settings
{id, groups?: [settingsGroup] (default: the groups the preset already sets)} — from the active photo

## presets

### presets.list — List Presets
{}

## crop

### crop.aspect — Crop Aspect
{aspect: "original"|"free"|"current" (lock the crop's present shape)|"toggle" (lock ↔ free)|"1x1"|"4x5"|"8.5x11"|"5x7"|"2x3"|"4x3"|"16x9"|"16x10"|[w,h], orientation?: "crop"|"given"} — a named ratio takes the crop's present orientation (landscape, or portrait after X); [w,h] is used as given (taller than wide → portrait); `orientation` overrides either

### crop.autoStraighten — Auto Straighten
{} — level the horizon (or plumb lines) with the crop angle

### crop.drag — Drag Crop Handle
{handle: topLeft|topRight|bottomRight|bottomLeft|top|right|bottom|left|move | 0..8, from: [x,y], to: [x,y] (normalized, straightened frame), start?: [x0,y0,x1,y1] (default: the current crop), keepRatio?: bool (default false)} — drags a crop handle; stops at the image edge, keeps the opposite edges, honours the aspect lock; keepRatio holds the frame's current proportions for this drag even with the lock off (the UI sends it while Shift is held)

### crop.reset — Reset Crop
shortcut: Cmd+Alt+R
{}

### crop.rotateAspect — Rotate Crop Aspect
shortcut: X
{}

### crop.set — Set Crop
{rect?: [x0,y0,x1,y1] normalized in the straightened frame, angle?: degrees}

### crop.straighten — Straighten
{angle: degrees -45..45} — keeps the crop if it still fits, else shrinks it about its centre (the largest crop of its aspect stays the largest)

## edit

### edit.redo — Redo
shortcut: Cmd+Shift+Z
{}

### edit.undo — Undo
shortcut: Cmd+Z
{}

## history

### history.clear — Clear History
{} — keeps the current settings as the only step

### history.list — List History
{id?} — returns {history: labels oldest first, cursor: index of the step the settings are at (later steps can be returned to), versions}

### history.next — Next History Step
{} — steps the History cursor forward one step

### history.previous — Previous History Step
{} — steps the History cursor back one step

### history.restore — Go to History Step
{index} — loads that step's settings and moves the History cursor there; later steps stay listed until a new edit

## version

### version.create — Create Version
shortcut: Cmd+Shift+S
{name?}

### version.delete — Delete Version
{index}

### version.rename — Rename Version
{index, name}

### version.restore — Restore Version
{index}

### version.update — Update Version with Current Settings
{index}

## export

### export.addToPhotos — Add to Apple Photos
{paths: [absolute file paths], album?: name (an album at the top level of Photos, made when missing; default none), wait?} → once Photos is done, {job, running: false, requested, album, imported, ids: [Photos media item ids], warning?}; with wait: false, at once {job, running: true, requested, album} and the outcome later from export.photosImports {job}. wait defaults to true without a window (lightcraft-cli, the MCP server) and to false in the desktop app, where wait: true is refused (its control requests are answered on the UI thread, which never waits for Photos). macOS: asks Photos to import the files (the first time, macOS asks the user to allow LightCraft to control Photos). One import runs at a time, and an export adding to Photos reserves it before writing: another is refused until it ends. app.export does this for the files it writes with `addToPhotos: true`

### export.checkTarget — Check Output Path
{path} — fails when writing `path` would replace a photo's original (or its XMP sidecar) in the library; front ends call it before saving a render or screenshot to a user-given path → {path}

### export.contactSheet — Export Contact Sheet PDF
{path, ids?: photo ids (default selection), paper?: a4|letter, landscape?: bool, columns?: 1..8, rows?: 1..10, captions?: bool} → {path, pages, photos, bytes}; replaces an existing output, never an original

### export.deletePreset — Delete Export Preset
{name} — removes a user preset → presets

### export.photosImports — Apple Photos Imports
{job?} → {imports: [{job, running, exporting?, requested, album, imported?, ids?, warning?, error?, skipped?}]} (this session's, oldest first), or the one job: how Add to Apple Photos is getting on (exporting: reserved by an export still writing its files)

### export.presets — Export Presets
{} → [{name, builtin, params}] (use with app.export {preset: name, …overrides})

### export.savePreset — Save Export Preset
{name, params?: app.export params (default: the last export's)} — adds or replaces a user preset, saved with the library → presets

## merge

### merge.hdr — HDR Merge
{ids?, align=true, deghost=none|low|medium|high, autoSettings=true, stack=false, preview=false, showOverlay=false, previewPath?}

### merge.hdrBatch — HDR for Each Bracket Set
{ids?, align=true, deghost=none|low|medium|high, autoSettings=true, stack=false}: an HDR merge of each bracket set among the photos (each stack, then photos taken less than a second apart at exposures ≥ ½ EV apart) → {merged: [{id, path, …}], failed: [{photos, error}]}

### merge.hdrPanorama — HDR Panorama Merge
{ids?, bracket=0 (auto from EXIF), align, deghost, projection, boundaryWarp, autoCrop, fillEdges, autoSettings, stack, preview, previewPath?}

### merge.panorama — Panorama Merge
{ids?, projection=auto|spherical|cylindrical|perspective, boundaryWarp=0..100, autoCrop=false, fillEdges=false, autoSettings=true, stack=false, maxMegapixels=full size (≤ 512, held to memory), preview=false, previewPath?}

## denoise

### denoise.cancel — Cancel Denoise
{id?, all?} → {cancelled} — stop the photo being made and/or forget the ones waiting (all of them when `id` is omitted)

### denoise.clear — Clear Denoise Cache
{} → {deleted, bytes} — delete every cached denoised picture of this library (they are made again when wanted)

### denoise.models.download — Download Denoise Model
{id, acknowledged: true} → {started, from} — fetch a model LightCraft has a pinned address for (see `downloadHost` in the list) in the background over HTTPS with lightcraft-fetch. `acknowledged` must be true: the user has been shown the model's terms and accepted them. It is checked against its size and SHA-256, installed and chosen by itself; `denoise.models.downloads` shows how far it is

### denoise.models.downloadCancel — Cancel Denoise Model Download
{id} → {discarded} — stop a download, or delete a finished one that was not installed

### denoise.models.downloads — Denoise Model Downloads
{} → {running, downloads: [{id, state: running | done | installed | failed | cancelled, bytes, total, error, from}]} — also installs any download that has arrived

### denoise.models.inspect — Inspect Denoise Model
{path} → model terms from an adjacent manifest; never executes the file

### denoise.models.install — Install Denoise Model
{path, acknowledged: true, activate?: true, background?: false} → {installed, model} or {started} — install a denoise model from a file: an .onnx with a denoise-model.json beside it, or an archive LightCraft knows (the darktable `.dtmodel`). `acknowledged` must be true: the user has been shown the model's licence and accepted it. Unless `activate` is false it becomes the model in use

### denoise.models.list — Denoise Models
{} → {dir, productsDir, model, runtime, auto, cacheGb, threads, runOn, models: [{id, name, version, licence{name, commercial, url, notice}, provenance, source, sizeBytes, sha256, tile, known, downloadHost, installed, selected, accepted}]}

### denoise.models.remove — Remove Denoise Model
{id} → {removed, model} — delete an installed model (its cached pictures stay until they are evicted)

### denoise.models.select — Choose Denoise Model
{id: installed model | null} → {model} — null uses the built-in denoiser

### denoise.models.test — Test Denoise Model
{id} → {ok, result} — load an installed model and check it gives sensible pictures; needs the denoise runtime

### denoise.pump — Denoise Pump
{pace?: pause | light | normal | full} → {active, running, queued, ready, generation, downloading} — called every frame by the app: takes in finished work and keeps one photo going

### denoise.queue — Denoise Photos
{ids?: [photoId], scope?: selected | visible | withAmount, retry?: false} → {added, …status} — make the denoised pictures of raw photos that have none, in the background. `retry` tries photos that failed before

### denoise.settings — Denoise Settings
{auto?: bool, cacheGb?: 1..10000, threads?: 1..64 | null, runOn?: auto | gpu | cpu} → the settings — `auto`: make the picture of the photos being looked at that have a Denoise amount; `cacheGb`: how much the cached pictures may take; `threads`: most tiles run at once; `runOn`: where the model runs — `auto` (the default) the graphics card where it is faster than the processor (both timed on this computer when the card is set up), `gpu` the card whenever it can run the model, `cpu` the processor. Setting `runOn` also lets the card be tried again after a set-up that failed or closed LightCraft

### denoise.status — Denoise Status
{id?} → {enabled, model, runtime, productsDir, queued, running: {photo, done, total, seconds} | null, ready, made, auto, runOn, device: {kind: gpu | cpu | pending | none, adapter?, reason?, cardMs?, cpuMs?, fellBack?, remote?: {address, state: pending | unavailable | used | idle | slower | given up, device?, remoteMs?, localMs?, reason?, failures?, lastError?}}, cache: {files, bytes, limitBytes}, generation, photo?: {state: notApplicable | ready | queued | running | failed | idle, …}}

### denoise.toggle — AI Denoise
{id?: photoId, enabled?: bool} → {id, enabled, amount} — turn AI Denoise on (50% initially) or off for one raw photo, independent of selection and Auto Sync; uses the built-in denoiser when no model is chosen

## segment

### segment.model.cancel — Cancel AI Mask Model Download
{} — stop the SAM 3 download (what has arrived is kept, and a new download resumes from it) → {cancelled}

### segment.model.download — Download AI Mask Model
{acknowledged: true} — download the SAM 3 model (about 3.4 GB, Meta's SAM License, not LightCraft's) in the background, from the configured mirrors; only after the user agreed to it. Watch segment.model.status; segment.model.cancel stops it (it resumes later) → {started, installed, downloading}

### segment.model.status — AI Mask Model Status
{} — whether this build has AI masks, whether the SAM 3 model is installed (and where), loaded, busy, and the download's progress → {available, installed, dir, loaded, busy, analyzing, sizeBytes, license, licenseUrl, mirrors, download: {running, done, total, file, error, finished}}

### segment.prepare — Prepare AI Masks
{} — load SAM 3 and analyze the active photo in the background, so Object clicks are instant → {busy}

## focus

### focus.pump — Read Focus Points in the Background
{pace?: pause | light | normal} → {active, running?: {done, total, found}, last?, lookedAt} — cheap to call every frame (the app does): takes in what the background focus-point reader has read and commits it in batches; reads nothing new while paused and rests between files when light. Starts the reader by itself once per library opening when photos are left to look at

## photo

### photo.addToLibrary — Add to My Photos
{ids?} — browsed (Local) photos join the library

### photo.allMetadata — All Metadata
{id?} → {exif: [{group, tag, name, value}], xmp: [{name, value}]} — every EXIF / TIFF / GPS tag of the file and its XMP properties

### photo.analyze — Assisted Culling
{ids?, rejectBelow?: sharpness 0..100, pickBest?: bool, burstGap?: seconds 0..86400 (10), similarity?: 0..1 (0.93)} — score the selected photos (else all in view) for focus (0..100) and clipping, group look-alike shots (signature similarity at least `similarity`) taken at most `burstGap` seconds apart and mark the sharpest of each; optionally reject blurry photos and pick each group's best; one undo step → {photos: [{id, sharpness, clipped, group, best}], groups, rejected, picked}

### photo.autoTagTracklog — Auto-Tag Photos from Tracklog
{path?: GPX file | gpx?: GPX text, ids?, offset?: camera clock's UTC offset for photos whose capture time has no zone (`+02:00`, or hours; default UTC), maxGap?: seconds (600), replace?: bool (also photos that already have GPS), dryRun?: bool} → {tagged, interpolated, nearest, skipped: {noTime, outside, hasGps}, assumedUtc, points, start, end, photos: [{id, gps, match}]} — positions from the track log by capture time; one undo step

### photo.clearLabel — Clear Color Label
{ids?, advance?: bool} — `photo.label` with `none`; without `ids`, the selection moves on when this takes the active photo out of the view

### photo.convertToDng — Convert to DNG
{ids?} — write each raw photo as a lossless DNG next to it (settings embedded) and relink the photo to it; originals are kept → {converted: [{id, path, original}], skipped}

### photo.copyMetadata — Copy Metadata
shortcut: Cmd+Alt+Shift+C
{} — title, caption, copyright (notice, status, usage terms, info URL), creator, location and keywords of the active photo

### photo.cycleFlag — Cycle Flag
shortcut: `
{ids?, advance?: bool} — each photo's own flag: unflagged -> pick -> reject -> unflagged; without `ids`, the selection moves on when this takes the active photo out of the view

### photo.decreaseFlag — Decrease Flag Status
shortcut: Cmd+Down
{ids?, advance?: bool} — pick -> unflagged -> reject (stops at reject); without `ids`, the selection moves on when this takes the active photo out of the view

### photo.decreaseRating — Decrease Rating
{ids?, advance?: bool} — without `ids`, the selection moves on when this takes the active photo out of the view

### photo.delete — Delete Photo
shortcut: Delete
{ids?} — moves to Recently Deleted

### photo.deletePermanently — Delete Permanently
{ids?}

### photo.duplicate — Duplicate
{ids?} — copy each photo's file next to it (`-copy`) and add it with the same settings, metadata and albums (a real file, unlike a virtual copy) → {ids}

### photo.editExternal — Edit Copy for External Editor
{ids?, colorSpace?: adobeRgb (default) | proPhoto | displayP3 | srgb, format?: tiff (default) | psd, bitDepth?: 16 (default) | 8, dir?} — render each selected photo (or `ids`, at most 50) with its edits as `<name>-Edit.tif` (or `.psd`, flat, which PhotoCraft saves back to in place) next to it, add each stacked on its original and select the copies → {path, id, original (the first copy), copies: [{path, id, original}]} (the app then opens them in the external editor)

### photo.flag — Set Flag
{flag: pick|reject|none, ids?, advance?: bool} — without `ids`, the selection moves on when this takes the active photo out of the view

### photo.flipHorizontal — Flip Horizontal
{ids?}

### photo.flipVertical — Flip Vertical
{ids?}

### photo.increaseFlag — Increase Flag Status
shortcut: Cmd+Up
{ids?, advance?: bool} — reject -> unflagged -> pick (stops at pick); without `ids`, the selection moves on when this takes the active photo out of the view

### photo.increaseRating — Increase Rating
{ids?, advance?: bool} — without `ids`, the selection moves on when this takes the active photo out of the view

### photo.inspect — Inspect Photo
{id?}

### photo.label — Set Color Label
{label: red|yellow|green|blue|purple|none, ids?, advance?: bool} — without `ids`, the selection moves on when this takes the active photo out of the view

### photo.moveToFolder — Move to Folder
{folder, ids?} — move the photos' files (default: the selection) with their XMP sidecars into `folder` on disk and relink them; virtual copies follow their master; across volumes the file is copied, verified and only then removed; never overwrites (a name taken in `folder` refuses the whole move); missing/offline and Local photos are refused; one undo step (undo moves them back) → {moved, folder}

### photo.pasteMetadata — Paste Metadata
shortcut: Cmd+Alt+Shift+V
{ids?, fields?: [title|caption|copyright|copyrightStatus|usageTerms|copyrightUrl|creator|location|keywords] (default: all copied)}

### photo.pick — Flag as Pick
shortcut: P
{ids?, advance?: bool} — without `ids`, the selection moves on when this takes the active photo out of the view

### photo.rate — Set Rating
{rating: 0..5, ids?, advance?: bool} — without `ids`, the selection moves on when this takes the active photo out of the view

### photo.readFocusPoints — Read Focus Points
{ids?, wait?: false} → {queued, running, last?: {total, done, found, none, unavailable, bytesRead, seconds, cancelled}} — read the camera's focus point for photos imported before it was read (Sony α1 and A7S III raws and JPEGs), from the few KB of each file that hold it, on a background job with a row in the activity stack. Without `ids`, every photo in the library not looked at yet; with `ids`, those photos, looked at again. Photos that have a point keep it. No undo step and no sidecar write. `wait: true` returns when all are read (scripts)

### photo.readMetadataFromFile — Read Metadata from File
{ids?} — reads each photo's XMP sidecar, or embedded XMP in raw/DNG and JPEG files when no sidecar exists: metadata and develop settings, one undo step; never writes the sidecar, even with auto-write on; JPEG uses the first complete standard XMP APP1 before SOS/EOI, within 16 MiB of headers and 4096 marker/fill steps; an unreadable sidecar fails without embedded fallback → {read, failed, warnings?: [{path, code, profile?, mode?, fields?}]}

### photo.reject — Flag as Reject
shortcut: X
{ids?, advance?: bool} — without `ids`, the selection moves on when this takes the active photo out of the view

### photo.relink — Locate Photo
{id?, path} — point a photo at its file's new location (undo never moves files)

### photo.reload — Reload from Disk
{ids?} — re-read photos whose files changed on disk (e.g. saved by an external editor), or raws shown from their embedded preview that can be decoded now; camera fields the catalog lacks are filled in, and so is the lens data the file carries (an untouched photo then gets its lens correction turned on as import would; an edited one keeps its settings); in the app the files are read in the background (activity row `reload`, cancellable) and the reply is {background: true, count} unless `wait: true` → {reloaded}

### photo.removeRegion — Remove Face Box
{id?, index} — remove one face / pet region (by its position in the photo's regions) from the photo in the catalog; undoable. The XMP sidecar is never rewritten for this, even with auto-write on, so reading the metadata from the file brings the region back

### photo.rename — Rename Photos
{template: e.g. `{date}_{name}`, `Trip-{seq:3}` (tokens: {name} {num} {seq} {seq:N} {date} {date:%Y%m%d} {folder} {camera} {lens} {iso} {rating} {title} {creator} {ext}; photo.renameTokens explains each), start?: first sequence number (1), ids?} — renames the files on disk (sidecars too, never overwriting: collisions get -1, -2…); undoable

### photo.renamePreview — Rename Preview
{template: e.g. `{date}_{name}`, `Trip-{seq:3}` (tokens: {name} {num} {seq} {seq:N} {date} {date:%Y%m%d} {folder} {camera} {lens} {iso} {rating} {title} {creator} {ext}; photo.renameTokens explains each), start?: first sequence number (1), ids?} — renames the files on disk (sidecars too, never overwriting: collisions get -1, -2…); undoable

### photo.renameTokens — Rename Template Tags
{} → {tokens: [{tag, aliases, meaning, example}], dateDirectives: [{directive, meaning}], notes: [..], sample} — the file-name template tags shared by photo.rename, library.import (rename) and app.export (naming); examples are for a sample photo

### photo.restore — Restore
{ids?}

### photo.rotateLeft — Rotate Left
shortcut: Cmd+[
{ids?}

### photo.rotateRight — Rotate Right
shortcut: Cmd+]
{ids?}

### photo.saveMetadataToFile — Save Metadata to File
shortcut: Cmd+S
{ids?} — writes each photo's XMP sidecar (metadata + develop settings) next to the original, merged into an existing one (other apps' data kept; an unreadable one is backed up first) → {written: [path], merged: [path], backups: [{path, backup}], failed}

### photo.setCaptureTime — Edit Capture Time
{ids?, time?: `2026-09-30T14:05:00` (the active photo gets it, the others shift by the same amount), each?: bool (every photo gets `time`), shift?: seconds, hours?: time-zone shift in hours} → {changed, captured: [..], unreadable: photos skipped because their capture time can't be read}

### photo.setMeta — Edit Info
{ids?, title?, caption?, altText?, extendedDescription?, copyright?, copyrightStatus?: unknown|copyrighted|publicDomain, usageTerms?, copyrightUrl?, creator?, location?, city?, state?, country?, gps?: "lat, lon" | [lat, lon] | null, keywords?: [..], addKeywords?: [..], removeKeywords?: [..]}

### photo.setRegion — Resize Face Box
{id?, index, rect: {x0, y0, x1, y1}} — set one face / pet region's box (normalized, in the photo's upright frame; clamped to the photo, at least 0.5 % each way) in the catalog; undoable. Like photo.removeRegion it never rewrites the XMP sidecar

### photo.smartPreview — Smart Preview Status
{id?} → {smartPreview: bool, originalOnline: bool}

### photo.unflag — Unflag
shortcut: U
{ids?, advance?: bool} — without `ids`, the selection moves on when this takes the active photo out of the view

### photo.virtualCopy — Create Virtual Copy
shortcut: Cmd+'
{ids?, name?} → {ids: [new photo ids]} — a new catalog entry sharing the original file, with independent settings; stacked with its original and named `name` or "Copy N"
