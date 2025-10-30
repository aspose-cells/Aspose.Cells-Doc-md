---
title: Papierbreite und höhe der Seiteneinrichtung des Arbeitsblatts mit Node.js über C++ abrufen
linktitle: Papierbreite und höhe des Seitenlayouts des Arbeitsblatts abrufen
type: docs
weight: 50
url: /de/nodejs-cpp/get-paper-width-and-height-of-page-setup-of-worksheet/
description: Entdecken Sie, wie Sie die Seiteneinrichtungs Papierbreite und höhe des Excel Arbeitsblatt Bogens mithilfe von Node.js über C++ programmatisch abrufen.
keywords: excel Seiteneinrichtung Papierbreite Node.js via C++, excel Seiteneinrichtung Papierhöhe Node.js via C++
---

## **Mögliche Verwendungsszenarien**

Manchmal müssen Sie die Breite und Höhe der Papiergröße kennen, wie sie in der Seiteneinrichtung des Arbeitsblatts festgelegt wurden. Bitte verwenden Sie die Eigenschaften [**PageSetup.getPaperWidth()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getPaperWidth--) und [**PageSetup.getPaperHeight()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getPaperHeight--) zu diesem Zweck.

## **Papierbreite und -höhe des Seitenlayouts des Arbeitsblatts abrufen**

Der folgende Beispielcode erklärt die Verwendung der Eigenschaften [**PageSetup.getPaperWidth()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getPaperWidth--) und [**PageSetup.getPaperHeight()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getPaperHeight--). Er ändert zunächst die Papiergröße auf *A2* und ermittelt dann die Breite und Höhe des Papiers, anschließend ändert er die Papiergröße auf *A3*, *A4*, *Brief* und ermittelt jeweils die Breite und Höhe.

### **Beispielcode**

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");

// Create an instance of Workbook class
const book = new AsposeCells.Workbook();

// Access first worksheet
const sheet = book.getWorksheets().get(0);

// Set paper size to A2 and print paper width and height in inches
sheet.getPageSetup().setPaperSize(AsposeCells.PaperSizeType.PaperA2);
console.log("PaperA2: " + sheet.getPageSetup().getPaperWidth() + "x" + sheet.getPageSetup().getPaperHeight());

// Set paper size to A3 and print paper width and height in inches
sheet.getPageSetup().setPaperSize(AsposeCells.PaperSizeType.PaperA3);
console.log("PaperA3: " + sheet.getPageSetup().getPaperWidth() + "x" + sheet.getPageSetup().getPaperHeight());

// Set paper size to A4 and print paper width and height in inches
sheet.getPageSetup().setPaperSize(AsposeCells.PaperSizeType.PaperA4);
console.log("PaperA4: " + sheet.getPageSetup().getPaperWidth() + "x" + sheet.getPageSetup().getPaperHeight());

// Set paper size to Letter and print paper width and height in inches
sheet.getPageSetup().setPaperSize(AsposeCells.PaperSizeType.PaperLetter);
console.log("PaperLetter: " + sheet.getPageSetup().getPaperWidth() + "x" + sheet.getPageSetup().getPaperHeight());
```

### **Konsolenausgabe**

Hier ist die Konsolenausgabe des obigen Beispielcodes.

{{< highlight java >}}

PaperA2: 16.54x23.39

PaperA3: 11.69x16.54

PaperA4: 8.27x11.69

PaperLetter: 8.5x11

{{< /highlight >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
