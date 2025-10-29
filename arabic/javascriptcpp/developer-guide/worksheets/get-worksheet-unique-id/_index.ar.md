---
title: الحصول على معرف فريد لورقة العمل باستخدام جافا سكريبت عبر C++
linktitle: الحصول على معرّف الورقة العمل فريد
type: docs
weight: 190
url: /ar/javascript-cpp/get-worksheet-unique-id/
description: يعرض هذا المقال كيفية الحصول على معرف فريد لورقة عمل إكسل باستخدام مكتبة جافا سكريبت وواجهة برمجة التطبيقات C++ برمجياً.
keywords: معرّف فريد لورقة إكسل باستخدام جافا سكريبت عبر C++، معرف فريد لورقة عمل جافا سكريبت عبر C++
---

## **الحصول على معرف فريد لورقة العمل**

يوفر Aspose.Cells for JavaScript عبر C++ إمكانية الحصول على المعرف الفريد لورقة العمل باستخدام خاصية [**Worksheet.uniqueId**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#uniqueId--). يوضح مقتطف الكود التالي استخدام خاصية [**Worksheet.uniqueId**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#uniqueId--) لطباعة المعرف الفريد لورقة العمل. يستخدم هذا المقتطف [ملف إكسل النموذجي](105480213.xlsx).

### كود المصدر

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Get Worksheet Unique Id Example</h1>
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

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Get Unique Id
            const uniqueId = worksheet.uniqueId;
            console.log("Unique Id: " + uniqueId);

            document.getElementById('result').innerHTML = '<p style="color: green;">Unique Id: ' + uniqueId + '</p>';
        });
    </script>
</html>
```
