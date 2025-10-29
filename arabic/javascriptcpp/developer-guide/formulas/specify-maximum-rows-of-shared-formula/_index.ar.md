---
title: تحديد الحد الأقصى لعدد الصفوف للصيغة المشتركة باستخدام JavaScript عبر C++
linktitle: كما يمكن استخدام الخاصية {0} لتحديد الصفوف القصوى للصيغة المشتركة.
type: docs
weight: 40
url: /ar/javascript-cpp/specify-maximum-rows-of-shared-formula/
description: تعلم كيفية تحديد الحد الأقصى للصفوف للصيغ المشتركة باستخدام Script Aspose.Cells for Java عبر C++.
---

## **سيناريوهات الاستخدام المحتملة**  

الحد الأقصى الافتراضي لصفوف الصيغة المشتركة هو 64. يمكن أن يكون أي رقم مثل 1000. تتغير أداء الصيغة المشتركة مع اختلاف عدد الصفوف. لذلك، يوفر Aspose.Cells الخاصية [**WorkbookSettings.maxRowsOfSharedFormula**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#maxRowsOfSharedFormula--) التي يمكن استخدامها لتحديد الحد الأقصى لصفوف الصيغة المشتركة. سيتم تقسيم الصيغة المشتركة إلى عدة صيغ مشتركة إذا كان إجمالي صفوفها أكبر من ذلك، كما هو موضح في لقطة الشاشة التالية.  

![todo:image_alt_text](specify-maximum-rows-of-shared-formula_1.png)  

## **تحديد الصفوف القصوى للصيغة المشتركة**  

يفسر الرمز النموذجي التالي استخدام الخاصية [**WorkbookSettings.maxRowsOfSharedFormula**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#maxRowsOfSharedFormula--). حيث يحدد الحد الأقصى لصفوف الصيغة المشتركة إلى 5 ويضيف الصيغة المشتركة في الخلية D1 لعشرة صفوف ويحفظها إلى [ملف إكسل الناتج](61767856.xlsx). إذا قمت باستخراج محتويات الملف وفحص *sheet1.xml*، سترى أن الصيغة المشتركة تنقسم بعد كل 5 صفوف كما هو موضح في لقطة الشاشة السابقة.  

## **الكود المثالي**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Specify Maximum Rows Of Shared Formula Example</title>
    </head>
    <body>
        <h1>Specify Maximum Rows Of Shared Formula Example</h1>
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
            let workbook;

            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                // Create a new workbook if no file is provided
                workbook = new Workbook();
            }

            // Set the max rows of shared formula to 5
            workbook.settings.maxRowsOfSharedFormula = 5;

            // Access first worksheet
            const ws = workbook.worksheets.get(0);

            // Access cell D1
            const cell = ws.cells.get("D1");

            // Set the shared formula in 100 rows
            cell.sharedFormula = ["=Sum(A1:A2)", 100, 1];

            // Save the output Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputSpecifyMaximumRowsOfSharedFormula.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
