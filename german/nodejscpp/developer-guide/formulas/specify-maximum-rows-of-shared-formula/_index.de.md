---  
title: Geben Sie die maximale Anzahl der Zeilen für gemeinsame Formeln mit Node.js über C++ an  
linktitle: Maximale Zeilen der gemeinsamen Formel angeben  
type: docs  
weight: 40  
url: /de/nodejs-cpp/specify-maximum-rows-of-shared-formula/  
description: Lernen Sie, wie Sie die maximale Zeilenanzahl für gemeinsame Formeln mit Aspose.Cells for Node.js via C++ angeben.  
---  

## **Mögliche Verwendungsszenarien**  

Die Standard-Maximalzahl der Zeilen für gemeinsame Formeln ist 64. Es kann eine beliebige Zahl sein, z.B. 1000. Die Leistung der gemeinsamen Formel ändert sich mit unterschiedlicher Zeilenanzahl. Daher bietet Aspose.Cells die Eigenschaft [**WorkbookSettings.getMaxRowsOfSharedFormula()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getMaxRowsOfSharedFormula--), um die maximale Zeilenanzahl für die gemeinsame Formel festzulegen. Die gemeinsame Formel wird in mehrere gemeinsame Formeln aufgeteilt, wenn die Gesamtzahl der Zeilen der gemeinsamen Formel größer ist als diese Zahl, wie im folgenden Screenshot gezeigt.  

![todo:image_alt_text](specify-maximum-rows-of-shared-formula_1.png)  

## **Maximale Zeilen der gemeinsamen Formel angeben**  

Der folgende Beispielcode erklärt die Verwendung der Eigenschaft [**WorkbookSettings.getMaxRowsOfSharedFormula()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getMaxRowsOfSharedFormula--). Er setzt die maximale Zeilenanzahl der gemeinsamen Formel auf 5 und fügt die gemeinsame Formel in Zelle D1 für 100 Zeilen ein und speichert sie in [Ausgabedatei] (61767856.xlsx). Wenn Sie den Inhalt der Ausgabedatei extrahieren und die *sheet1.xml* überprüfen, sehen Sie, wie die gemeinsame Formel alle 5 Zeilen aufgesplittet wird, wie im oberen Screenshot hervorgehoben.  

## **Beispielcode**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");

// Create a new workbook
const wb = new AsposeCells.Workbook();

// Set the max rows of shared formula to 5
wb.getSettings().setMaxRowsOfSharedFormula(5);

// Access first worksheet
const ws = wb.getWorksheets().get(0);

// Access cell D1
const cell = ws.getCells().get("D1");

// Set the shared formula in 100 rows
cell.setSharedFormula("=Sum(A1:A2)", 100, 1);

// Save the output Excel file
wb.save("outputSpecifyMaximumRowsOfSharedFormula.xlsx");
```  

