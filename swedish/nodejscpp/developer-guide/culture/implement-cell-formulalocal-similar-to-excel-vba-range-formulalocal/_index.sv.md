---
title: Implementera Cell.FormulaLocal liknande Excel VBA Range.FormulaLocal med Node.js via C++
linktitle: Implementera Cell.FormulaLocal liknande Excel VBA Range.FormulaLocal
type: docs
weight: 30
url: /sv/nodejs-cpp/implement-cell-formulalocal-similar-to-excel-vba-range-formulalocal/
description: Lär dig hur du implementerar Cell.FormulaLocal liknande Excel VBA Range.FormulaLocal med Aspose.Cells for Node.js via C++. 
---

## **Möjliga användningsscenario**

Microsoft Excel-formler kan ha olika namn i olika regioner eller språk. Till exempel kallas **SUM**-funktionen för **SUMME** på tyska. Aspose.Cells kan inte arbeta med icke-Engelska funktionsnamn. I Microsoft Excel VBA finns egenskapen **Range.FormulaLocal** som returnerar funktionsnamnet enligt språk eller region. Aspose.Cells for Node.js via C++ tillhandahåller också [**Cell.getFormulaLocal()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getFormulaLocal--)-egenskapen för detta ändamål. Denna egenskap fungerar dock endast när du implementerar [**GlobalizationSettings.getLocalFunctionName(standardName)**](https://reference.aspose.com/cells/nodejs-cpp/globalizationsettings/#getLocalFunctionName-string-)-metoden.

## **Implementera Cell.FormulaLocal liknande Excel VBA Range.FormulaLocal**

Följande kodexempel förklarar hur man implementerar [**GlobalizationSettings.getLocalFunctionName(standardName)**](https://reference.aspose.com/cells/nodejs-cpp/globalizationsettings/#getLocalFunctionName-string-)-metoden. Metoden returnerar det lokala namnet för en standardfunktion. Om standard funktionsnamnet är **SUM** returneras **UserFormulaLocal_SUM**. Du kan ändra koden efter behov och returnera rätt lokala funktionsnamn, t.ex. är **SUM** **SUMME** på tyska och **TEXT** är **ТЕКСТ** på ryska. Se även exempelutdata från kodexemplet nedan för referens.

## **Exempelkod**

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

## **Konsoloutput**

{{< highlight javascript >}}

Formula Local: =UserFormulaLocal_SUM(A1:A2)

Formula Local: =UserFormulaLocal_AVERAGE(B1:B2,B5)

{{< /highlight >}}
