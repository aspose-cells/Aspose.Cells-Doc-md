---
title: إنشاء، تعديل أو إزالة السيناريوهات من أوراق العمل باستخدام Node.js عبر C++
linktitle: إدارة السيناريوهات
type: docs
weight: 190
url: /ar/nodejs-cpp/create-manipulate-or-remove-scenarios-from-worksheets/
description: تعلم كيفية إنشاء، تعديل، أو إزالة السيناريوهات من أوراق عمل إكسل برمجياً باستخدام Node.js مع API C++.
keywords: إنشاء سيناريو لورقة العمل باستخدام node.js عبر C++، إزالة سيناريو ورقة العمل باستخدام node.js عبر C++، تعديل سيناريو ورقة العمل باستخدام node.js عبر C++
---

{{% alert color="primary" %}}

في بعض الأحيان، قد تحتاج إلى إنشاء، التلاعب أو حذف السيناريوهات في جداول البيانات. السيناريو هو نموذج 'ماذا لو؟' يتضمن خلايا إدخال متغيرة مرتبطة بواحد أو أكثر من الصيغ. قبل إنشاء سيناريو، صمم الورقة العمل بحيث تحتوي على صيغة واحدة على الأقل تعتمد على الخلايا التي يمكن إدراج قيم مختلفة فيها. يظهر المثال التالي كيفية إنشاء وإزالة السيناريوهات من ورقة عمل في مصنف باستخدام واجهات Aspose.Cells.

{{% /alert %}}

توفر Aspose.Cells بعض الفصول المفيدة، على سبيل المثال، [**ScenarioCollection**](https://reference.aspose.com/cells/nodejs-cpp/scenariocollection)، [**Scenario**](https://reference.aspose.com/cells/nodejs-cpp/scenario)، [**ScenarioInputCellCollection**](https://reference.aspose.com/cells/nodejs-cpp/scenarioinputcellcollection)، و [**ScenarioInputCell**](https://reference.aspose.com/cells/nodejs-cpp/scenarioinputcell). كما توفر الخاصية [**Worksheet.getScenarios()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getScenarios--). يفتح الكود المصدري العينة أدناه ملف إكسل XLSX الذي يحتوي على بعض السيناريوهات ويزيل السيناريو الحالي. كما يضيف سيناريوًا جديدًا إلى الورقة العمل قبل حفظ ملف إكسل. يستخدم المثال ملف قالب بسيط جدًا يحتوي على سيناريو.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Instantiate the Workbook
// Load an Excel file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "aspose-sample.xlsx"));
// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

if (worksheet.getScenarios().getCount() > 0) {
// Remove the existing first scenario from the sheet
worksheet.getScenarios().removeAt(0);

// Create a scenario
const i = worksheet.getScenarios().add("MyScenario");
// Get the scenario
const scenario = worksheet.getScenarios().get(i);
// Add comment to it
scenario.setComment("Test scenario is created.");
// Get the input cells for the scenario
const sic = scenario.getInputCells();
// Add the scenario on B4 (as changing cell) with default value
sic.add(3, 1, "1100000");

const outputFilePath = path.join(dataDir, "outBk_scenarios1.out.xlsx");

// Save the Excel file.
workbook.save(outputFilePath);
console.log("\nProcess completed successfully.\nFile saved at " + outputFilePath);
}
```
