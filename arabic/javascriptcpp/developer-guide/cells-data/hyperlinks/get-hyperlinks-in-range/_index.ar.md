---
title: الحصول على الارتباطات التشعبية في النطاق
type: docs
weight: 100
url: /ar/javascript-cpp/get-hyperlinks-in-range/
description: تعلم كيفية الحصول على الروابط التشعبية في النطاق عبر Aspose.Cells for JavaScript عبر API C++.
keywords: الحصول على الروابط التشعبية في النطاق باستخدام JavaScript عبر C++، الحصول على جميع الروابط التشعبية الموجودة في النطاق المحدد باستخدام JavaScript عبر C++، حذف الرابط التشعبي في النطاق باستخدام JavaScript، حذف الروابط التشعبية في النطاق المحدد باستخدام JavaScript عبر C++
---

## **الحصول على الارتباطات التشعبية في النطاق**

تقدم فئة [**Range**](https://reference.aspose.com/cells/javascript-cpp/range) طريقة [**hyperlinks**](https://reference.aspose.com/cells/javascript-cpp/range/#hyperlinks--) التي تعيد جميع الروابط التشعبية في النطاق المحدد. يمكنك أيضًا حذف الرابط عن طريق استدعاء طريقة [**Hyperlink.delete()**](https://reference.aspose.com/cells/javascript-cpp/hyperlink/#delete--).


```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Hyperlinks Example</title>
    </head>
    <body>
        <h1>Hyperlinks Example</h1>
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
            const resultDiv = document.getElementById('result');
            resultDiv.innerHTML = '';

            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate a Workbook object by opening the uploaded Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get the first (default) worksheet
            const worksheet = workbook.worksheets.get(0);

            // Create a range A2:B3
            const range = worksheet.cells.createRange("A2", "B3");

            // Get Hyperlinks in range
            const hyperlinks = range.hyperlinks;

            let logText = '';
            for (let i = 0; i < hyperlinks.count; i++) {
                const link = hyperlinks.get(i);
                logText += `${link.area} : ${link.address}\n`;

                // To delete the link, use the Hyperlink.Delete() method.
                link.delete();
            }

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'HyperlinksSample_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p><pre>' + (logText || 'No hyperlinks found') + '</pre>';
        });
    </script>
</html>
```
