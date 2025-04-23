---
title: Sütun Genişliğini Em veya Yüzde gibi Ölçeklenebilir Birim Olarak Ayarlama Node.js ve C++ ile
linktitle: Sütun Genişliğini Em veya Yüzde gibi Ölçeklenebilir Birim Olarak Ayarlama
type: docs
weight: 130
url: /tr/nodejs-cpp/set-column-width-to-scalable-unit-like-em-or-percent/
description: Aspose.Cells for Node.js via C++ te sütun genişliğini em veya yüzde gibi ölçeklenebilir birimlere ayarlamayı öğrenin. Oluşturulan HTML tablolarının sunumunu geliştirin.
---

Bir elektronik tabloyu HTML dosyasına dönüştürmek çok yaygındır. Sütunların boyutu "pt" cinsinden tanımlanır, bu birçok durumda işe yarar. Ancak, bu sabit boyut gerekmeyebilir. Örneğin, bir konteyner panel genişliği 600px ise ve bu HTML sayfası gösteriliyorsa, oluşturulan tablonun genişliği büyükse yatay kaydırıcı alabilirsiniz. Bu sabit boyutun em veya yüzde gibi ölçeklenebilir bir birime değiştirilmesi gerekebilir. Aşağıdaki örnek kod, [**HtmlSaveOptions.getWidthScalable()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getWidthScalable--) değeri **true** olarak ayarlandığında ölçeklenebilir genişlik oluşturmak için kullanılabilir.

Örnek kaynak dosyası ve çıktı dosyalarını aşağıdaki bağlantılardan indirebilirsiniz:

[sampleForScalableColumns.xlsx](73990150.xlsx)

[outsampleForScalableColumns.zip](73990151.zip)

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Load sample source file
const dataDir = path.join(__dirname, "data");
const sourceFilePath = path.join(dataDir, "sampleForScalableColumns.xlsx");
const workbook = new AsposeCells.Workbook(sourceFilePath);

// Specify Html Save Options
const options = new AsposeCells.HtmlSaveOptions();

// Set the property for scalable width
options.setWidthScalable(true);

// Specify image save format
options.setExportImagesAsBase64(true);

// Save the workbook in Html format with specified Html Save Options
const outputFilePath = path.join(dataDir, "outsampleForScalableColumns.html");
workbook.save(outputFilePath, options);
```
