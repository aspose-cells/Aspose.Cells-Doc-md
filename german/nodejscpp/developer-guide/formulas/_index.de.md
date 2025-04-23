---
title: Verwalten Sie Formeln von Excel Dateien mit Node.js über C++
linktitle: Formeln
type: docs
weight: 122
url: /de/nodejs-cpp/using-formulas-or-functions-to-process-data/
description: Erfahren Sie, wie Sie Formeln in Excel Dateien mit Aspose.Cells for Node.js via C++ verwalten. Aspose.Cells kann Formeln einfach abrufen, setzen und berechnen.
keywords: Wie man Formeln in Node.js über C++ berechnet, Formeln und Funktionen mit Node.js über C++, Node.js über C++ verwaltet eingebaute Funktionen, Wie man Add in Funktionen mit Node.js über C++ verwendet, Wie man Array Formeln mit Node.js über C++ anwendet, Wie man R1C1 Formeln in Node.js über C++ nutzt.
---

## **Einführung**

Eines der überzeugenden Merkmale von Microsoft Excel ist seine Fähigkeit, Daten mit Formeln und Funktionen zu verarbeiten. Microsoft Excel bietet eine Reihe integrierter Funktionen und Formeln, die Benutzern helfen, komplexe Berechnungen schnell durchzuführen. Aspose.Cells bietet ebenfalls eine große Menge an integrierten Funktionen und Formeln, die Entwicklern helfen, Werte einfach zu berechnen. Aspose.Cells unterstützt auch Add-In-Funktionen. Zudem unterstützt Aspose.Cells Array- und R1C1-Formeln.

## **Wie man Formeln und Funktionen verwendet**

Aspose.Cells bietet eine Klasse, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook), die eine Microsoft Excel-Datei repräsentiert. Die Klasse [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) enthält eine [**getWorksheets()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--)-Sammlung, die Zugriff auf jedes Arbeitsblatt in der Excel-Datei ermöglicht. Ein Arbeitsblatt wird durch die Klasse [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) repräsentiert. Die Klasse [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) bietet eine [**getCells()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--)-Sammlung. Jedes Element in der Cells-Sammlung repräsentiert ein Objekt der Klasse [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell).

Es ist möglich, Formeln auf Zellen anzuwenden, indem Eigenschaften und Methoden verwendet werden, die von der Klasse [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell) angeboten werden, die im Folgenden näher erläutert werden.

- Verwendung von integrierten Funktionen.
- Verwendung von Add-In-Funktionen.
- Arbeit mit Array-Formeln.
- Erstellen einer R1C1-Formel.

## **Verwendung von integrierten Funktionen**

Eingebaute Funktionen oder Formeln sind als fertige Funktionen bereitgestellt, um den Aufwand und die Zeit der Entwickler zu reduzieren. Siehe [eine Liste der unterstützten eingebauten Funktionen](/cells/de/nodejs-cpp/supported-formula-functions/), die von Aspose.Cells unterstützt werden. Die Funktionen sind alphabetisch aufgelistet. Weitere Funktionen werden in zukünftigen Versionen unterstützt.

Aspose.Cells unterstützt die meisten Formeln und Funktionen, die von Microsoft Excel angeboten werden. Entwickler können diese Formeln über die API oder [Designer-Tabellenvorlage](/cells/de/nodejs-cpp/what-is-a-designer-spreadsheet/) verwenden. Aspose.Cells unterstützt eine große Anzahl von mathematischen, Zeichenketten-, booleschen, Datum/Zeit-, statistischen, Datenbank-, Lookup- und Referenz-Formeln.

Verwenden Sie die [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell)-Eigenschaft der Klasse [**getFormula()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getFormula--), um einer Zelle eine Formel hinzuzufügen. **Komplexe Formeln**, zum Beispiel

{{< highlight java >}}

 = H7*(1+IF(P7 = $L$3,$M$3, (IF(P7=$L$4,$M$4,0))))

{{< /highlight >}}

, werden auch von Aspose.Cells unterstützt. Beim Anwenden einer Formel auf eine Zelle beginnen Sie immer die Zeichenfolge mit einem Gleichheitszeichen (=), wie Sie es bei der Erstellung einer Formel in Microsoft Excel tun, und verwenden ein Komma (,) zur Trennung der Funktionsparameter.

Im folgenden Beispiel wird eine komplexe Formel auf die erste Zelle der [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells)-Sammlung eines Arbeitsblatts angewendet. Die Formel verwendet eine integrierte **IF**-Funktion von Aspose.Cells.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Adding a new worksheet to the Excel object
const sheetIndex = workbook.getWorksheets().add();

// Obtaining the reference of the newly added worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(sheetIndex);

// Adding a value to "A1" cell
worksheet.getCells().get("A1").putValue(1);

// Adding a value to "A2" cell
worksheet.getCells().get("A2").putValue(2);

// Adding a value to "A3" cell
worksheet.getCells().get("A3").putValue(3);

// Adding a SUM formula to "A4" cell
worksheet.getCells().get("A4").setFormula("=SUM(A1:A3)");

// Calculating the results of formulas
workbook.calculateFormula();

// Get the calculated value of the cell
const value = worksheet.getCells().get("A4").getValue().toString();

// Saving the Excel file
workbook.save(path.join(dataDir, "output.xls"));
```

## **Verwendung von Add-in-Funktionen**

Es können benutzerdefinierte Formeln definiert werden, die als Excel-Add-In eingebunden werden sollen. Beim Setzen der Zell.Formel-Funktion funktionieren integrierte Funktionen gut, jedoch ist es erforderlich, benutzerdefinierte Funktionen oder Formeln unter Verwendung von Add-In-Funktionen zu setzen.

Aspose.Cells bietet Funktionen zur Registrierung von Add-In-Funktionen mit [**Worksheets.registerAddInFunction(string, string, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection/#registerAddInFunction-string-string-boolean-). Anschließend, wenn wir cell.Formula = anyFunctionFromAddIn setzen, enthält die Ausgabedatei Excel den berechneten Wert aus der AddIn-Funktion.

Die folgende XLAM-Datei soll zum Registrieren der Add-In-Funktion verwendet werden im untenstehenden Beispielcode. Ebenso kann die Ausgabedatei "test_udf.xlsx" heruntergeladen werden, um die Ausgabe zu überprüfen.

[TestUDF.xlam](81920908.xlam)

[test_udf.xlsx](81920909.xlsx)

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const outputDir = path.join(__dirname, "output");

// Create empty workbook
const workbook = new AsposeCells.Workbook();

// Register macro enabled add-in along with the function name
const id = workbook.getWorksheets().registerAddInFunction(path.join(dataDir, "TESTUDF.xlam"), "TEST_UDF", false);

// Register more functions in the file (if any)
workbook.getWorksheets().registerAddInFunction(id, "TEST_UDF1"); // in this way you can add more functions that are in the same file

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access first cell
const cell = worksheet.getCells().get("A1");

// Set formula name present in the add-in
cell.setFormula("=TEST_UDF()");

// Save workbook to output XLSX format.
workbook.save(path.join(outputDir, "test_udf.xlsx"), AsposeCells.SaveFormat.Xlsx);
```

## **Verwendung von Array-Formel**

Array-Formeln sind Formeln, die Arrays anstelle von einzelnen Zahlen als Argumente für die Funktionen, die die Formel bilden, verwenden. Wenn eine Array-Formel angezeigt wird, ist sie von geschweiften Klammern ({}) umgeben.

Einige Microsoft Excel-Funktionen geben Arrays von Werten zurück. Um mehrere Ergebnisse mit einer Array-Formel zu berechnen, geben Sie das Array in einen Zellenbereich mit derselben Anzahl von Zeilen und Spalten wie die Array-Argumente ein.

Es ist möglich, einer Zelle eine Array-Formel durch Aufruf der Methode [**setArrayFormula(string, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cell/#setArrayFormula-string-number-number-) der Klasse [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell) anzuwenden. Die Methode [**setArrayFormula(string, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cell/#setArrayFormula-string-number-number-) nimmt die folgenden Parameter an:

- **Array-Formel**, die Array-Formel.
- **Anzahl der Zeilen**, die Anzahl der Zeilen zum Ausfüllen des Ergebnisses der Array-Formel.
- **Anzahl der Spalten**, die Anzahl der Spalten zum Ausfüllen des Ergebnisses der Array-Formel.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Adding a new worksheet to the Excel object
const sheetIndex = workbook.getWorksheets().add();

// Obtaining the reference of the newly added worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(sheetIndex);

// Adding a value to "A1" cell
worksheet.getCells().get("A1").putValue(1);

// Adding a value to "A2" cell
worksheet.getCells().get("A2").putValue(2);

// Adding a value to "A3" cell
worksheet.getCells().get("A3").putValue(3);

// Adding a value to B1
worksheet.getCells().get("B1").putValue(4);

// Adding a value to "B2" cell
worksheet.getCells().get("B2").putValue(5);

// Adding a value to "B3" cell
worksheet.getCells().get("B3").putValue(6);

// Adding a value to C1
worksheet.getCells().get("C1").putValue(7);

// Adding a value to "C2" cell
worksheet.getCells().get("C2").putValue(8);

// Adding a value to "C3" cell
worksheet.getCells().get("C3").putValue(9);

// Adding a SUM formula to "A4" cell
worksheet.getCells().get("A6").setArrayFormula("=LINEST(A1:A3,B1:C3,TRUE,TRUE)", 5, 3);

// Calculating the results of formulas
workbook.calculateFormula();

// Get the calculated value of the cell
const value = worksheet.getCells().get("A6").getValue().toString();

// Saving the Excel file
workbook.save(path.join(dataDir, "output.xls"));
```

## **Verwendung der R1C1-Formel**

Fügen Sie einer Zelle mit der [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell) Klasse die Eigenschaft [**getR1C1Formula()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getR1C1Formula--) hinzu.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xls");
// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook(filePath);

const worksheet = workbook.getWorksheets().get(0);

// Setting an R1C1 formula on the "A11" cell, 
// Row and Column indices are relative to destination index
worksheet.getCells().get("A11").setR1C1Formula("=SUM(R[-10]C[0]:R[-7]C[0])");

// Saving the Excel file
workbook.save(path.join(dataDir, "output.xls"));
```

## **Erweiterte Themen**
- [Vorgänger und Abhängige](/cells/de/nodejs-cpp/precedents-and-dependents/)
- [Externe Verknüpfungen in Formeln festlegen](/cells/de/nodejs-cpp/set-external-links-in-formulas/)
- [Formel in Tabelle oder List-Objekt automatisch propagieren, während neue Zeilen eingegeben werden](/cells/de/nodejs-cpp/propagate-formula-in-table-or-list-object-automatically-while-entering-data-in-new-rows/)
- [Formel für benanntes Bereich setzen](/cells/de/nodejs-cpp/setting-formula-for-named-range/)
- [Formeln einstellen - Hinweis für nicht englischsprachige Benutzer](/cells/de/nodejs-cpp/setting-formulas-notice-for-non-english-users/)
- [Gemeinsame Formel festlegen](/cells/de/nodejs-cpp/setting-shared-formula/)
- [Maximale Zeilen der gemeinsamen Formel angeben](/cells/de/nodejs-cpp/specify-maximum-rows-of-shared-formula/)
- [Unterstützte Excel-Funktionen](/cells/de/nodejs-cpp/supported-formula-functions/)

