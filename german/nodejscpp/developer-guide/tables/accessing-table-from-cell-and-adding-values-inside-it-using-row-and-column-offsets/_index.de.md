---  
title: Zugriff auf Tabelle aus Zelle und Hinzufügen von Werten darin mit Zeilen und Spaltenversatz mit Node.js über C++  
linktitle: Zugriff auf Tabelle von Zelle und Hinzufügen von Werten in sie unter Verwendung von Zeilen und Spaltenversatz  
type: docs  
weight: 230  
url: /de/nodejs-cpp/accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets/  
---  

{{% alert color="primary" %}}  

Normalerweise fügen Sie Werte in die Tabelle oder das Listenobjekt mit der [**Cell.putValue(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/cell/#putValue-boolean-)-Methode ein. Manchmal müssen Sie jedoch Werte in die Tabelle oder das Listenobjekt unter Verwendung des Zeilen- und Spaltenoffsets hinzufügen.  

Um auf eine Tabelle oder Listenobjekt aus einer Zelle zuzugreifen, verwenden Sie die [**Cell.getTable()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getTable--)-Methode. Um Werte mit Zeilen- und Spaltenverschiebungen hinzuzufügen, verwenden Sie die [**ListObject.putCellValue(number, number, object)**](https://reference.aspose.com/cells/nodejs-cpp/listobject/#putCellValue-number-number-object-)-Methode.  

{{% /alert %}}  

Das folgende Screenshot zeigt die Quell-Excel-Datei, die im Code verwendet wird. Es enthält die leere Tabelle und hebt die Zelle D5 hervor, die innerhalb der Tabelle liegt. Wir greifen auf diese Tabelle über die Zelle D5 mit der [**Cell.getTable()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getTable--)-Methode zu und fügen dann die Werte mit den [**Cell.putValue(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/cell/#putValue-boolean-)- und [**ListObject.putCellValue(number, number, object)**](https://reference.aspose.com/cells/nodejs-cpp/listobject/#putCellValue-number-number-object-)-Methoden hinzu.  

## Beispiel  

### Screenshots zum Vergleich der Quell- und Ausgabedateien  

|![todo:image_alt_text](accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets_1.png)|  
| :- |  

Der folgende Screenshot zeigt die durch den Code generierte Ausgabedatei. Wie Sie sehen können, hat die Zelle D5 einen Wert und die Zelle F6, die sich im Offset 2,2 der Tabelle befindet, hat ebenfalls einen Wert.  

|![todo:image_alt_text](accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets_2.png)|  
| :- |  

### Node.js-Code zum Zugriff auf Tabelle aus Zelle und zum Hinzufügen von Werten darin mit Zeilen- und Spaltenoffsets  

Der folgende Beispielcode lädt die oben gezeigte Excel-Quelldatei und fügt Werte in die Tabelle ein, um die oben gezeigte Ausgabedatei zu generieren.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create workbook from source Excel file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "Accessing_Table.xlsx"));

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access cell D5 which lies inside the table
const cell = worksheet.getCells().get("D5");

// Put value inside the cell D5
cell.putValue("D5 Data");

// Access the Table from this cell
const table = cell.getTable();

// Add some value using Row and Column Offset
table.putCellValue(2, 2, "Offset [2,2]");

// Save the workbook
workbook.save(path.join(dataDir, "output_out.xlsx"));
```  

