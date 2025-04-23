---  
title: Excel Arbeitsblatt mit Node.js über C++ einfrieren  
linktitle: Fenster einfrieren  
type: docs  
weight: 190  
url: /de/nodejs-cpp/how-to-freeze-panes-of-excel-worksheet  
description: In diesem Artikel lernen Sie, wie Sie die Fenster eines Excel Arbeitsblatts programmatisch mit Aspose.Cells for Node.js via C++ einfrieren.  
keywords: Fenster einfrieren, Fenster fixieren.  
---  

## **Einführung**  

In diesem Artikel lernen Sie, wie man Fenster einfriert. Wenn Sie große Datenmengen unter einer gemeinsamen Überschrift haben, können Sie die Überschrift beim Herunterscrollen im Arbeitsblatt nicht mehr sehen. Jedes Datensatz enthält viele Daten. Sie können Fenster einfrieren, sodass Sie den eingefrorenen Bereich auch beim Scrollen des restlichen Daten sehen können. Sie können Kopfzeilen in den oberen Zeilen oder den ersten Spalten leicht erkennen. Das Einfrieren und Aufheben des Einfrierens ändert nur die Ansicht der Daten, ohne die Daten selbst zu verändern.  

## **In Excel**  

**![Fenster einfrieren in Excel](Freeze-panes.png)**  

1. Wenn Sie Fenster einfrieren möchten, Zeilen und Spalten einfrieren, wählen Sie zuerst eine Zelle (wie B2).  
2. Klicken Sie auf Ansicht > Fenster einfrieren.  
3. Im Dropdown-Menü klicken Sie auf Fenster einfrieren.  
4. Wenn Sie nach unten oder nach rechts scrollen, sind die erste Zeile und die erste Spalte eingefroren.  

**![Eingefrorene Fenster](Frozen-Panes.png)**  

Wie Sie sehen können, sind die Zeile 1 und die Spalte A eingefroren, die zweite Zeile ist 32 und die zweite sichtbare Spalte ist D.  

Das Einfrieren von Fenstern ermöglicht es Ihnen, Ihre großen Daten zu betrachten, ohne Zeilen- oder Spaltenbeschriftungen im Blick zu behalten.  

## **Fenster einfrieren mit Aspose.Cells for Node.js via C++**  
Es ist einfach, Fenster mit Aspose.Cells for Node.js via C++ einzufrieren. Bitte verwenden Sie die Methode [**Worksheet.freezePanes(number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#freezePanes-number-number-number-number-), um Fenster an der gewählten Zelle zu fixieren.  
1. Erstellen Sie eine Arbeitsmappe, um die Datei zu öffnen oder eine leere Datei zu erstellen.  
Zeige Pane mit der Methode Worksheet.freezePanes() an.  
3. Die Datei speichern.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook(path.join(dataDir, "Freeze.xlsx")); 
// Freezing panes at the cell B2
workbook.getWorksheets().get(0).freezePanes("B2", 1, 1);
// Saving the file
workbook.save("frozen.xlsx");
```  

Anbei [Beispielquelle Excel-Datei](Freeze.xlsx).  

