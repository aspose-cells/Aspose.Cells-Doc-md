---
title: دمج أوراق عمل متعددة في ورقة عمل واحدة باستخدام جافا سكريبت عبر C++
linktitle: دمج الأوراق العمل المتعددة في ورقة عمل واحدة
type: docs
weight: 160
url: /ar/javascript-cpp/combine-multiple-worksheets-into-a-single-worksheet/
description: تعلم كيفية دمج عدة أوراق عمل في ورقة عمل واحدة باستخدام سكربت Aspose.Cells for Java عبر C++. 
---

{{% alert color="primary" %}} 

في بعض الأحيان، قد تحتاج إلى دمج أوراق العمل المتعددة في ورقة عمل واحدة. يمكن بسهولة تحقيق ذلك باستخدام واجهة برمجة التطبيقات Aspose.Cells. سيوضح لك هذا المقال مثالًا على الكود الذي يقوم بقراءة دفتر عمل المصدر ويدمج البيانات من جميع أوراق العمل المصدر في ورقة عمل واحدة داخل دفتر عمل الوجهة.

{{% /alert %}} 

يُظهر مقطع الكود التالي لك كيفية دمج أوراق عمل متعددة في ورقة عمل واحدة.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Merge Worksheets into One Workbook</h1>
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Loads the workbook which contains hidden external links
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            const destWorkbook = new Workbook();
            const destSheet = destWorkbook.worksheets.get(0);

            let TotalRowCount = 0;

            for (let i = 0; i < workbook.worksheets.count; i++) {
                const sourceSheet = workbook.worksheets.get(i);

                const sourceRange = sourceSheet.cells.maxDisplayRange;
                const destRange = destSheet.cells.createRange(
                    sourceRange.firstRow + TotalRowCount,
                    sourceRange.firstColumn,
                    sourceRange.rowCount,
                    sourceRange.columnCount
                );

                destRange.copy(sourceRange);
                TotalRowCount += sourceRange.rowCount;
            }

            const outputData = destWorkbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Output.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Merged Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook merged successfully! Click the download link to get the result.</p>';
        });
    </script>
</html>
```
