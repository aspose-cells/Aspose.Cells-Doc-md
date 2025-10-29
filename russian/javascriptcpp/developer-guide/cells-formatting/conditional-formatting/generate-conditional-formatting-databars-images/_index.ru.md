---
title: Генерация изображений полос данных условного форматирования
linktitle: Генерация изображений полос данных условного форматирования
description: Aspose.Cells — это библиотека на JavaScript для работы с файлами таблиц. Она поддерживает генерацию условных форматированных полос данных и изображений, позволяя пользователям настраивать отображение таблицы в зависимости от значения ячеек. В этой статье будет подробно рассказано, как использовать библиотеку Aspose.Cells для создания условных форматированных полос данных и изображений.
keywords: Aspose.Cells, условное форматирование, полосы данных, изображения, таблицы, JavaScript через C++
type: docs
weight: 40
url: /ru/javascript-cpp/generate-conditional-formatting-databars-images/
---

{{% alert color="primary" %}}

Иногда вам может потребоваться создать изображения условного форматирования панелей данных. Вы можете использовать метод Aspose.Cells [**DataBar.toImage(Cell, ImageOrPrintOptions)**](https://reference.aspose.com/cells/javascript-cpp/databar/#toImage-cell-imageorprintoptions-) для создания этих изображений. В этой статье показано, как создать изображение панели данных с помощью Aspose.Cells.

{{% /alert %}}

Следующий пример кода создает изображение DataBar для ячейки C1. Он сначала обращается к объекту условного форматирования ячейки, затем через этот объект — к [**DataBar**](https://reference.aspose.com/cells/javascript-cpp/databar) объекту и использует его метод [**DataBar.toImage(Cell, ImageOrPrintOptions)**](https://reference.aspose.com/cells/javascript-cpp/databar/#toImage-cell-imageorprintoptions-) для генерации изображения ячейки. В конце он сохраняет изображение на диск.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Generate DataBar Image</title>
    </head>
    <body>
        <h1>Generate DataBar Image Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell, Utils } = AsposeCells;

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

            // Creating a workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access the cell which contains conditional formatting databar
            const cell = worksheet.cells.get("C1");

            // Create and get the conditional formatting of the worksheet
            const idx = worksheet.conditionalFormattings.add();
            const fcc = worksheet.conditionalFormattings.get(idx);
            fcc.addCondition(AsposeCells.FormatConditionType.DataBar);
            fcc.addArea(AsposeCells.CellArea.createCellArea("C1", "C4"));

            // Access the conditional formatting databar
            const dbar = fcc.get(0).dataBar;

            // Create image or print options
            const opts = new AsposeCells.ImageOrPrintOptions();
            opts.imageType = AsposeCells.ImageType.Png;

            // Get the image bytes of the databar
            const imgBytes = dbar.toImage(cell, opts);

            // Create a blob and provide download link
            const blob = new Blob([imgBytes], { type: "image/png" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputGenerateDatabarImage.png';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Generated DataBar Image';

            document.getElementById('result').innerHTML = '<p style="color: green;">Image generated successfully! Click the download link to save the PNG file.</p>';
        });
    </script>
</html>
```
