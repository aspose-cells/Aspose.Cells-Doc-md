---
title: JavaScript ile C++ kullanarak Sayfa Çizelgesini Grafik Bağlamına Çizmek
linktitle: Grafiksel Ortama Çalışsayısı Renderleme
type: docs
weight: 300
url: /tr/javascript-cpp/render-worksheet-to-graphic-context/
description: C++ ile Aspose.Cells for JavaScript kullanarak bir sayfa çizelgesini grafik bağlamına nasıl çizeceğinizi öğrenin. Bu, resim dosyaları, ekranlar ve yazıcılar için çizim yapmayı kapsar.
---

{{% alert color="primary" %}}

Aspose.Cells artık çalışma sayfalarını grafik bağlamına render edebilir. Grafik bağlamı, bir görüntü dosyası, ekran veya yazıcı gibi herhangi bir şey olabilir. Lütfen çalışma sayfasını grafik bağlamına render etmek için aşağıdaki iki yöntemden birini kullanın.

- [**SheetRender.toImage(int pageIndex, Graphics g, float x, float y)**](https://reference.aspose.com/cells/javascript-cpp/sheetrender/#toImage-number-)
- [**SheetRender.toImage(int pageIndex, Graphics g, float x, float y, float width, float height)**](https://reference.aspose.com/cells/javascript-cpp/sheetrender/#toImage-number-)

{{% /alert %}}

Aşağıdaki kod, Aspose.Cells kullanarak çalışma sayfasını grafik bağlamına nasıl render edeceğinizi gösterir. Kod çalıştırıldığında, çalışma sayfasını tamamıyla yazdırır ve kalan boş alanı mavi renk ile doldurur. Ayrıca resmi **OutputImage_out_.png** dosyası olarak kaydeder. Bu kodu denemek için herhangi bir Excel dosyasını kullanabilirsiniz. Ayrıca kod içindeki yorumları daha iyi anlamak için okuyunuz.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Render Worksheet to Image</title>
    </head>
    <body>
        <h1>Render Worksheet to Image</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, ImageOrPrintOptions, SheetRender, Utils } = AsposeCells;

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
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Create empty image buffer options
            const bmpOptions = new ImageOrPrintOptions();
            bmpOptions.onePagePerSheet = true;

            // Render worksheet to image
            const sheetRender = new SheetRender(worksheet, bmpOptions);
            const imageData = sheetRender.toImage(0);

            // Create blob and provide download link for PNG
            const blob = new Blob([imageData], { type: 'image/png' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'OutputImage_out.png';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Image';

            document.getElementById('result').innerHTML = '<p style="color: green;">Image rendered successfully! Click the download link to download the PNG.</p>';
        });
    </script>
</html>
```
