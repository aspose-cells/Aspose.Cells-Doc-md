---
title: Node.js üzerinden C++ kullanarak şekil metnine ön ayar WordArt stili ayarlayın
linktitle: Önceden Ayarlanmış Kelime Sanatı Stilini Şeklin Metni Olarak Ayarla
type: docs
weight: 280
url: /tr/nodejs-cpp/set-preset-wordart-style-to-the-text-of-the-shape/
description: Aspose.Cells for Node.js via C++ kullanarak şekil metnine ön ayar WordArt stili ayarlamayı öğrenin.
---

## **Olası Kullanım Senaryoları**
Aspose.Cells for Node.js via C++ kullanarak şeklin metnine ön ayar WordArt stili ayarlayabilirsiniz. Bu amaçla [FontSetting.setWordArtStyle(PresetWordArtStyle)](https://reference.aspose.com/cells/nodejs-cpp/fontsetting/#setWordArtStyle-presetwordartstyle-) veya [FontSettingCollection.setWordArtStyle(PresetWordArtStyle)](https://reference.aspose.com/cells/nodejs-cpp/fontsettingcollection/#setWordArtStyle-presetwordartstyle-) metodunu kullanın.

## **Metin şeklinin metnine önceden ayarlanmış WordArt stili ayarlayın**
Aşağıdaki örnek kod, bir metin kutusu oluşturur ve içine metin ekler, ardından metnin ön ayar WordArt stilini [FontSetting.setWordArtStyle(PresetWordArtStyle)](https://reference.aspose.com/cells/nodejs-cpp/fontsetting/#setWordArtStyle-presetwordartstyle-) yöntemiyle ayarlar. Bu, Microsoft Excel'de [çıktı excel dosyasının](5115445.xlsx) nasıl göründüğünü gösterir.

![todo:image_alt_text](set-preset-wordart-style-to-the-text-of-the-shape_1.png)

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const outputDir = path.join(__dirname, "output");

// Create workbook object
const workbook = new AsposeCells.Workbook();

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Create a textbox with some text
const textbox = worksheet.getShapes().addTextBox(0, 0, 0, 0, 100, 700);
textbox.setText("Aspose File Format APIs");
textbox.getFont().setSize(44);

// Sets preset WordArt style to the text of the shape.
const fntSetting = textbox.getRichFormattings()[0];
fntSetting.setWordArtStyle(AsposeCells.PresetWordArtStyle.WordArtStyle3);

// Save the workbook in xlsx format
workbook.save(outputDir + "outputSetPresetWordArtStyle.xlsx");
```
{{< app/cells/assistant language="nodejs-cpp" >}}
