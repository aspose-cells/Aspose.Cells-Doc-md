---
title: Hücreleri XML Map Öğelerine Bağlama Node.js ve C++ ile
linktitle: Hücreleri XML Haritası Öğelerine Bağla
type: docs
weight: 50
url: /tr/nodejs-cpp/link-cells-to-xml-map-elements/
---

## **Olası Kullanım Senaryoları**

 Hücrelerinizi XML Map öğelerine bağlamak için Aspose.Cells for Node.js via C++ kullanabilirsiniz. Lütfen bunun için [**Cells.linkToXmlMap(string, number, number, string)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#linkToXmlMap-string-number-number-string-) metodunu kullanın.

## **Hücreleri XML Haritası Elemanlarına Bağla**

Aşağıdaki örnek kod, XML Haritası içeren [kaynak excel dosyasını](5115471.xlsx) yükler ve ardından A1, B2, C3, D4, E5 ve F6 hücrelerini sırasıyla XML Haritası öğeleri FIELD1, FIELD2, FIELD4, FIELD5, FIELD7 ve FIELD8 ile bağlar ve daha sonra kitabı [çıktı excel dosyası](5115467.xlsx) olarak kaydeder.

[Çıktı excel dosyasını](5115467.xlsx) açarsanız ve Geliştirici > Kaynak düğmesine tıklarsanız, hücrelerin XML Haritası öğelerine bağlandığını ve bunların Microsoft Excel tarafından aşağıdaki gibi vurgulandığını göreceksiniz.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Load sample workbook
const workbook = new AsposeCells.Workbook(path.join(dataDir, "sample-xml-map.xlsx"));

// Access the Xml Map inside it
const map = workbook.getWorksheets().getXmlMaps().get(0);

// Access first worksheet
const ws = workbook.getWorksheets().get(0);

// Map FIELD1 and FIELD2 to cell A1 and B2
ws.getCells().linkToXmlMap(map.getName(), 0, 0, "/root/row/FIELD1");
ws.getCells().linkToXmlMap(map.getName(), 1, 1, "/root/row/FIELD2");

// Map FIELD4 and FIELD5 to cell C3 and D4
ws.getCells().linkToXmlMap(map.getName(), 2, 2, "/root/row/FIELD4");
ws.getCells().linkToXmlMap(map.getName(), 3, 3, "/root/row/FIELD5");

// Map FIELD7 and FIELD8 to cell E5 and F6
ws.getCells().linkToXmlMap(map.getName(), 4, 4, "/root/row/FIELD7");
ws.getCells().linkToXmlMap(map.getName(), 5, 5, "/root/row/FIELD8");

// Save the workbook in xlsx format
workbook.save(path.join(dataDir, "output.xlsx"));
```
