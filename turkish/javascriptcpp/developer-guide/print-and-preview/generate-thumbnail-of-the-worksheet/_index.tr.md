---
title: JavaScript ile C++ üzerinden Sayfa Öğesi için Küçük Resim Oluşturma
linktitle: Çalışma Sayfasının Küçük Resmi Oluşturma
type: docs
weight: 110
url: /tr/javascript-cpp/generate-thumbnail-of-the-worksheet/
description: Bir sayfa öğesinden küçük resim oluşturmayı öğrenin. Belgeler ve sunumlar için önizleme amaçlı küçük resimler oluşturun.
---

{{% alert color="primary" %}} 

Çalışma sayfalarından küçük resimler oluşturmak faydalı olabilir. Bir küçük resim, çalışma sayfasındaki içeriğin bir ön izlemesini vermek üzere bir Word belgesine veya bir PowerPoint sunumuna yapıştırılabilir. Gerçek belgenin indirme bağlantısına bir bağlantıyla bir web sayfasına eklenebilir ve diğer birçok kullanımı bulunmaktadır.

{{% /alert %}} 

Aspose.Cells for JavaScript ile C++ sayfa öğelerini resim dosyalarına çıktı alınmasını sağlar, bu nedenle küçük resim yapmak kolaydır. Aşağıdaki örnek kod, sayfa öğelerini resim dosyalarına nasıl çıktı alacağınızı gösterir.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Generate Worksheet Thumbnail Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Generate Thumbnail</button>
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

            // Instantiate and open an Excel file from the uploaded file
            const book = new Workbook(new Uint8Array(arrayBuffer));

            // Define ImageOrPrintOptions
            const imgOptions = new ImageOrPrintOptions();

            // Specify the image format
            imgOptions.imageType = ImageType.Jpeg;

            // Set the vertical and horizontal resolution
            imgOptions.verticalResolution = 200;
            imgOptions.horizontalResolution = 200;

            // One page per sheet is enabled
            imgOptions.onePagePerSheet = true;

            // Set desired thumbnail dimensions (converted to a property assignment)
            imgOptions.desiredSize = [600, 600, true];

            // Get the first worksheet
            const sheet = book.worksheets.get(0);

            // Render the sheet with respect to specified image/print options
            const sr = new SheetRender(sheet, imgOptions);

            // Generate the image for the first page (index 0)
            const outputData = sr.toImage(0);

            // Create a blob and provide a download link
            const blob = new Blob([outputData], { type: 'image/jpeg' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputGenerateThumbnailOfWorksheet.jpg';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Thumbnail Image';

            document.getElementById('result').innerHTML = '<p style="color: green;">Thumbnail generated successfully! Click the download link to get the image.</p>';
        });
    </script>
</html>
```
