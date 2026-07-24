---
title: الحصول على كائن الخلية حسب اسم العرض المتجانس لحقل PivotField من جدول الدوران
type: docs
weight: 70
url: /ar/javascript-cpp/get-the-cell-object-by-displayname-of-pivotfield-of-pivottable/
description: كيفية الحصول على كائن الخلية بواسطة DisplayName لحقل Pivot الخاص بـ PivotTable باستخدام Aspose.Cells for JavaScript عبر C++.
keywords: Aspose.Cells for JavaScript عبر C++ مكتبة Excel، JavaScript لـ Excel، الحصول على الكائن الخلية بواسطة DisplayName لحقل Pivot الخاص بـ PivotTable باستخدام Aspose.Cells for JavaScript عبر مكتبة Excel لـ C++.
---

{{% alert color="primary" %}}

يوفر Aspose.Cells for JavaScript عبر C++ طريقة [**PivotTable.cellByDisplayName(string)**](https://reference.aspose.com/cells/javascript-cpp/pivottable/#cellByDisplayName-string-) التي يمكنك استخدامها للوصول إلى كائن الخلية بواسطة اسم العرض لحقل البيانات. تعتبر هذه الطريقة مفيدة عندما تريد تمييز أو تنسيق رأس الحقل المحوري الخاص بك. يشرح هذا المقال كيفية استرجاع كائن الخلية بواسطة اسم العرض لحقل البيانات ثم تطبيق التنسيق عليه.

{{% /alert %}}

## **كيفية الحصول على كائن الخلية بواسطة اسم العرض لحقل PivotField في جدول البيانات المحوري**

يقوم الكود التالي بالوصول إلى أول جدول مفصلي في ورقة العمل ثم الحصول على الخلية بواسطة اسم العرض لحقل البيانات الثاني في الجدول المفصلي. يغير بعد ذلك لون التعبئة ولون الخط للخلية إلى اللون الأزرق الفاتح والأسود على التوالي. تُظهر اللقطات الشاشية أدناه كيفية ظهور الجدول المفصلي قبل وبعد تنفيذ الكود.

|**جدول مفصلي - قبل**|
| :- |
|![todo:image_alt_text](get-the-cell-object-by-displayname-of-pivotfield-of-pivottable_1.png)|

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Pivot Table Cell Styling Example</h1>
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
            const resultDiv = document.getElementById('result');
            const fileInput = document.getElementById('fileInput');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access first pivot table inside the worksheet
            const pivotTable = worksheet.pivotTables.get(0);

            // Access cell by display name of 2nd data field of the pivot table
            const dataFieldDisplayName = pivotTable.dataFields.get(1).displayName;
            const cell = pivotTable.cellByDisplayName(dataFieldDisplayName);

            // Access cell style and set its fill color and font color
            const style = cell.style;
            style.foregroundColor = AsposeCells.Color.LightBlue;
            style.font.color = AsposeCells.Color.Black;

            // Set the style of the cell
            pivotTable.format(cell.row, cell.column, style);

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

|**جدول مفصلي - بعد**|
| :- |
|![todo:image_alt_text](get-the-cell-object-by-displayname-of-pivotfield-of-pivottable_2.png)|
