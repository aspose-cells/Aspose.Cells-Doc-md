---
title: XML Daten, die mit der XML Karte verbunden sind, mit Node.js via C++ aus der Arbeitsmappe exportieren
linktitle: Exportieren von XML Daten, die mit der XML Map innerhalb der Arbeitsmappe verknüpft sind
type: docs
weight: 20
url: /de/nodejs-cpp/export-xml-data-linked-to-xml-map-inside-the-workbook/
description: Erfahren Sie, wie Sie XML Daten, die mit XML Karten in Ihrer Arbeitsmappe verbunden sind, mit Aspose.Cells for Node.js via C++ exportieren. 
---

## **Exportieren Sie XML-Daten, die mit der XML-Map in der Arbeitsmappe verknüpft sind**

Bitte verwenden Sie die [**Workbook.exportXml()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#exportXml-string-)-Methode, um XML-Daten, die mit Ihren XML-Karten in Ihrem Arbeitsbuch verbunden sind, zu exportieren. Der folgende Beispielcode exportiert die XML-Daten aller XML-Karten aus dem Arbeitsbuch nacheinander. Bitte überprüfen Sie die [Beispieldatei Excel](5115497.xlsx), die in diesem Code verwendet wird, und die [exportierten XML-Daten der ersten XML-Karte](5472487.xml).

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
