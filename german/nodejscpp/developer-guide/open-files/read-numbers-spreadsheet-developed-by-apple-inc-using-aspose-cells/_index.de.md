---
title: Nummertabellen, entwickelt von Apple Inc., mit Aspose.Cells for Node.js via C++
linktitle: Zahlen Tabelle entwickelt von Apple Inc. unter Verwendung von Aspose.Cells
type: docs
weight: 140
url: /de/nodejs-cpp/read-numbers-spreadsheet-developed-by-apple-inc-using-aspose-cells/
description: Lernen, wie man Numbers Tabellen, entwickelt von Apple Inc., mit Aspose.Cells for Node.js via C++ liest. 
---

## **Mögliche Verwendungsszenarien**

Numbers ist eine Tabellenkalkulationsanwendung, entwickelt von Apple Inc. Aspose.Cells kann Numbers-Tabellen lesen, aber das Schreiben in sie wird nicht unterstützt. Es kann Daten, Formatierungen und Formeln aus Numbers-Tabellen lesen.

## **Read Numbers Spreadsheet Developed by Apple Inc. using Aspose.Cells for Node.js via C++**

Der folgende Beispielcode lädt die [Beispiel Numbers Tabelle](sampleNumbersByAppleInc.numbers) und konvertiert sie in [Ausgabe PDF-Format](outputNumbersByAppleInc.pdf). Sie müssen die [**LoadOptions**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions)-Klasse verwenden und [**LoadFormat.Numbers**](https://reference.aspose.com/cells/nodejs-cpp/loadformat) als Parameter im Konstruktor angeben, um sie erfolgreich zu laden. Laden Sie beide von den angegebenen Links herunter. Sie können den Code mit jeder Numbers-Tabelle ausprobieren. Bitte lesen Sie auch die Kommentare im Code für weitere Hilfe.

## **Beispielcode**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const sourceFilePath = path.join(dataDir, "sampleNumbersByAppleInc.numbers");
const outputFilePath = path.join(dataDir, "outputNumbersByAppleInc.pdf");

// Specify load options, we want to load Numbers spreadsheet
const opts = new AsposeCells.LoadOptions(AsposeCells.LoadFormat.Numbers);

// Load the Numbers spreadsheet in workbook with above load options
const wb = new AsposeCells.Workbook(sourceFilePath, opts);

// Save the workbook to pdf format
wb.save(outputFilePath, AsposeCells.SaveFormat.Pdf);
```

