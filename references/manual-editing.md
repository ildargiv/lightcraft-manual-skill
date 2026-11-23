# Рецепты ручной правки

Числа — **стартовые точки**, не догма. Ставить их руками (`set_develop`), смотреть
`render_preview` и подправлять по кадру. Никаких `develop.auto`, `preset.apply`,
`crop.autoStraighten` (исключение — явная просьба пользователя).

## 0. База для любого raw

```json
{"wb":{"mode":"asShot"},
 "light":{"exposure":0.0,"contrast":10,"highlights":-35,"shadows":25,"whites":8,"blacks":-10},
 "effects":{"texture":6,"clarity":6,"dehaze":0},
 "color":{"vibrance":12,"saturation":0},
 "detail":{"sharpenAmount":40,"sharpenRadius":1.0,"sharpenDetail":25,
           "sharpenMasking":40,"nrColor":20,"nrLuminance":0},
 "optics":{"lens_profile":true,"profile_distortion":100,"profile_vignetting":100,
           "remove_ca":true}}
```

Что смотреть: небо не «залито», тени не серые, на краях нет радужной каймы.

## 1. Пейзаж, золотой час

```
exposure +0.15 … +0.35 | contrast +12…+18 | highlights −45…−65 | shadows +25…+40
whites +8…+15 | blacks −10…−18
temp +200…+500 K к тёплому (по интерактиву), tint −3…+5
vibrance +15…+22 | saturation 0…+5
texture +8…+12 | clarity +8…+12 | dehaze +5…+12
mixer.orange.sat +8, mixer.yellow.sat +6, mixer.blue.lum −8
grading.highlights {hue:40, sat:12, lum:+3}, grading.shadows {hue:210, sat:8, lum:−2}
sharpenAmount 45, sharpenMasking 40
```
Маски: небо — linear `(0.5,0.45) → (0.5,0.0)` с `exposure −0.25, dehaze +8, temp −8`;
земля — radial с `exposure +0.15, texture +10`.

## 2. Контровой свет / окно за спиной

```
exposure +0.3…+0.7 | highlights −60…−80 | shadows +35…+50 | whites +12…+20
 blacks −8…−15 | contrast +8…+14
curve.highlights −10, curve.lights +8, curve.darks −6
effects.dehaze +8…+15 (если дымка), clarity +6
маска по светам: luminanceRange lo 0.65 hi 1.0, exposure −0.5, highlights −40
```
Если есть настоящий запас в светах — сразу HDR-конвейер (`hdr.md`).

## 3. Синий час / город ночью

```
exposure +0.4…+0.9 (или +1.2 на raw) | contrast +15…+25 | highlights −40…−60
shadows +15…+25 | whites +5…+10 | blacks −15…−25
temp 3800…4800 K, tint +3…+10
vibrance +10…+18 | mixer.blue.sat +12, mixer.aqua.sat +8, mixer.orange.lum +8
grading.shadows {hue:215, sat:18, lum:−5}, highlights {hue:35, sat:14, lum:+4}
nrLuminance 20…35, nrColor 25…35, sharpenMasking 55
```
Не поднимать тени выше +35 — поплывёт шум и цвет неба.

## 4. Туман / мягкий свет

```
exposure +0.3…+0.6 | highlights −15…−30 | shadows +20…+35 | whites +10…+20
 blacks +5…+12 (поднять deepest shadows!) | contrast −5…−15
dehaze −10…−25 (усилить атмосферу) или +10…+20 (прояснить), clarity −5…+5
texture +5…+10 | saturation −5…+5 | vibrance +8
grading.highlights {hue:200…220, sat:6}
```

## 5. Портрет, естественный свет

```
exposure +0.1…+0.3 | highlights −25…−40 | shadows +15…+25 | whites +5…+10
 blacks −5…−10 | contrast +5…+10
temp — по коже, tint +2…+6
texture −8…−15 (сглаживает), clarity −5…−10, dehaze 0
vibrance +8…+14 | mixer.orange.sat +5, mixer.red.sat +3, mixer.yellow.lum +4
grading.highlights {hue:35, sat:8, lum:+3}, blending 60
sharpenAmount 25…35, sharpenMasking 60…80, nrLuminance 10…20
радиальная маска на лицо: feather 0.5, exposure +0.15, texture −10, sharpness −15
spot.add {mode:"heal"} на отдельные прыщики/волоски — вручную по координатам
```
Никогда `spot.findBlemishes` и `develop.autoBwMix` без вопроса.

## 6. Светлый студийный портрет

```
exposure +0.3…+0.6, highlights −30, shadows +20, whites +15, blacks +5
contrast +5, clarity −8, texture −10, vibrance +8
mixer.orange.lum +6, mixer.red.lum +4
sharpenAmount 30, sharpenMasking 70
```
Проверять уши/нос на пересвет: `whites` не выше +20, если кожа «мел».

## 7. Ч/б вручную

```
develop.treatment {bw:true}  // или settings.treatment:"bw"
light.contrast +20…+35, highlights −30, shadows +20, whites +12, blacks −15
bw_mix.red +15, bw_mix.orange +10, bw_mix.yellow 0,
bw_mix.green −10, bw_mix.blue −25  // классический красный фильтр для неба
effects.clarity +12…+20, texture +8
curve.master [[0,0],[0.25,0.18],[0.5,0.5],[0.75,0.82],[1,1]]
grading.highlights {hue:40, sat:10}, grading.shadows {hue:285, sat:12} — селен/сепия
grain.amount 12…20, grain.size 25, grain.roughness 50  // процесс V7, зерно «плёночное»
```
`process` < 7 даёт старое зерно; менять tylko по просьбе.

## 8. Еда / предметка

```
exposure +0.2…+0.4, highlights −30…−45, shadows +10…+20, contrast +8…+12
whites +8, blacks −8
temp +150…+300 K, vibrance +12…+18, mixer.red.sat +8, mixer.orange.sat +8
texture +6…+10, clarity +8…+12, dehaze +3…+6
radial center (0.5,0.5) rx 0.45 ry 0.45 feather 0.6: exposure +0.15, clarity +8
```
Фон приглушить: вторая radial-маска на край кадра с `exposure −0.2, blur` (или lens blur).

## 9. Звёзды / ночное небо

```
exposure +0.8…+1.5, highlights −20, shadows +15, contrast +15
temp 3600…4200 K, tint −5…+5
nrLuminance 20…30, nrColor 30…40, nrDetail 40
sharpenAmount 20, sharpenMasking 70
effects.dehaze +10, clarity +10
```
Не ставить `super_resolution` — это AI-апскейл, не ручная правка.

## 10. Снег / пляж (защита белого)

```
exposure −0.2…−0.5, highlights −50…−70, whites −10…−20, blacks +5…+10
contrast +10, vibrance +8, mixer.blue.sat +8
temp по снегу: 5500…6500 K, tint −3…+3
```
Белый должен остаться фактурным: смотреть `render_preview` на 100 % (size 1600).

## 11. Интерьер / недвижимость

```
optics.lens_profile:true, optics.distortion −10…−20 (выпрямить бочку)
geometry.horizontal −10…+10, geometry.vertical +10…+25 (вертикали стен),
 geometry.scale 102…108 (заполнить после трансформации)
exposure +0.3…+0.6, highlights −40, shadows +35…+45, whites +10, blacks −10
temp — нейтрализовать смешанный свет, tint 0…+5
vibrance +8, clarity +5…+10, dehaze +5
```
Край кадра после `geometry` может «поехать»: кроп `crop {rect:[0.02,0.02,0.98,0.98]}`.

## 12. Повтор пресета руками: Teal & Orange

Из `references/presets.md` (`lc.teal-orange`) — просто ставим его поля вручную:

```json
{"color":{"vibrance":12},
 "light":{"contrast":14},
 "grading":{"balance":10, "blending":50,
            "highlights":{"hue":35,"lum":0,"sat":22},
            "shadows":{"hue":195,"lum":0,"sat":28}},
 "treatment":"color"}
```

Затем доводим руками под кадр: тёплые блики и холодные тени уже заданы, осталось свет.

## Как проверять себя

- Есть ли детали в самых светлых и тёмных областях? `highlights`/`shadows` в минус/плюс.
- Кожа не оранжевая? `mixer.orange.sat`.
- Небо не фиолетовое? `temp`, `mixer.blue.hue`.
- Горизонт ровный? `crop {angle: ±0.5…3}` вместо автовыравнивания.
- Кроп: `crop {rect:[x0,y0,x1,y1]}` — от левого верхнего угла, 0..1.
- Сомневаешься — `history.list`, `history.restore`, `edit.undo`.

## Ошибки, которые портят кадр

- `contrast` раньше экспозиции — чёрные провалы.
- `clarity` +25 на портрете — «грязная» кожа.
- `sharpenAmount` 100 и `sharpenMasking` 0 — ореолы на ветках.
- `highlights` −100 + `shadows` +100 — PLAСТИК, особенно на JPEG.
- Правка до профиля объектива — маски уедут после коррекции дисторсии (у масок
  `on_photo:true`, но экстремальная дисторсия всё равно сдвигает визуальный край).
