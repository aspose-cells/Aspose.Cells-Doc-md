---
title: Export XML Data linked to XML Map inside the Workbook with Node.js via C++
linktitle: Export XML Data linked to XML Map inside the Workbook
type: docs
weight: 20
url: /nodejs-cpp/export-xml-data-linked-to-xml-map-inside-the-workbook/
description: Learn how to export XML data linked to XML Maps inside your workbook using Aspose.Cells for Node.js via C++. 
---

## **Export XML Data linked to XML Map inside the Workbook**

Please use the [**Workbook.exportXml()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#exportXml-string-) method to export XML data linked to your XML Maps inside your workbook. The following sample code exports XML data of all XML Maps from the workbook one by one. Please check the [sample excel file](5115497.xlsx) used in this code and the [exported XML data of the first XML Map](5472487.xml).

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
