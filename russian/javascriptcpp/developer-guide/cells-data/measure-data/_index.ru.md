---
title: Измерьте ширину и высоту значения ячейки в единицах пикселей
linktitle: Измерьте размер
type: docs
weight: 260
url: /ru/javascript-cpp/calculate-the-width-and-height-of-the-cell-value-in-unit-of-pixels/
description: Научитесь измерять ширину и высоту значения ячейки в пикселях через скрипт Aspose.Cells for Java на C++.
keywords: Измерить ширину значения ячейки в пикселях на JavaScript через C++, измерить высоту значения ячейки в пикселях на JavaScript через C++, получить ширину значения ячейки в пикселях на JavaScript через C++, получить высоту значения ячейки в пикселях на JavaScript через C++
---

{{% alert color="primary" %}}  

Иногда вам нужно рассчитать ширину и высоту значения ячейки, чтобы поместить значение внутри ячейки. Aspose.Cells предоставляет [**Cell.widthOfValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#widthOfValue--) и [**Cell.heightOfValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#heightOfValue--) методы для этой цели. Используя эти методы, вы можете рассчитать ширину и высоту значения ячейки, а затем установить ширину столбца и высоту строки этой ячейки соответственно, и это позволит автоматически масштабировать или вписать значение ячейки внутри ячейки.  

Или же вы можете [автоматически подгонять строки и столбцы вашей ячейки или диапазона ячеек](/cells/ru/javascript-cpp/autofit-rows-and-columns/) с помощью API Aspose.Cells.  

{{% /alert %}}  

Следующий код объясняет использование методов [**Cell.widthOfValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#widthOfValue--) и [**Cell.heightOfValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#heightOfValue--).  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Get Cell Size Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;

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

            // Create or load workbook
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access cell B2 and add some value inside it
            const cell = worksheet.cells.get("B2");
            cell.value = "Welcome to Aspose!";

            // Enlarge its font to size 16
            const style = cell.style;
            style.font.size = 16;
            cell.style = style;

            // Calculate the width and height of the cell value in unit of pixels
            const widthOfValue = cell.widthOfValue;
            const heightOfValue = cell.heightOfValue;

            // Print both values to the page
            document.getElementById('result').innerHTML = `<p>Width of Cell Value: ${widthOfValue}</p><p>Height of Cell Value: ${heightOfValue}</p>`;

            // Set the row height and column width to adjust/fit the cell value inside cell
            worksheet.cells.setColumnWidthPixel(1, widthOfValue);
            worksheet.cells.setRowHeightPixel(1, heightOfValue);

            // Save the output excel file and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';
        });
    </script>
</html>
```


## **Продвинутые темы**  
- [Получить ширину текста значения ячейки](/cells/ru/javascript-cpp/get-text-width-of-cell-value/)
