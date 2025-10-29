---
title: الحصول على قيمة سلسلة الخلية مع أو بدون تنسيق
type: docs
weight: 240
url: /ar/javascript-cpp/get-cell-string-value-with-and-without-formatting/
description: تعلم كيفية الحصول على قيمة سلسلة الخلية مع وبدون تنسيق من خلال Aspose.Cells for Javaسكريبت عبر واجهة برمجة التطبيقات C++.
keywords: احصل على قيمة سلسلة الخلية مع وبدون تنسيق جافا سكريبت عبر C++، استرجع قيمة سلسلة الخلية مع وبدون تنسيق جافا سكريبت عبر C++، احصل على قيمة سلسلة الخلية مع وبدون تنسيق جافا سكريبت عبر C++
---

{{% alert color="primary" %}}

توفر Aspose.Cells خاصية [**Cell.stringValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#stringValue--) التي يمكن استخدامها للحصول على القيمة النصية للخلية مع أو بدون أي تنسيق. لنفترض أن لديك خلية بقيمة 0.012345 وقمت بتنسيقها لعرض منزلتين عشريتين فقط. فستعرض في إكسل كـ 0.01. يمكنك استرجاع القيم النصية كل من 0.01 و 0.012345 باستخدام خاصية [**Cell.stringValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#stringValue--). تأخذ [**CellValueFormatStrategy**](https://reference.aspose.com/cells/javascript-cpp/cellvalueformatstrategy/) نوع تعداد كمعامل والذي يحتوي على القيم التالية

- CellValueFormatStrategy.CellStyle
- CellValueFormatStrategy.DisplayStyle
- CellValueFormatStrategy.DisplayString
- CellValueFormatStrategy.None

{{% /alert %}}

يوضح الشفرة النموذجية التالية استخدام الخاصية [**Cell.stringValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#stringValue--).

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Cell } = AsposeCells;

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
            // Creating a new workbook
            const workbook = new Workbook();

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access cell A1
            const cell = worksheet.cells.get("A1");

            // Put value inside the cell
            cell.putValue(0.012345);

            // Format the cell that it should display 0.01 instead of 0.012345
            const style = cell.style;
            style.number = 2;
            cell.style = style;

            // Get string value as Cell Style
            let value = cell.stringValue;
            console.log(value);
            document.getElementById('result').innerHTML = `<p>Formatted string value: ${value}</p>`;

            // Get string value without any formatting
            value = cell.stringValue;
            console.log(value);
            document.getElementById('result').innerHTML += `<p>Unformatted string value: ${value}</p>`;

            // Save workbook and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';
        });
    </script>
</html>
```
