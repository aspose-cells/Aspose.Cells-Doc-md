---
title: إزالة أنماط غير مستخدمة داخل مصنف العمل باستخدام جافا سكريبت عبر ++C
linktitle: إزالة الأنماط الغير مستخدمة في دفتر العمل
type: docs
weight: 340
url: /ar/javascript-cpp/remove-unused-styles-inside-the-workbook/
description: تعلم كيفية إزالة الأنماط غير المستخدمة من مصنف العمل باستخدام Aspose.Cells for JavaScript عبر ++C
---

{{% alert color="primary" %}}  
تستهلك الأنماط غير المستخدمة في ملفات Excel مساحة وتسبب أيضًا مشاكل في الأداء أثناء التحويل إلى تنسيقات مختلفة مثل PDF و HTML وغيرها. يوفر Aspose.Cells خاصية [**Workbook.removeUnusedStyles()**](https://reference.aspose.com/cells/javascript-cpp/workbook/#removeUnusedStyles--) لإزالة جميع الأنماط غير المستخدمة داخل دفتر العمل.  
{{% /alert %}}  

يوضح الكود التالي طريقة استخدام [**Workbook.removeUnusedStyles()**](https://reference.aspose.com/cells/javascript-cpp/workbook/#removeUnusedStyles--). يقوم الكود بتحميل ملف Excel النموذجي ([ملف القالب](5115520.xlsx)) الذي يمكنك تنزيله من الرابط المقدم. يحتوي على نمط غير مستخدم يُدعى **AsposeStyle**؛ سيتم حذف هذا النمط وجميع الأنماط غير المستخدمة الأخرى بعد تشغيل الكود.  

![todo:image_alt_text](remove-unused-styles-inside-the-workbook_1.png)  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Remove Unused Styles</title>
    </head>
    <body>
        <h1>Remove Unused Styles Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Utils } = AsposeCells;

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

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Remove all unused styles inside the workbook
            workbook.removeUnusedStyles();

            // Save the modified workbook as XLSX and provide a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Unused styles removed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
