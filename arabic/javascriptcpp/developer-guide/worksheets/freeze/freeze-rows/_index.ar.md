---
title: تجميد الصف العلوي / الصفوف العلوية لورقة عمل إكسل باستخدام جافا سكريبت عبر C++
linktitle: تجميد الصفوف
type: docs
weight: 190
url: /ar/javascript-cpp/how-to-freeze-rows-of-excel-worksheet
description: في هذا المقال، ستتعلم كيفية تجميد الصفوف العلوية لورقات عمل إكسل برمجياً باستخدام مكتبة جافا سكريبت مع API لـ C++.
keywords: تجميد الصفوف العلوية، تجميد الصف العلوي جافا سكريبت عبر C++.
---

## **مقدمة**

في هذا المقال، سنتعلم كيف نجمد الصف (الصفوف) العلوية. عندما يكون لديك كمية هائلة من البيانات تحت عنوان مشترك، لا يمكنك رؤية العنوان عند التمرير لأسفل في الورقة. يمكنك تجميد الصفوف العليا بحيث يمكنك رؤية الجزء المجمد حتى عند تمرير الباقي من البيانات. يمكنك بسهولة رؤية رؤوس الأعمدة في الصفوف العليا.

## **تجميد الصفوف في إكسل**

**![تجميد الصفوف العلوية في إكسل](Freeze-Rows.png)**

1. إذا أردت تجميد الصف العلوي، فابدأ بتحديد الصف تحت الصف الذي يحتاج إلى تجميده.
2. انقر على عرض > تجميد الأجزاء.
3. في القائمة المنسدلة، انقر على تجميد الصف العلوي.
4. إذا قمت بالتمرير لأسفل، سيكون الصف الأول دائماً في أعلى العرض.

**![صف مجمد](Frozen-Row.png)**

كما ترى، الصف الأول مجمد؛ يبقى الصف الأول دائمًا في أعلى العرض عند التمرير لأسفل.

تجميد الصفوف يتيح لك عرض بياناتك الكبيرة بدون الحاجة لمتابعة تسميات الصفوف.

## **تجميد الصفوف باستخدام Aspose.Cells for JavaScript عبر C++**
من السهل تجميد الصف / الصفوف باستخدام Aspose.Cells for JavaScript عبر C++. 
يرجى استخدام طريقة [**Worksheet.freezePanes(number, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#freezePanes-number-number-number-number-) لتجميد الصف (الصفوف) عند الصف المحدد.
1. إنشاء دفتر العمل لفتح الملف أو إنشاء ملف فارغ.
2. تجميد الصف الأول باستخدام طريقة Worksheet.freezePanes()
3. حفظ الملف.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Freeze Panes</title>
    </head>
    <body>
        <h1>Freeze Panes Example</h1>
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

            // Instantiate a new Workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Freezing panes at the cell B2 on the first worksheet
            const worksheet = workbook.worksheets.get(0);
            worksheet.freezePanes("A2", 1, 0);

            // Saving the file and providing a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'frozen.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Frozen Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Freeze panes applied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

[ملف Excel مصدري عينة مرفق](../Freeze.xlsx).
