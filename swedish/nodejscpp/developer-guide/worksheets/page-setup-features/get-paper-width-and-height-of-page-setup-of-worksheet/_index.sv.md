---
title: Hämta pappersbredd och höjd för Siduppställning av arbetsbladet med Node.js via C++
linktitle: Hämta papperets bredd och höjd för sidbildningsinställningen för arket
type: docs
weight: 50
url: /sv/nodejs-cpp/get-paper-width-and-height-of-page-setup-of-worksheet/
description: Upptäck hur man får pappersbredd och höjd för Excel Arbetsbords Siduppställning med Node.js via C++ programmässigt.
keywords: excel siduppställning pappersbredd Node.js via C++, excel siduppställning pappershöjd Node.js via C++
---

## **Möjliga användningsscenario**

Ibland behöver du veta bredden och höjden på papperstorleken som har anpassats i siduppställningen för arbetsbladet. Använd [**PageSetup.getPaperWidth()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getPaperWidth--)- och [**PageSetup.getPaperHeight()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getPaperHeight--)-egenskaperna för detta ändamål.

## **Hämta pappersbredd och höjd i sidinställningen för kalkylblad**

Följande exempel förklarar användningen av [**PageSetup.getPaperWidth()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getPaperWidth--) och [**PageSetup.getPaperHeight()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getPaperHeight--)-egenskaperna. Det ändrar först pappersstorleken till *A2* och hittar sedan bredden och höjden på papperet, därefter ändrar det till *A3*, *A4*, *Letter* och hittar respektive bredd och höjd på papperet.

### **Exempelkod**

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

### **Konsoloutput**

Här är konsoloutputen från ovanstående exempelkod.

{{< highlight java >}}

PaperA2: 16.54x23.39

PaperA3: 11.69x16.54

PaperA4: 8.27x11.69

PaperLetter: 8.5x11

{{< /highlight >}}
