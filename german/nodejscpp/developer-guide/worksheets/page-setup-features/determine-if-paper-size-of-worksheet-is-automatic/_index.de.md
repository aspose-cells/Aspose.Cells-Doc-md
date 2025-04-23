---
title: Bestimmen, ob die Papiergröße eines Arbeitsblatts automatisch ist mit Node.js über C++
linktitle: Feststellen, ob das Papierformat des Arbeitsblatts automatisch ist
type: docs
weight: 90
url: /de/nodejs-cpp/determine-if-paper-size-of-worksheet-is-automatic/
description: Dieses Dokument erklärt, wie man die Node.js API mit C++ Addons verwendet, um programmatisch zu bestimmen, ob die Papiergröße eines Arbeitsblatts auf automatisch eingestellt ist.
keywords: Bestimmen, ob die Papiergröße eines Arbeitsblatts automatisch ist Node.js über C++
---

## **Mögliche Verwendungsszenarien**

Die Papiergröße des Arbeitsblatts ist meistens automatisch eingestellt. Wenn sie automatisch ist, wird sie oft als *Letter* eingestellt. Manchmal legt der Benutzer die Papiergröße nach Bedarf fest. In diesem Fall ist die Papiergröße nicht automatisch. Sie können erkennen, ob die Papiergröße des Arbeitsblatts automatisch ist oder nicht, indem Sie die Eigenschaft [**Worksheet.isAutomaticPaperSize()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#isAutomaticPaperSize--) verwenden.

## **Feststellen, ob die Papiergröße des Arbeitsblatts automatisch ist**

Der folgende Beispielscode lädt die folgenden beiden Excel-Dateien

- [samplePageSetupIsAutomaticPaperSize-False.xlsx](48496681.xlsx)
- [samplePageSetupIsAutomaticPaperSize-True.xlsx](48496682.xlsx)

und überprüft, ob die Papiergröße ihres ersten Arbeitsblatts automatisch ist oder nicht. In Microsoft Excel können Sie über das Dialogfeld Seitenlayout wie in diesem Screenshot gezeigt feststellen, ob die Papiergröße automatisch ist oder nicht.

![todo:image_alt_text](determine-if-paper-size-of-worksheet-is-automatic_1.png)

## **Beispielcode**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const wb1 = new AsposeCells.Workbook(path.join(dataDir, "samplePageSetupIsAutomaticPaperSize-False.xlsx"));
const wb2 = new AsposeCells.Workbook(path.join(dataDir, "samplePageSetupIsAutomaticPaperSize-True.xlsx"));

// Access first worksheet of both workbooks
const ws11 = wb1.getWorksheets().get(0);
const ws12 = wb2.getWorksheets().get(0);

// Print the PageSetup.IsAutomaticPaperSize property of both worksheets
console.log("First Worksheet of First Workbook - IsAutomaticPaperSize: " + ws11.getPageSetup().isAutomaticPaperSize());
console.log("First Worksheet of Second Workbook - IsAutomaticPaperSize: " + ws12.getPageSetup().isAutomaticPaperSize());
```

## **Konsolenausgabe**

Hier ist die Konsolenausgabe des obigen Beispielscodes, wenn er mit den angegebenen Beispieldateien ausgeführt wird.

{{< highlight java >}}

First Worksheet of First Workbook - IsAutomaticPaperSize: False

First Worksheet of Second Workbook - IsAutomaticPaperSize: True

{{< /highlight >}}
