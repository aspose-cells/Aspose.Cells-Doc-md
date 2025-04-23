---
title: Berechnung von Formeln mit Node.js über C++
linktitle: Berechnung von Formeln
description: Dieser Artikel beschreibt, wie man die Aspose.Cells Bibliothek verwendet, um Formeln in Microsoft Excel mit Node.js via C++ zu berechnen. Durch das Laden einer bestehenden Excel Datei oder das Erstellen einer neuen Excel Datei können wir die Methoden von Aspose.Cells verwenden, um die Formel zu berechnen und das Ergebnis zu erhalten. Abschließend speichern wir die modifizierte Excel Datei auf Festplatte.
keywords: Aspose.Cells, Excel, Formeln, Berechnungen, Direkte Formelberechnung, Wiederholte Formelbfragen, Formeln in Node.js via C++ hinzufügen
type: docs
weight: 125
url: /de/nodejs-cpp/calculate-formulas/
---

## **Hinzufügen von Formeln & Berechnen von Ergebnissen**

Aspose.Cells verfügt über eine eingebaute Formelrechnungs-Engine. Es kann nicht nur Formeln, die aus Designer-Vorlagen importiert wurden, neu berechnen, sondern auch die Ergebnisse von Formeln, die zur Laufzeit hinzugefügt wurden, berechnen.

Aspose.Cells unterstützt die meisten Formeln oder Funktionen, die Teil von Microsoft Excel sind (lesen Sie [eine Liste der vom Berechnungs-Engine unterstützten Funktionen](/cells/de/nodejs-cpp/supported-formula-functions/)). Diese Funktionen können über die APIs oder Designer-Tabellen verwendet werden. Aspose.Cells unterstützt eine große Vielzahl an mathematischen, String-, booleschen, Datums-/Uhrzeit-, statistischen, Datenbank-, Lookup- und Referenzformeln.

Verwenden Sie die [**getFormula()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getFormula--)-Eigenschaft oder [**setFormula(string, object)**](https://reference.aspose.com/cells/nodejs-cpp/cell/#setFormula-string-object-)-Methoden der [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell)-Klasse, um eine Formel in eine Zelle einzufügen. Beim Anwenden einer Formel beginnt der String immer mit einem Gleichheitszeichen (=), so wie Sie es beim Erstellen einer Formel in Microsoft Excel tun, und verwenden Sie ein Komma (,) zur Trennung der Funktionsparameter.

Um die Ergebnisse von Formeln zu berechnen, kann der Benutzer die [**calculateFormula()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#calculateFormula--)-Methode der [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)-Klasse aufrufen, die alle in einer Excel-Datei eingebetteten Formeln verarbeitet. Oder, der Benutzer kann die [**calculateFormula(string)**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#calculateFormula-string-)-Methode der [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)-Klasse aufrufen, die alle in einem Blatt eingebetteten Formeln verarbeitet. Oder der Benutzer kann auch die [**calculate(CalculationOptions)**](https://reference.aspose.com/cells/nodejs-cpp/cell/#calculate-calculationoptions-)-Methode der [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell)-Klasse aufrufen, die die Formel einer einzelnen Zelle verarbeitet:

```javascript
const path = require("path");
const fs = require("fs");
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

### **Wichtiges zu Formeln**

{{% alert color="primary" %}}

Die Eigenschaften **Formel** und die Methoden **setFormula(...)** der [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell)-Klasse funktionieren anders als die **calculate**-Methoden der [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook), [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) und [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell)-Klassen. Die Eigenschaften **Formel** und **setFormula(...)** fügen die Formel lediglich einer Zelle hinzu, berechnen das Ergebnis aber nicht zur Laufzeit. Um die Ergebnisse der Formeln zu erhalten, rufen Sie bitte die **calculate**-Methoden auf.

{{% /alert %}}

## **Direkte Berechnung von Formeln**

Aspose.Cells verfügt über einen eingebetteten Formelberechnungsmotor. Neben der Berechnung von Formeln, die aus einer Designerdatei importiert wurden, kann Aspose.Cells auch Formelergebnisse direkt berechnen.

Manchmal müssen Sie Formelergebnisse direkt berechnen, ohne sie in ein Arbeitsblatt einzufügen. Die Werte der in der Formel verwendeten Zellen sind bereits in einem Arbeitsblatt vorhanden, und alles, was Sie brauchen, ist, das Ergebnis dieser Werte basierend auf einer Microsoft-Excel-Formel zu finden, ohne die Formel ins Arbeitsblatt einzufügen.

Sie können die APIs der Aspose.Cells-Formelberechnung engine für [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) bis [**calculateFormula(string, FormulaParseOptions, CalculationOptions, number, number, CalculationData)**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#calculateFormula-string-formulaparseoptions-calculationoptions-number-number-calculationdata-) nutzen, um die Ergebnisse solcher Formeln zu ermitteln, ohne sie ins Arbeitsblatt einzufügen:

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create a workbook
const workbook = new AsposeCells.Workbook();

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Put 20 in cell A1
const cellA1 = worksheet.getCells().get("A1");
cellA1.putValue(20);

// Put 30 in cell A2
const cellA2 = worksheet.getCells().get("A2");
cellA2.putValue(30);

// Calculate the Sum of A1 and A2
const results = worksheet.calculateFormula("=Sum(A1:A2)");

// Print the output
console.log("Value of A1: " + cellA1.getStringValue());
console.log("Value of A2: " + cellA2.getStringValue());
console.log("Result of Sum(A1:A2): " + results.toString());
```

Der obige Code erzeugt die folgende Ausgabe:
{{< highlight nodejs >}}
Value of A1: 20
Value of A2: 30
Result of Sum(A1:A2): 50.0
{{< /highlight >}}

## **Wie man Formeln wiederholt berechnet**

Wenn es viele Formeln im Arbeitsbuch gibt und der Benutzer sie mehrfach berechnen muss, während er nur einen kleinen Teil verändert, kann es performancefördernd sein, die Formelberechnungskette zu aktivieren: [**formulaSettings.getEnableCalculationChain()**](https://reference.aspose.com/cells/nodejs-cpp/formulasettings/#getEnableCalculationChain--).

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Load the template workbook
const workbook = new AsposeCells.Workbook(path.join(dataDir, "book1.xls"));

// Print the time before formula calculation
console.log(new Date());

// Set the CreateCalcChain as true
workbook.getSettings().getFormulaSettings().setEnableCalculationChain(true);

// Calculate the workbook formulas
workbook.calculateFormula();

// Print the time after formula calculation
console.log(new Date());

// Change the value of one cell
workbook.getWorksheets().get(0).getCells().get("A1").putValue("newvalue");

// Re-calculate those formulas which depend on cell A1
workbook.calculateFormula();
```

### **Wichtig zu wissen**

{{% alert color="primary" %}}

Standardmäßig ist die Berechnungskette deaktiviert. Da das Erstellen der Kette zusätzliche Zeit benötigt, kann die erste Berechnung der Formeln ([**Workbook.calculateFormula()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#calculateFormula--)) mehr CPU-Verarbeitungszeit und Speicher benötigen im Vergleich zur Berechnung ohne Kette. Wenn der Benutzer Formeln nicht wiederholt berechnen muss, ist das Standardverhalten (Direkte Berechnung ohne Kettenbildung) wahrscheinlich die bessere Wahl.

{{% /alert %}}

## **Erweiterte Themen**
- [Zellen zur Microsoft Excel-Formelüberwachung hinzufügen](/cells/de/nodejs-cpp/add-cells-to-microsoft-excel-formula-watch-window/)
- [Berechnung der IFNA-Funktion mit Aspose.Cells](/cells/de/nodejs-cpp/calculating-ifna-function-using-aspose-cells/)
- [Berechnung der Arrayformel von Datenblättern](/cells/de/nodejs-cpp/calculation-of-array-formula-of-data-tables/)
- [Berechnung der Excel 2016 MINIFS- und MAXIFS-Funktionen](/cells/de/nodejs-cpp/calculation-of-excel-2016-minifs-and-maxifs-functions/)
- [Berechnungszeit der Cell.calculate-Methode reduzieren](/cells/de/nodejs-cpp/decrease-the-calculation-time-of-cell-calculate-method/)
- [Erkennen von zirkulären Verweisen](/cells/de/nodejs-cpp/detecting-circular-reference/)
- [Direkte Berechnung einer benutzerdefinierten Funktion ohne Eintragung in ein Arbeitsblatt](/cells/de/nodejs-cpp/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/)
- [Implementieren eines benutzerdefinierten Berechnungsmotors zur Erweiterung des Standard-Berechnungsmotors von Aspose.Cells](/cells/de/nodejs-cpp/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/)
- [Unterbrechen oder Abbrechen der Formelberechnung des Arbeitsbuchs](/cells/de/nodejs-cpp/interrupt-or-cancel-the-formula-calculation-of-workbook/)
- [Rückgabe eines Bereichs von Werten unter Verwendung von AbstractCalculationEngine](/cells/de/nodejs-cpp/returning-a-range-of-values-using-abstractcalculationengine/)
- [Festlegen des Formelberechnungsmodus des Arbeitsbuchs](/cells/de/nodejs-cpp/setting-formula-calculation-mode-of-workbook/)
- [Verwendung der FormulaText-Funktion in Aspose.Cells](/cells/de/nodejs-cpp/using-formulatext-function-in-aspose-cells/)
