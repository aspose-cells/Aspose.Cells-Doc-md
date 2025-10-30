---
title: Hitta rot elementnamnet för XML karta med Node.js via C++
linktitle: Hitta det rotelementnamn för XML karta
type: docs
weight: 30
url: /sv/nodejs-cpp/find-the-root-element-name-of-xml-map/
description: Lär dig hur du hittar rot elementnamnet för en XML karta i Excel med Aspose.Cells for Node.js via C++.
---

## **Möjliga användningsscenario**

Du kan hitta *Rot Elementnamnet för Xml Map* med hjälp av Aspose.Cells for Node.js via C++ och egenskapen [**XmlMap.getRootElementName()**](https://reference.aspose.com/cells/nodejs-cpp/xmlmap/#getRootElementName--). Följande skärmbild visar rot-elementnamnet för XML-kartan i Microsoft Excel.

![todo:image_alt_text](find-the-root-element-name-of-xml-map_1.png)

## **Exempelkod**

Följande kodexempel laddar [exempel-Excelfil](55541789.xlsx) och går till den första XML-kartan och skriver ut dess egenskap [**XmlMap.getRootElementName()**](https://reference.aspose.com/cells/nodejs-cpp/xmlmap/#getRootElementName--). Se konsolutskriften för kodexemplet nedan.

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

## **Konsoloutput**

{{< highlight java >}}

Root Element Name Of Xml Map: MiscData

{{< /highlight >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
