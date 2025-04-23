---
title: Implementa Cell.FormulaLocal simile a Excel VBA Range.FormulaLocal con Node.js via C++
linktitle: Implementa la Cell.FormulaLocal simile a Excel VBA Range.FormulaLocal
type: docs
weight: 30
url: /it/nodejs-cpp/implement-cell-formulalocal-similar-to-excel-vba-range-formulalocal/
description: Impara come implementare Cell.FormulaLocal simile a Excel VBA Range.FormulaLocal usando Aspose.Cells for Node.js via C++. 
---

## **Possibili Scenari di Utilizzo**

Le formule di Microsoft Excel potrebbero avere nomi diversi in diverse localizzazioni, regioni o lingue. Ad esempio, la funzione **SUM** si chiama **SUMME** in tedesco. Aspose.Cells non può lavorare con nomi di funzioni non in inglese. In Microsoft Excel VBA, c'è la proprietà **Range.FormulaLocal** che restituisce il nome della funzione secondo la lingua o regione. Aspose.Cells for Node.js via C++ fornisce anche la proprietà [**Cell.getFormulaLocal()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getFormulaLocal--) a questo scopo. Tuttavia, questa proprietà funzionerà solo quando si implementa il metodo [**GlobalizationSettings.getLocalFunctionName(standardName)**](https://reference.aspose.com/cells/nodejs-cpp/globalizationsettings/#getLocalFunctionName-string-).

## **Implementa Cell.FormulaLocal simile a Excel VBA Range.FormulaLocal**

Il seguente esempio di codice spiega come implementare il metodo [**GlobalizationSettings.getLocalFunctionName(standardName)**](https://reference.aspose.com/cells/nodejs-cpp/globalizationsettings/#getLocalFunctionName-string-). Il metodo restituisce il nome locale della funzione standard. Se il nome della funzione standard è **SUM**, ritorna **UserFormulaLocal_SUM**. Puoi modificare il codice secondo le tue esigenze e restituire i nomi corretti delle funzioni locali, ad esempio **SUM** è **SUMME** in tedesco e **TEXT** è **ТЕКСТ** in Russo. Vedi anche l'output sulla console del codice di esempio fornito sotto per riferimento.

## **Codice di Esempio**

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

## **Output della console**

{{< highlight javascript >}}

Formula Local: =UserFormulaLocal_SUM(A1:A2)

Formula Local: =UserFormulaLocal_AVERAGE(B1:B2,B5)

{{< /highlight >}}
