---
title: Seitenansetzungsinformationen vom Quell zum Ziel Arbeitsblatt mit Node.js über C++ kopieren
linktitle: Kopieren von Seiteneinrichtungseinstellungen vom Quellarbeitsblatt in das Zielarbeitsblatt
type: docs
weight: 80
url: /de/nodejs-cpp/copy-page-setup-settings-from-source-worksheet-into-destination-worksheet/
description: Dieser Artikel erklärt, wie man die Node.js API oder C++ Bibliotheksbeispielcodes verwendet, um die Seiteneinrichtungs Einstellungen von einem Quellarbeitsblatt programmatisch in ein Zielarbeitsblatt zu kopieren.
keywords: Seitenlayout Einstellungen mit Node.js über C++, Einstellungen auf Zielarbeitsblatt kopieren mit Node.js über C++
---

## **Mögliche Verwendungsszenarien**

Wenn Sie ein neues Arbeitsblatt in einer Arbeitsmappe hinzufügen, enthält es die Standard-**Seitenlayout**-Einstellungen. Manchmal müssen Sie die Einstellungen ([**PageSetup**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup)) von einem Arbeitsblatt auf ein anderes übertragen. Dieses Dokument erklärt, wie man die Seiteneinrichtungs-Einstellungen von einem Arbeitsblatt mit den APIs Aspose.Cells for Node.js via C++ kopiert.

## **Seiteneinrichtungseinstellungen von der Quellarbeitsmappe in die Zieltabelle kopieren**

Der folgende Beispielcode veranschaulicht, wie die *Seiteneinrichtungseinstellungen* von einem Arbeitsblatt auf ein anderes mithilfe der Methode [**PageSetup.copy(PageSetup, CopyOptions)**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#copy-pagesetup-copyoptions-) kopiert werden. Bitte beachten Sie den folgenden Beispielcode und dessen Konsolenausgabe als Referenz.

## **Beispielcode**

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

## **Konsolenausgabe**

{{< highlight java >}}

Before Paper Size: PaperA3ExtraTransverse

Before Paper Size: PaperLetter

After Paper Size: PaperA3ExtraTransverse

After Paper Size: PaperA3ExtraTransverse

{{< /highlight >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
