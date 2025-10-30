---
title: Çalışma kitabı içinde bağlı XML Haritasına XML Verisi İhraç Edin Node.js ile C++
linktitle: Çalışma Kitabının İçine Bağlı XML Haritasından XML Verilerini Dışa Aktar
type: docs
weight: 20
url: /tr/nodejs-cpp/export-xml-data-linked-to-xml-map-inside-the-workbook/
description: Çalışma kitabınızdaki XML Haritalarına bağlı XML verisini nasıl ihraç edeceğinizi Aspose.Cells for Node.js via C++ ile öğrenin. 
---

## **Çalışma Kitabı içinde XML Haritasına bağlı XML Verilerini Dışa Aktar**

Lütfen çalışma kitabınızdaki XML Haritalarınıza bağlı XML verisini ihraç etmek için [**Workbook.exportXml()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#exportXml-string-) yöntemini kullanın. Aşağıdaki örnek kod, çalışma kitabındaki tüm XML Haritalarını tek tek ihraç eder. Bu kodda kullanılan [örnek excel dosyasını](5115497.xlsx) ve [birinci XML Haritasının ihraç edilen XML verisini](5472487.xml) kontrol edin.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object.
const workbook = new AsposeCells.Workbook(path.join(dataDir, "sample.xlsx"));

// Export all XML data from all XML Maps from the Workbook.
for (let i = 0; i < workbook.getWorksheets().getXmlMaps().getCount(); i++) {
// Access the XML Map.
const map = workbook.getWorksheets().getXmlMaps().get(i);

// Exports its XML Data to file.
workbook.exportXml(map.getName(), path.join(dataDir, `${map.getName()}.xml`));
}
```
{{< app/cells/assistant language="nodejs-cpp" >}}
