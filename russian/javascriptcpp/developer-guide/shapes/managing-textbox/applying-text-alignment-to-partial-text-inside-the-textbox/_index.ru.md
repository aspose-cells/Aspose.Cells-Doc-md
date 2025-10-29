---
title: Как применить/установить выравнивание текста в текстовом поле с помощью JavaScript через C++
linktitle: Применить/установить выравнивание текста для текстового поля
type: docs
weight: 20
url: /ru/javascript-cpp/applying-text-alignment-to-partial-text-inside-the-textbox/
description: Как применить/установить выравнивание текста в текстовом поле в Aspose.Cells for JavaScript через C++.
keywords: применить/установить выравнивание TextBox в листе Excel Aspose JavaScript через C++
---

Текстовые поля могут повысить выразительность наших документов и диаграмм, а применение разных выравниваний к разным частям TextBox может помочь выделить важные моменты для читателей. Но стандартное выравнивание TextBox не удовлетворяет все наши потребности. Для этого возможно потребуется настроить каждое TextBox под ваши требования. Если у вас немного объектов TextBox для настройки, это отлично. А если их много — это может стать проблемой. Не волнуйтесь, [Aspose.Cells](https://products.aspose.com/cells/) предоставляет API, который может помочь вам в этом.

Приведенный ниже образец кода применяет выравнивание текста к текстовому полю.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Add TextBox Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Utils } = AsposeCells;

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
            let workbook;

            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            const worksheet = workbook.worksheets.get(0);
            const shapes = worksheet.shapes;

            // add a TextBox
            const shape = shapes.addTextBox(2, 0, 2, 0, 50, 120);
            shape.text = "This is a test.";

            // set alignment
            shape.textHorizontalAlignment = AsposeCells.TextAlignmentType.Center;
            shape.textVerticalAlignment = AsposeCells.TextAlignmentType.Center;

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'result.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

Вы также можете изменить выравнивание текста внутри некоторого текста в фигуре TextBox с помощью соответствующего HTML текста. Следующий пример демонстрирует применение выравнивания текста внутри части текста в TextBox.

[исходный файл](SampleTextboxExcel2016.xlsx)

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells TextBox HTML Transfer Example</title>
    </head>
    <body>
        <h1>TextBox HTML Transfer Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, MsoDrawingType, Utils } = AsposeCells;

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

            // Load source workbook from the selected file
            const sourceWb = new Workbook(new Uint8Array(arrayBuffer));

            // Access the target textbox whose text is to be aligned
            const sourceTextBox = sourceWb.worksheets.get(0).shapes.get(0);

            // Create an object of the target workbook
            const destWb = new Workbook();

            // Access the first worksheet from the collection
            const _sheet = destWb.worksheets.get(0);

            // Create new textbox
            const _textBox = _sheet.shapes.addShape(MsoDrawingType.TextBox, 1, 0, 1, 0, 200, 200);

            // Use Html string from a template file textbox
            _textBox.htmlText = sourceTextBox.htmlText;

            // Save the workbook and provide download link
            const outputData = destWb.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Text box HTML copied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
