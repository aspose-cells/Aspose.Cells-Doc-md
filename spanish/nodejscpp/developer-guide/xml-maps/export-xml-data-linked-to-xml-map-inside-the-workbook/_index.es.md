---
title: Exportar datos XML vinculados a mapas XML dentro del libro de trabajo con Node.js a través de C++
linktitle: Exportar datos XML vinculados al XML Map dentro del libro de trabajo
type: docs
weight: 20
url: /es/nodejs-cpp/export-xml-data-linked-to-xml-map-inside-the-workbook/
description: Aprende cómo exportar datos XML vinculados a mapas XML en tu libro de trabajo usando Aspose.Cells for Node.js via C++. 
---

## **Exportar datos XML vinculados al mapa XML dentro del libro**

Por favor, usa el método [**Workbook.exportXml()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#exportXml-string-) para exportar datos XML vinculados a tus mapas XML dentro de tu libro de trabajo. El siguiente código de ejemplo exporta los datos XML de todos los mapas XML uno por uno. Revisa el [archivo de ejemplo de Excel](5115497.xlsx) usado en este código y los [datos XML exportados del primer mapa XML](5472487.xml).

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
