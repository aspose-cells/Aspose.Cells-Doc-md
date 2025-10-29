---
title: تحويل Excel إلى JSON باستخدام JavaScript عبر C++
linktitle: تحويل إكسل إلى JSON
type: docs
weight: 300
url: /ar/javascript-cpp/convert-excel-to-json/
description: تعلم كيفية تحويل ملف Excel إلى JSON باستخدام Aspose.Cells for JavaScript عبر C++. 
keywords: تصدير دفتر العمل إلى JSON جافا سكريبت عبر C++
---

{{% alert color="primary" %}}  
 يدعم Aspose.Cells تحويل مصنف إلى ملف JSON (ترميز كائن جافا سكريبت).  
{{% /alert %}}  

## **تحويل دفتر العمل Excel إلى JSON**  

لا حاجة للتساؤل عن كيفية تحويل دفتر عمل إكسل إلى JSON، لأن مكتبة Aspose.Cells for JavaScript عبر C++ توفر الحل الأمثل. توفر واجهة برمجة التطبيقات Aspose.Cells دعمًا لتحويل جداول البيانات إلى تنسيق JSON. لتصدير دفتر العمل إلى JSON، مرر [**SaveFormat.Json**](https://reference.aspose.com/cells/javascript-cpp/saveformat/) كوسيط ثاني لطريقة [**Workbook.save(string, SaveFormat)**](https://reference.aspose.com/cells/javascript-cpp/workbook/#save-string-saveformat-). يمكنك أيضًا استخدام فئة [**JsonSaveOptions**](https://reference.aspose.com/cells/javascript-cpp/jsonsaveoptions/) لتحديد إعدادات إضافية لتصدير ورقة العمل إلى JSON.  

يسهل مثال الكود التالي تصدير مصنف Excel إلى JSON. يرجى مراجعة الكود لتحويل [الملف المصدر](sample.xlsx) إلى ملف JSON الناتج كمثال.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Convert Excel to JSON Example</h1>
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

            // Convert the workbook to JSON
            const outputData = workbook.save(SaveFormat.Json);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'sample_out.json';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download JSON File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Conversion to JSON completed. Click the download link to get the JSON file.</p>';
        });
    </script>
</html>
```  

يستخدم مثال الكود التالي فئة JsonSaveOptions لتحديد إعدادات إضافية ويظهر تصدير مصنف Excel إلى JSON. يرجى مراجعة الكود لتحويل [الملف المصدر](sample.xlsx) إلى ملف JSON الناتج كمثال.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Convert Workbook to JSON Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, CellArea, JsonSaveOptions, Utils } = AsposeCells;

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

            // Load your source workbook
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Create an options of saving the file.
            const options = new JsonSaveOptions();

            // Set the exporting range.
            options.exportArea = CellArea.createCellArea("B1", "C4");

            // Convert the workbook to json file.
            const outputData = workbook.save(SaveFormat.Json, options);

            const blob = new Blob([outputData], { type: 'application/json' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'sample_out.json';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download JSON File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Conversion completed successfully! Click the download link to get the JSON file.</p>';
        });
    </script>
</html>
```
