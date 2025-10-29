---
title: تصفية مشروع VBA عند تحميل دفتر عمل باستخدام JavaScript عبر C++
linktitle: تصفية مشروع VBA أثناء تحميل جدول عمل
type: docs
weight: 140
url: /ar/javascript-cpp/filter-vba-project-while-loading-a-workbook/
description: تعلم كيفية تصفية مشاريع VBA أثناء تحميل أوراق عمل إكسل باستخدام Aspose.Cells for JavaScript عبر C++.
---

## **تصفية مشروع VBA أثناء تحميل دفتر إكسل في جافا سكريبت عبر C++**

بعض ملفات .xlsm/.xslb تحتوي على كمية هائلة من الماكرو (أو الماكرو طويل جدًا جدًا). Aspose.Cells for JavaScript عبر C++ سيقوم بتحميل هذه البيانات (البيانات الوصفية) بشكل غير مشروط عند فتح مثل هذه الكتب. قد تحتاج إلى التحكم في ذلك من خلال [**LoadDataFilterOptions**](https://reference.aspose.com/cells/javascript-cpp/loaddatafilteroptions) عندما تحتاج فقط إلى استخراج أسماء الأوراق لعدد كبير من الكتب، وذلك لتخطي المحتوى غير الضروري. يتم توفير هذا التصفية من خلال إدخال خيار جديد، [**LoadDataFilterOptions.VBA**](https://reference.aspose.com/cells/javascript-cpp/loaddatafilteroptions).

## **الكود المثالي**

يحمل الرمز العيني التالي عملاق العمل حتى يتم تصفية VBA فقط. يمكن تنزيل ملف عينة لاختبار هذه الميزة من الرابط التالي:

[sampleMacroEnabledWorkbook.xlsm](79527938.xlsm)

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Sample Macro-Enabled Workbook to XLSM</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.xlsm,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, LoadOptions, LoadFormat, LoadFilter, LoadDataFilterOptions } = AsposeCells;

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
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel macro-enabled (.xlsm) file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Set the load options, we do not want to load VBA
            const loadOptions = new LoadOptions(LoadFormat.Auto);
            const loadFilter = new LoadFilter(LoadDataFilterOptions.All & ~LoadDataFilterOptions.VBA);
            loadOptions.loadFilter = loadFilter;

            // Create workbook object from uploaded file using load options
            const book = new Workbook(new Uint8Array(arrayBuffer), loadOptions);

            // Save the output in xlsm format
            const outputData = book.save(SaveFormat.Xlsm);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'OutputSampleMacroEnabledWorkbook.xlsm';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download OutputSampleMacroEnabledWorkbook.xlsm';

            document.getElementById('result').innerHTML = '<p style="color: green;">Processing completed. Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
