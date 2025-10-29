---
title: تعيين الصيغة المشتركة باستخدام JavaScript عبر C++
linktitle: ضبط الصيغ المشتركة
type: docs
weight: 10
url: /ar/javascript-cpp/setting-shared-formula/
---

{{% alert color="primary" %}}

إذا كنت تريد إضافة دالة إلى ورقة عمل التي ستقوم ببعض العمليات الحسابية، يشرح هذا المقال كيفية تحقيق ذلك باستخدام Script Aspose.Cells for Java عبر C++.

{{% /alert %}}

## تعيين الصيغة المشتركة باستخدام Script Aspose.Cells for Java عبر C++

من المفترض أن يكون لديك ورقة عمل مليئة بالبيانات بتنسيق يبدو مثل الورقة العمل النموذجية التالية.

|**ملف الإدخال مع عمود واحد من البيانات**|
| :- |
|![todo:image_alt_text](setting-shared-formula_1.png)|

ترغب في إضافة وظيفة في B2 التي ستقوم بحساب ضريبة المبيعات للصف الأول من البيانات. الضريبة **9%**. الصيغة التي تحسب ضريبة المبيعات هي: **"=A2*0.09"**. يشرح هذا المقال كيفية تطبيق هذه الصيغة باستخدام Aspose.Cells.

يتيح لك Aspose.Cells تحديد صيغة باستخدام الخاصية [**Cell.formula**](https://reference.aspose.com/cells/javascript-cpp/cell/#formula--). هناك خياران لإضافة الصيغ إلى الخلايا الأخرى (B3 و B4 و B5، وهلم جرا.) في العمود.

إما أن تفعل ما فعلته للخلية الأولى، بحيث تقوم بشكل فعال بتعيين الصيغة لكل خلية، مع تحديث مرجع الخلية وفقًا لذلك (A3*0.09، A4*0.09، A5*0.09 وهكذا). يتطلب هذا تحديث مراجع الخلايا لكل صف. كما يتطلب أن يقوم Aspose.Cells بتحليل كل صيغة بشكل فردي، مما قد يكون مكلفًا من حيث الوقت لأوراق عمل كبيرة وصيغ معقدة. كما يضيف الكود خطوطًا إضافية على الرغم من أن الحلقات يمكن أن تقصرها بعض الشيء.

وهجاهدًا عبارة عن استخدام **صيغة مشتركة**. مع الصيغة المشتركة، تُحدث الصيغ تلقائيًا لمراجع الخلية في كل صف بحيث تُحسب الضريبة بشكل صحيح. الأسلوب [**Cell.sharedFormula(string, number, number)**](https://reference.aspose.com/cells/javascript-cpp/cell/#sharedFormula-string-number-number-) أكثر كفاءة من الأسلوب الأول.

تُظهر المثال التالي كيفية استخدامه.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Apply Shared Formula</title>
    </head>
    <body>
        <h1>Apply Shared Formula Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell } = AsposeCells;

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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate a Workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get the cells collection in the first worksheet
            const cells = workbook.worksheets.get(0).cells;

            // Apply the shared formula in the range i.e., B2:B14
            const cell = cells.get("B2");
            // Converted setSharedFormula(...) to property assignment per universal rule.
            cell.sharedFormula = { formula: "=A2*0.09", rowCount: 13, columnCount: 1 };

            // Save the excel file and provide a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData], { type: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Shared formula applied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
