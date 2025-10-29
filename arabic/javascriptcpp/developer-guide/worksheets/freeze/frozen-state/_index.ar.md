---
title: كيفية التحقق من حالة التجميد بدون إكسل باستخدام جافا سكريبت عبر C++
linktitle: الحالة المجمدة
type: docs
weight: 190
url: /ar/javascript-cpp/how-to-check-frozen-state-of-excel-worksheet
description: في هذا المقال، ستتعلم كيفية التحقق من حالة التجميد لورقة عمل إكسل برمجياً باستخدام جافا سكريبت مع مكتبة C++.
---

## **مقدمة**

في هذا المقال، سنتعلم كيفية التحقق من الحالة المجمدة لورقة عمل إكسل برمجياً. يمكننا ببساطة معرفة ما إذا كانت الورقة مجمدة أو مقسمة في MS Excel. لكن هل هناك طريقة لمعرفة ذلك باستخدام جافا سكريبت؟ يمكننا ببساطة القيام بذلك مع Aspose.Cells for JavaScript عبر C++.

## **هل النوافذ مجمدة**
باستخدام Aspose.Cells for JavaScript عبر C++، يمكننا التحقق مما إذا كانت النافذة مجمدة وكم عدد الصفوف والأعمدة المقفلة.

يرجى استخدام خاصية [**Worksheet.paneState**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#paneState--) للتحقق من حالة ألواح النوافذ والحصول على الصفوف والأعمدة المقفلة باستخدام خاصية [**Worksheet.freezedPanes**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#freezedPanes--).
1. إنشاء سجل العمل لفتح الملف.
2. التحقق ما إذا كانت ورقة العمل مجمدة.
3. احصل على الصفوف والأعمدة المقفلة.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Check Frozen Panes Example</title>
    </head>
    <body>
        <h1>Check Frozen Panes Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, PaneStateType, Utils } = AsposeCells;

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

            // Loading the workbook which contains frozen panes
            const workbook = new Workbook(new Uint8Array(arrayBuffer));
            const sheet = workbook.worksheets.get(0);

            // Check whether worksheet is frozen.
            const paneState = sheet.paneState;
            if (paneState === PaneStateType.Frozen || paneState === PaneStateType.FrozenSplit) {
                // Gets locked rows and columns.
                const panes = sheet.freezedPanes;
                let html = '<p style="color: green;">Worksheet has frozen panes. Details:</p><ul>';
                panes.forEach((value) => {
                    const row = value[0];
                    const column = value[1];
                    const rows = value[2];
                    const columns = value[3];
                    html += `<li>row: ${row}, column: ${column}, rows: ${rows}, columns: ${columns}</li>`;
                });
                html += '</ul>';
                document.getElementById('result').innerHTML = html;
            } else {
                document.getElementById('result').innerHTML = '<p>Worksheet is not frozen.</p>';
            }
        });
    </script>
</html>
```
