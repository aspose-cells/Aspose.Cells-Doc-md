---
title: Wurzelelementname der XML Karte mit Node.js via C++ finden
linktitle: Ermitteln Sie den Root Elementnamen der XML Map
type: docs
weight: 30
url: /de/nodejs-cpp/find-the-root-element-name-of-xml-map/
description: Erfahren Sie, wie Sie den Namen des Wurzelelements einer XML Karte in Excel mit Aspose.Cells for Node.js via C++ finden.
---

## **Mögliche Verwendungsszenarien**

Sie können den *Wurzelelementnamen der Xml-Karte* mit Aspose.Cells for Node.js via C++ und der [**XmlMap.getRootElementName()**](https://reference.aspose.com/cells/nodejs-cpp/xmlmap/#getRootElementName--)-Eigenschaft finden. Das folgende Screenshot zeigt den Namen des Wurzelelements der XML-Karte in Microsoft Excel.

![todo:image_alt_text](find-the-root-element-name-of-xml-map_1.png)

## **Beispielcode**

Der folgenden Beispielcode lädt die [Beispieldatei Excel](55541789.xlsx) und greift auf die erste XML-Karte zu, um deren [**XmlMap.getRootElementName()**](https://reference.aspose.com/cells/nodejs-cpp/xmlmap/#getRootElementName--)-Eigenschaft auszugeben. Bitte sehen Sie sich die Konsolenausgabe des Beispielcodes unten an.

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

## **Konsolenausgabe**

{{< highlight java >}}

Root Element Name Of Xml Map: MiscData

{{< /highlight >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
