---
title: تحليل السجلات المخزنة في حقول Pivot أثناء تحميل ملف Excel
type: docs
weight: 70
url: /ar/javascript-cpp/parsing-pivot-cached-records-while-loading-excel-file/
---

## **سيناريوهات الاستخدام المحتملة**

عند إنشاء جدول محوري، تقوم Microsoft Excel بنسخ البيانات المصدرية وتخزينها في ذاكرة التخزين المؤقت. تكون ذاكرة التخزين المؤقت موجودة داخل ذاكرة Microsoft Excel. لا يمكنك رؤيتها ولكن هذه هي البيانات التي يشير إليها الجدول المحوري عند بناء الجدول المحوري أو تغيير اختيار Slicer أو تحريك الصفوف/الأعمدة. يمكن لذلك Microsoft Excel أن يكون متجاوبًا جدًا مع التغييرات في الجدول المحوري ولكن يمكنه أيضًا مضاعفة حجم ملفك. بعد كل شيء، ذاكرة التخزين المؤقت مجرد نسخة مكررة من بياناتك المصدرية لذا يبدو منطقيًا أن يكون حجم ملفك مضاعف بشكل محتمل.

عند تحميل ملف Excel الخاص بك داخل كائن Workbook، يمكنك تحديد ما إذا كنت تريد أيضًا تحميل سجلات ذاكرة النقاط أو لا، باستخدام خاصية [**LoadOptions.parsingPivotCachedRecords**](https://reference.aspose.com/cells/javascript-cpp/loadoptions/#parsingPivotCachedRecords-boolean-). القيمة الافتراضية لهذه الخاصية هي **خطأ**. إذا كانت ذاكرة النقاط كبيرة جدًا، يمكن أن يزيد من الأداء. ولكن إذا كنت تريد أيضًا تحميل سجلات ذاكرة النقاط، يجب أن تضبط هذه الخاصية على **صحيح**.

## **تحليل السجلات المخزنة في حقول Pivot أثناء تحميل ملف Excel**

الرمز النموذجي التالي يشرح استخدام خاصية [**LoadOptions.parsingPivotCachedRecords**](https://reference.aspose.com/cells/javascript-cpp/loadoptions/#parsingPivotCachedRecords-boolean-). يقوم بتحميل ملف Excel النموذجي [مثال](61767773.xlsx) أثناء تحليل سجلات ذاكرة القطعة. ثم يقوم بتحديث جدول المحوري ويحفظه كـ [ملف Excel الناتج](61767774.xlsx).

## **الكود المثالي**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Parsing Pivot Cached Records While Loading Example</title>
    </head>
    <body>
        <h1>Parsing Pivot Cached Records While Loading Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, LoadOptions } = AsposeCells;

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
            const downloadLink = document.getElementById('downloadLink');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Create load options
            const options = new LoadOptions();
            // Set ParsingPivotCachedRecords true, default value is false
            options.parsingPivotCachedRecords = true;

            // Load the Excel file with load options
            const wb = new Workbook(new Uint8Array(arrayBuffer), options);

            // Access first worksheet
            const ws = wb.worksheets.get(0);

            // Access first pivot table
            const pt = ws.pivotTables.get(0);

            // Set refresh data flag true
            pt.refreshDataFlag = true;

            // Refresh and calculate pivot table
            pt.refreshData();
            pt.calculateData();

            // Set refresh data flag false
            pt.refreshDataFlag = false;

            // Save the output Excel file
            const outputData = wb.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputParsingPivotCachedRecordsWhileLoadingExcelFile.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
