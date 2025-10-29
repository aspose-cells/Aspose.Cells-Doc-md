---
title: الحصول على الحد الأقصى لمؤشر العمود في الصف والحد الأقصى لمؤشر الصف في العمود
type: docs
weight: 600
url: /ar/javascript-cpp/get-max-index-in-row-and-column/
description: تعلم كيفية الحصول على أقصى فهرس عمود في الصف وأقصى فهرس صف في العمود عبر Aspose.Cells for JavaScript باستخدام واجهة برمجة التطبيقات C++.
keywords: الحصول على أقصى فهرس عمود في الصف باستخدام JavaScript عبر C++، الحصول على أقصى فهرس صف في العمود باستخدام JavaScript عبر C++، الحصول على الحد الأقصى لفهرس عمود البيانات في الصف باستخدام JavaScript عبر C++، الحصول على الحد الأقصى لفهرس صف البيانات في العمود باستخدام JavaScript عبر C++.
---

## **سيناريوهات الاستخدام المحتملة**
عندما تحتاج فقط إلى التلاعب ببعض البيانات في الصفوف أو الأعمدة، تحتاج إلى معرفة مدى البيانات للصفوف والأعمدة. تقدم لك Aspose.Cells for JavaScript عبر C++ هذه الميزة. للحصول على الحد الأقصى لفهرس العمود في صف، يمكنك الحصول على طرق [**Row.lastCell**](https://reference.aspose.com/cells/javascript-cpp/row/#lastCell--) و [**Row.lastDataCell**](https://reference.aspose.com/cells/javascript-cpp/row/#lastDataCell--)، ثم استخدام طريقة [**Cell.column**](https://reference.aspose.com/cells/javascript-cpp/cell/#column--) للحصول على الحد الأقصى لفهرس العمود وفهرس بيانات العمود، ولكن للحصول على الحد الأقصى لفهرس الصف وفهرس بيانات الصف في عمود، عليك إنشاء مدى على العمود، ثم عبور المدى للعثور على آخر خلية، وأخيرًا استدعاء طريقة [**Cell.row**](https://reference.aspose.com/cells/javascript-cpp/cell/#row--) على الخلية.

يوفر Aspose.Cells for JavaScript عبر C++ الخصائص والطرق التالية لمساعدتك على تحقيق أهدافك.
- [**Row.lastCell**](https://reference.aspose.com/cells/javascript-cpp/row/#lastCell--)
- [**Row.lastDataCell**](https://reference.aspose.com/cells/javascript-cpp/row/#lastDataCell--)
- [**Cell.column**](https://reference.aspose.com/cells/javascript-cpp/cell/#column--)
- [**Cell.row**](https://reference.aspose.com/cells/javascript-cpp/cell/#row--)

## **الحصول على أقصى فهرس عمود في الصف وأقصى فهرس صف في العمود**
يوضح هذا المثال كيف:

1. قم بتحميل [ملف العينة](sample.xlsx).
2. الحصول على الصف الذي يحتاج إلى الحصول على الحد الأقصى لمؤشر العمود والحد الأقصى لمؤشر البيانات في العمود.
1. استدعاء طريقة [**Cell.column**](https://reference.aspose.com/cells/javascript-cpp/cell/#column--) على الخلية.
1. أنشئ نطاقًا استنادًا إلى العمود.
1. احصل على المحدد وانتقل عبر النطاق.
1. استدعاء طريقة [**Cell.row**](https://reference.aspose.com/cells/javascript-cpp/cell/#row--) على الخلية.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
        <meta charset="utf-8" />
        <style>
            body { font-family: Arial, sans-serif; margin: 20px; }
            #result pre { background: #f4f4f4; padding: 10px; }
            #downloadLink { display: none; margin-top: 10px; display: inline-block; }
        </style>
    </head>
    <body>
        <h1>Get Max Row/Column Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink">Download Result</a>
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
            const resultDiv = document.getElementById('result');
            resultDiv.innerHTML = '';

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object by opening the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const sheet = workbook.worksheets.get(0);

            // Accessing cells collection
            const cells = sheet.cells;

            // Check row at index 1
            const row = cells.checkRow(1);
            const outputLines = [];

            if (row != null) {
                // get Maximum column index of Row which contains data or style.
                outputLines.push("Max column index in row: " + row.lastCell.column);

                // get Maximum column index of Row which contains data.
                outputLines.push("Max data column index in row: " + row.lastDataCell.column);
            } else {
                outputLines.push("Row 1 is empty (checkRow returned null).");
            }

            // create the range of column B (index 1)
            const columnRange = cells.createRange(1, 1, true);

            var max_row_index  = cells.maxRow + 1;
            var maxRow = 0;
            var maxDataRow = 0;

            for (let row_index = 0; row_index < max_row_index; row_index++) {
                var curr_cell = cells.get(row_index, 1);

                if (curr_cell) {
                    if (curr_cell.stringValue) {
                        maxDataRow = curr_cell.row;
                    }

                    if (curr_cell.stringValue || curr_cell.hasCustomStyle) {
                        maxRow = curr_cell.row;
                    }
                }
            }

            // Maximum row index of Column which contains data or style.
            outputLines.push("Max row index in Column: " + maxRow);

            // Maximum row index of Column which contains data.
            outputLines.push("Max data row index in Column: " + maxDataRow);

            resultDiv.innerHTML = '<pre>' + outputLines.join('\n') + '</pre>';
        });
    </script>
</html>
```
