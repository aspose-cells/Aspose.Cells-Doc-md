---
title: تحويل JSON إلى CSV باستخدام جافا سكريبت عبر C++
linktitle: تحويل JSON إلى CSV
type: docs
weight: 210
url: /ar/javascript-cpp/convert-json-to-csv/
description: تعرّف على كيفية تحويل بيانات JSON إلى CSV باستخدام Aspose.Cells for JavaScript عبر C++.
---

## **تحويل JSON إلى CSV**

يدعم Aspose.Cells for JavaScript عبر C++ تحويل JSON البسيط والمتداخل إلى CSV. لهذا، توفر الواجهة [**JsonLayoutOptions**](https://reference.aspose.com/cells/javascript-cpp/jsonlayoutoptions) و [**JsonUtility**](https://reference.aspose.com/cells/javascript-cpp/jsonutility) من الفئات. توفر فئة [**JsonLayoutOptions**](https://reference.aspose.com/cells/javascript-cpp/jsonlayoutoptions) الخيارات لتنسيق JSON مثل [**JsonLayoutOptions.arrayAsTable**](https://reference.aspose.com/cells/javascript-cpp/jsonlayoutoptions/#arrayAsTable--) (يعالج المصفوفة كجدول). تعالج فئة [**JsonUtility**](https://reference.aspose.com/cells/javascript-cpp/jsonutility) JSON باستخدام خيارات التخطيط المحددة مع فئة [**JsonLayoutOptions**](https://reference.aspose.com/cells/javascript-cpp/jsonlayoutoptions).

يوضح الكود التالي استخدام فئتي [**JsonLayoutOptions**](https://reference.aspose.com/cells/javascript-cpp/jsonlayoutoptions) و [**JsonUtility**](https://reference.aspose.com/cells/javascript-cpp/jsonutility) لتحميل ملف JSON المصدر ([104398869.json]) وتوليد ملف CSV الإخراجي ([104398870.csv]).

### **الكود المثالي**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells JSON to CSV Example</title>
    </head>
    <body>
        <h1>Import JSON to CSV Example</h1>
        <input type="file" id="fileInput" accept=".json" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, JsonLayoutOptions, JsonUtility, Utils } = AsposeCells;

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
                resultDiv.innerHTML = '<p style="color: red;">Please select a JSON file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const jsonText = await file.text();

            // Create empty workbook
            const workbook = new Workbook();

            // Get Cells from first worksheet
            const cells = workbook.worksheets.get(0).cells;

            // Set JsonLayoutOptions
            const importOptions = new JsonLayoutOptions();
            importOptions.convertNumericOrDate = true;
            importOptions.arrayAsTable = true;
            importOptions.ignoreTitle = true;

            // Import JSON data into worksheet cells starting at A1 (0,0)
            JsonUtility.importData(jsonText, cells, 0, 0, importOptions);

            // Save Workbook as CSV
            const outputData = workbook.save(SaveFormat.Csv);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'SampleJson_out.csv';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download CSV File';

            resultDiv.innerHTML = '<p style="color: green;">JSON imported and CSV prepared. Click the download link to get the CSV file.</p>';
        });
    </script>
</html>
```
