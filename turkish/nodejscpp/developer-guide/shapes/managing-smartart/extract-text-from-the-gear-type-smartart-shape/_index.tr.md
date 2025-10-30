---
title: C++ ile Node.js kullanarak Gear Tipi SmartArt Şekilinden Metin Çıkarımı
linktitle: Dişli Türü Akıllı Sanat Şeklinden Metin Ayıklama
type: docs
weight: 500
url: /tr/nodejs-cpp/extract-text-from-the-gear-type-smartart-shape/
description: Aspose.Cells for Node.js via C++ kullanarak Gear Tipi SmartArt Şekilinden metin çıkarmayı öğrenin.
---

## **Olası Kullanım Senaryoları**

Aspose.Cells, Gear Tipi Smart Art Şekilinden metin çıkarabilir. Bunun için önce Smart Art Şekli [**Shape.getResultOfSmartArt()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getResultOfSmartArt--) yöntemi kullanılarak Grup Şekline dönüştürülmelidir. Ardından, [**GroupShape.getGroupedShapes()**](https://reference.aspose.com/cells/nodejs-cpp/groupshape/#getGroupedShapes--) yöntemi kullanılarak Gruplamadaki tüm Bireysel Şekillerin dizisi alınır. Son olarak, tüm Bireysel Şekilleri birer birer döngüyle yineleyerek ve [**Shape.getText()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getText--) özelliğiyle metinlerini çıkarabilirsiniz.

## **Dişli Türü Akıllı Sanat Şeklinden Metin Ayıklama**

Aşağıdaki örnek kod, Dişli Türü Akıllı Sanat Şeklini içeren [örnek Excel dosyasını](67338483.xlsx) yükler. Daha sonra yukarıda tartışıldığı gibi, bireysel şekillerinden metin çıkarır. Lütfen aşağıdaki kodun konsol çıktısına bakınız.

## **Örnek Kod**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleExtractTextFromGearTypeSmartArtShape.xlsx");

// Load sample Excel file containing gear type smart art shape.
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet.
const worksheet = workbook.getWorksheets().get(0);

// Access first shape.
const shape = worksheet.getShapes().get(0);

// Get the result of gear type smart art shape in the form of group shape.
const groupShape = shape.getResultOfSmartArt();

// Get the list of individual shapes consisting of group shape.
const shapes = groupShape.getGroupedShapes();

// Extract the text of gear type shapes and print them on console.
for (let i = 0; i < shapes.length; i++) {
const s = shapes[i];

if (s.getType() === AsposeCells.AutoShapeType.Gear9 || s.getType() === AsposeCells.AutoShapeType.Gear6) {
console.log("Gear Type Shape Text: " + s.getText());
}
}
```

## **Konsol Çıktısı**

{{< highlight javascript >}}

Gear Type Shape Text: Nice

Gear Type Shape Text: Good

Gear Type Shape Text: Excellent

{{< /highlight >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
