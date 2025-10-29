---
title: تحويل CSV إلى JSON باستخدام JavaScript عبر C++
linktitle: تحويل CSV إلى JSON
type: docs
weight: 220
url: /ar/javascript-cpp/convert-csv-to-json/
description: تحويل ملف CSV إلى JSON باستخدام API Aspose.Cells for JavaScript سهلة الاستخدام عبر C++.
keywords: التحويل، تحويل CSV إلى JSON، CSV إلى JSON، CSV، JSON، تحويل CSV إلى JSON باستخدام JavaScript عبر C++، كود C++ لتحويل CSV إلى JSON
---

## **تحويل CSV إلى JSON**

يدعم Aspose.Cells تحويل CSV إلى JSON. لهذا، توفر API الفئات [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/javascript-cpp/exportrangetojsonoptions/) و [**JsonUtility**](https://reference.aspose.com/cells/javascript-cpp/jsonutility/). توفر فئة [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/javascript-cpp/exportrangetojsonoptions/) الخيارات لتصدير النطاق إلى JSON. تحتوي فئة [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/javascript-cpp/exportrangetojsonoptions/) على الخصائص التالية.

- [**ExportRangeToJsonOptions.exportAsString**](https://reference.aspose.com/cells/javascript-cpp/exportrangetojsonoptions/#exportAsString--): يقوم بتصدير قيمة السلسلة للخلايا إلى JSON.
- [**ExportRangeToJsonOptions.hasHeaderRow**](https://reference.aspose.com/cells/javascript-cpp/exportrangetojsonoptions/#hasHeaderRow--): يشير إلى ما إذا كان النطاق يحتوي على صف رأس.
- [**ExportRangeToJsonOptions.indent**](https://reference.aspose.com/cells/javascript-cpp/exportrangetojsonoptions/#indent--): يشير إلى المسافة البادئة.

تقوم فئة [**JsonUtility**](https://reference.aspose.com/cells/javascript-cpp/jsonutility/) بتصدير JSON باستخدام خيارات التصدير المحددة بواسطة فئة [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/javascript-cpp/exportrangetojsonoptions/).

يوضح المثال البرمجي التالي استخدام فئات [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/javascript-cpp/exportrangetojsonoptions/) و [**JsonUtility**](https://reference.aspose.com/cells/javascript-cpp/jsonutility/) لتحميل ملف CSV المصدر (104398879.csv) وطباعة إخراج JSON في وحدة التحكم.

### **الكود المثالي**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Export CSV Range to JSON Example</title>
    </head>
    <body>
        <h1>Export CSV Range to JSON Example</h1>
        <input type="file" id="fileInput" accept=".csv" />
        <button id="runExample">Export to JSON</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, LoadOptions, LoadFormat, JsonSaveOptions, JsonUtility } = AsposeCells;

        const runButton = document.getElementById('runExample');
        runButton.disabled = true;

        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: [
                "arial.ttf",
                "NotoSansSC-Regular.ttf"
            ]
        }).then(() => {
            console.log("Aspose.Cells initialized");
            runButton.disabled = false;
        });

        function escapeHtml(unsafe) {
            return unsafe
                .replace(/&/g, "&amp;")
                .replace(/</g, "&lt;")
                .replace(/>/g, "&gt;")
                .replace(/"/g, "&quot;")
                .replace(/'/g, "&#039;");
        }

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            const resultDiv = document.getElementById('result');
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.style.display = 'none';
            downloadLink.href = '';
            downloadLink.textContent = '';

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select a CSV file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            const loadOptions = new LoadOptions(LoadFormat.Csv);
            const workbook = new Workbook(new Uint8Array(arrayBuffer), loadOptions);

            const worksheet = workbook.worksheets.get(0);
            const lastCell = worksheet.cells.lastCell;

            const jsonSaveOptions = new JsonSaveOptions();
            const range = worksheet.cells.createRange(0, 0, lastCell.row + 1, lastCell.column + 1);
            const data = JsonUtility.exportRangeToJson(range, jsonSaveOptions);

            // Display JSON in the result div
            resultDiv.innerHTML = '<p style="color: green;">Export completed successfully!</p><pre>' + escapeHtml(data) + '</pre>';

            // Create a downloadable JSON file
            const blob = new Blob([data], { type: 'application/json' });
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'exported_range.json';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download JSON File';
        });
    </script>
</html>
```

### **مخرجات الوحدة**
{{< highlight java >}}

[
{
"id": 1,
"language": "Java",
"edition": "third",
"author": "Herbert Schildt",
"streetAddress": 126,
"city": "San Jone",
"state": "CA",
"postalCode": 394221
},
{
"id": 2,
"language": "C++",
"edition": "second",
"author": "EAAAA",
"streetAddress": 126,
"city": "San Jone",
"state": "CA",
"postalCode": 394221
},
{
"id": 3,
"language": ".Net",
"edition": "second",
"author": "E.Balagurusamy",
"streetAddress": 126,
"city": "San Jone",
"state": "CA",
"postalCode": 394221
}
]

{{< /highlight >}}
