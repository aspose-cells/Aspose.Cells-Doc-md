---
title: Einfrieren der oberen Zeile(n) eines Excel Arbeitsblatts mit Node.js via C++
linktitle: Zeilen einfrieren
type: docs
weight: 190
url: /de/nodejs-cpp/how-to-freeze-rows-of-excel-worksheet
description: In diesem Artikel erfahren Sie, wie Sie mit Node.js Bibliothek mit C++ API programmatisch die oberen Zeilen von Excel Arbeitsblättern einfrieren.
keywords: Obere Zeilen einfrieren, Top Row mit Node.js via C++ einfrieren
---

## **Einführung**

In diesem Artikel lernen wir, wie man die obere Zeile(n) einfrieren kann. Wenn Sie eine große Datenmenge unter einer gemeinsamen Überschrift haben, können Sie die Überschrift beim Herunterscrollen nicht mehr sehen. Sie können die obere Zeile(n) einfrieren, sodass Sie diesen eingefrorenen Bereich auch beim Scrollen des restlichen Inhalts sehen können. Header in den oberen Zeilen sind leicht sichtbar.

## **Zeilen in Excel einfrieren**

**![Oberste Zeile(n) in Excel einfrieren](Freeze-Rows.png)**

1. Wenn Sie die oberen Zeile(n) einfrieren möchten, wählen Sie zuerst die Zeile unter der zu frierenden Zeile aus.
2. Klicken Sie auf Ansicht > Fenster einfrieren.
3. Wählen Sie im Dropdown-Menü "Oberste Zeile einfrieren" aus.
4. Wenn Sie nach unten scrollen, befindet sich die erste Zeile immer im oberen Sichtbereich.

**![Gefrorene Zeile](Frozen-Row.png)**

Wie Sie sehen können, ist die erste Zeile eingefroren; die erste Zeile bleibt beim Herunterscrollen immer oben im Blickfeld.

Das Einfrieren von Zeilen ermöglicht es Ihnen, große Datenmengen zu sehen, ohne die Zeilenbeschriftung im Blick behalten zu müssen.

## **Zeilen mit Aspose.Cells for Node.js via C++ einfrieren**
Es ist einfach, Zeile(n) mit Aspose.Cells for Node.js via C++ einzufrieren. 
Verwenden Sie die [**Worksheet.freezePanes(number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#freezePanes-number-number-number-number-) Methode, um die Zeile(n) an der ausgewählten Zeile einzufrieren.
1. Erstellen Sie eine Arbeitsmappe, um die Datei zu öffnen oder eine leere Datei zu erstellen.
2. Frieren Sie die erste Zeile mit der Worksheet.freezePanes() Methode ein.
3. Die Datei speichern.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Freeze.xlsx");

// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook(filePath);

// Freezing panes at the cell B2
workbook.getWorksheets().get(0).freezePanes("A2", 1, 0);

// Saving the file
workbook.save("frozen.xlsx");
```

Angehängte [Beispielquelle für Excel-Datei](../Freeze.xlsx).
