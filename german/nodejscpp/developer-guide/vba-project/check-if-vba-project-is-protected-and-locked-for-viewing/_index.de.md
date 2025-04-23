---
title: Überprüfen, ob das VBA Projekt geschützt und zum Betrachten gesperrt ist, mit Node.js via C++
linktitle: Überprüfen, ob das VBA Projekt geschützt und für die Anzeige gesperrt ist
type: docs
weight: 30
url: /de/nodejs-cpp/check-if-vba-project-is-protected-and-locked-for-viewing/
description: Erfahren Sie, wie Sie überprüfen, ob ein VBA Projekt in einer Excel Datei geschützt und zum Betrachten gesperrt ist, mit Aspose.Cells for Node.js via C++.
---

## Überprüfen, ob das VBA-Projekt geschützt und zum Betrachten gesperrt ist in Node.js

Aspose.Cells ermöglicht es, zu überprüfen, ob das VBA (Visual Basic for Applications)-Projekt einer Excel-Datei geschützt und zum Betrachten gesperrt ist. Für diese API bietet die [**VbaProject.getIslockedForViewing()**](https://reference.aspose.com/cells/nodejs-cpp/vbaproject/#getIslockedForViewing--)-Eigenschaft. Wenn es gesperrt ist, dann gibt die [**VbaProject.getIslockedForViewing()**](https://reference.aspose.com/cells/nodejs-cpp/vbaproject/#getIslockedForViewing--)-Eigenschaft **true** zurück.

## **Beispielcode**

Der folgende Beispielcode lädt die [Beispiel-Excel-Datei](43352065.xlsm) und überprüft, ob das VBA (Visual Basic for Applications)-Projekt der Excel-Datei geschützt und zum Betrachten gesperrt ist. Bitte beachten Sie auch die Konsolenausgabe zur Referenz.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Load your source Excel file.
const filePath = path.join(dataDir, "sampleCheckifVBAProjectisProtected.xlsm");
const workbook = new AsposeCells.Workbook(filePath);

// Access the VBA project of the workbook.
const vbaProject = workbook.getVbaProject();

// Whether "Lock project for viewing" is true or not.
console.log("Is VBA Project Locked for Viewing: " + vbaProject.getIslockedForViewing());
```

## **Konsolenausgabe**

Dies ist die Konsolenausgabe des obigen Beispielcodes, dass mit der bereitgestellten [Beispiel-Excel-Datei](43352065.xlsm) ausgeführt wird.

{{< highlight java >}}

Is VBA Project Locked for Viewing: True

{{< /highlight >}}
