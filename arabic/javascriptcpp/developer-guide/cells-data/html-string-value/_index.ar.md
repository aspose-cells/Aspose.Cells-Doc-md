---
title: إضافة نص HTML غني داخل الخلية
linktitle: قيمة سلسلة HTML
type: docs
weight: 50
url: /ar/javascript-cpp/adding-html-rich-text-inside-the-cell/
description: تعلم كيفية إضافة نص غني HTML داخل الخلية عبر Aspose.Cells for Javaسكريبت عبر API الخاص بـ C++.
keywords: إضافة نص غني HTML داخل الخلية جافا سكريبت عبر C++، تعيين نص غني HTML داخل الخلية جافا سكريبت عبر C++، إضافة نص غني HTML في الخلية جافا سكريبت عبر C++
---

{{% alert color="primary" %}}

يدعم Aspose.Cells تحويل HTML الموجه نحو Microsoft Excel إلى تنسيق XLS/XLSX. بمعنى أن HTML الذي ينتجه Microsoft Excel يمكن تحويله مرة أخرى إلى تنسيق XLS/XLSX باستخدام Aspose.Cells.

بالمثل، إذا كان هناك بعض HTML بسيط، يمكن لـ Aspose.Cells تحويله إلى Rich Text HTML. يوفر Aspose.Cells الخاصية[**Cell.htmlString**](https://reference.aspose.com/cells/javascript-cpp/cell/#htmlString-string-) التي يمكن أن تأخذ مثل هذا HTML البسيط وتحويله إلى نص خلية منسق.

{{% /alert %}}

تُظهر الشيفرة العينية أدناه كيفية إضافة نص HTML غني داخل الخلية. يرجى الاطلاع على لقطة شاشة لملف الإكسل الناتج.

![todo:image_alt_text](adding-html-rich-text-inside-the-cell_1)

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells HTML String Example</h1>
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
            let workbook;

            // If a file is provided, open it; otherwise create a new workbook
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Access the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access cell A1
            const cell = worksheet.cells.get("A1");

            // Set HTML formatted string to the cell (converted setter -> property)
            cell.htmlString = "<Font Style=\"FONT-WEIGHT: bold;FONT-STYLE: italic;TEXT-DECORATION: underline;FONT-FAMILY: Arial;FONT-SIZE: 11pt;COLOR: #ff0000;\">This is simple HTML formatted text.</Font>";

            // Save the workbook to XLSX format and provide a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData], { type: 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">HTML string written to A1. Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```


## مقالات ذات صلة

- [عرض الرموز باستخدام قيمة الخلية باستخدام HTML](/cells/ar/javascript-cpp/display-bullets-by-setting-cell-value-using/)
- [الحصول على سلسلة HTML5 من الخلية](/cells/ar/javascript-cpp/get-html5-string-from-cell/)
