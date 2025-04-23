---
title: Zeilen oder Spalten mit Node.js über C++ aufheben
linktitle: Fenster fixieren
type: docs
weight: 190
url: /de/nodejs-cpp/unfreeze-rows-or-columns-of-excel-worksheet
description: In diesem Artikel lernen Sie, wie Sie Zeilen, Spalten oder Bereiche von Excel Tabellen mithilfe der Node.js API mit C++ programmatisch aufheben.
keywords: Bereiche aufheben, Zeilen aufheben, Spalten aufheben, Fenster mit Node.js über C++ aufheben.
---

## **Einführung**

In diesem Artikel lernen wir, wie man Zeilen, Spalten und Bereiche aufhebt. Wenn Tabellen in Excel eingefroren sind, möchten wir manchmal die Sperre aufheben oder eingefrorene Zeilen, Spalten oder Bereiche anpassen.


## **In Excel**

1. Klicken Sie auf die Registerkarte Ansicht > Fenster fixieren > Fenster nicht fixieren.

**![Fenster nicht fixieren in Excel](Unfreeze-Panes.png)**




## **Zeilen, Spalten oder Bereiche mit Aspose.Cells for Node.js via C++ aufheben**
Das Aufheben von Bereichen mit Aspose.Cells for Node.js via C++ ist einfach. Bitte verwenden Sie die [**Worksheet.unFreezePanes()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#unFreezePanes--)-Methode, um Bereiche aufzuheben.

1. Arbeitsmappe erstellen, um die gefrorene Datei zu öffnen.
2. Bereiche mit der Methode Worksheet.unfreezePanes() aufheben.
3. Die Datei speichern.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

const dataDir = path.join(__dirname, "data");
const frozenFilePath = path.join(dataDir, "Frozen.xlsx");

const workbook = new AsposeCells.Workbook(frozenFilePath); 
workbook.getWorksheets().get(0).unFreezePanes();
workbook.save("Unfrozen.xlsx");
```

Angehängte [Beispiel-Excel-Quelldatei](Frozen.xlsx).
