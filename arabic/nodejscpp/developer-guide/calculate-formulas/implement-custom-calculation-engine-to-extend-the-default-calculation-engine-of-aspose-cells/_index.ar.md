---
title: تطبيق محرك حساب مخصص لتوسيع محرك الحساب الافتراضي لـ Aspose.Cells باستخدام Node.js عبر C++
linktitle: تنفيذ محرك الحساب المخصص لتوسيع محرك الحساب الافتراضي لـ Aspose.Cells
description: تصف هذه المقالة كيفية توسيع محرك الحساب الافتراضي في Node.js عن طريق تنفيذ محرك حساب مخصص باستخدام مكتبة Aspose.Cells لـ Node.js عبر C++. قم بتحميل ملف إكسل موجود أو أنشئ واحدًا جديدًا لاستخدام الطرق المقدمة وحفظ ملف إكسل المعدل.
keywords: Aspose.Cells، إكسل، محرك حساب مخصص، Node.js عبر C++
type: docs
weight: 80
url: /ar/nodejs-cpp/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/
---

## **تنفيذ محرك الحساب المخصص**

Aspose.Cells يمتلك محرك حساب قوي يمكنه حساب معظم صيغ Microsoft Excel تقريبًا. على الرغم من ذلك، يسمح لك أيضًا بتوسيع محرك الحساب الافتراضي مما يمنحك قوة ومرونة أكبر.

يتم استخدام الخصائص والفئات التالية في تنفيذ هذه الميزة.

- [**CalculationOptions.getCustomEngine()**](https://reference.aspose.com/cells/nodejs-cpp/calculationoptions/#getCustomEngine--)
- [**AbstractCalculationEngine**](https://reference.aspose.com/cells/nodejs-cpp/abstractcalculationengine)
- [**CalculationData**](https://reference.aspose.com/cells/nodejs-cpp/calculationdata)

الكود التالي ينفذ محرك الحساب المخصص. ينفذ الواجهة [**AbstractCalculationEngine**](https://reference.aspose.com/cells/nodejs-cpp/abstractcalculationengine) التي تحتوي على طريقة [**calculate(CalculationData data)**](https://reference.aspose.com/cells/nodejs-cpp/abstractcalculationengine/#calculate-calculationdata-). تُستدعى هذه الطريقة على جميع صيغك. داخل هذه الطريقة، نلتقط دالة **TODAY** ونضيف يومًا واحدًا إلى تاريخ النظام. لذلك، إذا كان التاريخ الحالي 27/07/2023، فإن المحرك المخصص سيحسب TODAY() كتاريخ 28/07/2023.

### **نموذج برمجة**

```javascript
const AsposeCells = require("aspose.cells.node");

// Create a new class derived from AbstractCalculationEngine
class CustomEngine extends AsposeCells.AbstractCalculationEngine {
// Override the Calculate method with custom logic
calculate(data) {
// Check the formula name and change the implementation
if (data.getFunctionName().toUpperCase() === "TODAY") {
// Assign the CalculationData.CalculatedValue: add one day offset for the date
data.setCalculatedValue(AsposeCells.CellsHelper.getDoubleFromDateTime(new Date(), false) + 1.0);
}
}
getProcessBuiltInFunctions() {
return true;
}
}

class ImplementCustomCalculationEngine {
static run() {
// Create an instance of Workbook
const workbook = new AsposeCells.Workbook();

// Access first Worksheet from the collection
const sheet = workbook.getWorksheets().get(0);

// Access Cell A1 and put a formula to sum values of B1 to B2
const a1 = sheet.getCells().get("A1");
const style = a1.getStyle();
style.setNumber(14);
a1.setStyle(style);

a1.setFormula("=TODAY()");

// Calculate all formulas in the Workbook 
workbook.calculateFormula();

// The result of A1 should be 20 as per default calculation engine
console.log("The value of A1 with default calculation engine: " + a1.getStringValue());

// Create an instance of CustomEngine
const engine = new CustomEngine();

// Create an instance of CalculationOptions
const opts = new AsposeCells.CalculationOptions();

// Assign the CalculationOptions.CustomEngine property to the instance of CustomEngine
opts.setCustomEngine(engine);

// Recalculate all formulas in Workbook using the custom calculation engine
workbook.calculateFormula(opts);

// The result of A1 will be 50 as per custom calculation engine
console.log("The value of A1 with custom calculation engine: " + a1.getStringValue());

console.log("Press any key to continue...");
}
}

// Call the run method to execute the example
ImplementCustomCalculationEngine.run();
```

### **النتيجة**

يرجى التحقق من مخرجات وحدة التحكم للكود أعلاه؛ قيمة (تاريخ ووقت) A1 مع المحرك المخصص يجب أن تكون يومًا واحدًا بعد النتيجة بدون المحرك المخصص.

### **مقال ذو صلة**

{{% alert color="primary" %}}

[الحساب المباشر لدالة مخصصة بدون كتابتها في ورقة](/cells/ar/nodejs-cpp/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/)

{{% /alert %}}
