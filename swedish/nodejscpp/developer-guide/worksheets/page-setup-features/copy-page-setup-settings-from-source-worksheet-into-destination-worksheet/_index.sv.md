---
title: Kopiera sidinställningsinställningar från källarbetsblad till destinationsarbetsblad med Node.js via C++
linktitle: Kopiera siduppsättning inställningar från kälark till destinationsark
type: docs
weight: 80
url: /sv/nodejs-cpp/copy-page-setup-settings-from-source-worksheet-into-destination-worksheet/
description: Denna artikel förklarar hur man använder Node.js API eller C++ bibliotek för att kopiera sidinställningsinställningar från ett källarbetsblad till ett destinationsarbetsblad programatiskt.
keywords: kopiera sidinställningar Node.js via C++, kopiera sidinställningar till målark och Node.js via C++
---

## **Möjliga användningsscenario**

När du lägger till ett nytt blad i en arbetsbok innehåller det standardinställningar för *Siduppställning*. Det kan finnas tillfällen då du behöver överföra inställningarna ([**PageSetup**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup)) från ett blad till ett annat. Detta dokument förklarar hur man kopierar Siduppställningsinställningar från ett blad till ett annat med hjälp av Aspose.Cells for Node.js via C++ API:er.

## **Kopiera siduppsättning inställningar från källkalkylblad till destinations kalkylblad**

Följande exempelkod illustrerar hur man kopierar *sidlayoutinställningar* från ett blad till ett annat med hjälp av [**PageSetup.copy(PageSetup, CopyOptions)**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#copy-pagesetup-copyoptions-)-metoden. Se följande exempelkod och dess konsolresultat som referens.

## **Exempelkod**

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");

// Create workbook
const wb = new AsposeCells.Workbook();

// Add two test worksheets
wb.getWorksheets().add("TestSheet1");
wb.getWorksheets().add("TestSheet2");

// Access both worksheets as TestSheet1 and TestSheet2
const TestSheet1 = wb.getWorksheets().get("TestSheet1");
const TestSheet2 = wb.getWorksheets().get("TestSheet2");

// Set the Paper Size of TestSheet1 to PaperA3ExtraTransverse
TestSheet1.getPageSetup().setPaperSize(AsposeCells.PaperSizeType.PaperA3ExtraTransverse);

// Print the Paper Size of both worksheets
console.log("Before Paper Size: " + TestSheet1.getPageSetup().getPaperSize());
console.log("Before Paper Size: " + TestSheet2.getPageSetup().getPaperSize());
console.log();

// Copy the PageSetup from TestSheet1 to TestSheet2
TestSheet2.getPageSetup().copy(TestSheet1.getPageSetup(), new AsposeCells.CopyOptions());

// Print the Paper Size of both worksheets
console.log("After Paper Size: " + TestSheet1.getPageSetup().getPaperSize());
console.log("After Paper Size: " + TestSheet2.getPageSetup().getPaperSize());
console.log();
```

## **Konsoloutput**

{{< highlight java >}}

Before Paper Size: PaperA3ExtraTransverse

Before Paper Size: PaperLetter

After Paper Size: PaperA3ExtraTransverse

After Paper Size: PaperA3ExtraTransverse

{{< /highlight >}}
