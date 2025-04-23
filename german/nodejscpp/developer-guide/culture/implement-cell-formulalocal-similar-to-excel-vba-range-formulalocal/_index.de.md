---
title: Implementieren Sie Cell.FormulaLocal ähnlich wie Excel VBA Range.FormulaLocal mit Node.js über C++
linktitle: Implementieren Sie Cell.FormulaLocal ähnlich wie Excel VBA Range.FormulaLocal
type: docs
weight: 30
url: /de/nodejs-cpp/implement-cell-formulalocal-similar-to-excel-vba-range-formulalocal/
description: Erfahren Sie, wie man Cell.FormulaLocal ähnlich wie Excel VBA Range.FormulaLocal mit Aspose.Cells for Node.js via C++ implementiert. 
---

## **Mögliche Verwendungsszenarien**

Microsoft Excel-Formeln können in verschiedenen Regionen, Ländern oder Sprachen unterschiedliche Namen haben. Zum Beispiel wird die **SUM**-Funktion in Deutsch **SUMME** genannt. Aspose.Cells kann nicht mit nicht-englischen Funktionsnamen arbeiten. In Microsoft Excel VBA gibt es die Eigenschaft **Range.FormulaLocal**, die den Funktionsnamen entsprechend der Sprache oder Region zurückgibt. Aspose.Cells for Node.js via C++ bietet auch die [**Cell.getFormulaLocal()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getFormulaLocal--)-Eigenschaft zu diesem Zweck an. Diese Eigenschaft funktioniert jedoch nur, wenn Sie die [**GlobalizationSettings.getLocalFunctionName(standardName)**](https://reference.aspose.com/cells/nodejs-cpp/globalizationsettings/#getLocalFunctionName-string-)-Methode implementieren.

## **Implementieren Sie Cell.FormulaLocal ähnlich wie Excel VBA Range.FormulaLocal**

Das folgende Beispiel erklärt, wie die [**GlobalizationSettings.getLocalFunctionName(standardName)**](https://reference.aspose.com/cells/nodejs-cpp/globalizationsettings/#getLocalFunctionName-string-)-Methode implementiert wird. Die Methode gibt den lokalen Namen der Standardfunktion zurück. Wenn der Standardfunktionsname **SUM** ist, gibt sie **UserFormulaLocal_SUM** zurück. Sie können den Code nach Ihren Bedürfnissen anpassen und die richtigen lokalen Funktionsnamen zurückgeben, z.B. ist **SUM** in Deutsch **SUMME** und **TEXT** in Russisch **ТЕКСТ**. Die Konsolenausgabe des unten stehenden Beispiels liefert ebenfalls Referenzinformationen.

## **Beispielcode**

```javascript
const AsposeCells = require("aspose.cells.node");

class GS extends AsposeCells.GlobalizationSettings {
getLocalFunctionName(standardName) {
// Change the SUM function name as per your needs.
if (standardName === "SUM") {
return "UserFormulaLocal_SUM";
}

// Change the AVERAGE function name as per your needs.
if (standardName === "AVERAGE") {
return "UserFormulaLocal_AVERAGE";
}

return "";
}
}

function run() {
// Create workbook
const wb = new AsposeCells.Workbook();

// Assign GlobalizationSettings implementation class
wb.getSettings().setGlobalizationSettings(new GS());

// Access first worksheet
const ws = wb.getWorksheets().get(0);

// Access some cell
const cell = ws.getCells().get("C4");

// Assign SUM formula and print its FormulaLocal
cell.setFormula("SUM(A1:A2)");
console.log("Formula Local: " + cell.getFormulaLocal());

// Assign AVERAGE formula and print its FormulaLocal
cell.setFormula("=AVERAGE(B1:B2, B5)");
console.log("Formula Local: " + cell.getFormulaLocal());
}

// Call the run function
run();
```

## **Konsolenausgabe**

{{< highlight javascript >}}

Formula Local: =UserFormulaLocal_SUM(A1:A2)

Formula Local: =UserFormulaLocal_AVERAGE(B1:B2,B5)

{{< /highlight >}}
