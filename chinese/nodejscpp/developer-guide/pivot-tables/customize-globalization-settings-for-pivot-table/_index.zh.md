---
title: 通过 Node.js 使用 C++ 自定义全局化设置的示例
linktitle: 自定义数据透视表的全球化设置
type: docs
weight: 50
url: /zh/nodejs-cpp/customize-globalization-settings-for-pivot-table/
---

## **可能的使用场景**

有时你希望根据需要自定义 *数据透视总计、小计、总计、所有项、多项、列标签、行标签、空值* 文本。Aspose.Cells for Node.js via C++ 允许你自定义数据透视表的全球化设置，以应对这些场景。你也可以利用此功能将标签更改为其他语言，如阿拉伯语、印地语、波兰语等。

## **自定义数据透视表的全球化设置**

以下示例代码说明了如何为数据透视表自定义全球化设置。它创建了一个继承自 [**PivotGlobalizationSettings**](https://reference.aspose.com/cells/nodejs-cpp/pivotglobalizationsettings/) 基类的 *CustomPivotTableGlobalizationSettings* 类，并重写了所有必要的方法。这些方法返回自定义的 *Pivot Total、Sub Total、Grand Total、All Items、Multiple Items、Column Labels、Row Labels、Blank Values* 的文本。然后将该类的对象分配给 [**WorkbookSettings.getPivotSettings()**](https://reference.aspose.com/cells/nodejs-cpp/globalizationsettings/#getPivotSettings--) 属性。该代码加载包含数据透视表的源Excel文件（40468488.xlsx），刷新并计算其数据，然后保存为输出PDF（40468487.pdf）。以下截图显示了示例代码对输出PDF的效果。可以看到，数据透视表的不同部分现在返回了由 [**PivotGlobalizationSettings**](https://reference.aspose.com/cells/nodejs-cpp/pivotglobalizationsettings/) 类的重写方法所定制的文本。

![todo:image_alt_text](customize-globalization-settings-for-pivot-table_1.png)

## **示例代码**

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
