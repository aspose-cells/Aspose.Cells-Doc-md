---  
title: Text mit Aspose.Cells for Node.js via C++ in Spalten umwandeln  
linktitle: Text in Spalten konvertieren  
type: docs  
weight: 30  
url: /de/nodejs-cpp/convert-text-to-columns-using-aspose-cells/  
description: Erfahren Sie, wie Sie Text in Excel mit Aspose.Cells for Node.js via C++ in Spalten umwandeln.  
---  

## **Mögliche Verwendungsszenarien**  

Sie können Ihren Text in Spalten mit Microsoft Excel umwandeln. Diese Funktion ist im Menü *Datenwerkzeuge* unter dem Reiter *Daten* verfügbar. Damit der Inhalt einer Spalte auf mehrere Spalten aufgeteilt wird, sollte die Daten eine bestimmte Trennzeichen besitzen, z.B. ein Komma (oder ein anderes Zeichen), anhand dessen Microsoft Excel den Inhalt einer Zelle aufteilt. Aspose.Cells for Node.js via C++ bietet diese Funktion ebenfalls über [**Cells.textToColumns(number, number, number, TxtLoadOptions)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#textToColumns-number-number-number-txtloadoptions-) an.  

## **Text in Spalten mit Aspose.Cells for Node.js via C++ umwandeln**  

Der folgende Beispielcode erklärt die Nutzung der [**Cells.textToColumns(number, number, number, TxtLoadOptions)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#textToColumns-number-number-number-txtloadoptions-) Methode. Der Code fügt zunächst einige Personennamen in Spalte A des ersten Arbeitsblatts ein. Vor- und Nachname sind durch ein Leerzeichen getrennt. Anschließend wendet er die [**Cells.textToColumns(number, number, number, TxtLoadOptions)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#textToColumns-number-number-number-txtloadoptions-) Methode auf Spalte A an und speichert das Ergebnis in eine Ausgabedatei. Wenn Sie die [Ausgabedatei](25395213.xlsx) öffnen, sehen Sie, dass die Vornamen in Spalte A sind, während die Nachnamen in Spalte B stehen, wie in diesem Screenshot gezeigt.  

![todo:image_alt_text](convert-text-to-columns-using-aspose-cells_1.png)  

## **Beispielcode**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Create a workbook.
const wb = new AsposeCells.Workbook();

// Access first worksheet.
const ws = wb.getWorksheets().get(0);

// Add people name in column A. First name and last name are separated by space.
ws.getCells().get("A1").putValue("John Teal");
ws.getCells().get("A2").putValue("Peter Graham");
ws.getCells().get("A3").putValue("Brady Cortez");
ws.getCells().get("A4").putValue("Mack Nick");
ws.getCells().get("A5").putValue("Hsu Lee");

// Create text load options with space as separator.
const opts = new AsposeCells.TxtLoadOptions();
opts.setSeparator(' ');

// Split the column A into two columns using TextToColumns() method.
// Now column A will have first name and column B will have second name.
ws.getCells().textToColumns(0, 0, 5, opts);

// Save the workbook in xlsx format.
wb.save(path.join(dataDir, "outputTextToColumns.xlsx"));
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
