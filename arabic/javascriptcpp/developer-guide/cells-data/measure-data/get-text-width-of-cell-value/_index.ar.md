---
title: الحصول على عرض النص لقيمة الخلية
type: docs
weight: 50
url: /ar/javascript-cpp/get-text-width-of-cell-value/
description: تعرف على كيفية الحصول على عرض نص قيمة الخلية من خلال Aspose.Cells for JavaScript عبر واجهة برمجة التطبيقات C++.
keywords: الحصول على عرض نص قيمة الخلية بواسطة جافا سكريبت عبر C++، الحصول على عرض نص قيمة الخلية بواسطة جافا سكريبت عبر C++
---

## **الحصول على عرض النص لقيمة الخلية**

في بعض الأحيان، قد يحتاج المطورون إلى حساب عرض قيمة الخلية لتنظيم البيانات في بعض التخطيطات. يوفر Aspose.Cells for JavaScript عبر C++ أسلوب [**CellsHelper.textWidth(string, Font, number)**](https://reference.aspose.com/cells/javascript-cpp/cellshelper/#textWidth-string-font-number-)، والذي يسمح للمطورين بالحصول على عرض النص لقيمة الخلية. يوضح الكود التالي كيفية استخدام [**CellsHelper.textWidth(string, Font, number)**](https://reference.aspose.com/cells/javascript-cpp/cellshelper/#textWidth-string-font-number-) للوصول إلى عرض النص لقيمة الخلية.

الملف المصدر المستخدم في مقطع الكود التالي مرفق للرجوع إليه.

ملف المصدر (96928090.xlsx)

## كود عينة

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Text Width Example</title>
    </head>
    <body>
        <h1>Get Text Width Example</h1>
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
            const resultDiv = document.getElementById('result');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet and A1 cell
            const worksheet = workbook.worksheets.get(0);
            const cell = worksheet.cells.get("A1");

            // Accessing default font style
            const font = workbook.defaultStyle.font;

            // Calculating text width using CellsHelper (converted getter name to property)
            const textWidth = AsposeCells.CellsHelper.textWidth(cell.stringValue, font, 1);

            resultDiv.innerHTML = `<p style="color: green;">Text width: ${textWidth}</p>`;
        });
    </script>
</html>
```
