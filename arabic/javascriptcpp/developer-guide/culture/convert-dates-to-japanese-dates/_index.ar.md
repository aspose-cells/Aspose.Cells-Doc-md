---
title: تحويل التواريخ إلى تواريخ يابانية باستخدام JavaScript عبر C++
linktitle: تحويل التواريخ إلى تواريخ يابانية
type: docs
weight: 350
url: /ar/javascript-cpp/convert-dates-to-japanese-dates/
description: تعلم كيفية تحويل التواريخ الميلادية إلى التواريخ اليابانية باستخدام Aspose.Cells for JavaScript عبر C++.
---  

{{% alert color="primary" %}}  

في التقويم الياباني، تبدأ حقبة جديدة مع تولي إمبراطور جديد. في 1 مايو 2019، تولى إمبراطور جديد السلطة حيث انتهت حقبة هيسي وبدأت حقبة ريوا.  

{{% /alert %}}  

توفر Aspose.Cells وسيلة لتحويل تواريخ الميلادي إلى تواريخ يابانية. أثناء هذا التحويل، يتم أيضًا أخذ تغييرات العهد في الاعتبار. يُحوّل مقتطف الكود التالي ملف [Excel المصدر](90112015.xlsx) الذي يحتوي على تواريخ ميلادية إلى ملف [PDF الناتج](90112016.pdf) بتواريخ يابانية كما هو موضح في الصورة أدناه.  

![todo:image_alt_text](convert-dates-to-japanese-dates_1.jpg)  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Convert Excel with Japanese Dates to PDF</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, LoadOptions, LoadFormat, CountryCode } = AsposeCells;

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

            // Create LoadOptions for XLSX and set language/region to Japan
            const options = new LoadOptions(LoadFormat.Xlsx);
            options.languageCode = CountryCode.Japan;
            options.region = CountryCode.Japan;

            // Instantiate workbook from uploaded file with load options
            const workbook = new Workbook(new Uint8Array(arrayBuffer), options);

            // Save workbook to PDF format
            const outputData = workbook.save(SaveFormat.Pdf);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'JapaneseDates.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">PDF created successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```
