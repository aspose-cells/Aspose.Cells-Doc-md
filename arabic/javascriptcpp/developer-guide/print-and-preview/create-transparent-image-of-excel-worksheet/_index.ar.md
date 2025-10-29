---
title: إنشاء صورة شفافة لورقة عمل Excel باستخدام JavaScript عبر C++
linktitle: Create Transparent Image of Excel Worksheet
type: docs
weight: 170
url: /ar/javascript-cpp/create-transparent-image-of-excel-worksheet/
description: تعلم كيفية توليد صورة شفافة لورقة عمل Excel باستخدام Aspose.Cells for JavaScript عبر C++.
---

{{% alert color="primary" %}}

أحيانًا، تحتاج إلى إنشاء صورة لورقة عملك كصورة شفافة. ترغب في تطبيق الشفافية على جميع الخلايا التي ليس لها ألوان تعبئة. توفر Aspose.Cells خاصية الشفافية لتطبيق الشفافية على صورة الورقة العمل. عندما تكون هذه الخاصية كاذبة، فإن الخلايا التي ليس لها ألوان تعبئة تُرسم بلون أبيض وعندما تكون صحيحة، تُرسم الخلايا التي ليس لها ألوان تعبئة كشفافة.

{{% /alert %}}

في صورة ورقة العمل التالية، لم يتم تطبيق الشفافية. الخلايا التي ليس لها ألوان تعبئة تُرسم باللون الأبيض.

|**الإخراج بدون شفافية: خلفية الخلية بيضاء**|
| :- |
|![todo:image_alt_text](create-transparent-image-of-excel-worksheet_1.png)|

بينما، في صورة ورقة العمل التالية، تم تطبيق الشفافية. الخلايا التي ليس لها ألوان تعبئة هي شفافة.

|**الإخراج مع تمكين الشفافية**|
| :- |
|![todo:image_alt_text](create-transparent-image-of-excel-worksheet_2.png)|

الكود العيني التالي يولِّد صورة شفافة من ورقة عمل Excel.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Create Transparent Image Example</title>
    </head>
    <body>
        <h1>Create Transparent Image Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.xlsm,.csv" />
        <button id="runExample">Create Transparent PNG</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, ImageOrPrintOptions, SheetRender, ImageType } = AsposeCells;

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

            // Create workbook object from uploaded file
            const wb = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const sheet = wb.worksheets.get(0);

            // Apply different image or print options
            const imgOption = new ImageOrPrintOptions();
            imgOption.imageType = ImageType.Png;
            imgOption.horizontalResolution = 200;
            imgOption.verticalResolution = 200;
            imgOption.onePagePerSheet = true;

            // Apply transparency to the output image
            imgOption.transparent = true;

            // Create image after applying image or print options
            const sr = new SheetRender(sheet, imgOption);
            const outputData = await sr.toImage(0);

            const blob = new Blob([outputData], { type: 'image/png' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputCreateTransparentImage.png';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PNG Image';

            document.getElementById('result').innerHTML = '<p style="color: green;">Image created successfully! Click the download link to get the PNG file.</p>';
        });
    </script>
</html>
```
