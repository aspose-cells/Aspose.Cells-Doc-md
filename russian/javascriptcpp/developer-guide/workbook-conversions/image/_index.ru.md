---
title: Изображение с JavaScript через C++
linktitle: Изображение
type: docs
weight: 300
url: /ru/javascript-cpp/convert-excel-to-image/
---

{{% alert color="primary" %}}  
Aspose.Cells позволяет экспортировать лист из книги Excel и преобразовать его в различные форматы. В этой статье объясняется, как преобразовать лист в различные форматы.  
{{% /alert %}}  

## Преобразование книги в TIFF  

Файл Excel может содержать несколько листов с несколькими страницами. [**WorkbookRender**](https://reference.aspose.com/cells/javascript-cpp/workbookrender) позволяет преобразовать Excel в TIFF с несколькими страницами. Также вы можете управлять несколькими параметрами TIFF, такими как [ImageOrPrintOptions.tiffCompression](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions/#tiffCompression--), [ImageOrPrintOptions.tiffColorDepth](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions/#tiffColorDepth--), Разрешение ([ImageOrPrintOptions.horizontalResolution](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions/#horizontalResolution--), [ImageOrPrintOptions.verticalResolution](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions/#verticalResolution--)).  

В следующем фрагменте кода показано, как конвертировать Excel в TIFF с несколькими страницами. [Исходный файл Excel](workbook-to-tiff-with-mulitiple-pages.xlsx) и [созданное изображение TIFF](workbook-to-tiff-with-mulitiple-pages.tiff) приложены для вашего справки.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Workbook to TIFF (Multiple Pages) Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, ImageOrPrintOptions, ImageType, TiffCompression, WorkbookRender } = AsposeCells;

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
            const wb = new Workbook(new Uint8Array(arrayBuffer));

            // Configure image/print options
            const imgOptions = new ImageOrPrintOptions();
            imgOptions.imageType = ImageType.Tiff;
            imgOptions.horizontalResolution = 200;
            imgOptions.verticalResolution = 200;
            imgOptions.tiffCompression = TiffCompression.CompressionLZW;

            // Render workbook to image (TIFF)
            const workbookRender = new WorkbookRender(wb, imgOptions);

            // Obtain image data (multi-page TIFF)
            const outputData = workbookRender.toImage();

            const blob = new Blob([outputData], { type: "image/tiff" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'workbook-to-tiff-with-mulitiple-pages.tiff';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download TIFF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">TIFF created successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```  

## **Преобразование Рабочего листа в изображение**  

Рабочие листы содержат данные, которые вы хотите проанализировать. Например, рабочий лист может содержать параметры, итоги, проценты, исключения и вычисления.  

Как разработчик, вам может понадобиться отображать рабочие листы в виде изображений. Например, рабочий лист можно использовать как изображение в приложении или на веб-странице. Возможно, вы захотите вставить изображение в документ Microsoft Word, файл PDF, презентацию PowerPoint или другой тип документа. Проще говоря, вы хотите, чтобы рабочий лист был отрисован как изображение, чтобы вы могли использовать его в другом месте.  

[**SheetRender**](https://reference.aspose.com/cells/javascript-cpp/sheetrender)
[**ImageOrPrintOptions**](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions)
[**WorkbookRender**](https://reference.aspose.com/cells/javascript-cpp/workbookrender)

Класс [**SheetRender**](https://reference.aspose.com/cells/javascript-cpp/sheetrender) представляет рабочий лист, который нужно отобразить как изображение. У него есть перегруженный метод [**SheetRender.toImage(number, string)**](https://reference.aspose.com/cells/javascript-cpp/sheetrender/#toImage-number-string-), который может преобразовать рабочий лист в файл(ы) изображения с разными атрибутами или опциями. Он возвращает объект Buffer, и вы можете сохранить файл изображения на диск или передать его поток. Поддерживаются несколько форматов изображений, например BMP, PNG, GIF, JPG, JPEG, TIFF, EMF.  

Ниже приведен фрагмент кода, демонстрирующий, как преобразовать рабочий лист в Excel-файле в файл изображения.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Convert Worksheet To Images By Page</title>
    </head>
    <body>
        <h1>Convert Worksheet To Images By Page</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, ImageOrPrintOptions, SheetRender, ImageType, Utils } = AsposeCells;

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
            resultDiv.innerHTML = '';

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const sheet = workbook.worksheets.get(0);

            // Preparing image/print options
            const options = new ImageOrPrintOptions();
            options.horizontalResolution = 200;
            options.verticalResolution = 200;
            options.imageType = ImageType.Tiff;

            // Sheet to Image By Page conversion
            const sr = new SheetRender(sheet, options);
            const pageCount = sr.pageCount;

            if (pageCount === 0) {
                resultDiv.innerHTML = '<p style="color: red;">No pages found to render.</p>';
                return;
            }

            const linksContainer = document.createElement('div');
            linksContainer.innerHTML = '<p style="color: green;">Conversion completed. Download the generated images below:</p>';
            for (let j = 0; j < pageCount; j++) 
            {
                // sr.toImage(pageIndex) returns image bytes in browser build
                const imageData = sr.toImage(j);
                const blob = new Blob([imageData], { type: 'image/tiff' });
                const url = URL.createObjectURL(blob);

                const link = document.createElement('a');
                link.href = url;
                link.download = "outputConvertWorksheetToImageByPage_" + (j + 1) + ".tif";
                link.textContent = "Download Image Page " + (j + 1);
                link.style.display = 'block';
                linksContainer.appendChild(link);
            }

            resultDiv.appendChild(linksContainer);
        });
    </script>
</html>
```  

{{% alert color="primary" %}}  
В настоящее время API для преобразования листов в изображения не поддерживает 3D-графики в виде пузырьков.  
{{% /alert %}}  

## **Преобразование Рабочего листа в SVG**  

SVG означает масштабируемую векторную графику. SVG является спецификацией на основе стандартов XML для двумерной векторной графики. Это открытый стандарт, над разработкой которого работает Консорциум Всемирной паутины (W3C) с 1999 года.  

Script на C++ с помощью Aspose.Cells for JavaScript с версии 7.1.0 способен конвертировать рабочие листы в SVG изображения. Следующий пример показывает, как преобразовать рабочий лист в файле Excel в SVG изображение.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Convert Worksheet to SVG Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, SheetType } = AsposeCells;

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
            // Instantiate a workbook
            const workbook = new Workbook();

            // Put sample text in the first cell of the first worksheet in the newly created workbook
            workbook.worksheets.get(0).cells.get("A1").putValue("DEMO TEXT ON SHEET1");

            // Add second worksheet in the workbook
            workbook.worksheets.add(SheetType.Worksheet);

            // Set text in the first cell of the second sheet
            workbook.worksheets.get(1).cells.get("A1").putValue("DEMO TEXT ON SHEET2");

            // Set currently active sheet index to 1 i.e. Sheet2
            workbook.worksheets.activeSheetIndex = 1;

            // Save workbook to SVG. It shall render the active sheet only to SVG
            const outputData = workbook.save(SaveFormat.Svg);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'ConvertWorksheetToSVG_out.svg';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download SVG File';

            document.getElementById('result').innerHTML = '<p style="color: green;">SVG generated successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```  

## **Продвинутые темы**  
- [Конвертировать диаграмму Excel в изображение](/cells/ru/javascript-cpp/convert-an-excel-chart-to-image/)  
- [Преобразование диаграммы в изображение в формате SVG](/cells/ru/javascript-cpp/converting-chart-to-image-in-svg-format/)  
- [Экспорт диаграммы в SVG с атрибутом viewBox](/cells/ru/javascript-cpp/export-chart-to-svg-with-viewbox-attribute/)  
- [Отслеживание процесса преобразования Excel в TIFF](/cells/ru/javascript-cpp/track-conversion-progress-of-excel-to-tiff/)
