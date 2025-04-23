---
title: Node.js ile C++ üzerinden Çalışma Sayfasına WordArt Su İşareti ekleme
linktitle: WordArt ı Yönetme
type: docs
weight: 180
url: /tr/nodejs-cpp/add-wordart-watermark-to-worksheet/
description: Aspose.Cells for Node.js via C++ kullanarak WordArt ı bir çalışma sayfasının arka planında su işareti olarak eklemeyi öğrenin.
---

{{% alert color="primary" %}} 

WordArt'ı kullanarak elektronik tablolara özel metin efektleri ekleyin. Örneğin, başlığı dosyanın üst kısmına uzatın, metni süsleyin ve metni önceden ayarlanmış bir şekle uygun hale getirin veya metni bir Excel çalışma sayfasına arka plan filigranı olarak uygulayın. WordArt, elektronik tablolara dekorasyon eklemek için taşıyabileceğiniz bir nesne haline gelir.

{{% /alert %}} 

Aşağıdaki örnek, bir çalışma sayfası için arka plan filigranı olarak bir WordArt şekli eklemenin nasıl yapıldığını göstermektedir.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiate a new Workbook
const workbook = new AsposeCells.Workbook();

// Get the first default sheet
const sheet = workbook.getWorksheets().get(0);

// Add Watermark
const wordart = sheet.getShapes().addTextEffect(AsposeCells.MsoPresetTextEffect.TextEffect1,
"CONFIDENTIAL", "Arial Black", 50, false, true, 18, 8, 1, 1, 130, 800);

// Get the fill format of the word art
const wordArtFormat = wordart.getFill();            

// Set the transparency
wordArtFormat.setTransparency(0.9);

// Make the line invisible
const lineFormat = wordart.getLine();          

const outputFilePath = path.join(dataDir, "Watermark_Test.out.xls");
// Save the file
workbook.save(outputFilePath);
```

## **Gelişmiş Konular**
- [Dahili Stillerle Word Art Metni Ekleme](/cells/tr/nodejs-cpp/add-word-art-text-with-built-in-styles/)
- [WordArt Filigranı Kilitleme](/cells/tr/nodejs-cpp/locking-wordart-watermark/)
- [Metin şeklinin metnine önceden ayarlanmış WordArt stili ayarlayın](/cells/tr/nodejs-cpp/set-preset-wordart-style-to-the-text-of-the-shape/)
