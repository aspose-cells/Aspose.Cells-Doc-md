---
title: Node.js ile C++ kullanarak Workbook da HTML yüklerken Sütun ve Satırları Otomatik Sığdırma
linktitle: Çalışma Kitabında HTML yüklenirken Sütunları ve Satırlar Otomatik Uydurma
type: docs
weight: 120
url: /tr/nodejs-cpp/autofit-columns-and-rows-while-loading-html-in-workbook/
description: Aspose.Cells for Node.js via C++ kullanarak Workbook içinde HTML yüklerken sütun ve satırları otomatik sığdırmayı öğrenin.
---

## **Olası Kullanım Senaryoları**

HTML dosyasını Workbook nesnesi içine yüklerken sütun ve satırları otomatik sığdırabilirsiniz. Bu amaçla [**HtmlLoadOptions.getAutoFitColsAndRows()**](https://reference.aspose.com/cells/nodejs-cpp/htmlloadoptions/#getAutoFitColsAndRows--) özelliğini **true** olarak ayarlayın.

## **HTML yüklenirken Sütunları ve Satırları Otomatik Uydurma**

Aşağıdaki örnek kod, ilk olarak örnek HTML'yi herhangi bir yükleme seçeneği olmadan Workbook'a yükler ve XLSX formatında kaydeder. Daha sonra tekrar örnek HTML'yi Workbook'a yükler, bu sefer [**HtmlLoadOptions.getAutoFitColsAndRows()**](https://reference.aspose.com/cells/nodejs-cpp/htmlloadoptions/#getAutoFitColsAndRows--) özelliğini **true** yapar ve XLSX formatında kaydeder. Lütfen her iki çıktı Excel dosyasını indirin: [AutoFitColsAndRows Olmadan Çıktı Excel Dosyası](outputWithout_AutoFitColsAndRows.xlsx) ve [AutoFitColsAndRows ile Çıktı Excel Dosyası](outputWith_AutoFitColsAndRows.xlsx). Aşağıdaki ekran görüntüsü [**HtmlLoadOptions.getAutoFitColsAndRows()**](https://reference.aspose.com/cells/nodejs-cpp/htmlloadoptions/#getAutoFitColsAndRows--) özelliğinin her iki çıktı Excel dosyasına etkisini gösterir.

![todo:image_alt_text](autofit-columns-and-rows-while-loading-html-in-workbook_1.png)

## **Örnek Kod**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Sample HTML.
const sampleHtml = "<html><body><table><tr><td>This is sample text.</td><td>Some text.</td></tr><tr><td>This is another sample text.</td><td>Some text.</td></tr></table></body></html>";

// Load HTML string into memory stream.
const ms = Uint8Array.from(sampleHtml, c => c.charCodeAt(0));

// Load memory stream into workbook.
let wb = new AsposeCells.Workbook(ms);

// Save the workbook in xlsx format.
wb.save(path.join(dataDir, "outputWithout_AutoFitColsAndRows.xlsx"));

// Specify the HTMLLoadOptions and set AutoFitColsAndRows = true.
const opts = new AsposeCells.HtmlLoadOptions();
opts.setAutoFitColsAndRows(true);

// Load memory stream into workbook with the above HTMLLoadOptions.
wb = new AsposeCells.Workbook(ms, opts);

// Save the workbook in xlsx format.
wb.save(path.join(dataDir, "outputWith_AutoFitColsAndRows.xlsx"));
```

