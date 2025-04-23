---  
title: Einfrieren der ersten Spalte(n) eines Excel Arbeitsblatts mit Node.js via C++  
linktitle: Spalten fixieren  
type: docs  
weight: 190  
url: /de/nodejs-cpp/how-to-freeze-columns-of-excel-worksheet  
description: Lernen Sie, wie Sie die linken Spalten von Excel Arbeitsblättern programmgesteuert mit Aspose.Cells for Node.js via C++ einfrieren.  
keywords: Linke Spalten einfrieren, Erste Spalten einfrieren, Spalte(n) sperren  
---  

## **Einführung**  

In diesem Artikel lernen wir, wie man linke Spalte(n) einfriert. Wenn Sie eine große Datenmenge in einer Zeile haben, können Sie die linken Spalten beim horizontalen Scrollen durch das Arbeitsblatt nicht sehen. Sie können die erste(n) Spalte(n) einfrieren und sperren, sodass Sie diesen eingefrorenen Bereich auch beim Scrollen des restlichen Inhalts sehen können. Header in den linken Spalten sind leicht sichtbar.  

## **Spalten in Excel einfrieren**  

**![Linke Spalte(n) in Excel einfrieren](freeze-columns.png)**  

1. Wenn du die linke(n) Spalte(n) einfrieren möchtest, wähle zuerst die Spalte unter der Spalte, die eingefroren werden soll.
2. Klicken Sie auf Ansicht > Fenster einfrieren.
3. Klicken Sie im Dropdown-Menü auf Spalte fixieren.
4. Wenn du nach unten scrollst, ist die erste Spalte immer im linken Ansichtsbereich.

**![Gefrorene Spalte](frozen-columns.png)**  

Wie Sie sehen können, ist die erste Spalte eingefroren, und die erste Spalte bleibt beim horizontalen Scrollen immer oben im Blickfeld fixiert.

Das Einfrieren von Spalten ermöglicht es Ihnen, große Datenmengen ohne Schwierigkeiten im Blick zu behalten.

## **Spalten mit Aspose.Cells for Node.js via C++ einfrieren**  
Es ist einfach, die erste(n) Spalte(n) mit Aspose.Cells for Node.js via C++ einzufrieren.  
Bitte verwenden Sie die Methode [**Worksheet.freezePanes(number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#freezePanes-number-number-number-number-), um die Spalte(n) an der ausgewählten Spalte einzufrieren.  
1. Erstellen Sie eine Arbeitsmappe, um die Datei zu öffnen oder eine leere Datei zu erstellen.
2. Frieren Sie die erste Spalte mit der Worksheet.freezePanes() Methode ein.
3. Die Datei speichern.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Freeze.xlsx");
// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook(filePath);
// Freezing panes at the second column
workbook.getWorksheets().get(0).freezePanes("B1", 0, 1);
// Saving the file
workbook.save("frozen.xlsx");
```  

Anbei [Beispielquelle Excel-Datei](Freeze.xlsx).  

