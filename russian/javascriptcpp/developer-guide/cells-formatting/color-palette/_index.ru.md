---
title: Как использовать цветовую палитру
linktitle: Как использовать цветовую палитру
type: docs
weight: 80
url: /ru/javascript-cpp/excel-color-palette/
description: JavaScript код для добавления пользовательских цветов в палитру и использования цветовой палитры Excel с Aspose.Cells for JavaScript через C++.
keywords: JavaScript добавляет пользовательские цвета в палитру, программное управление палитрой цветов Excel, как программно использовать палитру в рабочей книге, JavaScript как использовать палитру цветов в Excel
---

## **Цвета и палитра**

Палитра - это количество цветов, доступных для использования при создании изображения. Использование стандартной палитры в презентации позволяет пользователю создавать однородный вид. Каждый файл Microsoft Excel (97-2003) имеет палитру из 56 цветов, которые могут быть применены к ячейкам, шрифтам, сеткам, графическим объектам, заливкам и линиям в диаграмме.

С помощью Aspose.Cells for JavaScript через C++, возможно использовать не только существующие цвета палитры, но и пользовательские. Перед использованием пользовательского цвета его нужно добавить в палитру.

Эта тема обсуждает, как добавить пользовательские цвета в палитру.

## **Добавление пользовательских цветов в палитру**

Aspose.Cells поддерживает 56-цветную палитру Microsoft Excel. Для использования пользовательского цвета, который не определен в палитре, добавьте цвет в палитру.

Aspose.Cells предоставляет класс [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook/), который представляет файл Microsoft Excel. Класс [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook/) содержит метод [**changePalette(Color, number)**](https://reference.aspose.com/cells/javascript-cpp/workbook/#changePalette-color-number-), принимающий следующие параметры для добавления пользовательского цвета и изменения палитры:

- Пользовательский цвет, пользовательский цвет, который будет добавлен.
- Индекс, индекс цвета в палитре, который будет заменен пользовательским цветом. Должен быть от 0 до 55.

Приведенный ниже пример добавляет пользовательский цвет (Орхидея) в палитру перед его применением к шрифту.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Color } = AsposeCells;

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
            const resultDiv = document.getElementById('result');
            const fileInput = document.getElementById('fileInput');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Checks if a color is in the palette for the spreadsheet.
            const isInPaletteBefore = workbook.isColorInPalette(Color.Orchid);
            console.log(isInPaletteBefore);
            resultDiv.innerHTML = `<p>Is Orchid in palette before change: ${isInPaletteBefore}</p>`;

            // Adding Orchid color to the palette at 55th index
            workbook.changePalette(Color.Orchid, 55);

            const isInPaletteAfter = workbook.isColorInPalette(Color.Orchid);
            console.log(isInPaletteAfter);
            resultDiv.innerHTML += `<p>Is Orchid in palette after change: ${isInPaletteAfter}</p>`;

            // Adding a new worksheet to the Excel object
            const i = workbook.worksheets.add();

            // Obtaining the reference of the newly added worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(i);

            // Accessing the "A1" cell from the worksheet
            const cell = worksheet.cells.get("A1");

            // Adding some value to the "A1" cell
            cell.putValue("Hello Aspose!");

            // Defining new Style object
            const styleObject = workbook.createStyle();
            // Setting the Orchid (custom) color to the font
            styleObject.font.color = workbook.colors[55];

            // Applying the style to the cell
            cell.style = styleObject;

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML += '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

{{% alert color="primary" %}}

Палитра может содержать только 56 цветов. Когда вы добавляете пользовательский цвет в палитру, палитра изменяется, и любой элемент в файле, отформатированный предыдущим цветом, изменяется. Поэтому при изменении палитры, пожалуйста, будьте очень осторожны. Более того, это ограничение только для формата файла XLS (Excel 97-2003), так как нет такого ограничения для форматов файлов XLSX или других более продвинутых форматов файлов MS Excel (2007/2010 или 2013).

{{% /alert %}}
