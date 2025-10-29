---
title: إلغاء تجميد الصفوف أو الأعمدة باستخدام جافا سكريبت عبر C++
linktitle: إلغاء تجميد الأجزاء
type: docs
weight: 190
url: /ar/javascript-cpp/unfreeze-rows-or-columns-of-excel-worksheet
description: في هذه المقالة، ستتعلم كيفية إلغاء تجميد الصفوف والأعمدة أو اللوحات في أوراق عمل اكسل برمجيًا باستخدام API جافا سكريبت مع C++.
keywords: إلغاء تجميد الألواح، إلغاء تجميد الصفوف، إلغاء تجميد الأعمدة، إلغاء تجميد النافذة جافا سكريبت عبر C++.
---

## **مقدمة**

في هذا المقال، سنتعلم كيفية إلغاء تثبيت الصفوف والأعمدة والألواح. إذا كانت أوراق عمل في ملفات Excel مجمدة، أحيانًا نرغب في إلغاء تجميد الورقة أو تعديل الصفوف والأعمدة أو الألواح المجمدة.


## **في إكسل**

1. انقر على علامة التبويب عرض > تجميد الألواح > إلغاء تجميد الألواح.

**![إلغاء تجميد الألواح في إكسل](Unfreeze-Panes.png)**




## **إلغاء تجميد الصفوف أو الأعمدة أو الألواح باستخدام Aspose.Cells for JavaScript عبر C++**
من السهل إلغاء تجميد الألواح باستخدام Aspose.Cells for JavaScript عبر C++. يرجى استخدام طريقة [**Worksheet.unFreezePanes()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#unFreezePanes--) لإلغاء تجميد الألواح.

1. إنشاء ورقة عمل لفتح الملف المجمد.
2. إلغاء تجميد الألواح باستخدام طريقة Worksheet.unFreezePanes().
3. حفظ الملف.

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8" />
        <title>Aspose.Cells Example - Unfreeze Panes</title>
    </head>
    <body>
        <h1>Unfreeze Panes Example</h1>
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

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet and unfreezing panes
            const worksheet = workbook.worksheets.get(0);
            worksheet.unFreezePanes();

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Unfrozen.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Unfrozen Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Panes unfrozen successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

المرفق [ملف إكسل عيني](Frozen.xlsx).
