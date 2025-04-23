---  
title: Wie und wo Enumeratoren mit Node.js via C++ verwenden  
linktitle: Daten durchlaufen  
type: docs  
weight: 55  
url: /de/nodejs-cpp/how-and-where-to-use-enumerators/  
description: Erfahren Sie, wie Sie Enumeratoren durch die API Aspose.Cells for Node.js via C++ verwenden.  
keywords: Wie man Enumeratoren Node.js via C++, Cells Enumerator Node.js via C++, Rows Enumerator Node.js via C++, Columns Enumerator Node.js via C++  
---  

{{% alert color="primary" %}}  

Ein Enumerator ist ein Objekt, das die Fähigkeit bietet, einen Container oder eine Sammlung zu durchlaufen. Enumeratoren können verwendet werden, um die Daten in der Sammlung zu lesen, aber sie können nicht verwendet werden, um die zugrunde liegende Sammlung zu modifizieren. Im Gegensatz dazu ist Array eine Schnittstelle, die eine Methode `getEnumerator` definiert, die eine `IEnumerator`-Schnittstelle zurückgibt. Dies ermöglicht lesenden Zugriff auf eine Sammlung.  

Aspose.Cells APIs bieten eine Reihe von Enumeratoren, in diesem Artikel werden jedoch hauptsächlich die drei unten aufgeführten Typen diskutiert.  

1. Zellen-Enumerator  
1. Zeilen Enumerator  
1. Spalten Enumerator  

{{% /alert %}}  

## **Wie man Enumerators verwendet**  

### **Zellen Enumerator**  

Es gibt verschiedene Möglichkeiten, auf den Zellen Enumerator zuzugreifen, und man kann eine dieser Methoden basierend auf den Anforderungen der Anwendung verwenden. Hier sind die Methoden, die den Zellen Enumerator zurückgeben.  

1. [**Cells.getEnumerator()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getEnumerator--)  
1. [**Row.getEnumerator()**](https://reference.aspose.com/cells/nodejs-cpp/row/#getEnumerator--)  
1. [**Range.getEnumerator()**](https://reference.aspose.com/cells/nodejs-cpp/range/#getEnumerator--)  

Alle oben genannten Methoden geben den Enumerator zurück, der das Durchlaufen der Sammlung von Zellen ermöglicht, die initialisiert wurden.  

{{% alert color="primary" %}}  

Beim Durchlaufen der Zellen sollte die Sammlung nicht geändert werden (Operationen, die dazu führen, dass eine neue Zelle instanziiert oder eine vorhandene Zelle gelöscht wird). Andernfalls kann der Enumerator möglicherweise nicht in der Lage sein, alle Zellen korrekt zu durchlaufen (einige Elemente können wiederholt durchlaufen oder übersprungen werden).  

{{% /alert %}}  

Das folgende Codebeispiel demonstriert die Implementierung der `IEnumerator`-Schnittstelle für eine Cells-Sammlung.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
const workbook = new AsposeCells.Workbook(filePath);

const cells = workbook.getWorksheets().get(0).getCells().getEnumerator();
for (const cell of cells) {
console.log(`${cell.getName()} ${cell.getValue()}`);
}

const rowCells = workbook.getWorksheets().get(0).getCells().getRows().get(0).getEnumerator();
for (const cell of rowCells) {
console.log(`${cell.getName()} ${cell.getValue()}`);
}

const rangeCells = workbook.getWorksheets().get(0).getCells().createRange("A1:B10").getEnumerator();
for (const cell of rangeCells) {
console.log(`${cell.getName()} ${cell.getValue()}`);
}
```  

### **Zeilen Enumerator**  

Der Rows-Enumerator kann beim Verwenden der [**RowCollection.getEnumerator()**](https://reference.aspose.com/cells/nodejs-cpp/rowcollection/#getEnumerator--)-Methode aufgerufen werden. Das folgende Codebeispiel zeigt die Implementierung der `IEnumerator`-Schnittstelle für [**RowCollection**](https://reference.aspose.com/cells/nodejs-cpp/rowcollection).  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Get RowCollection and iterate using index
const rows = workbook.getWorksheets().get(0).getCells().getRows();
const rowCount = rows.getCount();

// Traverse rows in the collection
for (let i = 0; i < rowCount; i++) {
const row = rows.get(i);
console.log(row.getIndex());
}
```  

### **Spalten Enumerator**  

Der Columns-Enumerator kann beim Verwenden der [**ColumnCollection.getEnumerator**](https://reference.aspose.com/cells/nodejs-cpp/columncollection)-Methode aufgerufen werden. Das folgende Codebeispiel zeigt die Implementierung der `IEnumerator`-Schnittstelle für [**ColumnCollection**](https://reference.aspose.com/cells/nodejs-cpp/columncollection).  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Get columns collection
const columns = workbook.getWorksheets().get(0).getCells().getColumns();
// Traverse columns using index
const count = columns.getCount();
for (let i = 0; i < count; i++) {
const col = columns.get(i);
console.log(col.getIndex());
}
```  

## **Wo man Enumerators verwenden sollte**  

Um die Vorteile der Verwendung von Enumerator zu besprechen, nehmen wir ein Beispiel in Echtzeit.  

**Szenario**  

Eine Anforderung der Anwendung besteht darin, alle Zellen in einem gegebenen [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) zu durchlaufen, um ihre Werte zu lesen. Es könnten mehrere Möglichkeiten geben, dieses Ziel zu implementieren. Einige sind unten dargestellt.  

### **Die Anzeigebereich verwenden**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Get Cells collection of first worksheet
const cells = workbook.getWorksheets().get(0).getCells();

// Get the MaxDisplayRange
const displayRange = cells.getMaxDisplayRange();

// Loop over all cells in the MaxDisplayRange
for (let row = displayRange.getFirstRow(); row < displayRange.getRowCount(); row++) {
for (let col = displayRange.getFirstColumn(); col < displayRange.getColumnCount(); col++) {
// Read the Cell value
console.log(displayRange.get(row, col).getStringValue());
}
}
```  

### **Verwenden von MaxDataRow & MaxDataColumn**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Get Cells collection of first worksheet
const cells2 = workbook.getWorksheets().get(0).getCells();
const maxDataRow = cells2.getMaxDataRow();
const maxDataColumn = cells2.getMaxDataColumn();

// Loop over all cells
for (let row = 0; row <= maxDataRow; row++) {
for (let col = 0; col <= maxDataColumn; col++) {
// Read the Cell value
const currentCell = cells2.checkCell(row, col);
if (currentCell) {
console.log(currentCell.getStringValue());
}
}
}
```  

Wie Sie beobachten können, verwenden beide oben genannten Ansätze mehr oder weniger ähnliche Logik, nämlich das Durchlaufen aller Zellen in der Sammlung, um die Zellwerte zu lesen. Dies könnte aus einer Reihe von Gründen problematisch sein, wie unten diskutiert.  

1. APIs wie [**getMaxRow()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getMaxRow--), [**getMaxDataRow()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getMaxDataRow--), [**getMaxColumn()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getMaxColumn--), [**getMaxDataColumn()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getMaxDataColumn--) & [**getMaxDisplayRange()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getMaxDisplayRange--) benötigen zusätzliche Zeit, um die entsprechenden Statistiken zu sammeln. Wenn die Datenmatrix (Zeilen x Spalten) groß ist, könnte die Verwendung dieser APIs eine Leistungseinbuße bedeuten.  
1. In den meisten Fällen sind nicht alle Zellen in einem bestimmten Bereich instanziiert. In solchen Situationen ist es nicht so effizient, jede Zelle in der Matrix zu überprüfen, im Vergleich dazu nur die initialisierten Zellen zu überprüfen.  
1. Das Zugreifen auf eine Zelle in einer Schleife als Cells row, column wird alle Zellenobjekte in einem Bereich instanziieren, was letztendlich zu einem OutOfMemoryException führen könnte.  

## **Fazit**  

Basierend auf den oben genannten Fakten sind die folgenden möglichen Szenarien, in denen Enumeratoren verwendet werden sollten.  

1. Nur Lesezugriff auf die Zellsammlung erforderlich ist, d.h. die Anforderung besteht darin, nur die Zellen zu inspizieren.  
1. Eine große Anzahl von Zellen muss durchlaufen werden.  
1. Nur initialisierte Zellen/Zeilen/Spalten müssen durchlaufen werden.  

