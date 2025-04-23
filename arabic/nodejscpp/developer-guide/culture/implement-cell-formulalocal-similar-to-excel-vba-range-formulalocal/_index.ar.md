---
title: تنفيذ Cell.FormulaLocal مشابه لـ Range.FormulaLocal في Excel VBA باستخدام Node.js عبر C++
linktitle: تنفيذ Cell.FormulaLocal مماثل لـ Excel VBA Range.FormulaLocal
type: docs
weight: 30
url: /ar/nodejs-cpp/implement-cell-formulalocal-similar-to-excel-vba-range-formulalocal/
description: تعلم كيفية تنفيذ Cell.FormulaLocal مماثل لـ Excel VBA Range.FormulaLocal باستخدام Aspose.Cells for Node.js via C++. 
---

## **سيناريوهات الاستخدام المحتملة**

قد تحتوي معادلات Microsoft Excel على أسماء مختلفة في مناطق أو لغات أو بيئات مختلفة. على سبيل المثال، تُسمى وظيفة **SUM** بـ **SUMME** باللغة الألمانية. لا يمكن لـ Aspose.Cells العمل مع أسماء الوظائف غير الإنجليزية. في VBA في Excel، هناك خاصية **Range.FormulaLocal** التي تسترجع اسم الوظيفة حسب لغتها أو منطقتها. يوفر Aspose.Cells for Node.js via C++ أيضًا [**Cell.getFormulaLocal()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getFormulaLocal--) لهذه الغاية. ولكن، ستعمل هذه الخاصية فقط عند تنفيذ [**GlobalizationSettings.getLocalFunctionName(standardName)**](https://reference.aspose.com/cells/nodejs-cpp/globalizationsettings/#getLocalFunctionName-string-).

## **تنفيذ Cell.FormulaLocal مماثل لـ Excel VBA Range.FormulaLocal**

يشرح رمز العينة التالي كيفية تنفيذ طريقة [**GlobalizationSettings.getLocalFunctionName(standardName)**](https://reference.aspose.com/cells/nodejs-cpp/globalizationsettings/#getLocalFunctionName-string-). تعيد الطريقة الاسم المحلي للوظيفة القياسية. إذا كان اسم الوظيفة القياسية هو **SUM**، فستُعيد **UserFormulaLocal_SUM**. يمكنك تعديل الكود حسب حاجتك وإرجاع الأسماء الصحيحة للوظائف المحلية، على سبيل المثال، يكون **SUM** هو **SUMME** بالألمانية و **TEXT** هو **ТЕКСТ** بالروسية. يُرجى أيضًا مراجعة مخرجات وحدة التحكم للرمز المقدم أدناه للمرجع.

## **الكود المثالي**

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

## **مخرجات الوحدة**

{{< highlight javascript >}}

Formula Local: =UserFormulaLocal_SUM(A1:A2)

Formula Local: =UserFormulaLocal_AVERAGE(B1:B2,B5)

{{< /highlight >}}
