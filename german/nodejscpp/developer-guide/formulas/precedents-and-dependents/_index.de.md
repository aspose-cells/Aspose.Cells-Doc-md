---
title: Voraussetzungen und Abhängigkeiten mit Node.js über C++
linktitle: Vorgänger und Abhängige
type: docs
weight: 230
url: /de/nodejs-cpp/precedents-and-dependents/
description: Lernen Sie, vorgelagerte und nachgelagerte Zellen in Tabellenblättern mit Aspose.Cells for Node.js via C++ zu verfolgen. Verstehen Sie, wie verbundene Zellen in komplexen Finanzarbeitsblättern erkannt werden.
---

{{% alert color="primary" %}} 

Komplexe Finanzarbeitsblätter, insbesondere solche, die in Zusammenarbeit entwickelt wurden, können die peinlichsten Fehler verbergen. Formeln auf ihre Genauigkeit zu überprüfen und die Fehlerquelle zu finden, kann schwierig sein, wenn die Formel Vorgänger- und Abhängigenzellen verwendet.

{{% /alert %}} 
## **Einführung**
- **Vorgängerzellen** sind Zellen, auf die in einer anderen Zelle eine Formel verweist. Wenn beispielsweise Zelle D10 die Formel =B5 enthält, dann ist die Zelle B5 ein Vorgänger von Zelle D10.
- **Abhängige Zellen** enthalten Formeln, die sich auf andere Zellen beziehen. Zum Beispiel, wenn Zelle D10 die Formel =B5 enthält, ist D10 abhängig von B5.

Um die Tabelle übersichtlicher zu gestalten, möchten Sie möglicherweise klar zeigen, welche Zellen in einer Tabelle in einer Formel verwendet werden. Ebenso möchten Sie die abhängigen Zellen anderer Zellen extrahieren.

Aspose.Cells ermöglicht es Ihnen, die Zellen zu verfolgen und herauszufinden, welche verknüpft sind.
## **Vorgänger- und Abhängige Zellen verfolgen: Microsoft Excel**
Formeln können sich ändern, basierend auf Änderungen, die von einem Kunden vorgenommen wurden. Wenn beispielsweise die Zelle C1 von C3 und C4 abhängt, die eine Formel enthalten, und C1 geändert wird (d. h. die Formel überschrieben wird), müssen C3 und C4 oder andere Zellen entsprechend den Geschäftsregeln angepasst werden, um die Tabelle auszugleichen.

Ebenso angenommen, C1 enthält die Formel "=(B1*22)/(M2*N32)". Ich möchte die Zellen finden, von denen C1 abhängt, d. h. die vorhergehenden Zellen B1, M2 und N32.

Sie müssen möglicherweise die Abhängigkeit einer bestimmten Zelle zu anderen Zellen verfolgen. Wenn Geschäftsregeln in Formeln eingebettet sind, möchten wir die Abhängigkeit herausfinden und einige Regeln entsprechend ausführen. Ebenso, wenn der Wert einer bestimmten Zelle geändert wird, welche Zellen im Arbeitsblatt sind von dieser Änderung betroffen?

Microsoft Excel ermöglicht es Benutzern, Vorgänger und Abhängige zu verfolgen.

1. Auf der **Ansichts-Symbolleiste** wählen Sie **Formelüberwachung** aus. Der Dialog zur Formelüberwachung wird angezeigt.
1. Vorgänger verfolgen:
   1. Wählen Sie die Zelle aus, die die Formel enthält, für die Sie Vorgängerzellen finden möchten.
   1. Um an jede Zelle einen Tracer-Pfeil anzuzeigen, die direkt Daten an die aktive Zelle bereitstellt, klicken Sie auf **Vorgänger verfolgen** auf der **Formelüberwachungs**-Symbolleiste.
1. Formeln verfolgen, die auf eine bestimmte Zelle verweisen (Abhängige)
   1. Wählen Sie die Zelle aus, für die Sie die abhängigen Zellen identifizieren möchten.
   1. Um einen Nachverfolgungspfeil für jede Zelle anzuzeigen, die von der aktiven Zelle abhängig ist, klicken Sie auf **Abhängige nachverfolgen** in der Formel-Überprüfungsleiste.
## **Vorgänger- und Abhängige Zellen verfolgen: Aspose.Cells**
### **Vorgänger verfolgen**
Aspose.Cells erleichtert das Abrufen von Vorgängerzellen. Es kann nicht nur Zellen abrufen, die Daten zu einfachen Formelvorgängern bereitstellen, sondern auch Zellen finden, die Daten zu komplexen Formelvorgängern mit benannten Bereichen bereitstellen.

Im folgenden Beispiel wird eine Vorlagen-Excel-Datei, Book1.xls, verwendet. Das Arbeitsblatt enthält Daten und Formeln.

Aspose.Cells bietet die [Cell](https://reference.aspose.com/cells/nodejs-cpp/cell) Klasse mit der Methode [Cell.getPrecedents()](https://reference.aspose.com/cells/nodejs-cpp/cell/#getPrecedents--), um die Vorgänger einer Zelle zu verfolgen. Diese gibt eine Sammlung der referenzierten Bereiche zurück. Wie oben gezeigt, enthält in Book1.xls die Zelle B7 die Formel "=SUM(A1:A3)". Daher sind die Zellen A1:A3 die Vorgängerzellen von B7. Das folgende Beispiel zeigt die Funktion zum Nachverfolgen von Vorgängern mit der Vorlage Datei Book1.xls.


```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);
const cells = workbook.getWorksheets().get(0).getCells();
const cell = cells.get("B4");
// Check if the cell object is not null before proceeding
if (cell) 
{
const ret = cell.getPrecedents();
if (!ret.isNull() && ret.getCount() > 0)
{
const area = ret.get(0);
console.log(area.getSheetName());
console.log(AsposeCells.CellsHelper.cellIndexToName(area.getStartRow(), area.getStartColumn()));
console.log(AsposeCells.CellsHelper.cellIndexToName(area.getEndRow(), area.getEndColumn()));
}
else
{
console.error("No precedents found for the cell.");
}
} 
else 
{
console.error("Cell B4 is null.");
}
```
### **Abhängige verfolgen**
Aspose.Cells ermöglicht es, abhängige Zellen in Tabellenblättern zu erhalten. Aspose.Cells kann nicht nur Zellen abrufen, die Daten im Zusammenhang mit einer einfachen Formel liefern, sondern auch Zellen finden, die Daten zu komplexen Formeln mit benannten Bereichen liefern.

Aspose.Cells bietet die [Cell](https://reference.aspose.com/cells/nodejs-cpp/cell) Klasse mit der Methode [Cell.getDependents(boolean)](https://reference.aspose.com/cells/nodejs-cpp/cell/#getDependents-boolean-) zum Nachverfolgen der abhängigen Zellen. Zum Beispiel enthält in Book1.xlsx die Zelle B2 die Formel "=A1+20" und in C2 die Formel "=A1+30". Das folgende Beispiel zeigt, wie man die Abhängigen für die Zelle A1 mithilfe der Vorlage Datei Book1.xlsx verfolgt.


```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);
const cells = workbook.getWorksheets().get(0).getCells();
const cell = cells.get("B2");
// Ensure dependents is an array
const dependents = cell.getDependents(true);

if (Array.isArray(dependents)) 
{
for (const c of dependents) 
{
console.log(c.getName());
}
} 
else 
{
console.error("Dependents is not an array");
}
```
### **Nachverfolgung von Vorgänger- und abhängigen Zellen gemäß der Berechnungskette**
Die oben genannten APIs zum Nachverfolgen von Vorgängern und Abhängigkeiten basieren auf dem Formelausdruck selbst. Sie bieten einfach eine bequeme Möglichkeit, Interabhängigkeiten für einige Formeln zu verfolgen. Wenn im Arbeitsbuch eine große Anzahl von Formeln vorhanden ist und der Benutzer Vorgänger und Abhängige für jede Zelle verfolgen muss, wird die Leistung schlecht sein. Für solche Situationen sollten die Methoden [Cell.getPrecedentsInCalculation()](https://reference.aspose.com/cells/nodejs-cpp/cell/#getPrecedentsInCalculation--) und [Cell.getDependentsInCalculation(boolean)](https://reference.aspose.com/cells/nodejs-cpp/cell/#getDependentsInCalculation-boolean-) verwendet werden. Diese beiden Methoden verfolgen Abhängigkeiten basierend auf der Berechnungskette. Um sie zu verwenden, müssen Sie zunächst die Berechnungskette aktivieren mit [FormulaSettings.getEnableCalculationChain()](https://reference.aspose.com/cells/nodejs-cpp/formulasettings/#getEnableCalculationChain--). Danach führen Sie eine vollständige Berechnung für das Arbeitsbuch mit [Workbook.calculateFormula()](https://reference.aspose.com/cells/nodejs-cpp/workbook/#calculateFormula--) durch. Danach können Sie Vorgänger oder Abhängige für alle Zellen verfolgen, die Sie benötigen.

Für einige Formeln können die resultierenden Vorgänger unterschiedlich sein, je nachdem, ob Sie getPrecedents oder getPrecedentsInCalculation verwenden, und die abhängigen Zellen können unterschiedlich sein, je nachdem, ob Sie getDependents oder getDependentsInCalculation verwenden. Beispielsweise liefert die Formel in Zelle A1 "=IF(TRUE,B2,C3)" getPrecedents die Zellen B2 und C3 als Vorgänger von A1. Entsprechend haben sowohl B2 als auch C3 die abhängige Zelle A1 bei der Überprüfung mit getDependents. Für die Berechnung dieser Formel ist jedoch offensichtlich, dass nur B2 den berechneten Wert beeinflussen kann. Daher liefert getPrecedentsInCalculation für A1 kein C3 und getDependentsInCalculation für C3 kein A1. Manchmal hat der Benutzer nur die Anforderung, die tatsächlichen Interabhängigkeiten zu verfolgen, die die berechneten Ergebnisse der Formeln basierend auf den aktuellen Daten im Arbeitsbuch beeinflussen. In solchen Fällen sollten die Methoden getDependentsInCalculation/getPrecedentsInCalculation anstelle von getDependents/getPrecedents verwendet werden.

Das folgende Beispiel zeigt, wie man die Vorgänger und Abhängige anhand der Berechnungskette für Zellen verfolgt:


```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");
// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);
const cells = workbook.getWorksheets().get(0).getCells();
cells.get("A1").setFormula("=B1+SUM(B1:B10)+[Book1.xls]Sheet1!B2");
cells.get("A2").setFormula("=IF(TRUE,B2,B1)");
workbook.getSettings().getFormulaSettings().setEnableCalculationChain(true);
workbook.calculateFormula();

let en = cells.get("B1").getDependentsInCalculation(false);
console.log("B1's calculation dependents:");
for (var cell of en) {
console.log(cell.getName());
}


en = cells.get("B2").getDependentsInCalculation(false);
console.log("B2's calculation dependents:");
for (var cell of en) {
console.log(cell.getName());
}

en = cells.get("A1").getPrecedentsInCalculation();
console.log("A1's calculation precedents:");
for (var area of en) {
console.log(area.toString());
}


en = cells.get("A2").getPrecedentsInCalculation();
console.log("A2's calculation precedents:");
for (var area of en) {
console.log(area.toString());
}
```
{{< app/cells/assistant language="nodejs-cpp" >}}
