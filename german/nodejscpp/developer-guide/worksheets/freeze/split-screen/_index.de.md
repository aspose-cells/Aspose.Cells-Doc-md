---
title: Geteilte Ansicht des Excel Arbeitsblatts mit Node.js über C++
linktitle: Bildschirm aufteilen
type: docs
weight: 190
url: /de/nodejs-cpp/how-to-split-screen-of-excel-worksheet
description: In diesem Artikel lernen Sie, wie Sie bestimmte Zeilen und/oder Spalten durch Programmierung in separate Bereiche aufteilen, indem Sie das Arbeitsblatt in zwei oder vier Teile aufteilen, mithilfe von Node.js C++ Addon.
keywords: Obere Zeile(n) einfrieren, obere Zeile einfrieren.
---

## **Einführung**

In diesem Artikel lernen wir, wie man bestimmte Zeilen und/oder Spalten in separaten Bereichen anzeigt, indem man das Arbeitsblatt in zwei oder vier Teile aufteilt. Bei großen Datensätzen müssen wir bestimmte Bereiche desselben Arbeitsblatts gleichzeitig sehen, um verschiedene Datensubsets zu vergleichen. Die Funktion zum Teilen des Bildschirms kann Ihre Anforderungen erfüllen.

## **Wie man den Bildschirm in Excel aufteilt**
Um ein Arbeitsblatt in zwei oder vier Teile aufzuteilen, führen Sie folgende Schritte aus:

1. Wählen Sie die Zeile/Spalte/Zelle aus, vor der Sie den Split platzieren möchten.
2. Klicken Sie im Register Ansicht auf der Registerkarte Fenster in der Gruppe Windows auf die Schaltfläche Split.

**![Bildschirm teilen](Split-Screen.png)**

## **Arbeitsblatt vertikal in Spalten teilen**

Um zwei Bereiche des Tabellenblatts vertikal zu trennen, wählen Sie die Spalte rechts von der Spalte aus, an der die Trennung erscheinen soll, und klicken Sie auf die Schaltfläche Split in Excel.

Es ist einfach, Arbeitsblätter programmatisch vertikal nach Spalten mit Aspose.Cells for Node.js via C++ zu teilen. Wir müssen nur eine Zelle in der oberen Zeile als aktive Zelle auswählen und dann mit [**Worksheet.split()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#split--) Methode teilen.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook(filePath);

const sheet = workbook.getWorksheets().get(0);

// Sets C1 cell in the top row as the active cell.
sheet.setActiveCell("C1");

// Split worksheet vertically on columns
sheet.split();
```

## **Arbeitsblatt horizontal in Zeilen teilen**
Um Ihr Excel-Fenster horizontal zu trennen, wählen Sie die Zeile unterhalb der Zeile, an der die Trennung in Excel erfolgen soll.

Es ist einfach, Arbeitsblätter programmatisch horizontal nach Zeilen mit Aspose.Cells for Node.js via C++ zu teilen. Wir müssen nur eine Zelle in der linken Spalte als aktive Zelle auswählen und dann mit [**Worksheet.split()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#split--) Methode teilen.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");
// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook(filePath);

const sheet = workbook.getWorksheets().get(0);

// Sets A6 cell in the left column as the active cell.
sheet.setActiveCell("A6");

// Split worksheet horizontally on rows
sheet.split();

workbook.save("dest.xlsx");
```

## **Arbeitsblatt in vier Teile teilen**
Um vier verschiedene Abschnitte desselben Arbeitsblatts gleichzeitig anzuzeigen, teilen Sie Ihren Bildschirm sowohl vertikal als auch horizontal in Excel.

Es ist einfach, Arbeitsblätter programmatisch vertikal nach Spalten mit Aspose.Cells for Node.js via C++ zu teilen. Wir müssen nur eine Zelle auswählen, die nicht in der ersten Zeile und Spalte ist, als aktive Zelle, und dann mit [**Worksheet.split()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#split--) Methode teilen.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook(filePath);

const sheet = workbook.getWorksheets().get(0);

// Sets E6 cell as the active cell.
sheet.setActiveCell("E6");

// Split worksheet into four parts
sheet.split();
```

## **So entfernen Sie die Trennung**
Um die Trennung des Arbeitsblatts zu entfernen, klicken Sie einfach erneut auf die Schaltfläche Split.

Aspose.Cells for Node.js via C++ stellt eine [**Worksheet.removeSplit()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#removeSplit--)-Methode zum Entfernen der Teilungseinstellungen bereit.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook(filePath);
const sheet = workbook.getWorksheets().get(0);

// Remove split.
sheet.removeSplit();

// Split worksheet into four parts
sheet.split();
```

