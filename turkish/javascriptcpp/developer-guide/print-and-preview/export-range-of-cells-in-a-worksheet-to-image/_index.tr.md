---
title: Bir Çalışma Sayfasındaki Hücreleri Belirli Aralıklara Görüntüye Aktarma JavaScript kullanarak C++ üzerinden
linktitle: Çalışma Sayfasındaki Hücre Aralığını Bir Görüntüye Aktarma
type: docs
weight: 60
url: /tr/javascript-cpp/export-range-of-cells-in-a-worksheet-to-image/
---

## **Olası Kullanım Senaryoları**  

Aspose.Cells for JavaScript kullanarak C++ ile çalışma sayfası veya grafiği görüntüsüne aktarabilirsiniz. Ancak bazen sadece belli hücre aralığını görüntüye aktarmanız gerekebilir. Bu makale bunu nasıl başaracağınızı açıklar.  

## **Bir Çalışma Sayfasındaki Hücre Aralığını Görüntüye Aktar**  

Bir alanın görüntüsünü almak için, yazdırma alanını istediğiniz aralığa ayarlayın ve tüm kenar boşluklarını 0 yapın. Ayrıca [**ImageOrPrintOptions.onePagePerSheet**](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions/#onePagePerSheet--) değerini **true** olarak ayarlayın. Aşağıdaki kod D8:G16 aralığının görüntüsünü alır. Aşağıda, kodda kullanılan [örnek Excel dosyasının](47153160.xlsx) ekran görüntüsü bulunmaktadır. Kodu herhangi bir Excel dosyasıyla deneyebilirsiniz.  

## **Örnek Excel Dosyası ve Dışa Aktarılan Görüntü Ekran Görüntüsü**  

**![todo:image_alt_text](export-range-of-cells-in-a-worksheet-to-image_1.png)**  

Kod çalıştırıldığında yalnızca D8:G16 aralığının bir görüntüsü oluşturulur.  

**![todo:image_alt_text](Output-Image.png)**  

## **Örnek Kod**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Export Range To Image</title>
    </head>
    <body>
        <h1>Export Range Of Cells In Worksheet To Image</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, ImageOrPrintOptions, ImageType, SheetRender } = AsposeCells;

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

            // Create workbook from uploaded file.
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Set the print area with your desired range
            worksheet.pageSetup.printArea = "D8:G16";

            // Set all margins as 0
            worksheet.pageSetup.leftMargin = 0;
            worksheet.pageSetup.rightMargin = 0;
            worksheet.pageSetup.topMargin = 0;
            worksheet.pageSetup.bottomMargin = 0;

            // Set OnePagePerSheet option as true and image options
            const options = new ImageOrPrintOptions();
            options.onePagePerSheet = true;
            options.imageType = ImageType.Jpeg;
            options.horizontalResolution = 200;
            options.verticalResolution = 200;

            // Take the image of your worksheet
            const sr = new SheetRender(worksheet, options);
            const outputData = sr.toImage(0);

            const blob = new Blob([outputData], { type: 'image/jpeg' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputExportRangeOfCellsInWorksheetToImage.jpg';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Image';

            document.getElementById('result').innerHTML = '<p style="color: green;">Image exported successfully! Click the download link to download the image.</p>';
        });
    </script>
</html>
```
