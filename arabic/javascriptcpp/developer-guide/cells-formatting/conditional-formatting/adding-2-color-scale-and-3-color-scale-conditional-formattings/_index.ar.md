---
title: إضافة التدرج اللوني ثنائي اللون والثلاثي اللون وتنسيقهما الشرطي 
linktitle: إضافة التدرج اللوني ثنائي اللون والثلاثي اللون وتنسيقهما الشرطي  
description: كيفية استخدام مكتبة Aspose.Cells في جافا سكريبت عبر C++ لإضافة تنسيق شرطي لنسب لونين وثلاثة ألوان. من خلال تعديل هذه المعايير، تتحكم بشكل أكبر في مظهر الخلايا.  
keywords: Aspose.Cells، التنسيق الشرطي، جافا سكريبت عبر C++، نسبة اللون، مقياس لونين، مقياس ثلاثة ألوان  
type: docs  
weight: 20  
url: /ar/javascript-cpp/adding-2-color-scale-and-3-color-scale-conditional-formattings/  
---

{{% alert color="primary" %}}  
يتم إضافة التنسيقات الشرطية لمقياس لوني بمعدين لونين ومقياس ثلاثي الألوان بنفس الطريقة، لكن تختلف بواسطة طريقة [**ColorScale.is3ColorScale(boolean)**](https://reference.aspose.com/cells/javascript-cpp/colorscale/#is3ColorScale-boolean-). تكون هذه الطريقة **false** لمقياس الألوان بمعدين لونين و**true** لمقياس الألوان ثلاثي الألوان.  
{{% /alert %}}  

يقوم الكود العيني التالي بإضافة الدوال المشروطة بمقياسي اللون والدالة المشروطة بمقياس اللون الثلاثي. يولد [ملف الإكسيل الناتج](5115058.xlsx).  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Conditional Formatting Example</h1>
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

            if (!fileInput.files.length) {
                // No file selected - we'll create a new workbook
            }

            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Add some data in cells
            worksheet.cells.get("A1").value = "2-Color Scale";
            worksheet.cells.get("D1").value = "3-Color Scale";

            for (let i = 2; i <= 15; i++) {
                worksheet.cells.get("A" + i).value = i;
                worksheet.cells.get("D" + i).value = i;
            }

            // Adding 2-Color Scale Conditional Formatting
            let ca = AsposeCells.CellArea.createCellArea("A2", "A15");

            let idx = worksheet.conditionalFormattings.add();
            let fcc = worksheet.conditionalFormattings.get(idx);
            fcc.addCondition(AsposeCells.FormatConditionType.ColorScale);
            fcc.addArea(ca);

            let fc = worksheet.conditionalFormattings.get(idx).get(0);
            fc.colorScale.is3ColorScale = false;
            fc.colorScale.maxColor = AsposeCells.Color.LightBlue;
            fc.colorScale.minColor = AsposeCells.Color.LightGreen;

            // Adding 3-Color Scale Conditional Formatting
            ca = AsposeCells.CellArea.createCellArea("D2", "D15");

            idx = worksheet.conditionalFormattings.add();
            fcc = worksheet.conditionalFormattings.get(idx);
            fcc.addCondition(AsposeCells.FormatConditionType.ColorScale);
            fcc.addArea(ca);

            fc = worksheet.conditionalFormattings.get(idx).get(0);
            fc.colorScale.is3ColorScale = true;
            fc.colorScale.maxColor = AsposeCells.Color.LightBlue;
            fc.colorScale.midColor = AsposeCells.Color.Yellow;
            fc.colorScale.minColor = AsposeCells.Color.LightGreen;

            // Save the workbook
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook processed successfully. Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
