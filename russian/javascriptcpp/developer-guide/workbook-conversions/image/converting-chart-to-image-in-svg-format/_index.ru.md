---
title: Конвертация диаграммы в изображение в формате SVG с помощью JavaScript через C++
linktitle: Преобразование диаграммы в изображение в формате SVG
type: docs
weight: 240
url: /ru/javascript-cpp/converting-chart-to-image-in-svg-format/
description: Узнайте, как конвертировать диаграмму в изображение формата SVG с помощью Aspose.Cells for JavaScript через C++.
---

{{% alert color="primary" %}}

Масштабируемая векторная графика (SVG) - это формат векторных изображений на основе XML для двумерной графики, который также поддерживает интерактивность и анимацию. Спецификация SVG является открытым стандартом, разработанным Консорциумом Всемирной паутины (W3C) с 1999 года.

Изображения SVG и их поведение определены в XML-текстовых файлах. Это означает, что их можно искать, индексировать, сценаризировать и сжимать. Как XML-файлы, изображения SVG могут быть созданы и отредактированы с использованием любого текстового редактора, но их чаще создают с помощью графического программного обеспечения.

Aspose.Cells может сохранять диаграммы в изображения в различных форматах, таких как BMP, JPEG, PNG, GIF, SVG и др. В этой статье объясняется, как сохранить диаграмму в формате SVG.

{{% /alert %}}

В следующем образце кода объясняется, как использовать Aspose.Cells для преобразования диаграммы в изображение в формате SVG. Код загружает исходный файл Microsoft Excel, а затем сохраняет первую найденную диаграмму на первом листе в SVG.

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
