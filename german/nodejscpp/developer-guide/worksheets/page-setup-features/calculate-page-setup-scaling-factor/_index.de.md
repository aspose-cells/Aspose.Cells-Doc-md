---
title: Seitenansichtskalierungsfaktor mit Node.js über C++ berechnen
linktitle: Berechnen des Maßstabsfaktors für die Seiteneinrichtung
type: docs
weight: 300
url: /de/nodejs-cpp/calculate-page-setup-scaling-factor/
description: Dieser Artikel enthält Beispielcode, der erklärt, wie man die Node.js API mit C++ verwendet, um den Skalierungsfaktor der Seiteneinrichtung anhand der Option auf breite n Seite(n) und hohe m Seite(n) programmatisch zu berechnen.
keywords: Fit to n Seite(n) breit und m hoch, Excel Node.js über C++, Berechnung des Skalierungsfaktors der Seiteneinrichtung mit Node.js über C++
---

{{% alert color="primary" %}}

Wenn Sie die Skalierung der Seiteneinrichtung mit der Option **Auf n Seite(n) breit und m hoch** festlegen, berechnet Microsoft Excel den Skalierungsfaktor der Seiteneinrichtung. Sie können dasselbe mit der Eigenschaft [**SheetRender.getPageScale()**](https://reference.aspose.com/cells/nodejs-cpp/sheetrender/#getPageScale--) berechnen. Diese Eigenschaft gibt einen Doppeldoppelwert zurück, der in Prozent umgerechnet werden kann. Wenn er 0,5 zurückgibt, bedeutet dies, dass der Skalierungsfaktor 50% ist.

{{% /alert %}}

Der folgende Beispielcode veranschaulicht, wie der Maßstabsfaktor für die Seiteneinrichtung mit der Eigenschaft [**SheetRender.getPageScale()**](https://reference.aspose.com/cells/nodejs-cpp/sheetrender/#getPageScale--) berechnet wird.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Put some data in these cells
worksheet.getCells().get("A4").putValue("Test");
worksheet.getCells().get("S4").putValue("Test");

// Set paper size
worksheet.getPageSetup().setPaperSize(AsposeCells.PaperSizeType.PaperA4);

// Set fit to pages wide as 1
worksheet.getPageSetup().setFitToPagesWide(1);

// Calculate page scale via sheet render
const sr = new AsposeCells.SheetRender(worksheet, new AsposeCells.ImageOrPrintOptions());

// Convert page scale double value to percentage
const strPageScale = (sr.getPageScale() * 100).toFixed(0) + "%";

// Write the page scale value
console.log(strPageScale);
```
{{< app/cells/assistant language="nodejs-cpp" >}}
