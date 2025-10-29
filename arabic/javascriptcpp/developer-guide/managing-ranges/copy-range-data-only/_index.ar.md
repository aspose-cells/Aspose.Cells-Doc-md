---
title: نسخ بيانات النطاق فقط باستخدام JavaScript عبر C++
linktitle: نسخ بيانات النطاق فقط
type: docs
weight: 600
url: /ar/javascript-cpp/copy-range-data-only/
description: تعلم كيف تنسخ البيانات من نطاق خلايا إلى آخر باستخدام Aspose.Cells for JavaScript عبر C++.
---

{{% alert color="primary" %}}  
في بعض الأحيان، قد تحتاج إلى نسخ البيانات من نطاق خلايا إلى آخر، نسخ البيانات فقط، دون التنسيق. تقدم Aspose.Cells هذه الميزة.  

تقدم هذه المقالة كود عينة تستخدم Aspose.Cells لنسخ نطاق البيانات.  
{{% /alert %}}  

يوضح هذا المثال كيف:  

1. إنشاء دفتر عمل.  
1. إضافة بيانات إلى الخلايا في ورقة العمل الأولى.  
1. إنشاء [**Range**](https://reference.aspose.com/cells/javascript-cpp/range).  
1. إنشاء [**Style**](https://reference.aspose.com/cells/javascript-cpp/style) object باستخدام سمات التنسيق المحددة.  
1. تطبيق تنسيق النمط على النطاق.  
1. إنشاء نطاق آخر من الخلايا.  
1. نسخ بيانات النطاق الأول إلى هذا النطاق الثاني.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Copy Range Data Example</title>
    </head>
    <body>
        <h1>Copy Range Data Example</h1>
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
            // If a file is provided, open it; otherwise create a new blank workbook
            let workbook;
            if (fileInput.files && fileInput.files.length > 0) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Get the first Worksheet Cells.
            const cells = workbook.worksheets.get(0).cells;

            // Fill some sample data into the cells.
            for (let i = 0; i < 50; i++) {
                for (let j = 0; j < 10; j++) {
                    const cell = cells.get(i, j);
                    cell.value = `${i},${j}`;
                }
            }

            // Create a range (A1:D3).
            const range = cells.createRange("A1", "D3");

            // Create a style object.
            const style = workbook.createStyle();
            // Specify the font attribute.
            style.font.name = "Calibri";
            // Specify the shading color.
            style.foregroundColor = AsposeCells.Color.Yellow;
            style.pattern = AsposeCells.BackgroundType.Solid;
            // Specify the border attributes.
            style.borders.get(AsposeCells.BorderType.TopBorder).lineStyle = AsposeCells.CellBorderType.Thin;
            style.borders.get(AsposeCells.BorderType.TopBorder).color = AsposeCells.Color.Blue;
            style.borders.get(AsposeCells.BorderType.BottomBorder).lineStyle = AsposeCells.CellBorderType.Thin;
            style.borders.get(AsposeCells.BorderType.BottomBorder).color = AsposeCells.Color.Blue;
            style.borders.get(AsposeCells.BorderType.LeftBorder).lineStyle = AsposeCells.CellBorderType.Thin;
            style.borders.get(AsposeCells.BorderType.LeftBorder).color = AsposeCells.Color.Blue;
            style.borders.get(AsposeCells.BorderType.RightBorder).lineStyle = AsposeCells.CellBorderType.Thin;
            style.borders.get(AsposeCells.BorderType.RightBorder).color = AsposeCells.Color.Blue;

            // Create the style flag object.
            const flag1 = new AsposeCells.StyleFlag();
            // Implement font attribute
            flag1.fontName = true;
            // Implement the shading / fill color.
            flag1.cellShading = true;
            // Implement border attributes.
            flag1.borders = true;
            // Set the Range style.
            range.applyStyle(style, flag1);

            // Create a second range (C10:F12).
            const range2 = cells.createRange("C10", "F12");

            // Copy the range data only.
            range2.copyData(range);

            // Save the workbook and provide download link.
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'CopyRangeData.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
