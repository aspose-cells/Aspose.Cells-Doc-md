---
title: تحديث عنصر صيغة Power Query مع جافا سكريبت عبر C++
linktitle: تحديث عنصر صيغة Power Query
type: docs
weight: 120
url: /ar/javascript-cpp/update-power-query-formula-item/
description: تعلم كيفية تحديث مصدر بيانات عنصر صيغة Power Query في ملف Excel باستخدام Aspose.Cells for JavaScript عبر C++.
---

## **سيناريو الاستخدام**

قد تكون هناك حالات يتم فيها نقل ملفات المصدر البيانات ولا يستطيع ملف Excel تحديد الموقع. في مثل هذه الحالات، تقدم API الخاص بـ Aspose.Cells خيارًا لتحديث عنصر صيغة Power Query باستخدام فئة [*PowerQueryFormulaItem*](https://reference.aspose.com/cells/javascript-cpp/powerqueryformulaitem) لتحديث موقع ملف المصدر.

## **تحديث عنصر صيغة Power Query**

توفر API لـ Aspose.Cells القدرة على تحديث عناصر صيغة Power Query. يعرض المقطع التالي تحديث موقع ملف مصدر البيانات في ملف Excel باستخدام خاصية [**PowerQueryFormulaItem.value**](https://reference.aspose.com/cells/javascript-cpp/powerqueryformulaitem/#value--). المرفقات من الملفات المصدر والمخرج لمراجعتك.

- [ملف المصدر 1](106364953.xlsx)
- [ملف المصدر 2](106364954.xlsx)
- [ملف الناتج](106364955.xlsx)

## **الكود المثالي**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Power Query Formula Update Example</h1>
        <p>Select the workbook containing Power Query formulas and an optional source workbook to reference in the "Source" item.</p>
        <input type="file" id="fileInputMain" accept=".xls,.xlsx,.csv" />
        <br/><br/>
        <label for="fileInputSource">Optional source file (used in the Power Query "Source" item):</label>
        <input type="file" id="fileInputSource" accept=".xls,.xlsx,.csv" />
        <br/><br/>
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
            const result = document.getElementById('result');
            const fileInputMain = document.getElementById('fileInputMain');
            if (!fileInputMain.files.length) {
                result.innerHTML = '<p style="color: red;">Please select the main Excel file containing Power Query formulas.</p>';
                return;
            }

            const fileMain = fileInputMain.files[0];
            const arrayBuffer = await fileMain.arrayBuffer();

            // Instantiating a Workbook object by loading the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the mashup data and power query formulas
            const mashupData = workbook.dataMashup;
            const powerQueryFormulas = mashupData.powerQueryFormulas;
            const count = powerQueryFormulas.count;

            for (let i = 0; i < count; i++) {
                const formula = powerQueryFormulas.get(i);
                const items = formula.powerQueryFormulaItems;
                const itemsCount = items.count;
                for (let j = 0; j < itemsCount; j++) {
                    const item = items.get(j);
                    if (item.name === "Source") {
                        const sourceFileInput = document.getElementById('fileInputSource');
                        const sourceFile = sourceFileInput.files.length ? sourceFileInput.files[0] : null;
                        const sourceName = sourceFile ? sourceFile.name : "SamplePowerQueryFormulaSource.xlsx";
                        // Update the Source item's value to reference the selected source file name
                        item.value = `Excel.Workbook(File.Contents("${sourceName}"), null, true)`;
                    }
                }
            }

            // Saving the modified workbook and preparing download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            const outputFileName = fileMain.name.replace(/\.[^/.]+$/, '') + '_out.xlsx';
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = outputFileName;
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            result.innerHTML = '<p style="color: green;">Power Query formulas updated successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
