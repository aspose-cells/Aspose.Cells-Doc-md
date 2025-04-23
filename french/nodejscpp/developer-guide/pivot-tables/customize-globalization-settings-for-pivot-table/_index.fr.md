---
title: Configurer les paramètres de localisation pour le tableau croisé dynamique avec Node.js via C++
linktitle: Personnaliser les paramètres de globalisation pour la table croisée dynamique
type: docs
weight: 50
url: /fr/nodejs-cpp/customize-globalization-settings-for-pivot-table/
---

## **Scénarios d'utilisation possibles**

Parfois, vous souhaitez personnaliser le texte *Total de Pivot, Sous-total, Total général, Tous les éléments, éléments multiples, Étiquettes de colonnes, Étiquettes de lignes, Valeurs vides* selon vos besoins. Aspose.Cells for Node.js via C++ vous permet de personnaliser les paramètres de globalisation du tableau croisé dynamique pour gérer ces scénarios. Vous pouvez également utiliser cette fonctionnalité pour changer les étiquettes dans d'autres langues comme l'Arabe, l'Hindi, le Polonais, etc.

## **Personnaliser les paramètres de globalisation pour le tableau croisé dynamique**

Le code d'exemple ci-dessous explique comment personnaliser les paramètres de globalisation pour le tableau croisé dynamique. Il crée une classe *CustomPivotTableGlobalizationSettings* dérivée d'une classe de base [**PivotGlobalizationSettings**](https://reference.aspose.com/cells/nodejs-cpp/pivotglobalizationsettings/) et redéfinit toutes ses méthodes nécessaires. Ces méthodes renvoient le texte personnalisé pour *Total de Pivot, Sous-total, Total général, Tous les éléments, éléments multiples, Étiquettes de colonnes, Étiquettes de lignes, Valeurs vides*. Ensuite, il assigne l'objet de cette classe à la propriété [**WorkbookSettings.getPivotSettings()**](https://reference.aspose.com/cells/nodejs-cpp/globalizationsettings/#getPivotSettings--). Le code charge le fichier excel source (40468488.xlsx) contenant le tableau croisé dynamique, le rafraîchit, calcule ses données et le sauvegarde en tant que fichier [PDF de sortie](40468487.pdf). La capture d'écran suivante montre l'effet du code exemple sur le PDF de sortie. Comme vous pouvez le voir sur la capture, différentes parties du tableau croisé dynamique ont maintenant un texte personnalisé renvoyé par les méthodes redéfinies de la classe [**PivotGlobalizationSettings**](https://reference.aspose.com/cells/nodejs-cpp/pivotglobalizationsettings/).

![todo:image_alt_text](customize-globalization-settings-for-pivot-table_1.png)

## **Code d'exemple**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

class CustomPivotTableGlobalizationSettings extends AsposeCells.PivotGlobalizationSettings {
// Gets the name of "Total" label in the PivotTable.
getTextOfTotal() {
console.log("---------GetPivotTotalName-------------");
return "AsposeGetPivotTotalName";
}

// Gets the name of "Grand Total" label in the PivotTable.
getTextOfGrandTotal() {
console.log("---------GetPivotGrandTotalName-------------");
return "AsposeGetPivotGrandTotalName";
}

// Gets the name of "(Multiple Items)" label in the PivotTable.
getTextOfMultipleItems() {
console.log("---------GetMultipleItemsName-------------");
return "AsposeGetMultipleItemsName";
}

// Gets the name of "(All)" label in the PivotTable.
getTextOfAll() {
console.log("---------GetAllName-------------");
return "AsposeGetAllName";
}

// Gets the name of "Column Labels" label in the PivotTable.
getTextOfColumnLabels() {
console.log("---------GetColumnLabelsOfPivotTable-------------");
return "AsposeGetColumnLabelsOfPivotTable";
}

// Gets the name of "Row Labels" label in the PivotTable.
getTextOfRowLabels() {
console.log("---------GetRowLabelsNameOfPivotTable-------------");
return "AsposeGetRowLabelsNameOfPivotTable";
}

// Gets the name of "(blank)" label in the PivotTable.
getTextOfEmptyData() {
console.log("---------GetEmptyDataName-------------");
return "(blank)AsposeGetEmptyDataName";
}

// Gets the name of PivotFieldSubtotalType type in the PivotTable.
getTextOfSubTotal(subTotalType) {
console.log("---------GetSubTotalName-------------");

switch (subTotalType) {
case AsposeCells.PivotFieldSubtotalType.Sum:
return "AsposeSum";

case AsposeCells.PivotFieldSubtotalType.Count:
return "AsposeCount";

case AsposeCells.PivotFieldSubtotalType.Average:
return "AsposeAverage";

case AsposeCells.PivotFieldSubtotalType.Max:
return "AsposeMax";

case AsposeCells.PivotFieldSubtotalType.Min:
return "AsposeMin";

case AsposeCells.PivotFieldSubtotalType.Product:
return "AsposeProduct";

case AsposeCells.PivotFieldSubtotalType.CountNums:
return "AsposeCount";

case AsposeCells.PivotFieldSubtotalType.Stdev:
return "AsposeStdDev";

case AsposeCells.PivotFieldSubtotalType.Stdevp:
return "AsposeStdDevp";

case AsposeCells.PivotFieldSubtotalType.Var:
return "AsposeVar";

case AsposeCells.PivotFieldSubtotalType.Varp:
return "AsposeVarp";
}

return "AsposeSubTotalName";
}
}

async function run() {
// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Load your excel file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "samplePivotTableGlobalizationSettings.xlsx"));

workbook.getSettings().setGlobalizationSettings(new AsposeCells.GlobalizationSettings());

// Setting Custom Pivot Table Globalization Settings
workbook.getSettings().getGlobalizationSettings().setPivotSettings(new CustomPivotTableGlobalizationSettings());

// Hide first worksheet that contains the data of the pivot table
workbook.getWorksheets().get(0).setIsVisible(false);

// Access second worksheet
const ws = workbook.getWorksheets().get(1);

// Access the pivot table, refresh and calculate its data
const pt = ws.getPivotTables().get(0);
pt.setRefreshDataFlag(true);
pt.refreshData();
pt.calculateData();
pt.setRefreshDataFlag(false);

// Pdf save options - save entire worksheet on a single pdf page
const options = new AsposeCells.PdfSaveOptions();
options.setOnePagePerSheet(true);

// Save the output pdf 
workbook.save(path.join(dataDir, "outputPivotTableGlobalizationSettings.pdf"), options);
}

run().catch(console.error);
```
