---
title: تنفيذ محرك حساب مخصص لتوسيع محرك الحساب الافتراضي لمكتبة Aspose.Cells باستخدام JavaScript عبر C++
linktitle: تنفيذ محرك الحساب المخصص لتوسيع محرك الحساب الافتراضي لـ Aspose.Cells
description: تصف هذه المقالة كيفية توسيع محرك الحساب الافتراضي في JavaScript من خلال تنفيذ محرك حساب مخصص باستخدام مكتبة Aspose.Cells لـ JavaScript عبر C++. قم بتحميل ملف إكسل موجود أو أنشئ واحدًا جديدًا لاستخدام الطرق المقدمة وحفظ ملف الإكسل المعدل.
keywords: Aspose.Cells، إكسل، محرك حساب مخصص، JavaScript عبر C++
type: docs
weight: 80
url: /ar/javascript-cpp/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/
---

## **تنفيذ محرك الحساب المخصص**

Aspose.Cells يمتلك محرك حساب قوي يمكنه حساب معظم صيغ Microsoft Excel تقريبًا. على الرغم من ذلك، يسمح لك أيضًا بتوسيع محرك الحساب الافتراضي مما يمنحك قوة ومرونة أكبر.

يتم استخدام الخصائص والفئات التالية في تنفيذ هذه الميزة.

- [**CalculationOptions.customEngine**](https://reference.aspose.com/cells/javascript-cpp/calculationoptions/#customEngine--)
- [**AbstractCalculationEngine**](https://reference.aspose.com/cells/javascript-cpp/abstractcalculationengine)
- [**CalculationData**](https://reference.aspose.com/cells/javascript-cpp/calculationdata)

الكود التالي ينفذ محرك الحساب المخصص. ينفذ الواجهة [**AbstractCalculationEngine**](https://reference.aspose.com/cells/javascript-cpp/abstractcalculationengine) التي تحتوي على طريقة [**calculate(CalculationData data)**](https://reference.aspose.com/cells/javascript-cpp/abstractcalculationengine/#calculate-calculationdata-). تُستدعى هذه الطريقة على جميع صيغك. داخل هذه الطريقة، نلتقط دالة **TODAY** ونضيف يومًا واحدًا إلى تاريخ النظام. لذلك، إذا كان التاريخ الحالي 27/07/2023، فإن المحرك المخصص سيحسب TODAY() كتاريخ 28/07/2023.

### **نموذج برمجة**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Custom Calculation Engine Example</title>
    </head>
    <body>
        <h1>Custom Calculation Engine Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample" disabled>Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, CalculationOptions, CellsHelper } = AsposeCells;

        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: [
                "arial.ttf",
                "NotoSansSC-Regular.ttf"
            ]
        }).then(() => {
            console.log("Aspose.Cells initialized");
            document.getElementById('runExample').disabled = false;
        });

        // Create a new class derived from AbstractCalculationEngine
        class CustomEngine extends AsposeCells.AbstractCalculationEngine {
            constructor() {
                super();
                // Indicate processing built-in functions
                this.processBuiltInFunctions = true;
            }

            // Override the Calculate method with custom logic
            calculate(data) {
                // Check the formula name and change the implementation
                if (data.functionName.toUpperCase() === "TODAY") {
                    // Assign the CalculationData.CalculatedValue: add one day offset for the date
                    data.calculatedValue = CellsHelper.getDoubleFromDateTime(new Date(), false) + 1.0;
                }
            }
        }

        class ImplementCustomCalculationEngine {
            static run() {
                // Create an instance of Workbook
                const workbook = new Workbook();

                // Access first Worksheet from the collection
                const sheet = workbook.worksheets.get(0);

                // Access Cell A1 and put a formula to sum values of B1 to B2
                const a1 = sheet.cells.get("A1");
                const style = a1.style;
                style.number = 14;
                a1.style = style;

                a1.formula = "=TODAY()";

                // Calculate all formulas in the Workbook 
                workbook.calculateFormula();

                // The result of A1 with default calculation engine
                console.log("The value of A1 with default calculation engine: " + a1.stringValue);

                // Create an instance of CustomEngine
                const engine = new CustomEngine();

                // Create an instance of CalculationOptions
                const opts = new CalculationOptions();

                // Assign the CalculationOptions.CustomEngine property to the instance of CustomEngine
                opts.customEngine = engine;

                // Recalculate all formulas in Workbook using the custom calculation engine
                workbook.calculateFormula(opts);

                // The result of A1 with custom calculation engine
                console.log("The value of A1 with custom calculation engine: " + a1.stringValue);

                console.log("Press any key to continue...");

                document.getElementById('result').innerHTML = '<p style="color: green;">Calculation completed. Check console for output.</p>';
            }
        }

        document.getElementById('runExample').addEventListener('click', () => {
            ImplementCustomCalculationEngine.run();
        });
    </script>
</html>
```

### **النتيجة**

يرجى التحقق من مخرجات وحدة التحكم للكود أعلاه؛ قيمة (تاريخ ووقت) A1 مع المحرك المخصص يجب أن تكون يومًا واحدًا بعد النتيجة بدون المحرك المخصص.

### **مقال ذو صلة**

{{% alert color="primary" %}}

[الحساب المباشر للدالة المخصصة دون كتابتها في ورقة عمل](/cells/ar/javascript-cpp/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/)

{{% /alert %}}
