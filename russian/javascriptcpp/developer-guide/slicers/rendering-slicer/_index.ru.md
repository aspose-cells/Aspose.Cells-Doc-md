---
title: Отрисовка слайсера с помощью JavaScript через C++
linktitle: Рендеринг срезки
type: docs
weight: 40
url: /ru/javascript-cpp/rendering-slicer/
---  

## **Возможные сценарии использования**  
Aspose.Cells for JavaScript через C++ поддерживает отображение форм фигур слайсера. Если вы преобразуете ваш лист в изображение или сохраняете книгу в формате PDF или HTML, вы увидите, что слайсеры отображаются правильно.  

## **Рендеринг срезки**  
 Следующий пример кода загружает [пример файла Excel](67338479.xlsx), содержащий существующий сегментатор. Он преобразует лист в изображение, задав область печати, охватывающую только сегментатор. Полученное изображение — это [выходное изображение](67338480.png), показывающее прорисованный сегментатор. Как видно, сегментатор отображается корректно и выглядит так же, как в исходном файле Excel.  

![todo:image_alt_text](rendering-slicer_1)  
## **Образец кода**  
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
