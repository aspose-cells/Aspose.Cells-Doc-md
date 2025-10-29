---
title: Implémentez Cell.FormulaLocal de manière similaire à Excel VBA Range.FormulaLocal avec Node.js via C++
linktitle: Implémenter Cell.FormulaLocal similaire à Excel VBA Range.FormulaLocal
type: docs
weight: 30
url: /fr/nodejs-cpp/implement-cell-formulalocal-similar-to-excel-vba-range-formulalocal/
description: Apprenez comment implémenter Cell.FormulaLocal de manière similaire à Excel VBA Range.FormulaLocal en utilisant Aspose.Cells for Node.js via C++. 
---

## **Scénarios d'utilisation possibles**

Les formules de Microsoft Excel peuvent avoir des noms différents selon les régions ou les langues. Par exemple, la fonction **SUM** est appelée **SUMME** en allemand. Aspose.Cells ne peut pas fonctionner avec des noms de fonctions non anglophones. Dans Microsoft Excel VBA, il existe la propriété **Range.FormulaLocal** qui retourne le nom de la fonction dans la langue ou la région. Aspose.Cells for Node.js via C++ fournit également la propriété [**Cell.getFormulaLocal()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getFormulaLocal--) à cette fin. Cependant, cette propriété ne fonctionnera que lorsque vous implémentez la méthode [**GlobalizationSettings.getLocalFunctionName(standardName)**](https://reference.aspose.com/cells/nodejs-cpp/globalizationsettings/#getLocalFunctionName-string-).

## **Implémenter Cell.FormulaLocal similaire à Excel VBA Range.FormulaLocal**

Le code d'exemple suivant explique comment implémenter la méthode [**GlobalizationSettings.getLocalFunctionName(standardName)**](https://reference.aspose.com/cells/nodejs-cpp/globalizationsettings/#getLocalFunctionName-string-). La méthode retourne le nom local de la fonction standard. Si le nom de la fonction standard est **SUM**, elle retourne **UserFormulaLocal_SUM**. Vous pouvez modifier le code selon vos besoins et retourner les noms de fonctions locaux corrects, par exemple, **SUM** est **SUMME** en allemand et **TEXT** est **ТЕКСТ** en russe. Veuillez également voir la sortie console du code d'exemple ci-dessous pour référence.

## **Code d'exemple**

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

## **Sortie console**

{{< highlight javascript >}}

Formula Local: =UserFormulaLocal_SUM(A1:A2)

Formula Local: =UserFormulaLocal_AVERAGE(B1:B2,B5)

{{< /highlight >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
