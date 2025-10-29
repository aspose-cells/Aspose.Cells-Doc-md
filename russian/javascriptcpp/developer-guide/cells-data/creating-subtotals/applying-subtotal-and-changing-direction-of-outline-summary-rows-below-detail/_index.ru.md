---
title: Применение итоговой строки и изменение направления итоговых строк справа от детальной
type: docs
weight: 100
url: /ru/javascript-cpp/applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail/
description: Узнайте, как применять итоги и менять направление строк сводки оглавления под Таблицей с помощью скрипта Aspose.Cells for Java и API C++.
keywords: Применить итог, добавить итог, изменить направление строк аутлайна суммари снизу от детализации, изменить направление столбцов аутлайна суммари справа от детализации, создать итог и изменить направление строк аутлайна суммари снизу от детализации
---

{{% alert color="primary" %}}

Эта статья объяснит, как применить итоговую строку к данным и изменить направление итоговых строк ниже детали.

Вы можете применить итоговую строку к данным, используя метод [**Worksheet.cells.subtotal()**](https://reference.aspose.com/cells/javascript-cpp/cells/#subtotal-cellarea-number-consolidationfunction-numberarray-boolean-boolean-boolean-). Он принимает следующие параметры.

- **CellArea** - Диапазон, на котором применяется промежуточный итог
- **GroupBy** - Поле для группировки по нулевому индексу
- **Function** - Функция промежуточного итога
- **TotalList** - Массив смещений нулевого индекса, указывающий на поля, к которым добавляются итоги
- **Replace** - Указывает, нужно ли заменить текущие промежуточные итоги
- **Разрывы страниц** - Указывает, добавлять ли разрыв страницы между группами
- **SummaryBelowData** - Указывает, нужно ли добавить итоги ниже данных

Также можно управлять направлением сводных строк **Ниже строки деталей** , как показано на следующем скриншоте, используя свойство Worksheet.Outline.SummaryRowBelow. Вы можете открыть этот параметр в Microsoft Excel, используя **Данные > Контур > Настройки**

![todo:image_alt_text](1.png)

{{% /alert %}}

## Изображения исходных и выходных файлов

На следующем скриншоте показан исходный файл Excel, используемый в приведенном ниже образцовом коде, содержащий некоторые данные в столбцах A и B.

![todo:image_alt_text](2.png)

На следующем скриншоте показан выходной файл Excel, созданный образцовым кодом. Как видно, к диапазону A2:B11 было применено итого, и направление контура - сводные строки ниже деталей.

![todo:image_alt_text](3.png)

## JavaScript для применения итога и изменения направления строк сводки оглавления



```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Subtotal Example</title>
    </head>
    <body>
        <h1>Apply Subtotal Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, CellArea, ConsolidationFunction, Utils } = AsposeCells;

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

            // Create workbook from uploaded Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Get the Cells collection in the first worksheet
            const cells = worksheet.cells;

            // Create a cellarea i.e., A2:B11
            const ca = CellArea.createCellArea("A2", "B11");

            // Apply subtotal, the consolidation function is Sum and it will applied to Second column (B) in the list
            cells.subtotal(ca, 0, ConsolidationFunction.Sum, [1], true, false, true);

            // Set the direction of outline summary
            worksheet.outline.summaryRowBelow = true;

            // Save the excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Subtotal applied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
