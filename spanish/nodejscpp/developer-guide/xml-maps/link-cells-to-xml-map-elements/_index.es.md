---
title: Vincular celdas a elementos de mapas XML con Node.js a través de C++
linktitle: Vincular celdas a elementos del mapa XML
type: docs
weight: 50
url: /es/nodejs-cpp/link-cells-to-xml-map-elements/
---

## **Escenarios de uso posibles**

Puedes enlazar tus celdas a los elementos de mapas XML usando Aspose.Cells for Node.js via C++. Usa el método [**Cells.linkToXmlMap(string, number, number, string)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#linkToXmlMap-string-number-number-string-) para este propósito.

## **Vincular celdas a elementos del mapa XML**

El siguiente código de ejemplo carga el [archivo de Excel fuente](5115471.xlsx) que contiene un mapa XML y luego vincula las celdas A1, B2, C3, D4, E5 y F6 a los elementos de mapa XML FIELD1, FIELD2, FIELD4, FIELD5, FIELD7 y FIELD8 respectivamente, y luego guarda el libro de trabajo en el [archivo de Excel de salida](5115467.xlsx).

Si abre el [archivo de Excel de salida](5115467.xlsx) y hace clic en el botón Desarrollador > Origen, verá que las celdas están vinculadas con elementos de mapa XML y también serán resaltadas por Microsoft Excel como se muestra en esta imagen.

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
{{< app/cells/assistant language="nodejs-cpp" >}}
