---
title: JavaScript kullanarak çalışma sayfasını görüntüye ve sayfaya göre çalışma sayfasını görüntüye dönüştürme C++ üzerinden
linktitle: Çalışma Sayfasını Görüntüye Dönüştürme ve Sayfa Başına Çalışma Sayfasını Görüntüye Dönüştürme
type: docs
weight: 80
url: /tr/javascript-cpp/converting-worksheet-to-image-and-worksheet-to-image-by-page/
---

{{% alert color="primary" %}}
Bu belge, geliştirilicilere bir çalışma sayfasını görsel dosyasına dönüştürme ve çok sayfalı çalışma sayfasını her sayfa için ayrı görsel dosyasına dönüştürme konusunda detaylı bilgi sağlamayı amaçlamaktadır.

Bazı durumlarda, çalışma sayfalarını örneğin uygulamalarda veya web sayfalarında kullanmak için resim olarak sunmanız gerekebilir. Resimleri bir Word belgesine, bir PDF dosyasına, bir PowerPoint sunumuna eklemek veya başka bir senaryoda kullanmak gerekebilir. Temel olarak, çalışma sayfasını bir resim olarak oluşturmak istersiniz. Aspose.Cells, Microsoft Excel dosyalarındaki çalışma sayfalarını resimlere dönüştürmeyi destekler. Ayrıca, Aspose.Cells, bir çalışma kitabını birden fazla resim dosyasına, sayfa başına bir tane olmak üzere dönüştürmeyi destekler.

Bunu başarmak için Office Automation'ı kullanabilirsiniz, ancak Office Automation'ın kendi dezavantajları vardır. Güvenlik, istikrar, ölçeklenebilirlik/hız, fiyat ve özellikler gibi birçok neden ve sorun bulunmaktadır. Kısacası, birçok neden bulunmaktadır, ancak ana nedenlerden biri Microsoft'un Office Automation'u kesinlikle önermemesidir.
{{% /alert %}}

## **Aspose.Cells for JavaScript kullanarak Çalışma Sayfasını Resim Dosyasına Dönüştürme**

Bu makale, bir konsol uygulaması oluşturmayı, çalışma sayfasını görsele dönüştürmeyi ve Aspose.Cells API kullanarak kod satırlarını en basit ve birkaç adımda çalışma sayfasını her biri ayrı görsel dosyası olacak şekilde dönüştürmeyi gösterir.

Programınıza veya projenize, [**SheetRender**](https://reference.aspose.com/cells/javascript-cpp/sheetrender/), [**ImageOrPrintOptions**](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions/), [**WorkbookRender**](https://reference.aspose.com/cells/javascript-cpp/workbookrender/) gibi render özellikleriyle ilgili birkaç değerli sınıfı içe aktarmanız gerekir. [**SheetRender**](https://reference.aspose.com/cells/javascript-cpp/sheetrender/) sınıfı, görüntüleri render etmek için çalışma sayfasını temsil eder ve herhangi bir özellik veya seçenek ayarlanarak doğrudan çalışma sayfasını görüntü dosyalarına dönüştürebilen aşırı yüklenmiş [**toImage(number)**](https://reference.aspose.com/cells/javascript-cpp/sheetrender/#toImage-number-) yöntemine sahiptir. Bu, bir görüntü nesnesi dönebilir ve disk/akışa bir görüntü dosyası kaydedebilirsiniz. BMP, PNG, GIF, JPG, JPEG, TIFF, EMF ve diğerleri gibi birkaç görüntü formatı desteklenmektedir.

Bu makalede şunları açıklar:

- Bir çalışma sayfasını bir resme dönüştürme
- Bir çalışma sayfasındaki her sayfayı bir resme dönüştürme

Bu görev, Aspose.Cells'ı kullanarak bir şablon çalışma kitabındaki bir çalışma sayfasını bir resim dosyasına dönüştürmenin nasıl yapıldığını gösterir.

### **Proje Kurulumu**

1. İlk olarak, [Aspose.Cells for JavaScript kullanarak C++ ile İndir](https://downloads.aspose.com/cells/javascript-cpp).
1. Geliştirme bilgisayarınıza yükleyin. Tüm [Aspose](http://www.aspose.com/) bileşenleri yüklendiğinde değerlendirme modunda çalışır. Değerlendirme modunun zaman sınırlaması yoktur ve sadece üretilen belgelere filigranlar eklenir. Şimdi geliştirme ortamınızı başlatın ve yeni bir konsol uygulaması oluşturun. Bu örnek bir JavaScript konsol uygulaması kullanıyor, ancak JavaScript ile bütünleşen herhangi bir kurulum kullanabilirsiniz. Oluşturulan projeye Aspose.Cells referansı ekleyin.

### **Çalışma Sayfasını Resim Dosyasına Dönüştürme**

Microsoft Excel'de yeni bir çalışma kitabı oluşturdum ve ilk çalışma sayfasına bazı veriler ekledim: **Testbook.xlsx** (1 çalışma sayfası). Daha sonra, şablon dosyasının Sheet1 çalışma sayfasını SheetImage.jpg adında bir resim dosyasına dönüştürdüm.

Bileşen tarafından görevi tamamlamak için kullanılan kod aşağıda verilmiştir. Bu kod, **Testbook.xlsx**'teki Sheet1'i, bu dönüşümün ne kadar kolay olduğunu açıklamak için bir resim dosyasına dönüştürür.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Convert Worksheet to Image Example</title>
    </head>
    <body>
        <h1>Convert Worksheet to Image Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, ImageOrPrintOptions, SheetRender, ImageType, Utils } = AsposeCells;

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

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get the first worksheet.
            const sheet = workbook.worksheets.get(0);

            // Define ImageOrPrintOptions
            const imgOptions = new ImageOrPrintOptions();
            imgOptions.onePagePerSheet = true;

            // Specify the image format
            imgOptions.imageType = ImageType.Jpeg;

            // Render the sheet with respect to specified image/print options
            const sr = new SheetRender(sheet, imgOptions);

            // Generate the image data for the first page (index 0)
            const outputData = sr.toImage(0);

            // Create a blob and provide a download link
            const blob = new Blob([outputData], { type: 'image/jpeg' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputConvertWorksheettoImageFile.jpg';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Image File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Worksheet converted to image successfully! Click the download link to get the image file.</p>';
        });
    </script>
</html>
```

## **C++ kullanarak Aspose.Cells for JavaScript ile Çalışma Sayfasını Sayfa Bazında Görüntü Dosyasına Dönüştürme**

Bu örnek, birkaç sayfası olan bir şablon çalışma kitabından bir çalışma sayfasını bir resim dosyasına dönüştürmek için Aspose.Cells'ı kullanmanın nasıl yapıldığını göstermektedir.

### **Sayfa bazında Çalışma Sayfasını Görüntüye Dönüştürme**

Microsoft Excel'de yeni bir çalışma kitabı oluşturdum ve ilk çalışma sayfasına bazı veriler ekledim: **Testbook2.xlsx** (1 çalışma sayfası).

Şimdi, şablon dosyasının Sheet1 çalışma sayfasını resim dosyalarına dönüştür (sayfa başına bir dosya). Zaten kopyalama görevini gerçekleştirmek için konsol uygulaması oluşturmuştum, bu nedenle konsol uygulaması oluşturma adımlarını atlayacak ve doğrudan çalışma sayfası dönüşüm adımlarına geçeceğim.

Bunu gerçekleştirmek için kullanılan kod aşağıdadır. Sheet1 in Testbook2.xlsx dosyasını sayfa başına görüntü dosyalarına dönüştürür.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Convert Worksheet to Images By Page</title>
    </head>
    <body>
        <h1>Convert Worksheet to Images By Page</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <div id="downloadLinks"></div>
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
            const resultDiv = document.getElementById('result');
            const linksDiv = document.getElementById('downloadLinks');
            linksDiv.innerHTML = '';
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

            // Create image/print options and set properties
            const options = new ImageOrPrintOptions();
            options.horizontalResolution = 200;
            options.verticalResolution = 200;
            options.imageType = ImageType.Tiff;

            // Sheet to Image By Page conversion
            const sr = new SheetRender(sheet, options);

            const pageCount = sr.pageCount;
            const createdLinks = [];

            for (let j = 0; j < pageCount; j++) 
            {
                // toImage returns image data for the specified page
                const outputData = sr.toImage(j);
                const blob = new Blob([outputData], { type: 'image/tiff' });
                const url = URL.createObjectURL(blob);
                const link = document.createElement('a');
                const pageNumber = j + 1;
                const fileName = 'outputConvertWorksheetToImageByPage_' + pageNumber + '.tif';
                link.href = url;
                link.download = fileName;
                link.textContent = 'Download ' + fileName;
                link.style.display = 'block';
                linksDiv.appendChild(link);
                createdLinks.push(url);
            }

            resultDiv.innerHTML = '<p style="color: green;">Conversion completed! Click the links below to download the generated TIFF images.</p>';
        });
    </script>
</html>
```
