---
title: تخصيص إعدادات التدويل للجداول المحورية عبر Node.js باستخدام C++
linktitle: تخصيص إعدادات العالمية لجدول محوري
type: docs
weight: 50
url: /ar/nodejs-cpp/customize-globalization-settings-for-pivot-table/
---

## **سيناريوهات الاستخدام المحتملة**

أحيانًا تريد تخصيص نص *إجمالي المحور، فرعي، الإجمالي الكلي، جميع العناصر، عناصر متعددة، تسميات الأعمدة، تسميات الصفوف، القيم الفارغة* حسب متطلباتك. يُتيح لك Aspose.Cells for Node.js via C++ تخصيص إعدادات التدويل للجدول المحوري للتعامل مع مثل هذه الحالات. يمكنك أيضًا استخدام هذه الميزة لتغيير التسميات إلى لغات أخرى مثل العربية، الهندية، البولندية، وغيرها.

## **تخصيص إعدادات العالمية لجدول محوري**

الشيفرة التالية تشرح كيفية تخصيص إعدادات التدويل للجدول المحوري. تُنشئ فئة *CustomPivotTableGlobalizationSettings* المشتقة من فئة الأساس [**PivotGlobalizationSettings**](https://reference.aspose.com/cells/nodejs-cpp/pivotglobalizationsettings/) وتُعيد تعريف جميع طرقها الضرورية. هذه الطرق تُرجع النص المُخصص لـ *إجمالي المحور، فرعي، الإجمالي الكلي، جميع العناصر، عناصر متعددة، تسميات الأعمدة، تسميات الصفوف، القيم الفارغة*. ثم تُعيّن كائن هذه الفئة إلى الخاصية [**WorkbookSettings.getPivotSettings()**](https://reference.aspose.com/cells/nodejs-cpp/globalizationsettings/#getPivotSettings--). الشيفرة تقوم بتحميل ملف إكسل المصدر ([40468488.xlsx]) الذي يحتوي على الجدول المحوري، تحديثه وحسابه، وحفظه كملف [PDF الناتج](40468487.pdf). تُظهر الصورة التالية تأثير الشيفرة على ملف PDF الناتج. كما ترى في الصورة، الأجزاء المختلفة من الجدول المحوري أصبحت تحتوي على نص مخصص يُرجعه الطرق المُعرفة في فئة [**PivotGlobalizationSettings**](https://reference.aspose.com/cells/nodejs-cpp/pivotglobalizationsettings/)،

![todo:image_alt_text](customize-globalization-settings-for-pivot-table_1.png)

## **الكود المثالي**

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
