---
title: Anpassa globaliseringsinställningar för pivot tabell med Node.js via C++
linktitle: Anpassa globaliseringsinställningarna för Pivot tabell
type: docs
weight: 50
url: /sv/nodejs-cpp/customize-globalization-settings-for-pivot-table/
---

## **Möjliga användningsscenario**

Ibland vill du anpassa texten för *Pivot Total, Sub Total, Grand Total, All Items, Multiple Items, Column Labels, Row Labels, Blank Values* enligt dina behov. Aspose.Cells for Node.js via C++ gör det möjligt att anpassa globaliseringsinställningarna för pivot-tabellen för att hantera sådana scenarier. Du kan också använda denna funktion för att ändra etiketter till andra språk som arabiska, hindi, polska, etc.

## **Anpassa globaliseringsinställningarna för Pivot-tabell**

Följande exempelkod visar hur man anpassar globaliseringsinställningar för pivot-tabellen. Det skapar en klass *CustomPivotTableGlobalizationSettings* härledd från en bas<ol>klass [**PivotGlobalizationSettings**](https://reference.aspose.com/cells/nodejs-cpp/pivotglobalizationsettings/) och överskuggar alla nödvändiga metoder. Dessa metoder returnerar den anpassade texten för *Pivot Total, Sub Total, Grand Total, All Items, Multiple Items, Column Labels, Row Labels, Blank Values*. Sedan tilldelas objektet av denna klass till [**WorkbookSettings.getPivotSettings()**](https://reference.aspose.com/cells/nodejs-cpp/globalizationsettings/#getPivotSettings--)-egenskapen. Koden laddar det [ursprungliga excel-filen](40468488.xlsx) som innehåller pivot-tabellen, uppdaterar och beräknar dess data och sparar det som [utdata PDF](40468487.pdf). Följande skärmbild visar effekten av exemplet på PDF-filen. Som du kan se har olika delar av pivot-tabellen nu anpassad text som returneras av de överskuggade metoderna i [**PivotGlobalizationSettings**](https://reference.aspose.com/cells/nodejs-cpp/pivotglobalizationsettings/)-klassen.

![todo:image_alt_text](customize-globalization-settings-for-pivot-table_1.png)

## **Exempelkod**

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
{{< app/cells/assistant language="nodejs-cpp" >}}
