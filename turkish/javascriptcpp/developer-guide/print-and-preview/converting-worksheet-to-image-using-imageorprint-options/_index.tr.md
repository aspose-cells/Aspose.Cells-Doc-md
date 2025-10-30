---
title: JavaScript kullanarak ImageOrPrint Seçenekleri ile Çalışma Sayfasını Görüntüye Dönüştürme C++ üzerinden
linktitle: Resim veya Yazdır Seçeneklerini Kullanarak Çalışma Sayfasını Resme Dönüştürme
type: docs
weight: 90
url: /tr/javascript-cpp/converting-worksheet-to-image-using-imageorprint-options/
description: Bir çalışma sayfasını görüntü dosyasına dönüştürmeyi ve çeşitli görüntü ve yazdırma seçeneklerini nasıl uygulayacağınızı Aspose.Cells for JavaScript kullanarak C++ üzerinden öğrenin.   
---

{{% alert color="primary" %}}  
Bu belge, bir çalışma sayfasını bir resim dosyasına dönüştürme ve resim için farklı resim ve yazdır seçeneklerini (çözünürlük, TIFF sıkıştırma, resim formatı ve sayfa kalitesi gibi) uygulama konusunda ayrıntılı bir anlayış sağlamak amacıyla tasarlanmıştır.  
{{% /alert %}}  

## **Çalışma Sayfalarını Resim Olarak Kaydetme - Farklı Yaklaşımlar**  

Bazen çalışsayılarınızı resimsel bir temsil olarak sunmanız gerekebilir. Çalışsayı resimlerini uygulamalarınıza veya web sayfalarınıza eklemeniz veya kullanmanız gerekebilir. Resimlerini bir Word belgesine, bir PDF dosyasına, bir PowerPoint sunumuna eklemeniz veya bunları başka bir senaryoda kullanmanız gerekebilir. Basitçe başka bir yerde kullanabilmek için çalışsayısının bir resim olarak görüntülenmesini istersiniz. Aspose.Cells, Excel dosyalarındaki çalışsayıları resme dönüştürmeyi destekler. Ayrıca, Aspose.Cells, resim formatı, çözünürlük (dikey ve yatay), resim kalitesi ve diğer resim ve yazdırma seçenekleri belirleme gibi farklı seçenekleri destekler.  

Office Otomasyonu deneyebilirsiniz, ancak Office otomasyonunun kendi zayıf noktaları vardır. Güvenlik, kararlılık, ölçeklenebilirlik ve hız, fiyat ve özellikler gibi birkaç nedeni ve sorun içerir. Kısacası, birçok nedeni vardır ve en önemlisi Microsoft'un kendisinin yazılım çözümlerinden Office otomasyonuna karşı şiddetle tavsiye etmemesidir.  

Bu makale, Visual Studio .NET'te bir konsol uygulaması oluşturmayı, Aspose.Cells API'sını kullanarak bir çalışma sayfasını farklı resim ve yazdır seçenekleriyle bir resme dönüştürmeyi ve bunu birkaç basit satır kodla gerçekleştirmeyi gösteriyor.  

[**SheetRender**](https://reference.aspose.com/cells/javascript-cpp/sheetrender/) sınıfı, çalışma sayfası için görüntüler oluşturmak amacıyla bir çalışma sayfasını temsil eder, doğrudan çalışma sayfasını belirttiğiniz özelliklerle veya seçeneklerle görüntü dosyasına dönüştürebilen aşırı yüklenmiş [**toImage(number)**](https://reference.aspose.com/cells/javascript-cpp/sheetrender/#toImage-number-) yöntemine sahiptir. Bir nesne döndürebilir ve bu nesneye görüntü dosyasını disk/akışa kaydedebilirsiniz. Desteklenen birkaç görüntü formatı vardır, örn BMP, PNG, GIFF, JPEG, TIFF, EMF ve diğerleri.  

## **Aspose.Cells'ı Kullanarak Resme Dönüştürme İçin Resim veya Yazdır Seçeneklerini Kullanma**  

### **Microsoft Excel'de şablon çalışma kitabı oluşturma**  

MS Excel'de yeni bir çalışma kitabı oluşturdum ve ilk çalışma sayfasına bazı veriler ekledim. Şimdi, şablon dosyasının "Sheet1" adlı çalışma sayfasını "SheetImage.tiff" adlı bir görüntü dosyasına dönüştüreceğim ve yatay ve dikey çözünürlük, TiffCompression vb. gibi farklı görüntü seçenekleri uygulayacağım.  

### **Aspose.Cells'i İndirin ve Yükleyin**  

İlk olarak, [indir](https://downloads.aspose.com/cells/javascript-cpp) Aspose.Cells for JavaScript kullanarak C++ ile. Geliştirme bilgisayarınıza kurun. Tüm [Aspose](http://www.aspose.com/) bileşenleri yüklendiğinde değerlendirme modunda çalışır. Değerlendirme modunda zaman sınırı yoktur ve yalnızca filigranlar ekler.  

### **Bir Proje Oluşturun**  

Tercih ettiğiniz geliştirme ortamınızı (örneğin, Visual Studio) başlatın. Yeni bir konsol uygulaması oluşturun.  

### **Referanslar Ekle**  

Bu proje Aspose.Cells kullanacaktır. Bu nedenle, projenize Aspose.Cells bileşenine referans eklemeniz gerekir. Örneğin, ….\Program Files\Aspose\Aspose.Cells for JavaScript kullanarak C++\Bin\Aspose.Cells.node  

### **Çalışma Sayfasını Bir Görüntü Dosyasına Dönüştürme**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Worksheet to Image Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, ImageOrPrintOptions, SheetRender, ImageType, TiffCompression, PrintingPageType, Utils } = AsposeCells;

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

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get the first worksheet
            const sheet = workbook.worksheets.get(0);

            // Apply different Image and Print options
            const options = new ImageOrPrintOptions();

            // Set Horizontal Resolution
            options.horizontalResolution = 300;

            // Set Vertical Resolution
            options.verticalResolution = 300;

            // Set TiffCompression
            options.tiffCompression = TiffCompression.CompressionLZW;

            // Set Image Format
            options.imageType = ImageType.Tiff;

            // Set printing page type
            options.printingPage = PrintingPageType.Default;

            // Render the sheet with respect to specified image/print options
            const sr = new SheetRender(sheet, options);

            // Render/save the image for the sheet (pageIndex is zero-based)
            const pageIndex = 3;
            const imageData = sr.toImage(pageIndex);

            const blob = new Blob([imageData], { type: 'image/tiff' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = `outputWorksheetToAnImage_${pageIndex + 1}.tiff`;
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download TIFF Image';

            resultDiv.innerHTML = '<p style="color: green;">Image rendered successfully! Click the download link to get the image.</p>';
        });
    </script>
</html>
```  

## **Dönüşüm Seçenekleri**  

Belirli sayfaları resme kaydetmek mümkündür. Aşağıdaki kod, bir çalışma kitabındaki ilk ve ikinci çalışsayılarını JPG resimlerine dönüştürür.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Specific Pages To Images</title>
    </head>
    <body>
        <h1>Specific Pages To Images Example</h1>
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object by opening the Excel file through the file stream
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get the first worksheet.
            const sheet = workbook.worksheets.get(0);

            // Define ImageOrPrintOptions
            const imgOptions = new ImageOrPrintOptions();

            // Specify the image format
            imgOptions.imageType = ImageType.Jpeg;

            // Render the sheet with respect to specified image/print options
            const sr = new SheetRender(sheet, imgOptions);

            // Specify page index to be rendered
            const idxPage = 3;

            // Render the third image for the sheet
            const bitmap = sr.toImage(idxPage);

            // Save the image file as a downloadable blob
            const blob = new Blob([bitmap], { type: 'image/jpeg' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = `outputSpecificPagesToImage_${idxPage + 1}.jpg`;
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Image File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Image rendered successfully! Click the download link to get the image file.</p>';
        });
    </script>
</html>
```  

## **WorkbookRender kullanarak Görüntü dönüşümü**  

Bir TIFF görüntüsü birden fazla çerçeve içerebilir. Tüm çalışma kitabını tek bir TIFF görüntüsüne çoklu çerçeve veya sayfa olarak kaydedebilirsiniz:  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Use WorkbookRender for Image Conversion Example</title>
    </head>
    <body>
        <h1>Use WorkbookRender for Image Conversion Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;"></a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, ImageOrPrintOptions, ImageType, WorkbookRender, Utils } = AsposeCells;

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
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Prepare image/print options
            const opts = new ImageOrPrintOptions();
            opts.imageType = AsposeCells.ImageType.Tiff;

            // Create WorkbookRender and convert to image
            const workbookRender = new WorkbookRender(workbook, opts);

            // toImage may return a single Uint8Array or an array of Uint8Array pages
            const imageResult = await workbookRender.toImage();

            let imageData = imageResult;
            if (Array.isArray(imageResult) && imageResult.length > 0) {
                imageData = imageResult[0];
            }

            // Ensure imageData is a Uint8Array or ArrayBuffer
            let blob;
            if (imageData instanceof Uint8Array || imageData instanceof ArrayBuffer) {
                blob = new Blob([imageData], { type: 'image/tiff' });
            } else {
                // Fallback: try to stringify/convert if possible
                blob = new Blob([imageData], { type: 'application/octet-stream' });
            }

            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputUseWorkbookRenderForImageConversion.tiff';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Converted TIFF Image';

            document.getElementById('result').innerHTML = '<p style="color: green;">Image conversion completed! Click the download link to get the TIFF file.</p>';
        });
    </script>
</html>
```
