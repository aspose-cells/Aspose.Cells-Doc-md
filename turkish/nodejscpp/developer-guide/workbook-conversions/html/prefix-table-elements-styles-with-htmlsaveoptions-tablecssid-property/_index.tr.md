---
title: Node.js kullanarak C++ ile HtmlSaveOptions.TableCssId özelliği ile tablo elementlerinin stillerine önek ekleme
linktitle: HtmlSaveOptions.TableCssId özelliği ile Tablo Öğeleri Stillerini Ön Eklemek
type: docs
weight: 110
url: /tr/nodejs-cpp/prefix-table-elements-styles-with-htmlsaveoptions-tablecssid-property/
description: Aspose.Cells for Node.js via C++ kullanarak HTML de tablo elementleri stillerini öneklemeyi öğrenin. 
---

## **Olası Kullanım Senaryoları**

Aspose.Cells, tablo ögeleri stillerine [**HtmlSaveOptions.getTableCssId()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getTableCssId--) özelliği ile önek eklemenize izin verir. Diyelim ki bu özelliği **MyTest_TableCssId** gibi bir değere ayarlarsanız, aşağıdaki gibi tablo elementleri stillerini bulacaksınız:

{{< highlight javascript >}}
 table#MyTest_TableCssId

#MyTest_TableCssId tr

#MyTest_TableCssId col

#MyTest_TableCssId br

etc.
{{< /highlight >}}

Aşağıdaki ekran görüntüsü, çıktı HTML'sine [**HtmlSaveOptions.getTableCssId()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getTableCssId--) özelliğinin kullanılmasının etkisini gösterir.

![todo:image_alt_text](prefix-table-elements-styles-with-htmlsaveoptions-tablecssid-property_1.png)

## **HtmlSaveOptions.TableCssId özelliği ile Tablo Öğeleri Stillerini Ön Eklemek**

Aşağıdaki örnek kod, [**HtmlSaveOptions.getTableCssId()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getTableCssId--) özelliğinin kullanımını gösterir. Referans için kod tarafından oluşturulan [çıktı HTML'si](60489790.zip)'ni inceleyin.

## **Örnek Kod**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");

// Create workbook object
const wb = new AsposeCells.Workbook();

// Access first worksheet
const ws = wb.getWorksheets().get(0);

// Access cell B5 and put value inside it
const cell = ws.getCells().get("B5");
cell.putValue("This is some text.");

// Set the style of the cell - font color is Red
const st = cell.getStyle();
st.getFont().setColor(AsposeCells.Color.Red);
cell.setStyle(st);

// Specify html save options - specify table css id
const opts = new AsposeCells.HtmlSaveOptions();
opts.setTableCssId("MyTest_TableCssId");

// Save the workbook in html
wb.save("outputTableCssId.html", opts);
```
