---
title: تقليم الصفوف والأعمدة الفارغة في البداية أثناء تصدير جداول البيانات إلى تنسيق CSV باستخدام جافا سكريبت عبر C++
linktitle: تقليم الصفوف والأعمدة الفارغة الرائدة أثناء تصدير الجداول الجدولية إلى تنسيق CSV
type: docs
weight: 100
url: /ar/javascript-cpp/trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format/
description: تعلم كيفية تقليم الصفوف والأعمدة الفارغة في البداية عند تصدير جداول البيانات إلى تنسيق CSV باستخدام Aspose.Cells for JavaScript عبر C++.
---

## **سيناريوهات الاستخدام المحتملة**

في بعض الأحيان، يحتوي ملف Excel أو CSV الخاص بك على أعمدة أو صفوف فارغة رئيسية. على سبيل المثال، تأمل هذا السطر

{{< highlight javascript >}}

 ,,,data1,data2

{{< /highlight >}}

هنا تكون الأعمدة الثلاثة الأولى فارغة. عند فتح مثل هذا الملف CSV في Microsoft Excel، فإن Microsoft Excel يتجاهل هذه الأعمدة الرئيسية والصفوف.

 بشكل افتراضي، Aspose.Cells for JavaScript عبر C++ لا يتجاهل الأعمدة والصفوف الفارغة في البداية عند الحفظ ولكن إذا رغبت في إزالتها تمامًا كما يفعل Microsoft Excel، يوفر Aspose.Cells خاصية [**TxtSaveOptions.trimLeadingBlankRowAndColumn**](https://reference.aspose.com/cells/javascript-cpp/txtsaveoptions/#trimLeadingBlankRowAndColumn--). يرجى تعيينها إلى **true** وسيتم تجاهل جميع الصفوف والأعمدة الفارغة في البداية عند الحفظ.

{{% alert color="primary" %}}

 قبل إصدار Aspose.Cells for JavaScript عبر C++ 20.4، كانت القيمة الافتراضية لـ [**TxtSaveOptions.trimLeadingBlankRowAndColumn**](https://reference.aspose.com/cells/javascript-cpp/txtsaveoptions/#trimLeadingBlankRowAndColumn--) هي **false**. منذ إصدار 20.4، القيمة الافتراضية لـ [**TxtSaveOptions.trimLeadingBlankRowAndColumn**](https://reference.aspose.com/cells/javascript-cpp/txtsaveoptions/#trimLeadingBlankRowAndColumn--) هي **true.**

{{% /alert %}}

## **تقليص الصفوف والأعمدة الخالية أثناء تصدير جداول البيانات إلى تنسيق CSV**

يحمّل الرمز النموذجي التالي ملف Excel [المصدر](sampleTrimBlankColumns.xlsx) الذي يحتوي على عمودين فارغين في البداية. يحفظ الملف بصيغة CSV بدون تغييرات ثم يضبط خاصية [**TxtSaveOptions.trimLeadingBlankRowAndColumn**](https://reference.aspose.com/cells/javascript-cpp/txtsaveoptions/#trimLeadingBlankRowAndColumn--) على **true** ويحفظه مرة أخرى. تظهر الصورة ملف Excel المصدر، وملف CSV الناتج بدون القص، وملف CSV الناتج مع القص.

![todo:image_alt_text](trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format_1.png)

## **الكود المثالي**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Trim Blank Columns</title>
    </head>
    <body>
        <h1>Trim Blank Columns Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink1" style="display: none;">Download Result 1</a>
        <a id="downloadLink2" style="display: none; margin-left: 10px;">Download Result 2</a>
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
            const resultDiv = document.getElementById('result');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Load source workbook
            const wb = new Workbook(new Uint8Array(arrayBuffer));

            // Save in csv format (without trimming)
            const outputData1 = wb.save(SaveFormat.Csv);
            const blob1 = new Blob([outputData1]);
            const downloadLink1 = document.getElementById('downloadLink1');
            downloadLink1.href = URL.createObjectURL(blob1);
            downloadLink1.download = 'outputWithoutTrimBlankColumns.csv';
            downloadLink1.style.display = 'inline-block';
            downloadLink1.textContent = 'Download CSV Without Trimming';

            // Now save again with TrimLeadingBlankRowAndColumn as true
            const opts = new TxtSaveOptions();
            opts.trimLeadingBlankRowAndColumn = true;

            // Save in csv format (with trimming)
            const outputData2 = wb.save(opts);
            const blob2 = new Blob([outputData2]);
            const downloadLink2 = document.getElementById('downloadLink2');
            downloadLink2.href = URL.createObjectURL(blob2);
            downloadLink2.download = 'outputTrimBlankColumns.csv';
            downloadLink2.style.display = 'inline-block';
            downloadLink2.textContent = 'Download CSV With Trimmed Blank Columns';

            resultDiv.innerHTML = '<p style="color: green;">Files generated. Use the links above to download the CSVs.</p>';
        });
    </script>
</html>
```
