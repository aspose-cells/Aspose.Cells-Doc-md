---
title: حذف جدول الدوران من ورقة العمل
type: docs
weight: 60
url: /ar/javascript-cpp/delete-pivot-table-from-a-worksheet/
description: استخدام رمز Aspose.Cells for Javaنص برمجي عبر C++ لإزالة الجدول المحوري من أوراق العمل Excel
keywords: Aspose.Cells for Javaنص برمجي عبر C++ إكسل، مكتبة جافا سكريبت إكسل، إزالة الجدول المحوري من ورقة العمل، حذف الجدول المحوري من إكسل، كيفية حذف الجدول المحوري باستخدام Aspose.Cells for Javaنص برمجي عبر C++، حذف الجدول المحوري، حذف الجدول المحوري من إكسل، حذف الجدول المحوري، Aspose.Cells for Javaنص برمجي عبر C++ يزيل الجدول المحوري، إزالته، حذفه، كيفية حذفه
---

{{% alert color="primary" %}}

يوفر Aspose.Cells for Javaنص برمجي عبر C++ ميزة حذف أو إزالة الجدول المحوري من ورقة العمل. يمكنك حذف الجدول المحوري باستخدام كائن الجدول المحوري أو موضعه. يرجى استخدام دالة [**Worksheet.pivotTables.remove(pivotTable)**](https://reference.aspose.com/cells/javascript-cpp/pivottablecollection/#remove-pivottable-) لحذف الجدول المحوري باستخدام كائن الجدول المحوري ودالة [**Worksheet.pivotTables.removeAt(index, keepData)**](https://reference.aspose.com/cells/javascript-cpp/pivottablecollection/#removeAt-number-boolean-) لحذف كائن الجدول المحوري باستخدام موقعه داخل مجموعة الجداول المحورية.

{{% /alert %}}

## **كيفية حذف جدول محوري من ورقة عمل باستخدام Aspose.Cells for JavaScript عبر C++**

تحتوي رمز العينة التالي على حذف جدولين للدوران من ورقة العمل. أولاً يقوم بإزالة جدول الدوران باستخدام الطريقة [**Worksheet.pivotTables.remove(pivotTable)**](https://reference.aspose.com/cells/javascript-cpp/pivottablecollection/#remove-pivottable-) ثم يزيل جدول الدوران باستخدام الطريقة [**Worksheet.pivotTables.removeAt(index, keepData)**](https://reference.aspose.com/cells/javascript-cpp/pivottablecollection/#removeAt-number-boolean-)

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Remove Pivot Table</title>
    </head>
    <body>
        <h1>Remove Pivot Table Example</h1>
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
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();
            // Instantiate Workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access the first pivot table object
            const pivotTable = worksheet.pivotTables.get(0);

            // Remove pivot table using pivot table object
            worksheet.pivotTables.remove(pivotTable);
            // OR remove by index:
            // worksheet.pivotTables.removeAt(0);

            // Saving the modified workbook
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Pivot table removed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
