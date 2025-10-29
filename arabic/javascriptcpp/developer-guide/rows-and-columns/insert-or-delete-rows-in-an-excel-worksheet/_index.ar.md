---
title: إدراج أو حذف الصفوف في ورقة إكسل باستخدام جافاسكرابت عبر C++
linktitle: إدراج أو حذف الصفوف في ورقة عمل Excel
type: docs
weight: 20
url: /ar/javascript-cpp/insert-or-delete-rows-in-an-excel-worksheet/
description: يزود هذا المقال بكود جافاسكرابت باستخدام C++ لإضافة وحذف الصفوف في ورقة عمل إكسل. 
keywords: جافاسكرابت لإدراج أو حذف الصفوف في ورقة إكسل، جافاسكرابت لإضافة أو حذف الصفوف في إكسل، جافاسكرابت لإدراج الصفوف في إكسل، جافاسكرابت لحذف الصفوف في إكسل، إدراج أو حذف الصفوف في ورقة إكسل باستخدام جافاسكرابت، إدراج أو حذف الصفوف في إكسل باستخدام جافاسكرابت، إدراج الصفوف في إكسل باستخدام جافاسكرابت، حذف الصفوف في إكسل باستخدام جافاسكرابت
---

{{% alert color="primary" %}}  

عند إنشاء ورقة عمل جديدة أو العمل مع ورقة موجودة، قد تحتاج إلى إضافة صفوف أو أعمدة إضافية لاستيعاب البيانات. وفي أوقات أخرى، قد تحتاج إلى حذف صفوف أو أعمدة من مواقع محددة في ورقة العمل.  

{{% /alert %}}  

يوفر Aspose.Cells for JavaScript عبر C++ طريقتين لإضافة وحذف الصفوف: [**Cells.insertRows(number, number, boolean)**](https://reference.aspose.com/cells/javascript-cpp/cells/#insertRows-number-number-boolean-) و [**Cells.deleteRows(number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#deleteRows-number-number-). تم تحسين هذه الطرق للأداء وتقوم بالمهمة بسرعة كبيرة.  

لإدراج أو إزالة عدد من الصفوف ، نوصي دائمًا باستخدام طرق [**Cells.insertRows(number, number, boolean)**](https://reference.aspose.com/cells/javascript-cpp/cells/#insertRows-number-number-boolean-) و [**Cells.deleteRows(number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#deleteRows-number-number-) بدلاً من استخدام طرق [**Cells.insertRow(number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#insertRow-number-) أو [**Cells.deleteRow(number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#deleteRow-number-) في حلقة.  

تعمل Aspose.Cells بنفس الطريقة التي يعمل بها برنامج Microsoft Excel. عند إضافة صفوف أو أعمدة، يتم نقل محتوى ورقة العمل لأسفل ولليمين. وعند إزالة صفوف أو أعمدة، يتم نقل محتوى ورقة العمل لأعلى أو لليسار. يتم تحديث أي مراجع في ورقات العمل والخلايا الأخرى عند إضافة أو إزالة الصفوف.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Insert and Delete Rows</title>
    </head>
    <body>
        <h1>Insert and Delete Rows Example</h1>
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

            // Instantiate a Workbook object and load the selected file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get the first worksheet in the book
            const sheet = workbook.worksheets.get(0);

            // Insert 10 rows at row index 2 (insertion starts at 3rd row)
            sheet.cells.insertRows(2, 10);

            // Delete 5 rows now. (8th row - 12th row)
            sheet.cells.deleteRows(7, 5);

            // Save the excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out_book1.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Rows modified successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
