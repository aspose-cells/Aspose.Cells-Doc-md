---
title: Рассчитать коэффициент масштабирования страниц с помощью JavaScript через C++
linktitle: Вычислить масштабирование настройки страницы
type: docs
weight: 300
url: /ru/javascript-cpp/calculate-page-setup-scaling-factor/
description: В этой статье приведен пример кода, объясняющий, как использовать JavaScript API через C++ для расчета коэффициента масштабирования страницы с помощью функции «Подогнать под n страниц по ширине и m по высоте» в программе Excel.
keywords: Подогнать под n страниц по ширине и m по высоте JavaScript для Excel через C++, рассчитать коэффициент масштабирования страницы JavaScript через C++
---

{{% alert color="primary" %}}

При установке масштаба оформления страницы с помощью опции **подогнать на n страниц в ширину и m страниц по высоте** Microsoft Excel вычисляет коэффициент масштабирования. Вы можете вычислить то же самое, используя свойство [**SheetRender.pageScale**](https://reference.aspose.com/cells/javascript-cpp/sheetrender/#pageScale--). Оно возвращает число с плавающей точкой, которое можно преобразовать в процент. Например, если возвращается 0.5, это означает масштаб 50%.

{{% /alert %}}

В следующем примере кода показано, как рассчитать масштабный коэффициент настроек страницы, используя свойство [**SheetRender.pageScale**](https://reference.aspose.com/cells/javascript-cpp/sheetrender/#pageScale--).

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Page Scale</title>
    </head>
    <body>
        <h1>Page Scale Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, SheetRender, ImageOrPrintOptions, PaperSizeType, Utils } = AsposeCells;

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

            // Opening the Excel file through the file stream
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Put some data in these cells
            worksheet.cells.get("A4").putValue("Test");
            worksheet.cells.get("S4").putValue("Test");

            // Set paper size
            worksheet.pageSetup.paperSize = PaperSizeType.PaperA4;

            // Set fit to pages wide as 1
            worksheet.pageSetup.fitToPagesWide = 1;

            // Calculate page scale via sheet render
            const sr = new SheetRender(worksheet, new ImageOrPrintOptions());

            // Convert page scale double value to percentage
            const strPageScale = (sr.pageScale * 100).toFixed(0) + "%";

            // Write the page scale value
            document.getElementById('result').innerHTML = `<p>Page Scale: ${strPageScale}</p>`;
            console.log(strPageScale);
        });
    </script>
</html>
```
