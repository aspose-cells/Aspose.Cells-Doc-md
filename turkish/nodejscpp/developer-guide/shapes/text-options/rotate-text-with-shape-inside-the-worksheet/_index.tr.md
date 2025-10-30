---
title: Çalışma Sayfası İçinde Şekil ile Metni Döndürme Node.js kullanarak C++ ile
linktitle: Çalışma Sayfası İçindeki Şekil ile Metni Döndürme
type: docs
weight: 1300
url: /tr/nodejs-cpp/rotate-text-with-shape-inside-the-worksheet/
description: Aspose.Cells for Node.js via C++ kullanarak Excel çalışma sayfasında şekil ile metni nasıl döndüreceğinizi öğrenin.
---

## **Olası Kullanım Senaryoları**

Microsoft Excel kullanarak herhangi bir şeklin içine metin ekleyebilirsiniz. Çok eski Microsoft Excel 2003 kullanarak şekil eklerseniz, metin şekille birlikte dönmez. Ancak, 2007, 2010, 2013 veya 2016 gibi daha yeni sürümler kullanılarak şekil eklerseniz, metin şekille birlikte döner. Metnin şekille birlikte dönüp dönmeyeceğini [**ShapeTextAlignment.getRotateTextWithShape()**](https://reference.aspose.com/cells/nodejs-cpp/shapetextalignment/#getRotateTextWithShape--) özelliğini kullanarak kontrol edebilirsiniz. Varsayılan değeri **true** olan bu özellik, metnin şekille birlikte döneceği anlamına gelir, ancak **false** olarak ayarlarsanız, metin şekille birlikte dönmez.

## **Çalışma Sayfası İçindeki Şekil ile Metni Döndürme**

Aşağıdaki örnek kod, üçgen şekli içeren ve metni şekille birlikte dönen [örnek Excel dosyasını](64716896.xlsx) yükler. Eğer örnek Excel dosyasını Microsoft Excel'de açarsanız ve üçgen şekli döndürürseniz, metin de onunla birlikte döner. Kod daha sonra [**ShapeTextAlignment.getRotateTextWithShape()**](https://reference.aspose.com/cells/nodejs-cpp/shapetextalignment/#getRotateTextWithShape--) özelliğini **false** yapar ve [çıktı Excel dosyasına](64716897.xlsx) kaydeder. Şimdi çıktı dosyasını Microsoft Excel'de açıp üçgen şekli döndürürseniz, metin onunla birlikte dönmez. Aşağıdaki ekran görüntüsü, kodun örnek Excel dosyasına etkisini gösterir.

![todo:image_alt_text](rotate-text-with-shape-inside-the-worksheet_1.png)

## **Örnek Kod**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const sourceFilePath = path.join(dataDir, "sampleRotateTextWithShapeInsideWorksheet.xlsx");

// Load sample Excel file.
const workbook = new AsposeCells.Workbook(sourceFilePath);

// Access first worksheet.
const worksheet = workbook.getWorksheets().get(0);

// Access cell B4 and add message inside it.
const cellB4 = worksheet.getCells().get("B4");
cellB4.putValue("Text is not rotating with shape because RotateTextWithShape is false.");

// Access first shape.
const shape = worksheet.getShapes().get(0);

// Access shape text alignment.
const shapeTextAlignment = shape.getTextBody().getTextAlignment();

// Do not rotate text with shape by setting RotateTextWithShape as false.
shapeTextAlignment.setRotateTextWithShape(false);

// Save the output Excel file.
const outputFilePath = path.join(dataDir, "outputRotateTextWithShapeInsideWorksheet.xlsx");
workbook.save(outputFilePath);
```
{{< app/cells/assistant language="nodejs-cpp" >}}
