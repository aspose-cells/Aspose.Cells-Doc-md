---
title: Json مع JavaScript عبر C++
linktitle: Json
type: docs
weight: 300
url: /ar/javascript-cpp/convert-workbook-to-json/
description: تعلم كيفية تحويل مصنف Excel إلى JSON باستخدام Script عبر C++ Aspose.Cells for Java.
---

{{% alert color="primary" %}}
يدعم Aspose.Cells تحويل مصنف إلى ملف Json (ترميز كائن JavaScript).
{{% /alert %}}

## **تحويل دفتر العمل Excel إلى JSON**

توفر API Aspose.Cells دعمًا لتحويل جداول البيانات إلى تنسيق JSON. لتصدير دفتر العمل إلى JSON، مرر [**SaveFormat.Json**](https://reference.aspose.com/cells/javascript-cpp/saveformat) كوسيط ثاني لطريقة [**Workbook.save(string, SaveFormat)**](https://reference.aspose.com/cells/javascript-cpp/workbook/#save-string-saveformat-). يمكنك أيضًا استخدام فئة [**JsonSaveOptions**](https://reference.aspose.com/cells/javascript-cpp/jsonsaveoptions) لتحديد إعدادات إضافية لتصدير ورقة العمل إلى JSON.

يوضح المثال التالي تصدير ورقة العمل النشطة إلى JSON باستخدام عضو التعداد [**SaveFormat.Json**](https://reference.aspose.com/cells/javascript-cpp/saveformat/#json). يرجى مراجعة الكود لتحويل [ملف المصدر](book1.xlsx) إلى ملف JSON الناتج [الذي أنشأه الكود](book1.Json) للمرجعية.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Convert Workbook to JSON</title>
    </head>
    <body>
        <h1>Convert Workbook to JSON Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Convert to JSON</button>
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

            // Instantiate Workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Save workbook as JSON
            const outputData = workbook.save(SaveFormat.Json);
            const blob = new Blob([outputData], { type: 'application/json' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'book1.json';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download JSON File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook converted to JSON successfully! Click the download link to get the JSON file.</p>';
        });
    </script>
</html>
```

## **مواضيع متقدمة**
- [تحويل CSV إلى JSON](/cells/ar/javascript-cpp/convert-csv-to-json/)
- [تحويل-Excel-إلى-JSON](/cells/ar/javascript-cpp/convert-excel-to-json/)
- [تحويل JSON إلى CSV](/cells/ar/javascript-cpp/convert-json-to-csv/)
- [تحويل JSON إلى Excel](/cells/ar/javascript-cpp/convert-json-to-excel/)
