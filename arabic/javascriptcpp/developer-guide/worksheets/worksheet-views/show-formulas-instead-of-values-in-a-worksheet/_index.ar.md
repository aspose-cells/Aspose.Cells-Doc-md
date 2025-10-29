---
title: عرض الصيغ بدلاً من القيم في ورقة عمل باستخدام جافا سكريبت عبر ++C
linktitle: عرض الصيغ بدلاً من القيم في ورقة العمل
type: docs
weight: 20
url: /ar/javascript-cpp/show-formulas-instead-of-values-in-a-worksheet/
description: يوفر هذا المقال رمزًا نماذجياً لاستخدام واجهة برمجة التطبيقات جافا سكريبت عبر ++C لعرض الصيغ بدلاً من القيم في ورقة عمل أو جدول إكسل.
---

{{% alert color="primary" %}}

من الممكن عرض الصيغ بدلاً من القيم المحسوبة في إكسل باستخدام خيار **عرض الصيغ** من الشريط **الصيغ**. عند عرض الصيغ، يظهر إكسل الصيغ في ورقة العمل. يمكنك تحقيق نفس الشيء باستخدام Aspose.Cells for JavaScript عبر ++C.

{{% /alert %}}

توفر Aspose.Cells خاصية اختيار التحقق من الأخطاء. تدير فئة {0} أنواع مختلفة من فحوصات الأخطاء، على سبيل المثال، الأرقام المخزنة كنص، أخطاء حساب الصيغ، وأخطاء التحقق من الصحة. استخدم تعداد {1} لضبط نوع التحقق من الأخطاء المطلوب.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Show Formulas Example</title>
    </head>
    <body>
        <h1>Show Formulas Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell, Utils } = AsposeCells;

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

            // Load the source workbook
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Show formulas of the worksheet
            worksheet.showFormulas = true;

            // Save the workbook
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'source.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Formulas are now visible. Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
