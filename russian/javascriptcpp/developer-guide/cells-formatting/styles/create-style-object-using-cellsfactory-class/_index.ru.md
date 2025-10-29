---
title: Создайте объект стиля с использованием класса CellsFactory.
linktitle: Создайте объект стиля с использованием класса CellsFactory.
description: Научитесь создавать объект стиля ячейки с помощью класса CellsFactory в Aspose.Cells for JavaScript через C++. Настройте внешний вид ячеек таблицы по необходимости.
keywords: Aspose.Cells, JavaScript через C++, электронная таблица, объект стиля, стиль ячейки, настройка
type: docs
weight: 70
url: /ru/javascript-cpp/create-style-object-using-cellsfactory-class/
---

## **Создайте объект стиля с использованием класса CellsFactory.**
Следующий пример кода создает объект [Style](https://reference.aspose.com/cells/javascript-cpp/style) с помощью класса [CellsFactory](https://reference.aspose.com/cells/javascript-cpp/cellsfactory) и устанавливает его как стиль по умолчанию для рабочей книги. Для просмотра результатов скачайте [выходной файл Excel](5115153.xlsx).


```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Create Workbook with Default Style</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, CellsFactory, BackgroundType, Color, Utils } = AsposeCells;

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
            // Create a Style object using CellsFactory class
            const cf = new CellsFactory();
            const st = cf.createStyle();

            // Set the Style fill color to Yellow
            st.pattern = BackgroundType.Solid;
            st.foregroundColor = Color.Yellow;

            // Create a workbook and set its default style using the created Style object
            const wb = new Workbook();
            wb.defaultStyle = st;

            // Save the workbook
            const outputData = wb.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created successfully. Click the download link to save the file.</p>';
        });
    </script>
</html>
```
