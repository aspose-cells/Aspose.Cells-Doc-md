---
title: JavaScript ile C++ kullanarak Grafiklerin SVG Formatına Dönüştürülmesi
linktitle: SVG Formatında Görüntüye Grafik Dönüştürme
type: docs
weight: 240
url: /tr/javascript-cpp/converting-chart-to-image-in-svg-format/
description: Bir grafiği SVG formatında görsele dönüştürmenin nasıl yapılacağını Aspose.Cells for JavaScript kullanarak C++ ile öğrenin.
---

{{% alert color="primary" %}}

Ölçeklenebilir Vektör Grafikleri (SVG), aynı zamanda etkileşimliliği ve animasyonu destekleyen iki boyutlu grafikler için XML tabanlı bir vektör görüntü formatıdır. SVG belirtmesi, 1999'dan beri World Wide Web Consortium (W3C) tarafından geliştirilen açık bir standarttır.

SVG görüntüleri ve davranışları, XML metin dosyalarında tanımlanır. Bu, aranabilir, dizine eklenir, betiklenir ve sıkıştırılabilir anlamına gelir. XML dosyaları olarak, SVG görüntüleri herhangi bir metin düzenleyici ile oluşturulabilir ve düzenlenebilir, ancak genellikle çizim yazılımı ile oluşturulur.

Aspose.Cells, grafikleri BMP, JPEG, PNG, GIF, SVG ve diğer formatlarda görsellere kaydedebilir. Bu makale, bir grafiği SVG formatında kaydetme yöntemini anlatmaktadır.

{{% /alert %}}

Aşağıdaki örnek kod, Aspose.Cells'in bir grafiği SVG biçimli bir resme dönüştürmek için nasıl kullanılacağını açıklar. Kod, kaynak Microsoft Excel dosyasını yükler ve ardından ilk çalışta bulunan ilk grafiği SVG biçiminde kaydeder.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Export Chart to SVG</title>
    </head>
    <body>
        <h1>Export First Chart to SVG</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, ImageOrPrintOptions, ImageType } = AsposeCells;

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

            // Access first chart inside the worksheet
            const chart = worksheet.charts.get(0);

            // Set image or print options
            const opts = new ImageOrPrintOptions();
            opts.imageType = ImageType.Svg;

            // Export the chart to SVG format (returns image bytes)
            const imageData = chart.toImage(opts);

            // Create downloadable SVG blob
            const blob = new Blob([imageData], { type: 'image/svg+xml' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Image_out.svg';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download SVG Image';

            document.getElementById('result').innerHTML = '<p style="color: green;">Chart exported to SVG. Click the download link to download the SVG file.</p>';
        });
    </script>
</html>
```
