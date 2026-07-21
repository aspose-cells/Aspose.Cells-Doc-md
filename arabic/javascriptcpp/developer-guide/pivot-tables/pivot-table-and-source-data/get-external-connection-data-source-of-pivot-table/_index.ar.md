---
title: الحصول على مصدر بيانات الاتصال الخارجي لجدول الدوران
type: docs
weight: 150
url: /ar/javascript-cpp/get-external-connection-data-source-of-pivot-table/
description: كيفية الحصول على مصدر البيانات الخارجي لجدول محوري باستخدام Aspose.Cells for JavaScript عبر C++.
keywords: Aspose.Cells for JavaScript مكتبة Excel، JavaScript لـ Excel، للحصول على مصدر البيانات الخارجي لجدول محوري باستخدام Aspose.Cells for JavaScript عبر مكتبة Excel لـ C++.
---

## **كيفية الحصول على مصدر بيانات الاتصال الخارجي لجدول محوري**

يوفر Aspose.Cells for JavaScript عبر C++ القدرة على الحصول على مصدر البيانات الخارجي للجدول المحوري. لهذه الغاية، يوفر API الخاص خاصية [**externalConnectionDataSource**](https://reference.aspose.com/cells/javascript-cpp/pivottable/#externalConnectionDataSource--) من فئة [**PivotTable**](https://reference.aspose.com/cells/javascript-cpp/pivottable/). ترجع الخاصية [**externalConnectionDataSource**](https://reference.aspose.com/cells/javascript-cpp/pivottable/#externalConnectionDataSource--) كائن [**ExternalConnection**](https://reference.aspose.com/cells/javascript-cpp/externalconnection/). توضح قطعة الكود التالية كيفية استخدام الخاصية [**externalConnectionDataSource**](https://reference.aspose.com/cells/javascript-cpp/pivottable/#externalConnectionDataSource--) للحصول على مصدر البيانات الخارجي للجدول المحوري.

## **الكود المثالي**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Pivot Table External Connection Example</title>
    </head>
    <body>
        <h1>Pivot Table External Connection Example</h1>
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

            // Instantiating a Workbook object by opening the selected Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Get the pivot table
            const pivotTable = worksheet.pivotTables.get(0);

            // Get external connection data source
            const externalConnection = pivotTable.externalConnectionDataSource;

            const name = externalConnection.name;
            const type = externalConnection.type;

            console.log("External Connection Data Source");
            console.log("Name: " + name);
            console.log("Type: " + type);

            resultDiv.innerHTML = `<p style="color: green;">External Connection Data Source</p>
                                   <p>Name: ${name}</p>
                                   <p>Type: ${type}</p>`;
        });
    </script>
</html>
```

الملف المصدر المستخدم في مقتطف الشفرة مرفق للرجوع إليه.

[ملف المصدر](104398862.xlsx)
