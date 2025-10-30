---
title: JavaScript ile C++ üzerinden Dilimleyici Gösterimi
linktitle: Süzgeci Rendering Etme
type: docs
weight: 40
url: /tr/javascript-cpp/rendering-slicer/
---  

## **Olası Kullanım Senaryoları**  
Aspose.Cells for JavaScript C++ ile dilimleyici şekillerinin gösterimini destekler. Eğer çalışma sayfanızı bir görüntüye dönüştürür veya kitabınızı PDF veya HTML formatlarına kaydederseniz, dilimleyicilerin düzgün şekilde gösterildiğini göreceksiniz.  

## **Dilimleyiciyi Oluşturma**  
 Aşağıdaki örnek kod, var olan bir dilimleyici içeren [örnek Excel dosyasını](67338479.xlsx) yükler. Çalışma sayfasını, yalnızca dilimleyiciyi kapsayan sayfa alanını ayarlayarak bir görüntüye dönüştürür. Oluşan görüntü, [çıktı görüntüsü](67338480.png) olarak gösterilen render edilmiş dilimleyiciyi içerir. Görüntüde, dilimleyicinin düzgün şekilde render edildiği ve örnek Excel dosyasındaki gibi göründüğü görülebilir.  

![todo:image_alt_text](rendering-slicer_1)  
## **Örnek Kod**  
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Render Slicer to Image</title>
    </head>
    <body>
        <h1>Render Slicer to Image</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
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

            // Instantiating a Workbook object from uploaded file
            const wb = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet.
            const ws = wb.worksheets.get(0);

            // Set the print area because we want to render slicer only.
            ws.pageSetup.printArea = "B15:E25";

            // Specify image or print options, set one page per sheet and only area to true.
            const imgOpts = new ImageOrPrintOptions();
            imgOpts.horizontalResolution = 200;
            imgOpts.verticalResolution = 200;
            imgOpts.imageType = ImageType.Png;
            imgOpts.onePagePerSheet = true;
            imgOpts.onlyArea = true;

            // Create sheet render object and render worksheet to image.
            const sr = new SheetRender(ws, imgOpts);

            // Render to image (first page/index 0) and prepare download link
            const imageData = sr.toImage(0);
            const blob = new Blob([imageData], { type: 'image/png' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputRenderingSlicer.png';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Rendered Image';

            document.getElementById('result').innerHTML = '<p style="color: green;">Rendering completed successfully! Click the download link to get the image.</p>';
        });
    </script>
</html>
```
