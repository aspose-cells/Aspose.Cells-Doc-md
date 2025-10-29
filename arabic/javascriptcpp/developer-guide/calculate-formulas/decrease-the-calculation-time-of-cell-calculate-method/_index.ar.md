---
title: تقليل وقت حساب طريقة Cell.Calculate باستخدام JavaScript عبر C++
linktitle: تقليل وقت حساب أسلوب Cell.Calculate
description: تقدم هذه المقالة كيفية استخدام مكتبة Aspose.Cells لتقليل وقت الحوسبة لطرائق حساب الخلايا في Excel باستخدام JavaScript عبر C++.
keywords: Aspose.Cells، إكسل، طرق حساب الخلايا، تحسين، أداء، تقليل وقت الحساب، جافا سكريبت عبر C++
type: docs
weight: 100
url: /ar/javascript-cpp/decrease-the-calculation-time-of-cell-calculate-method/
---

## **سيناريوهات الاستخدام المحتملة**

عادةً، نوصي المستخدمين باستدعاء طريقة [**Workbook.calculateFormula()**](https://reference.aspose.com/cells/javascript-cpp/workbook/#calculateFormula--) مرة واحدة ثم الحصول على القيم المحسوبة للخلايا الفردية. لكن أحيانًا، لا يرغب المستخدمون في حساب المصنف بأكمله. إنهم يرغبون فقط في حساب خلية واحدة. توفر Aspose.Cells الخاصية [**CalculationOptions.recursive**](https://reference.aspose.com/cells/javascript-cpp/calculationoptions/#recursive--)، والتي يمكنك تعيينها إلى **false** لتقليل وقت حساب الخلايا الفردية بشكل كبير. عندما تكون الخاصية التكرارية مضبوطة على **true**، يتم إعادة حساب جميع الاعتمادات لكل استدعاء. ومع ذلك، عندما تكون الخاصية التكرارية **false**، يتم حساب الخلايا المعتمدة مرة واحدة فقط ولا يُعاد حسابها في الاستدعاءات التالية.

## **تقليل وقت الحساب باستخدام طريقة Cell.calculate()**

يُمثل رمز العينة التالي استخدام خاصية [**CalculationOptions.recursive**](https://reference.aspose.com/cells/javascript-cpp/calculationoptions/#recursive--). يُرجى تشغيل هذا الرمز مع [ملف الإكسل النموذجي](5113710.xlsx) والتحقق من مخرجات وحدة التحكم. ستجد أن تعيين الخاصية التكرارية إلى **false** قد قلل بشكل كبير من وقت الحساب. يُرجى أيضًا قراءة التعليقات لفهم أفضل لهذه الخاصية.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Calculate Formulas Example</title>
    </head>
    <body>
        <h1>Calculate Formulas Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;

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

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            const resultEl = document.getElementById('result');
            if (!fileInput.files.length) {
                resultEl.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object by loading the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Test calculation time after setting recursive true
            workbook.calculateFormula(); // initiate calculation

            // Test calculation time after setting recursive false (specify ignoreError as false)
            workbook.calculateFormula(false);

            // Save the modified workbook and provide a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.calculated.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Calculated Excel File';

            resultEl.innerHTML = '<p style="color: green;">Calculation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
        <meta charset="utf-8" />
    </head>
    <body>
        <h1>Calculation Time Recursive Test</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Calculation Test (Recursive true/false)</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, CalculationOptions } = AsposeCells;

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

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            const resultDiv = document.getElementById('result');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object by loading the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const ws = workbook.worksheets.get(0);

            const runs = [true, false];
            let outputHtml = '';
            for (let r = 0; r < runs.length; r++) {
                const rec = runs[r];

                // Set the calculation option, set recursive true or false as per parameter
                const opts = new CalculationOptions();
                opts.recursive = rec;

                // Start stopwatch
                const start = performance.now();

                // Calculate cell A1 one million times
                for (let i = 0; i < 1000000; i++) {
                    ws.cells.get("A1").calculate(opts);
                }

                // Stop the watch
                const end = performance.now();

                // Calculate elapsed time in seconds
                const estimatedTime = (end - start) / 1000;

                // Record the elapsed time
                const message = `Recursive ${rec}: ${estimatedTime} seconds`;
                console.log(message);
                outputHtml += `<p>${message}</p>`;
            }

            resultDiv.innerHTML = `<div style="color: green;">${outputHtml}</div>`;
        });
    </script>
</html>
```

## **مخرجات الوحدة**

هذه مخرجات وحدة التحكم الخاصة بالرمز أعلاه عند تنفيذه باستخدام ملف إكسل النموذجي [5113710.xlsx](5113710.xlsx) على جهازنا. يُرجى ملاحظة أن مخرجاتك قد تختلف، ولكن وقت التنفيذ بعد تعيين الخاصية التكرارية إلى **false** سيكون دائمًا أقل من تعيينها إلى **true**.

{{< highlight java >}}  
Recursive True: 96 seconds  

Recursive False: 42 seconds  
{{< /highlight >}}
