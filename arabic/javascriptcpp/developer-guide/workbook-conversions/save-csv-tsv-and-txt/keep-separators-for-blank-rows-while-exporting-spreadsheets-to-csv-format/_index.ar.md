---
title: الاحتفاظ بالفواصل للصفوف الفارغة أثناء تصدير جداول البيانات إلى تنسيق CSV باستخدام جافا سكريبت عبر C++
linktitle: الاحتفاظ بالفواصل للصفوف الفارغة أثناء تصدير أوراق الجدول إلى تنسيق CSV
type: docs
weight: 160
url: /ar/javascript-cpp/keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format/
---

## **الاحتفاظ بالفواصل للصفوف الفارغة أثناء تصدير جداول البيانات إلى تنسيق CSV**  

تقدم Aspose.Cells القدرة على الاحتفاظ بفواصل الأسطر أثناء تحويل جداول البيانات إلى تنسيق CSV. لاستخدام ذلك، يمكنك استخدام خاصية [**TxtSaveOptions.keepSeparatorsForBlankRow**](https://reference.aspose.com/cells/javascript-cpp/txtsaveoptions/#keepSeparatorsForBlankRow--) من [**TxtSaveOptions**](https://reference.aspose.com/cells/javascript-cpp/txtsaveoptions/). [**TxtSaveOptions.keepSeparatorsForBlankRow**](https://reference.aspose.com/cells/javascript-cpp/txtsaveoptions/#keepSeparatorsForBlankRow--) هي خاصية منطقية. للحفاظ على المفاصل للفواصل الفارغة أثناء تحويل ملف Excel إلى CSV، قم بضبط الخاصية [**TxtSaveOptions.keepSeparatorsForBlankRow**](https://reference.aspose.com/cells/javascript-cpp/txtsaveoptions/#keepSeparatorsForBlankRow--) على **true**.  

يعرض الرمز النموذجي التالي تحميل ملف Excel [المصدر](84378743.xlsx). حيث يضبط الخاصية [**TxtSaveOptions.keepSeparatorsForBlankRow**](https://reference.aspose.com/cells/javascript-cpp/txtsaveoptions/#keepSeparatorsForBlankRow--) على **true** ويحفظه كـ [ملف CSV الناتج](84378744.csv). تظهر الصورة المجمعة المقارنة بين ملف Excel المصدر، والناتج الافتراضي عند تحويل ورقة العمل إلى CSV، والناتج الناتج عن ضبط [**TxtSaveOptions.keepSeparatorsForBlankRow**](https://reference.aspose.com/cells/javascript-cpp/txtsaveoptions/#keepSeparatorsForBlankRow--) على **true**.  

![todo:image_alt_text](keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format_1.jpg)  

## **الكود المثالي**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells TxtSaveOptions Example</title>
    </head>
    <body>
        <h1>TxtSaveOptions to CSV Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Convert to CSV</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, TxtSaveOptions, Utils } = AsposeCells;

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

            // Create a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Instantiate TxtSaveOptions
            const options = new TxtSaveOptions();

            // Set KeepSeparatorsForBlankRow to true to show separators in blank rows
            options.keepSeparatorsForBlankRow = true;

            // Save the workbook to CSV using the options
            const outputData = workbook.save(SaveFormat.CSV, options);

            const blob = new Blob([outputData], { type: 'text/csv' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.csv';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download CSV File';

            document.getElementById('result').innerHTML = '<p style="color: green;">File converted successfully! Click the download link to get the CSV file.</p>';
        });
    </script>
</html>
```
