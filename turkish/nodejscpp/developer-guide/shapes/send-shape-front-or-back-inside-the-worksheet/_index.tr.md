---
title: Shape Ön veya Arka Plan Sendesiyle Tekne İçinde Node.js kullanımıyla şekil gönderme
linktitle: Çalışma sayfası içindeki Şekil Önüne veya Arkasına Gönderme
type: docs
weight: 3400
url: /tr/nodejs-cpp/send-shape-front-or-back-inside-the-worksheet/
description: Aspose.Cells for Node.js via C++ kullanarak çalışma sayfasında bir şekli öne veya arkaya göndermeyi öğrenin. 
---

## **Olası Kullanım Senaryoları**

Birden fazla şeklin aynı konumda bulunduğu durumlarda, görünürlükleri Z sırasına göre belirlenir. Aspose.Cells [**Shape.toFrontOrBack()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#toFrontOrBack-number-) metodunu sağlar, bu da şeklin Z sırasını değiştirir. Bir şekli arkaya göndermek için negatif bir sayı kullanırsınız, örneğin -1, -2, -3, vb., ve öne getirmek için pozitif bir sayı kullanırsınız, örneğin 1, 2, 3, vb.

## **Çalışma Sayfası İçinde Şekil Önüne veya Arkasına Gönderme**

Aşağıdaki örnek kod, [**Shape.toFrontOrBack()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#toFrontOrBack-number-) metodunun kullanımını açıklar. Kodda kullanılan [örnek Excel dosyasını](50528330.xlsx) ve bunun oluşturduğu [çıktı Excel dosyasını](50528331.xlsx) görebilirsiniz. Ekran görüntüsü kodun çalıştırılmasıyla sample Excel dosyasındaki etkisini gösterir.

![todo:image_alt_text](send-shape-front-or-back-inside-the-worksheet_1.png)

## **Örnek Kod**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const sourceFilePath = path.join(dataDir, "sampleToFrontOrBack.xlsx");

// Load source Excel file
const workbook = new AsposeCells.Workbook(sourceFilePath);

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access first and fourth shape
const shape1 = worksheet.getShapes().get(0);
const shape4 = worksheet.getShapes().get(3);

// Print the Z-Order position of the shape
console.log("Z-Order Shape 1: " + shape1.getZOrderPosition());

// Send this shape to front
shape1.toFrontOrBack(2);

// Print the Z-Order position of the shape
console.log("Z-Order Shape 4: " + shape4.getZOrderPosition());

// Send this shape to back
shape4.toFrontOrBack(-2);

// Save the output Excel file
const outputFilePath = path.join(dataDir, "outputToFrontOrBack.xlsx");
workbook.save(outputFilePath);
```
