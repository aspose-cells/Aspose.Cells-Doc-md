---
title: وظيفة التوحيد
type: docs
weight: 20
url: /ar/javascript-cpp/consolidation-function/
description: كيفية تطبيق وظيفة التوحيد ConsolidationFunction على حقول البيانات في الجدول المحوري باستخدام Aspose.Cells for JavaScript عبر C++.
keywords: Aspose.Cells for JavaScript عبر C++ إكسل، مكتبة جافا سكريبت إكسل، وظيفة التوحيد ConsolidationFunction على حقول البيانات في الجدول المحوري باستخدام Aspose.Cells for JavaScript عبر مكتبة إكسل C++. 
---

## **وظيفة التوحيد**

يمكن استخدام Aspose.Cells for JavaScript عبر C++ لتطبيق وظيفة التوحيد على حقول البيانات (أو حقول القيمة) في الجدول المحوري. في Microsoft Excel، يمكنك النقر بزر الماوس الأيمن على حقل القيمة ثم اختيار خيار **إعدادات حقل القيمة...** ثم التبديل إلى علامة التبويب **تلخيص القيم بـ**. من هناك، يمكنك اختيار أي وظيفة توحيد من اختيارك مثل المجموع، العد، المتوسط، الحد الأقصى، الحد الأدنى، المنتج، العد الفريد، وغيرها.

يوفر Aspose.Cells for JavaScript عبر C++ تعداد [**ConsolidationFunction**](https://reference.aspose.com/cells/javascript-cpp/consolidationfunction/) لدعم وظائف التوحيد التالية.

- ConsolidationFunction.Average
- ConsolidationFunction.Count
- ConsolidationFunction.CountNums
- ConsolidationFunction.DistinctCount
- ConsolidationFunction.Max
- ConsolidationFunction.Min
- ConsolidationFunction.Product
- ConsolidationFunction.StdDev
- ConsolidationFunction.StdDevp
- ConsolidationFunction.Sum
- ConsolidationFunction.Var
- ConsolidationFunction.Varp

## **كيفية تطبيق وظيفة التوحيد على حقول البيانات في الجدول المحوري باستخدام Aspose.Cells for JavaScript عبر C++**

يطبق الكود التالي وظيفة تجميع **المتوسط** على الحقل الأول من البيانات (أو حقل القيمة) ووظيفة تجميع **عدد فريد** على الحقل الثاني من البيانات (أو حقل القيمة).

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - PivotTable Consolidation Function</title>
    </head>
    <body>
        <h1>Apply Consolidation Function to PivotTable</h1>
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

            // Instantiating a Workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet of the workbook
            const worksheet = workbook.worksheets.get(0);

            // Access the first pivot table of the worksheet
            const pivotTable = worksheet.pivotTables.get(0);

            // Apply Average consolidation function to first data field
            pivotTable.dataFields.get(0).function = AsposeCells.ConsolidationFunction.Average;

            // Apply DistinctCount consolidation function to second data field
            pivotTable.dataFields.get(1).function = AsposeCells.ConsolidationFunction.DistinctCount;

            // Calculate the data to make changes affect
            pivotTable.calculateData();

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">PivotTable consolidation functions applied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

{{% alert color="primary" %}}

وظيفة التوحيد DISTINCT_COUNT مدعومة فقط في Microsoft Excel 2013.

{{% /alert %}}
