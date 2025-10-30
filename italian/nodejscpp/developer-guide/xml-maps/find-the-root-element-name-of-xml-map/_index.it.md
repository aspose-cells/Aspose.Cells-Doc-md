---
title: Trova il nome dell’elemento radice della mappa XML con Node.js tramite C++
linktitle: Trova il nome dell elemento radice della mappa XML
type: docs
weight: 30
url: /it/nodejs-cpp/find-the-root-element-name-of-xml-map/
description: Impara come trovare il nome dell’elemento radice di una mappa XML in Excel usando Aspose.Cells for Node.js via C++.
---

## **Possibili Scenari di Utilizzo**

Puoi trovare il *Nome dell’Elemento Radice della Mappa Xml* utilizzando Aspose.Cells for Node.js via C++ con la proprietà [**XmlMap.getRootElementName()**](https://reference.aspose.com/cells/nodejs-cpp/xmlmap/#getRootElementName--). La schermata seguente mostra il nome dell’elemento radice della mappa XML in Microsoft Excel.

![todo:image_alt_text](find-the-root-element-name-of-xml-map_1.png)

## **Codice di Esempio**

Il seguente esempio di codice carica il [file Excel di esempio](55541789.xlsx) e accede alla prima mappa XML, stampando la sua proprietà [**XmlMap.getRootElementName()**](https://reference.aspose.com/cells/nodejs-cpp/xmlmap/#getRootElementName--). Si prega di consultare l’output della console del codice di esempio qui sotto.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleRootElementNameOfXmlMap.xlsx");

// Load sample Excel file having Xml Map
const wb = new AsposeCells.Workbook(filePath);

// Access first Xml Map inside the Workbook
const xmap = wb.getWorksheets().getXmlMaps().get(0);

// Print Root Element Name of Xml Map on Console
console.log("Root Element Name Of Xml Map: " + xmap.getRootElementName());
```

## **Output della console**

{{< highlight java >}}

Root Element Name Of Xml Map: MiscData

{{< /highlight >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
