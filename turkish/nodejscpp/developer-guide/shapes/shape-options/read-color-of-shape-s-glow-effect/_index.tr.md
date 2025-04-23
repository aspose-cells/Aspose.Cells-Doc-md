---
title: Node.js kullanarak Şekil nin Parlaklık Efektinin Rengini Oku
linktitle: Şeklin Parlama Etkisinin Rengini Oku
type: docs
weight: 330
url: /tr/nodejs-cpp/read-color-of-shape-s-glow-effect/
description: Aspose.Cells for Node.js via C++ kullanarak bir şeklin parlaklık efektinin rengini nasıl okuyacağınızı öğrenin. 
---

## Olası Kullanım Senaryoları

Bir şeklin parlaklık efektinin rengini okumak istiyorsanız, lütfen [**Shape.getColor()**](https://reference.aspose.com/cells/nodejs-cpp/gloweffect/#getColor--) özelliğini kullanın. Bu, şeklin parlaklık efektinin rengini ilişkili çeşitli özellikleri bulmanıza yardımcı olacaktır.

## Şeklin Parlama Efektinin Rengini Oku

Lütfen aşağıdaki örnek kodu ve [kaynak excel dosyasını](22774108.xlsx) ve başvurunuz için konsol çıktısını görün. Aşağıdaki ekran görüntüsü, Microsoft Excel'de görüldüğünde kaynak excel dosyasının parlama efektini gösterir.

![todo:image_alt_text](read-color-of-shape-s-glow-effect_1.png)

## Node.js kodu ile şeklin parlaklık efektinin rengini okuma

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Read the source excel file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "sourceGlowEffectColor.xlsx"));

// Access the first worksheet
const sheet = workbook.getWorksheets().get(0);

// Access the shape
const shape = sheet.getShapes().get(0);

// Read the glow effect color and its various properties
const effect = shape.getGlow();
const color = effect.getColor();
console.log("Color: " + color.getColor());
console.log("ColorIndex: " + color.getColorIndex());
console.log("IsShapeColor: " + color.isShapeColor());
console.log("Transparency: " + color.getTransparency());
console.log("Type: " + color.getType());
```

## Konsol Çıkışı

Yukarıdaki örnek kodun, sağlanan [kaynak excel dosyası](22774108.xlsx) ile birlikte çalıştırıldığında konsol çıktısı. İşte yukarıdaki örnek kodun konsol çıktısı.

{{< highlight javascript >}}

Color: Color [A=222, R=255, G=0, B=0]

ColorIndex: 16711672

IsShapeColor: True

Transparency: 0.13

Type: RGB

{{< /highlight >}}
