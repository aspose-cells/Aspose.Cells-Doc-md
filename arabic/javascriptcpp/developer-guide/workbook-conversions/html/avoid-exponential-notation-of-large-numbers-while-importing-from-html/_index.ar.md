---
title: تجنب العلامة العلمية للأرقام الكبيرة أثناء الاستيراد من HTML
linktitle: تجنب العلامة العلمية للأرقام الكبيرة أثناء الاستيراد من HTML
type: docs
weight: 10
url: /ar/javascript-cpp/avoid-exponential-notation-of-large-numbers-while-importing-from/
description: تعرف على كيفية منع تحويل الأرقام الكبيرة إلى صيغة الأس عندما تستورد من HTML باستخدام Aspose.Cells for JavaScript عبر C++.
--- 

{{% alert color="primary" %}}  

في بعض الأحيان، يحتوي HTML الخاص بك على أرقام مثل 1234567890123456، وهي أطول من 15 رقمًا، وعند استيراد HTML إلى ملف Excel، تتحول هذه الأرقام إلى صيغة الأُس مثل 1.23457E+15. إذا كنت تريد استيراد الرقم كما هو وعدم تحويله إلى صيغة الأُس، يرجى استخدام خاصية [**HtmlLoadOptions.keepPrecision**](https://reference.aspose.com/cells/javascript-cpp/htmlloadoptions/#keepPrecision--) وتعيينها إلى **true** أثناء تحميل HTML.  

{{% /alert %}}  

يوضح الرمز النموذجي التالي كيفية استخدام خاصية [**HtmlLoadOptions.keepPrecision**](https://reference.aspose.com/cells/javascript-cpp/htmlloadoptions/#keepPrecision--). ستقوم API باستيراد الرقم كما هو دون تحويله إلى صيغة الأُس.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Example Title</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, HtmlLoadOptions, LoadFormat } = AsposeCells;

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
            // Sample Html containing large number with digits greater than 15
            const html = "<html><body><p>1234567890123456</p></body></html>";

            // Convert Html to byte array
            const byteArray = new TextEncoder().encode(html);

            // Set Html load options and keep precision true
            const loadOptions = new HtmlLoadOptions(LoadFormat.Html);
            loadOptions.keepPrecision = true;

            // Convert byte array into stream
            const stream = byteArray;

            // Create workbook from stream with Html load options
            const workbook = new Workbook(stream, loadOptions);

            // Access first worksheet
            const sheet = workbook.worksheets.get(0);

            // Auto fit the sheet columns
            sheet.autoFitColumns();

            // Save the workbook
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputAvoidExponentialNotationWhileImportingFromHtml.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created successfully. Click the download link to download the file.</p>';
        });
    </script>
</html>
```
