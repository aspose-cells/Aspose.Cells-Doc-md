---
title: الحساب المباشر لدالة مخصصة بدون كتابتها في ورقة باستخدام Node.js عبر C++
linktitle: الحساب المباشر للوظيفة المخصصة دون كتابتها في ورقة عمل
description: تقدم هذه المقالة شرحًا عن كيفية استخدام مكتبة Aspose.Cells لحساب دوال مخصصة مباشرة في مايكروسوفت إكسل دون كتابتها في ورقة باستخدام Node.js عبر C++. قم بتحميل ملف إكسل موجود أو أنشئ واحدًا جديدًا، احسب الدالة المخصصة، ثم قم بحفظ الملف المعدل.
keywords: Aspose.Cells، إكسل، دوال مخصصة، حساب مباشر، Node.js عبر C++، بدون الحاجة للكتابة، أوراق العمل
type: docs
weight: 90
url: /ar/nodejs-cpp/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/
---

## **الحساب المباشر للوظيفة المخصصة دون كتابتها في ورقة العمل**

يشرح هذا الموضوع كيف يمكنك حساب وظائفك المخصصة مباشرة دون كتابتها أولاً في ورقة عمل. يرجى استخدام طريقة [**Worksheet.calculateFormula(formula, opts)**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#calculateFormula-string-CalculationOptions-) لهذا الغرض.

يرجى الاطلاع على الرمز العيني التالي الذي يوضح استخدام هذه الطريقة. لقد استخدمنا وظيفة مخصصة باسم MyCompany.CustomFunction() وقمنا بحساب قيمتها كـ 'Aspose.Cells.' بأنفسنا ثم يتم دمج هذه القيمة تلقائيًا مع قيمة الخلية A1 التي هي 'مرحبًا بك في ' بواسطة محرك الحساب وتعيد القيمة المحسوبة النهائية كـ 'مرحبا بك في Aspose.Cells.' كما ترون في الرمز البرمجي لم نكتب وظيفتنا المخصصة في أي مكان في ورقة العمل ويتم حسابها مباشرة بواسطة منطقنا المخصص.

### **نموذج برمجة**

```javascript
const AsposeCells = require("aspose.cells.node");

class CustomEngine extends AsposeCells.AbstractCalculationEngine {
// Override the Calculate method with custom logic
calculate(data) {
// Check the formula name and calculate it yourself
if (data.getFunctionName() === "MyCompany.CustomFunction") {
// This is our calculated value
data.setCalculatedValue("Aspose.Cells.");
}
}
}

class ImplementDirectCalculationOfCustomFunction {
static run() {
// Create a workbook
const wb = new AsposeCells.Workbook();

// Access first worksheet
const ws = wb.getWorksheets().get(0);

// Add some text in cell A1
ws.getCells().get("A1").putValue("Welcome to ");

// Create a calculation options with custom engine
const opts = new AsposeCells.CalculationOptions();
opts.setCustomEngine(new CustomEngine());

// This line shows how you can call your own custom function without
// a need to write it in any worksheet cell
// After the execution of this line, it will return
// Welcome to Aspose.Cells.
const ret = ws.calculateFormula("=A1 & MyCompany.CustomFunction()", opts);

// Print the calculated value
console.log("Calculated Value: " + ret);
}
}

// Example invocation
ImplementDirectCalculationOfCustomFunction.run();
```

### **مخرجات الوحدة**

فيما يلي إخراج وحدة التحكم للرمز العيني أعلاه.

{{< highlight javascript >}}

Calculated Value: Welcome to Aspose.Cells.

{{< /highlight >}}

### **مقال ذو صلة**

{{% alert color="primary" %}}

[تطبيق محرك حساب مخصص لتوسيع محرك الحساب الافتراضي لـ Aspose.Cells](/cells/ar/nodejs-cpp/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/)

{{% /alert %}}
{{< app/cells/assistant language="nodejs-cpp" >}}
