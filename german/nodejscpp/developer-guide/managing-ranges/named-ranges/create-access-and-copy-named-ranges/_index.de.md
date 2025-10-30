---  
title: Named Ranges mit Node.js über C++ erstellen und kopieren  
linktitle: Zugriff erstellen und benannte Bereiche kopieren  
type: docs  
weight: 200  
url: /de/nodejs-cpp/create-access-and-copy-named-ranges/  
description: Erfahren Sie, wie man benannte Bereiche in Excel mit Aspose.Cells for Node.js via C++ erstellt, zugreift und kopiert.  
---  

## **Einführung**  

Normalerweise werden Spalten- und Zeilenlabels verwendet, um einzelne Zellen zu referenzieren. Es ist möglich, beschreibende Namen zu erstellen, um Zellen, Zellbereiche, Formeln oder Konstanten zu repräsentieren. Das Wort **Name** kann sich auf eine Zeichenkette beziehen, die eine Zelle, einen Zellbereich, eine Formel oder einen Konstantenwert darstellt. Das Zuweisen eines Namens zu einem Bereich bedeutet, dass dieser Zellbereich anhand seines Namens referenziert werden kann. Verwenden Sie leicht verständliche Namen, wie Produkte, um schwer verständliche Bereiche wie Verkäufe!C20:C30 zu repräsentieren. Labels können in Formeln verwendet werden, die sich auf Daten im selben Arbeitsblatt beziehen; wenn Sie einen Bereich auf einem anderen Arbeitsblatt darstellen möchten, können Sie einen Namen verwenden. *Benannte Bereiche gehören zu den leistungsstärksten Funktionen von Microsoft Excel, insbesondere wenn sie als Quellbereich für Listensteuerungen, Pivot-Tabellen, Diagramme usw. verwendet werden.*  

## **Arbeiten mit benannten Bereich unter Verwendung von Microsoft Excel**  

### **Benannte Bereiche erstellen**  

Die folgenden Schritte beschreiben, wie man eine Zelle oder einen Zellbereich mit **MS Excel** benennt. Diese Methode gilt für **Microsoft Office Excel 2003**, **Microsoft Excel 97**, **2000** und **2002**.  

1. Wählen Sie die Zelle oder den Zellbereich aus, den Sie benennen möchten.  
2. Klicken Sie auf das **Namensfeld** am linken Ende der Formelleiste.  
3. Geben Sie den Namen für die Zellen ein.  
4. Drücken Sie ENTER.  

{{% alert color="primary" %}}  
Sie können eine Zelle nicht benennen, während Sie den Inhalt der Zelle ändern.  
{{% /alert %}}  

## **Arbeiten mit benannten Bereich unter Verwendung von Aspose.Cells**  

Hier verwenden wir die Aspose.Cells API, um die Aufgabe zu erledigen.  
Aspose.Cells bietet eine Klasse [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook), die eine Microsoft Excel-Datei repräsentiert. Die Klasse [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) enthält eine [**getWorksheets()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--)-Sammlung, die den Zugriff auf jede Arbeitsmappe in einer Excel-Datei ermöglicht. Eine Arbeitsmappe wird durch die Klasse [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) repräsentiert. Die Klasse [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) bietet eine [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells)-Sammlung.  

### **Benannten Bereich erstellen**  

Es ist möglich, einen benannten Bereich zu erstellen, indem die überladene [**createRange(string, string)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#createRange-string-string-)-Methode der [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells)-Sammlung aufgerufen wird. Eine typische Version der [**createRange(string)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#createRange-string-)-Methode nimmt die folgenden Parameter:  

- Name der oberen linken Zelle, Name der oberen linken Zelle im Bereich.  
- Name der unteren rechten Zelle, Name der unteren rechten Zelle im Bereich.  

Wenn die Methode [**createRange(string)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#createRange-string-) aufgerufen wird, wird der neu erstellte Bereich als Instanz der Klasse [**Range**](https://reference.aspose.com/cells/nodejs-cpp/range) zurückgegeben. Verwenden Sie dieses Objekt [**Range**](https://reference.aspose.com/cells/nodejs-cpp/range), um den benannten Bereich zu konfigurieren. Setzen Sie beispielsweise den Namen des Bereichs mit der [**getName()**](https://reference.aspose.com/cells/nodejs-cpp/range/#getName--)-Eigenschaft. Das folgende Beispiel zeigt, wie man einen benannten Bereich von Zellen erstellt, der sich über B4:G14 erstreckt.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Opening the Excel file through the file stream
const workbook = new AsposeCells.Workbook(path.join(dataDir, "book1.xls"));

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Creating a named range
const range = worksheet.getCells().createRange("B4", "G14");

// Setting the name of the named range
range.setName("TestRange");

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.out.xls"));
```  

### **Daten in die Zellen des benannten Bereichs eingeben**  

Sie können Daten in die einzelnen Zellen eines Bereichs einfügen, indem Sie dem Muster folgen  

- **JavaScript**: Range[row,Spalte]  

Angenommen, Sie haben einen benannten Bereich von Zellen, der sich über A1:C4 erstreckt. Die Matrix enthält 4 * 3 = 12 Zellen. Die einzelnen Bereichszellen sind sequentiell angeordnet: Bereich[0,0], Bereich[0,1], Bereich[0,2], Bereich[1,0], Bereich[1,1], Bereich[1,2], Bereich[2,0], Bereich[2,1], Bereich[2,2], Bereich[3,0], Bereich[3,1], Bereich[3,2].  

Verwenden Sie die folgenden Eigenschaften, um die Zellen im Bereich zu identifizieren:  

- firstRow gibt den Index der ersten Zeile im benannten Bereich zurück.  
- firstColumn gibt den Index der ersten Spalte im benannten Bereich zurück.  
- rowCount gibt die Gesamtzahl der Zeilen im benannten Bereich zurück.  
- columnCount gibt die Gesamtzahl der Spalten im benannten Bereich zurück.  

Das folgende Beispiel zeigt, wie einige Werte in die Zellen eines bestimmten Bereichs eingegeben werden.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook();

// Get the first worksheet in the workbook.
const worksheet1 = workbook.getWorksheets().get(0);

// Create a range of cells based on H1:J4.
const range = worksheet1.getCells().createRange("H1", "J4");

// Name the range.
range.setName("MyRange");

// Input some data into cells in the range.
range.get(0, 0).setValue("USA");
range.get(0, 1).setValue("SA");
range.get(0, 2).setValue("Israel");
range.get(1, 0).setValue("UK");
range.get(1, 1).setValue("AUS");
range.get(1, 2).setValue("Canada");
range.get(2, 0).setValue("France");
range.get(2, 1).setValue("India");
range.get(2, 2).setValue("Egypt");
range.get(3, 0).setValue("China");
range.get(3, 1).setValue("Philipine");
range.get(3, 2).setValue("Brazil");

// Save the excel file.
workbook.save(path.join(dataDir, "rangecells.out.xls"));
```  

### **Zellen im benannten Bereich identifizieren**  

Sie können Daten in die einzelnen Zellen eines Bereichs einfügen, indem Sie dem Muster folgen:  

- **JavaScript**: Range[row,Spalte]  

Wenn Sie einen benannten Bereich haben, der A1:C4 umfasst. Die Matrix umfasst 4 * 3 = 12 Zellen. Die einzelnen Bereichszellen sind sequentiell angeordnet: Bereich[0,0], Bereich[0,1], Bereich[0,2], Bereich[1,0] ,Bereich[1,1], Bereich[1,2], Bereich[2,0], Bereich[2,1], Bereich[2,2], Bereich[3,0], Bereich[3,1], Bereich[3,2].  

Verwenden Sie die folgenden Eigenschaften, um die Zellen im Bereich zu identifizieren:  

- firstRow gibt den Index der ersten Zeile im benannten Bereich zurück.  
- firstColumn gibt den Index der ersten Spalte im benannten Bereich zurück.  
- rowCount gibt die Gesamtzahl der Zeilen im benannten Bereich zurück.  
- columnCount gibt die Gesamtzahl der Spalten im benannten Bereich zurück.  

Das folgende Beispiel zeigt, wie einige Werte in die Zellen eines bestimmten Bereichs eingegeben werden.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook(path.join(dataDir, "book1_testrange.xls"));

// Getting the specified named range
const range = workbook.getWorksheets().getRangeByName("TestRange");

// Identify range cells.
console.log("First Row : " + range.getFirstRow());
console.log("First Column : " + range.getFirstColumn());
console.log("Row Count : " + range.getRowCount());
console.log("Column Count : " + range.getColumnCount());
```  

### **Zugriff auf benannte Bereiche**  

#### **Auf einen bestimmten benannten Bereich zugreifen**  

Rufen Sie die Methode [**getRangeByName(string)**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection/#getRangeByName-string-) der [**worksheets**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection)-Sammlung auf, um einen Bereich nach dem angegebenen Namen zu erhalten. Eine typische [**getRangeByName(string)**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection/#getRangeByName-string-)-Methode nimmt den Namen des benannten Bereichs entgegen und gibt den angegebenen benannten Bereich als Instanz der [**Range**](https://reference.aspose.com/cells/nodejs-cpp/range)-Klasse zurück. Das folgende Beispiel zeigt, wie auf einen bestimmten Bereich nach seinem Namen zugegriffen wird.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Opening the Excel file through the file stream
const workbook = new AsposeCells.Workbook(path.join(dataDir, "book1_testrange.xls"));

// Getting the specified named range
const range = workbook.getWorksheets().getRangeByName("TestRange");

if (range !== null) 
{
console.log("Named Range : " + range.getRefersTo());
}
```  

#### **Zugriff auf alle benannten Bereiche in einer Arbeitsmappe**  

Rufen Sie die [**worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection)-Sammlung auf, um die [**getNamedRanges()**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection/#getNamedRanges--)-Methode aufzurufen und alle benannten Bereiche in einer Tabelle zu erhalten. Die [**getNamedRanges()**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection/#getNamedRanges--)-Methode gibt ein Array aller benannten Bereiche in der [**worksheets**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection)-Sammlung zurück.  

Das folgende Beispiel zeigt, wie auf alle benannten Bereiche in einer Arbeitsmappe zugegriffen wird.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Opening the Excel file through the file stream
const workbook = new AsposeCells.Workbook(path.join(dataDir, "book1.xls"));

// Getting all named ranges
const ranges = workbook.getWorksheets().getNamedRanges();

if (ranges != null) {
console.log("Total Number of Named Ranges: " + ranges.length);
}
```  

### **Benannte Bereiche kopieren**  

Aspose.Cells bietet die [**range.copy(Range, PasteOptions)**](https://reference.aspose.com/cells/nodejs-cpp/range/#copy-range-pasteoptions-)-Methode zum Kopieren eines Zellenbereichs mit Formatierung in einen anderen Bereich.  

Das folgende Beispiel zeigt, wie ein Quellbereich von Zellen in einen anderen benannten Bereich kopiert wird.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");
// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook();

// Get all the worksheets in the book.
const worksheets = workbook.getWorksheets();

// Get the first worksheet in the worksheets collection.
const worksheet = workbook.getWorksheets().get(0);

// Create a range of cells.
const range1 = worksheet.getCells().createRange("E12", "I12");

// Name the range.
range1.setName("MyRange");

// Set the outline border to the range.
range1.setOutlineBorder(AsposeCells.BorderType.TopBorder, AsposeCells.CellBorderType.Medium, new AsposeCells.Color(0, 0, 128));
range1.setOutlineBorder(AsposeCells.BorderType.BottomBorder, AsposeCells.CellBorderType.Medium, new AsposeCells.Color(0, 0, 128));
range1.setOutlineBorder(AsposeCells.BorderType.LeftBorder, AsposeCells.CellBorderType.Medium, new AsposeCells.Color(0, 0, 128));
range1.setOutlineBorder(AsposeCells.BorderType.RightBorder, AsposeCells.CellBorderType.Medium, new AsposeCells.Color(0, 0, 128));

// Input some data with some formattings into
// A few cells in the range.
range1.get(0, 0).putValue("Test");
range1.get(0, 4).putValue("123");

// Create another range of cells.
const range2 = worksheet.getCells().createRange("B3", "F3");

// Name the range.
range2.setName("testrange");

// Copy the first range into second range.
range2.copy(range1);

// Save the excel file.
workbook.save(path.join(dataDir, "copyranges.out.xls"));
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
