---
title: Excel Çalışma Sayfasının Saydam Görüntüsünü JavaScript kullanarak C++ üzerinden oluşturma
linktitle: Create Transparent Image of Excel Worksheet
type: docs
weight: 170
url: /tr/javascript-cpp/create-transparent-image-of-excel-worksheet/
description: Aspose.Cells for JavaScript kullanarak C++ üzerinden Excel çalışma sayfasının saydam görüntüsünü nasıl oluşturacağınızı öğrenin.
---

{{% alert color="primary" %}}

Bazen çalışma sayfanızın görüntüsünü şeffaf bir görüntü olarak oluşturmanız gerekebilir. Dolgu renkleri olmayan tüm hücrelere şeffaflık uygulamak istersiniz. Aspose.Cells, çalışma sayfasına şeffaflık uygulamak için [**ImageOrPrintOptions.transparent**](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions/#transparent--) özelliğini sağlar. Bu özellik **false** olduğunda, dolgu renkleri olmayan hücreler beyaz renkle çizilir ve **true** olduğunda, dolgu renkleri olmayan hücreler şeffaf şekilde çizilir.

{{% /alert %}}

Aşağıdaki çalışma sayfası görüntüsünde şeffaflık uygulanmamıştır. Dolgu rengi olmayan hücreler beyaz olarak çizilmiştir.

|**Şeffaflık olmadan çıktı: hücre arka planı beyazdır**|
| :- |
|![todo:image_alt_text](create-transparent-image-of-excel-worksheet_1.png)|

Ancak aşağıdaki çalışma sayfası görüntüsünde şeffaflık uygulanmıştır. Dolgu rengi olmayan hücreler şeffaf olarak çizilmiştir.

|**Şeffaflık etkinleştirilmiş çıktı**|
| :- |
|![todo:image_alt_text](create-transparent-image-of-excel-worksheet_2.png)|

Aşağıdaki örnek kod, bir Excel çalışma sayfasından şeffaf bir görüntü oluşturur.

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
