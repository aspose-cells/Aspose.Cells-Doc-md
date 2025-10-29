---
title: الحساب المباشر للدالة المخصصة بدون كتابتها في ورقة العمل باستخدام JavaScript عبر C++
linktitle: الحساب المباشر للوظيفة المخصصة دون كتابتها في ورقة عمل
description: تقدم هذه المقالة كيفية استخدام مكتبة Aspose.Cells لحساب الدالات المخصصة مباشرة في Microsoft Excel دون كتابة الدالة في ورقة العمل باستخدام JavaScript عبر C++. قم بتحميل ملف إكسل موجود أو أنشئ واحدًا جديدًا، احسب الدالة المخصصة، واحتفظ بالملف المعدل.
keywords: Aspose.Cells، إكسل، الدالات المخصصة، الحساب المباشر، JavaScript عبر C++، دون الحاجة للكتابة، أوراق العمل
type: docs
weight: 90
url: /ar/javascript-cpp/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/
---

## **الحساب المباشر للوظيفة المخصصة دون كتابتها في ورقة العمل**

يشرح هذا الموضوع كيف يمكنك حساب وظائفك المخصصة مباشرة دون كتابتها أولاً في ورقة عمل. يرجى استخدام طريقة [**Worksheet.calculateFormula(formula, opts)**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#calculateFormula-string-CalculationOptions-) لهذا الغرض.

يرجى الاطلاع على الرمز العيني التالي الذي يوضح استخدام هذه الطريقة. لقد استخدمنا وظيفة مخصصة باسم MyCompany.CustomFunction() وقمنا بحساب قيمتها كـ 'Aspose.Cells.' بأنفسنا ثم يتم دمج هذه القيمة تلقائيًا مع قيمة الخلية A1 التي هي 'مرحبًا بك في ' بواسطة محرك الحساب وتعيد القيمة المحسوبة النهائية كـ 'مرحبا بك في Aspose.Cells.' كما ترون في الرمز البرمجي لم نكتب وظيفتنا المخصصة في أي مكان في ورقة العمل ويتم حسابها مباشرة بواسطة منطقنا المخصص.

### **نموذج برمجة**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Custom Function Example</title>
    </head>
    <body>
        <h1>Implement Direct Calculation Of Custom Function</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, AbstractCalculationEngine, CalculationOptions } = AsposeCells;

        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: [
                "arial.ttf",
                "NotoSansSC-Regular.ttf"
            ]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });

        class CustomEngine extends AbstractCalculationEngine {
            // Override the calculate method with custom logic
            calculate(data) {
                // Check the formula name and calculate it yourself
                if (data.functionName === "MyCompany.CustomFunction") {
                    // This is our calculated value
                    data.calculatedValue = "Aspose.Cells.";
                }
            }
        }

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                // Create a new workbook if no file is provided
                workbook = new Workbook();
            }

            // Access first worksheet
            const ws = workbook.worksheets.get(0);

            // Add some text in cell A1
            ws.cells.get("A1").putValue("Welcome to ");

            // Create a calculation options with custom engine
            const opts = new CalculationOptions();
            opts.customEngine = new CustomEngine();

            // This line shows how you can call your own custom function without
            // a need to write it in any worksheet cell
            // After the execution of this line, it will return
            // Welcome to Aspose.Cells.
            const ret = ws.calculateFormula("=A1 & MyCompany.CustomFunction()", opts);

            // Write the returned value into B1 for demonstration
            ws.cells.get("B1").putValue(ret);

            // Prepare download of the modified workbook
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Calculated Value: ' + ret + '</p>';
        });
    </script>
</html>
```

### **مخرجات الوحدة**

فيما يلي إخراج وحدة التحكم للرمز العيني أعلاه.

{{< highlight javascript >}}

Calculated Value: Welcome to Aspose.Cells.

{{< /highlight >}}

### **مقال ذو صلة**

{{% alert color="primary" %}}

[تنفيذ محرك حساب مخصص لتوسيع محرك الحساب الافتراضي لمكتبة Aspose.Cells](/cells/ar/javascript-cpp/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/)

{{% /alert %}}
