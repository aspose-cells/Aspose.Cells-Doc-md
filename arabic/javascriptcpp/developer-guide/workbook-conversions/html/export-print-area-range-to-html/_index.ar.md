---
title: تصدير نطاق منطقة الطباعة إلى HTML باستخدام JavaScript عبر C++
linktitle: تصدير نطاق منطقة الطباعة إلى HTML
type: docs
weight: 60
url: /ar/javascript-cpp/export-print-area-range-to/
---

## **سيناريوهات الاستخدام المحتملة**

هذا سيناريو شائع حيث نحتاج إلى تصدير منطقة الطباعة المحددة فقط أي مجموعة مختارة من الخلايا بدلاً من الورقة كاملة إلى HTML. تتوفر هذه الميزة بالفعل للطباعة؛ ومع ذلك، يمكنك الآن تنفيذ هذه المهمة لـ HTML أيضًا. أولاً، قم بضبط منطقة الطباعة في كائن إعداد الصفحة لورقة العمل. فيما بعد، استخدم العلامة [**HtmlSaveOptions.exportPrintAreaOnly()**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions/#exportPrintAreaOnly--) لتصدير النطاق المحدد فقط.

## كود عينة

يقوم الكود العيني التالي بتحميل دفتر عمل ثم يصدر منطقة الطباعة إلى HTML. يمكن تنزيل ملف العينة لاختبار هذه الميزة من الرابط التالي:

[sampleInlineCharts.xlsx](79527946.xlsx)

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Export Print Area to HTML Example</h1>
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

            // Instantiating a Workbook object by opening the Excel file through the file stream
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Set the print area.
            worksheet.pageSetup.printArea = "D2:M20";

            // Initialize HtmlSaveOptions
            const options = new AsposeCells.HtmlSaveOptions();

            // Set flag to export print area only
            options.exportPrintAreaOnly = true;

            // Save to HTML format (options specify HTML)
            const outputData = workbook.save(options);
            const blob = new Blob([outputData], { type: 'text/html' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputInlineCharts.html';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download HTML File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Export completed successfully! Click the download link to get the HTML file.</p>';
        });
    </script>
</html>
```
