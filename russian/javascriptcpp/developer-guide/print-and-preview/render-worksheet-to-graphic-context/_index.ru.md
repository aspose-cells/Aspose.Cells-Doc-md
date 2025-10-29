---
title: Отрисовка листа в графический контекст с помощью JavaScript через C++
linktitle: Отобразить Рабочий лист на графический контекст
type: docs
weight: 300
url: /ru/javascript-cpp/render-worksheet-to-graphic-context/
description: Узнайте, как отображать лист в графическом контексте с помощью Aspose.Cells for JavaScript на C++. Включает вывод в файлы изображений, на экраны и принтеры.
---

{{% alert color="primary" %}}

Aspose.Cells теперь может рендерить рабочие листы в графический контекст. Графический контекст может быть чем угодно, например, изображением, экраном или принтером. Пожалуйста, используйте один из следующих двух методов для рендеринга рабочего листа в графический контекст.

- [**SheetRender.toImage(int pageIndex, Graphics g, float x, float y)**](https://reference.aspose.com/cells/javascript-cpp/sheetrender/#toImage-number-)
- [**SheetRender.toImage(int pageIndex, Graphics g, float x, float y, float width, float height)**](https://reference.aspose.com/cells/javascript-cpp/sheetrender/#toImage-number-)

{{% /alert %}}

Следующий код демонстрирует, как использовать Aspose.Cells для рендеринга рабочего листа в графический контекст. После выполнения кода он распечатает весь рабочий лист и заполнит оставшееся пустое пространство синим цветом в графическом контексте и сохранит изображение как файл **OutputImage_out_.png**. Вы можете использовать любой исходный файл Excel для тестирования этого кода. Также ознакомьтесь с комментариями внутри кода для лучшего понимания.

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
