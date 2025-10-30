---
title: Export Chart to SVG with viewBox attribute using JavaScript via C++
linktitle: viewBox属性を使用してチャートをSVG形式にエクスポート
type: docs
weight: 280
url: /ja/javascript-cpp/export-chart-to-svg-with-viewbox-attribute/
description: C++経由のAspose.Cells for JavaScriptを使用して、viewBox属性を持つSVG形式へのチャートエクスポート方法を学びます。
---

{{% alert color="primary" %}}

デフォルトでは、チャートをSVG形式にエクスポートするとき、そのXMLには**viewBox**属性が含まれません。しかし、Aspose.Cellsは、**true**に設定された場合に**viewBox**属性でチャートをSVG形式でエクスポートする[**ImageOrPrintOptions.svgFitToViewPort**](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions/#svgFitToViewPort--)プロパティを提供します。

{{% /alert %}}

## viewBox属性を含むSVG形式でチャートをエクスポート

次のコードサンプルは、viewBox属性を含むSVG形式でチャートをエクスポートします。

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

チャートのSVGをNotepadで開くと、次のような**viewBox**属性が見つかります。

{{< highlight java >}}

 <svg xmlns="http://www.w3.org/2000/svg"

     xmlns:xlink="http://www.w3.org/1999/xlink"

     width="100%" height="100%"

     viewBox="0 0 480 288">

{{< /highlight >}}

{{% /alert %}}
