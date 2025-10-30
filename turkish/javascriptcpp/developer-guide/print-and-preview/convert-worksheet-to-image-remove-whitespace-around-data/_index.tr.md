---
title: Sayfayı Görüntüye Dönüştür  JavaScript ile Çevre boşluğunu kaldırma
linktitle: Elektronik tabloyu Görüntüye Dönüştür  Veri Etrafındaki Boşlukları Kaldırma
type: docs
weight: 40
url: /tr/javascript-cpp/convert-worksheet-to-image-remove-whitespace-around-data/
description: Microsoft Excel çalışma sayfalarını resimlere dönüştürmeyi ve veriler etrafındaki boşlukları kaldırmayı Aspose.Cells for JavaScript kullanarak C++ üzerinden öğrenin. 
---

{{% alert color="primary" %}}

Bazen, çalışma sayfalarını uygulamalarda veya web sayfalarında sunmanız gerekebilir. Örneğin, çalışma sayfalarını bir Word belgesine, bir PDF dosyasına, bir PowerPoint sunumuna veya başka bir belgeye yerleştirmeniz gerekebilir. Temelde, bir çalışma sayfasını bir görüntü olarak oluşturmak ve başka uygulamalara yapıştırmak istersiniz. Aspose.Cells, Microsoft Excel çalışma sayfalarını görüntülere dönüştürmenizi sağlar.

{{% /alert %}}

## **Veri Etrafındaki Boşlukları Kaldır**

[**SheetRender**](https://reference.aspose.com/cells/javascript-cpp/sheetrender) API'si, örneğin görüntü biçimi, sayfa sayfalama çalışma sayfaları vb. gibi belirli özelliklere sahip bir çalışma sayfasını bir görüntü dosyasına dönüştürür. BMP, GIF, JPG, TIFF ve EMF gibi birçok görüntü formatı desteklenir.

Sayfa görüntüleme özelliğini kullandığınızda, çıktı görüntüsü varsayılan olarak etrafında boşluk bulunur. Bu, kaynak çalışma sayfası için üst, alt, sol ve sağ sayfa düzeni kenarlarını 0 olarak ayarlayarak ve buna uygun [**ImageOrPrintOptions**](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions) özniteliklerini belirleyerek kaldırabilirsiniz.

Aşağıdaki kod parçası, çıktı görüntüsündeki veri etrafındaki boşluğu kaldırır.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Convert Sheet to EMF</title>
    </head>
    <body>
        <h1>Convert Worksheet to EMF Image</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Convert to EMF</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, LoadOptions, LoadFilter, LoadDataFilterOptions, ImageOrPrintOptions, ImageType, PrintingPageType, SheetRender, Utils } = AsposeCells;

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

            // Prepare load options and filters
            const loadOptions = new LoadOptions();
            loadOptions.loadFilter = new LoadFilter(LoadDataFilterOptions.All);

            // Instantiate workbook with load options
            const workbook = new Workbook(new Uint8Array(arrayBuffer), loadOptions);

            // Get the first worksheet
            const sheet = workbook.worksheets.get(0);

            // To remove the white border around the image.
            sheet.pageSetup.leftMargin = 0;
            sheet.pageSetup.rightMargin = 0;
            sheet.pageSetup.bottomMargin = 0;
            sheet.pageSetup.topMargin = 0;

            // Define ImageOrPrintOptions
            const imgOptions = new ImageOrPrintOptions();
            imgOptions.imageType = ImageType.Emf;

            // Set only one page would be rendered for the image
            imgOptions.onePagePerSheet = true;
            imgOptions.printingPage = PrintingPageType.IgnoreBlank;

            // Create the SheetRender object based on the sheet with its ImageOrPrintOptions attributes
            const sr = new SheetRender(sheet, imgOptions);

            // Convert the image (returns image data in browser environment)
            const imageData = sr.toImage(0);

            // Create a blob and provide download link
            const blob = new Blob([imageData], { type: 'image/emf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputRemoveWhitespaceAroundData.emf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download EMF Image';

            document.getElementById('result').innerHTML = '<p style="color: green;">Image conversion completed successfully! Click the download link to get the EMF file.</p>';
        });
    </script>
</html>
```
