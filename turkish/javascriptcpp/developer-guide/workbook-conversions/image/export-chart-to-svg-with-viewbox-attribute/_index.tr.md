---
title: Grafiği viewBox özniteliği ile SVG e dışa aktarın, JavaScript ve C++ kullanarak
linktitle: viewBox özniteliği ile SVG ye Grafik Dışa Aktarma
type: docs
weight: 280
url: /tr/javascript-cpp/export-chart-to-svg-with-viewbox-attribute/
description: Grafiği viewBox özniteliği ile SVG formatına dışa aktarmanın nasıl yapılacağını Aspose.Cells for JavaScript kullanarak C++ ile öğrenin.
---

{{% alert color="primary" %}}

Varsayılan olarak, grafik SVG biçimine dışa aktarıldığında, **viewBox** özniteliği içinde yer almaz. Ancak, Aspose.Cells, **true** olarak ayarlandığında grafiği viewBox özniteliği ile SVG'ye dışa aktarır.

{{% /alert %}}

## viewBox Özniteliği ile SVG'ye Grafik Dışa Aktarma

Aşağıdaki örnek kod, grafiği viewBox özniteliği ile SVG biçiminde dışa aktarır.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Chart to SVG Example</title>
    </head>
    <body>
        <h1>Chart to SVG Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Convert Chart to SVG</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, ImageOrPrintOptions, ImageType, Utils } = AsposeCells;

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

            // Set image or print options with SVGFitToViewPort true
            const opts = new ImageOrPrintOptions();
            opts.imageType = ImageType.Svg;
            opts.svgFitToViewPort = true;

            // Save the chart to svg format (returns data in browser)
            const svgData = await chart.toImage(opts);

            // Create blob and download link for SVG
            const blob = new Blob([svgData], { type: 'image/svg+xml' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Image_out.svg';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download SVG File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Chart converted to SVG successfully! Click the download link to get the SVG file.</p>';
        });
    </script>
</html>
```

{{% alert color="primary" %}}

Grafiğin SVG'sini not defterinde açarsanız, benzer bir **viewBox** özniteliği bulacaksınız.

{{< highlight java >}}

 <svg xmlns="http://www.w3.org/2000/svg"

     xmlns:xlink="http://www.w3.org/1999/xlink"

     width="100%" height="100%"

     viewBox="0 0 480 288">

{{< /highlight >}}

{{% /alert %}}
