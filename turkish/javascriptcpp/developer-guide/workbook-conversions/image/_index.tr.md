---
title: JavaScript ile Görüntü
linktitle: Görüntü
type: docs
weight: 300
url: /tr/javascript-cpp/convert-excel-to-image/
---

{{% alert color="primary" %}}  
Aspose.Cells, bir çalışma kitabından çalışsayı dışa aktarmanıza ve farklı biçimlere dönüştürmenize olanak tanır. Bu makale, bir çalışsayının farklı biçimlere nasıl dönüştürüleceğini açıklar.  
{{% /alert %}}  

## Çalışma Kitabını TIFF'e Dönüştürme  

Bir Excel dosyası, birden fazla sayfaya ve sayfaya sahip olabilir. [**WorkbookRender**](https://reference.aspose.com/cells/javascript-cpp/workbookrender) Excel’i çok sayfalı TIFF’e dönüştürmenize olanak tanır. Ayrıca, TIFF için [ImageOrPrintOptions.tiffCompression](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions/#tiffCompression--), [ImageOrPrintOptions.tiffColorDepth](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions/#tiffColorDepth--), Çözünürlük ([ImageOrPrintOptions.horizontalResolution](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions/#horizontalResolution--), [ImageOrPrintOptions.verticalResolution](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions/#verticalResolution--)) gibi çeşitli seçenekleri kontrol edebilirsiniz.  

Aşağıdaki kod örneği, birden çok sayfa içeren Excel dosyasını TIFF'e nasıl dönüştüreceğinizi gösterir. [Kaynak Excel dosyası](workbook-to-tiff-with-mulitiple-pages.xlsx) ve [oluşturulan TIFF görüntüsü](workbook-to-tiff-with-mulitiple-pages.tiff) referansınız için ekli.  

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

## **Çalışsayıyı Görüntüye Dönüştürme**  

Çalışma sayfaları analiz etmek istediğiniz verileri içerebilir. Örneğin, bir çalışma sayfası parametreleri, toplamları, yüzdeleri, istisnaları ve hesaplamaları içerebilir.  

Bir geliştirici olarak, çalışma sayfalarını görüntü olarak sunmanız gerekebilir. Örneğin, bir çalışma sayfası bir uygulama veya web sayfasında resim olarak kullanılabilir. Bir Microsoft Word belgesine, PDF dosyasına, PowerPoint sunumuna veya başka bir belge türüne resim eklemek isteyebilirsiniz. Basitçe söylemek gerekirse, başka bir yerde kullanmak için çalışma sayfasını görüntü olarak oluşturmak istiyorsunuz.  

[**SheetRender**](https://reference.aspose.com/cells/javascript-cpp/sheetrender)
[**ImageOrPrintOptions**](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions)
[**WorkbookRender**](https://reference.aspose.com/cells/javascript-cpp/workbookrender)

[**SheetRender**](https://reference.aspose.com/cells/javascript-cpp/sheetrender) sınıfı, resim olarak görüntülenecek bir çalışma sayfasını temsil eder. Aşırı yüklenmiş bir yöntemi, [**SheetRender.toImage(number, string)**](https://reference.aspose.com/cells/javascript-cpp/sheetrender/#toImage-number-string-), ile farklı öznitelik veya seçeneklerle bir çalışma sayfasını resim dosyasına dönüştürebilir. Bir Buffer nesnesi döner ve resmi diske kaydedebilir veya akış olarak kullanabilirsiniz. Birkaç resim formatı desteklenmektedir, örneğin BMP, PNG, GIF, JPG, JPEG, TIFF, EMF.  

Aşağıdaki kod örneği, bir Excel dosyasındaki bir çalışma sayfasını bir görüntü dosyasına dönüştürmenin nasıl yapıldığını gösterir.  

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
Şu anda, çalışma sayfalarını görüntülere dönüştürmek için API, 3D kabarcık grafiklerini desteklememektedir.  
{{% /alert %}}  

## **Çalışma Sayfasını SVG'ye Dönüştürme**  

SVG, Ölçeklenebilir Vektör Grafikleri anlamına gelir. SVG, iki boyutlu vektör grafikleri için XML standartlarına dayanan bir spesifikasyondur. 1999'dan beri World Wide Web Consortium (W3C) tarafından geliştirilen açık bir standarttır.  

Aspose.Cells for JavaScript, C++ aracılığıyla, sürüm 7.1.0'dan beri çalışma sayfalarını SVG görseline dönüştürebilmektedir. Aşağıdaki kod parçacığı, bir Excel dosyasındaki çalışma sayfasını SVG görseline nasıl dönüştüreceğinizi gösterir.  

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

## **Gelişmiş Konular**  
- [Bir Excel Grafiğini Görüntüye Dönüştürme](/cells/tr/javascript-cpp/convert-an-excel-chart-to-image/)  
- [SVG Biçiminde Grafikleri Görüntüye Dönüştürme](/cells/tr/javascript-cpp/converting-chart-to-image-in-svg-format/)  
- [Görünüm Kutusu Özelliği ile Grafiksel Bir Ortama Tabloyu Dışa Aktarma](/cells/tr/javascript-cpp/export-chart-to-svg-with-viewbox-attribute/)  
- [Excel'den TIFF'e Dönüşüm İlerlemesini İzle](/cells/tr/javascript-cpp/track-conversion-progress-of-excel-to-tiff/)
