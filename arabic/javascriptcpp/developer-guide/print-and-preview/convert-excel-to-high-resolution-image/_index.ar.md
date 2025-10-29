---
title: تحويل Excel إلى صورة عالية الدقة باستخدام JavaScript عبر C++
linktitle: تحويل إكسل إلى صورة عالية الدقة
type: docs
weight: 100
url: /ar/javascript-cpp/convert-excel-to-high-resolution-image/
description: تعلم كيفية تحويل ملفات Excel إلى صور عالية الدقة باستخدام Aspose.Cells for JavaScript عبر C++.
---

مع الانتشار المتزايد للشاشات عالية الدقة، تظهر الصور الناتجة عند الدقة الافتراضية 96 نقطة في البوصة ضبابية وغير واضحة. لضمان الوضوح على الشاشات عالية الدقة، من المهم إنشاء صور بدقة أعلى. يقدم Aspose.Cells for JavaScript عبر C++ وظيفة لضبط [**ImageOrPrintOptions.horizontalResolution**](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions/#horizontalResolution--) و[**ImageOrPrintOptions.verticalResolution**](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions/#verticalResolution--)، مما يسمح لك بإنشاء صور عالية الجودة من ملفات Excel التي تظهر حادة على شاشات عالية الدقة.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Sheet to Image</title>
    </head>
    <body>
        <h1>Convert Worksheet to PNG Image</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Generate Image</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, ImageOrPrintOptions, ImageType, SheetRender, Utils } = AsposeCells;

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

            // Instantiate workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Create ImageOrPrintOptions and set properties
            const options = new ImageOrPrintOptions();
            options.horizontalResolution = 300;
            options.verticalResolution = 300;
            options.imageType = ImageType.Png;

            // Get the first worksheet
            const sheet = workbook.worksheets.get(0);

            // Create SheetRender instance
            const render = new SheetRender(sheet, options);

            // Generate image for the first page/index (0)
            const imageData = render.toImage(0);

            // Create blob and provide download link
            const blob = new Blob([imageData], { type: 'image/png' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.png';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PNG Image';

            document.getElementById('result').innerHTML = '<p style="color: green;">Image generated successfully! Click the download link to get the image.</p>';
        });
    </script>
</html>
```
