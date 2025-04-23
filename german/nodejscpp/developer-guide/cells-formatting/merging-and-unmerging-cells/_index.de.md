---
title: Zellen mit Verschmelzung und Aufhebung der Verschmelzung mit Node.js über C++
linktitle: Zusammenführen und Aufteilen von Zellen
description: Aspose.Cells ist eine Node.js Bibliothek für die Arbeit mit Tabellenkalkulationsdateien, die das Verschmelzen und Aufheben der Verschmelzung von Zellen unterstützt. Dieser Artikel zeigt, wie man Zellen mit der Aspose.Cells Bibliothek verschmilzt und wieder auseinanderzieht, inklusive Optionen zur Anpassung des Styles der verschmolzenen Zellen.
keywords: Aspose.Cells, Node.js Bibliothek, Tabellenblatt, Zellen verschmelzen, Zellen aufheben, Style Einstellungen, benutzerdefinierte Styles
type: docs
weight: 190
url: /de/nodejs-cpp/merging-and-unmerging-cells/
---

{{% alert color="primary" %}} 

Aspose.Cells unterstützt diese Funktion und kann auch Zellen in einem Arbeitsblatt zusammenführen. Sie können auch Zellen trennen oder aufteilen. Der Zellenbezug einer zusammengeführten Zelle ist der Bezug der links oben Zelle im ursprünglich ausgewählten Bereich.

{{% /alert %}} 
## **Einführung**
Nicht immer benötigen Sie dieselbe Anzahl von Zellen in jeder Zeile oder Spalte. Zum Beispiel möchten Sie möglicherweise einen Titel in einer Zelle haben, die mehrere Spalten umspannt. Oder wenn Sie eine Rechnung erstellen, möchten Sie weniger Spalten für die Gesamtsumme haben. Um eine Zelle aus zwei oder mehr Zellen zu machen, führen Sie sie zusammen. Microsoft Excel ermöglicht es Benutzern, Zellen auszuwählen und zu verschmelzen, um die Tabelle nach ihren Wünschen zu strukturieren.

{{% alert color="primary" %}} 

Beachten Sie, dass beim Zusammenführen von Zellen nur die Daten in der oberen linken Zelle beibehalten werden. Wenn in den anderen Zellen im Bereich Daten vorhanden sind, werden diese gelöscht. Formatierung basiert ebenfalls auf der Referenzzelle, sodass beim Zusammenführen von Zellen die Formatierungseinstellungen der oberen linken Zelle im Bereich auf die zusammengeführte Zelle angewendet werden. Beim Aufteilen der Zelle behalten die neuen Zellen ihre ursprünglichen Formatierungseinstellungen.

{{% /alert %}} 
## **Zellen in einem Arbeitsblatt zusammenführen**
### **Zusammenführen von Zellen in Microsoft Excel**
Die folgenden Schritte beschreiben, wie Sie Zellen im Arbeitsblatt mit MS Excel zusammenführen können.

1. Kopieren Sie die Daten, die Sie in die oberste linke Zelle innerhalb des Bereichs einfügen möchten.
1. Wählen Sie die Zellen aus, die Sie zusammenführen möchten.
1. Um Zellen in einer Zeile oder Spalte zusammenzuführen und den Zellinhalt zu zentrieren, klicken Sie auf das Icon **Zusammenführen und Zentrieren** in der **Formatierung**-Symbolleiste.

### **Zellen zusammenführen mit Aspose.Cells**
Die Aspose.Cells.Cells-Klasse verfügt über nützliche Methoden für diese Aufgabe. Zum Beispiel verbindet die Methode `merge()` die Zellen in einem bestimmten Bereich zu einer einzigen Zelle.

Das folgende Beispiel zeigt, wie Zellen (C6:E7) in einem Arbeitsblatt zusammengeführt werden.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create a Workbook.
const wbk = new AsposeCells.Workbook();

// Create a Worksheet and get the first sheet.
const worksheet = wbk.getWorksheets().get(0);

// Create a Cells object to fetch all the cells.
const cells = worksheet.getCells();

// Merge some Cells (C6:E7) into a single C6 Cell.
cells.merge(5, 2, 2, 3);

// Input data into C6 Cell.
cells.get(5, 2).putValue("This is my value");

// Create a Style object to fetch the Style of C6 Cell.
const style = cells.get(5, 2).getStyle();

// Create a Font object
const font = style.getFont();

// Set the name.
font.setName("Times New Roman");

// Set the font size.
font.setSize(18);

// Set the font color
font.setColor(AsposeCells.Color.Blue);

// Bold the text
font.setIsBold(true);

// Make it italic
font.setIsItalic(true);

// Set the background color of C6 Cell to Red
style.setForegroundColor(AsposeCells.Color.Red);
style.setPattern(AsposeCells.BackgroundType.Solid);

// Apply the Style to C6 Cell.
cells.get(5, 2).setStyle(style);

// Save the Workbook.
wbk.save(path.join(dataDir, "mergingcells.out.xls"));
```

## **Aufsplitten (Teilen) von zusammengeführten Zellen**
### **Verwendung von Microsoft Excel**
Die folgenden Schritte beschreiben, wie Sie zusammengeführte Zellen mit Microsoft Excel aufspalten können.

1. Wählen Sie die zusammengeführte Zelle aus.
   Wenn Zellen kombiniert wurden, ist **Zusammenführen und Zentrieren** in der **Formatierung**-Symbolleiste ausgewählt.
1. Klicken Sie auf **Zusammenführen und Zentrieren** in der **Formatierung**-Symbolleiste.

### **Verwendung von Aspose.Cells**
Die Klasse Aspose.Cells.Cells hat eine Methode namens `unmerge()`, die die Zellen in ihren ursprünglichen Zustand zurücksetzt. Die Methode entmerge die Zellen anhand der Referenz der Zelle im zusammengeführten Zellenbereich.

Das folgende Beispiel zeigt, wie die zusammengeführten Zellen (C6) aufgeteilt werden. Das Beispiel verwendet die Datei, die im vorherigen Beispiel erstellt wurde, und teilt die zusammengeführten Zellen auf.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create a Workbook.
// Open the excel file.
const workbook = new AsposeCells.Workbook(path.join(dataDir, "mergingcells.xls"));

// Create a Worksheet and get the first sheet.
const worksheet = workbook.getWorksheets().get(0);

// Create a Cells object to fetch all the cells.
const cells = worksheet.getCells();

// Unmerge the cells.
cells.unMerge(5, 2, 2, 3);

// Save the file.
workbook.save(path.join(dataDir, "unmergingcells.out.xls"));
```

## **Erweiterte Themen**
- [Erkennen von zusammengeführten Zellen in einem Arbeitsblatt](/cells/de/nodejs-cpp/detect-merged-cells-in-a-worksheet/)
