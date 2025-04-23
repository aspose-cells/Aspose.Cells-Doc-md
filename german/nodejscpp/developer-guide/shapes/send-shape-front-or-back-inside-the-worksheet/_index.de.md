---
title: Zeigen Sie eine Form im Arbeitsblatt mit Node.js via C++ vor oder nach
linktitle: Form vorwärts oder rückwärts innerhalb des Arbeitsblatts senden
type: docs
weight: 3400
url: /de/nodejs-cpp/send-shape-front-or-back-inside-the-worksheet/
description: Erfahren Sie, wie Sie eine Form mit Aspose.Cells for Node.js via C++ in den Vorder oder Hintergrund eines Arbeitsblattes senden. 
---

## **Mögliche Verwendungsszenarien**

Wenn mehrere Formen am selben Ort vorhanden sind, bestimmt ihre Z-Reihenfolge die Sichtbarkeit. Aspose.Cells bietet die Methode [**Shape.toFrontOrBack()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#toFrontOrBack-number-), mit der die Z-Order-Position der Form geändert wird. Um eine Form nach hinten zu senden, verwenden Sie eine negative Zahl wie -1, -2, -3 usw., und um eine Form nach vorne zu bringen, verwenden Sie eine positive Zahl wie 1, 2, 3 usw.

## **Form nach vorn oder hinten im Arbeitsblatt senden**

Der folgende Beispielcode zeigt die Verwendung der Methode [**Shape.toFrontOrBack()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#toFrontOrBack-number-). Bitte sehen Sie sich die[Beispiel-Excel-Datei](50528330.xlsx) an, die im Code verwendet wird, sowie die[Ausgabedatei](50528331.xlsx), die damit erstellt wurde. Der Screenshot zeigt die Wirkung des Codes auf die Beispiel-Excel-Datei nach der Ausführung.

![todo:image_alt_text](send-shape-front-or-back-inside-the-worksheet_1.png)

## **Beispielcode**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const sourceFilePath = path.join(dataDir, "sampleToFrontOrBack.xlsx");

// Load source Excel file
const workbook = new AsposeCells.Workbook(sourceFilePath);

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access first and fourth shape
const shape1 = worksheet.getShapes().get(0);
const shape4 = worksheet.getShapes().get(3);

// Print the Z-Order position of the shape
console.log("Z-Order Shape 1: " + shape1.getZOrderPosition());

// Send this shape to front
shape1.toFrontOrBack(2);

// Print the Z-Order position of the shape
console.log("Z-Order Shape 4: " + shape4.getZOrderPosition());

// Send this shape to back
shape4.toFrontOrBack(-2);

// Save the output Excel file
const outputFilePath = path.join(dataDir, "outputToFrontOrBack.xlsx");
workbook.save(outputFilePath);
```
