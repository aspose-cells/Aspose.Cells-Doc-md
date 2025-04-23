---
title: إرجاع مجموعة من القيم باستخدام AbstractCalculationEngine مع Node.js عبر C++
linktitle: إرجاع مجموعة من القيم باستخدام محرك الحساب النموذجي
description: تقدم هذه المقالة محرك حساب مجرد يُعيد مجموعة من القيم في إكسل باستخدام مكتبة Aspose.Cells لـ Node.js عبر C++. تعلم كيفية تحميل أو إنشاء ملف إكسل وحفظ الملف المعدل على القرص.
keywords: Aspose.Cells، إكسل، محرك حساب مجرد يعيد القيم، Node.js عبر C++، دوال مخصصة
type: docs
weight: 55
url: /ar/nodejs-cpp/returning-a-range-of-values-using-abstractcalculationengine/
---

{{% alert color="primary" %}}

توفر Aspose.Cells فئة [**AbstractCalculationEngine**](https://reference.aspose.com/cells/nodejs-cpp/abstractcalculationengine) التي تستخدم لتنفيذ وظائف مخصصة غير مدعومة من قبل Microsoft Excel كوظائف مدمجة.

سيشرح هذا المقال كيفية إرجاع مجموعة القيم من [**AbstractCalculationEngine**](https://reference.aspose.com/cells/nodejs-cpp/abstractcalculationengine).

{{% /alert %}}

يوضح الكود التالي استخدام فئة [**AbstractCalculationEngine**](https://reference.aspose.com/cells/nodejs-cpp/abstractcalculationengine) ويعيد مجموعة القيم عبر طريقتها.

إنشاء فئة تحتوي على دالة *calculateCustomFunction*. تنفذ هذه الفئة [**AbstractCalculationEngine**](https://reference.aspose.com/cells/nodejs-cpp/abstractcalculationengine).

```javascript
const AsposeCells = require("aspose.cells.node");

class CustomFunctionStaticValue extends AsposeCells.AbstractCalculationEngine {
calculate(data) {
data.setCalculatedValue([
[new Date(2015, 5, 12, 10, 6, 30), 2],
[3.0, "Test"]
]);
}
}
```

استخدم الآن الدالة أعلاه في برنامجك

```javascript
const AsposeCells = require("aspose.cells.node");

class CustomFunctionStaticValue extends AsposeCells.AbstractCalculationEngine {
calculate(data) {
data.setCalculatedValue([
[new Date(2015, 5, 12, 10, 6, 30), 2],
[3.0, "Test"]
]);
}
}

try {
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create workbook
const workbook = new AsposeCells.Workbook();
const cells = workbook.getWorksheets().get(0).getCells();

// Set formula
const cell = cells.get(0, 0);
cell.setArrayFormula("=MYFUNC()", 2, 2);

const style = cell.getStyle();
style.setNumber(14);
cell.setStyle(style);

// Set calculation options for formula
const calculationOptions = new AsposeCells.CalculationOptions();
calculationOptions.setCustomEngine(new CustomFunctionStaticValue());
workbook.calculateFormula(calculationOptions);

// Save to xlsx by setting the calc mode to manual
workbook.getSettings().getFormulaSettings().setCalculationMode(AsposeCells.CalcModeType.Manual);
workbook.save(dataDir + "output_out.xlsx");

// Save to pdf
workbook.save(dataDir + "output_out.pdf");
} catch (error) {
console.error(`Test failed: ${error.message}`);
throw error;
}
```
