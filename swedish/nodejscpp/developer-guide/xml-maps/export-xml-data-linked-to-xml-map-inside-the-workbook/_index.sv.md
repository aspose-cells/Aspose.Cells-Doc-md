---
title: Exportera XML data kopplad till XML karta i arbetsboken med Node.js och C++
linktitle: Exportera XML data kopplad till XML karta i arbetsboken
type: docs
weight: 20
url: /sv/nodejs-cpp/export-xml-data-linked-to-xml-map-inside-the-workbook/
description: Lär dig hur man exporterar XML data kopplad till XML kartor i din arbetsbok med Aspose.Cells for Node.js via C++. 
---

## **Exportera XML-data som är länkad till XML-karta inuti arbetsboken**

Vänligen använd metoden [**Workbook.exportXml()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#exportXml-string-) för att exportera XML-data kopplad till dina XML-kartor i arbetsboken. Följande kodexempel exporterar XML-data för alla XML-kartor i arbetsboken en efter en. Kontrollera filen [exempel-Excelfil](5115497.xlsx) som används i detta kodexempel och [exporterad XML-data för första XML-kart](5472487.xml).

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
