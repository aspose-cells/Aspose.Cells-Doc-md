---
title: Обнаружение пустых листов с помощью JavaScript через C++
linktitle: Обнаружение пустых рабочих листов
type: docs
weight: 410
url: /ru/javascript-cpp/detecting-empty-worksheets/
description: Эта статья показывает код, объясняющий, как программно обнаруживать пустые листы Excel с помощью JavaScript API с библиотекой C++.
keywords: обнаружение пустого листа JavaScript через C++, поиск пустого листа Excel JavaScript через C++
---

## **Проверка заполненных ячеек**

Листы могут иметь один или более заполненных ячеек со значениями, где значение может быть простым (текст, число, дата/время) или формулой или значением на основе формулы. В таком случае легко определить, является ли лист пустым или нет. Все, что нужно проверить — это свойства [**Cells.maxDataRow**](https://reference.aspose.com/cells/javascript-cpp/cells/#maxDataRow--) или [**Cells.maxDataColumn**](https://reference.aspose.com/cells/javascript-cpp/cells/#maxDataColumn--). Если эти свойства возвращают ноль или положительные значения, это означает, что одна или более ячеек заполнены; однако, если любое из этих свойств возвращает -1, это говорит о том, что ни одна ячейка не заполнена на данном листе.

{{% alert color="primary" %}}

Коллекции строк и столбцов имеют нумерацию с нуля; следовательно, ячейка в строке 0 и столбце 0 — это первая ячейка в листе, то есть A1.

{{% /alert %}}

## **Проверка пустых инициализированных ячеек**

Все ячейки, содержащие значения, автоматически инициализируются; однако существует вероятность, что лист содержит ячейки только с форматированием. В таком случае свойства [**Cells.maxDataRow**](https://reference.aspose.com/cells/javascript-cpp/cells/#maxDataRow--) или [**Cells.maxDataColumn**](https://reference.aspose.com/cells/javascript-cpp/cells/#maxDataColumn--) вернут -1, что указывает на отсутствие заполненных значений, но инициализированные ячейки из-за форматирования определить этим методом нельзя. Чтобы проверить, есть ли в листе пустые инициализированные ячейки, рекомендуется использовать метод `Enumerator.MoveNext()` на полученном из коллекции [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells) перечислителе. Если метод `Enumerator.MoveNext()` возвращает **true**, это означает, что на листе есть одна или более инициализированных ячеек.

## **Проверка фигур**

Возможно, что на листе отсутствуют заполненные ячейки; при этом, он может содержать фигуры и объекты, такие как элементы управления, диаграммы, изображения и так далее. Если нужно проверить, содержит ли лист фигуры, можно сделать это, проверяя свойство [**ShapeCollection.count**](https://reference.aspose.com/cells/javascript-cpp/shapecollection/#count--). Любое положительное значение свидетельствует о наличии фигур на листе.

## **Пример программирования**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Check Non-Empty Worksheets Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
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
            const resultDiv = document.getElementById('result');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const book = new Workbook(new Uint8Array(arrayBuffer));

            const messages = [];

            // Loop over all worksheets in the workbook
            for (let i = 0; i < book.worksheets.count; i++) {
                const sheet = book.worksheets.get(i);
                // Check if worksheet has populated cells
                if (sheet.cells.maxDataRow !== -1) {
                    messages.push(`${sheet.name} is not empty because one or more cells are populated`);
                }
                // Check if worksheet has shapes
                else if (sheet.shapes.count > 0) {
                    messages.push(`${sheet.name} is not empty because there are one or more shapes`);
                }
                // Check if worksheet has empty initialized cells
                else {
                    const range = sheet.cells.maxDisplayRange;
                    const rangeIterator = range.getEnumerator();
                    if (rangeIterator.moveNext()) {
                        messages.push(`${sheet.name} is not empty because one or more cells are initialized`);
                    }
                }
            }

            if (messages.length) {
                resultDiv.innerHTML = '<ul>' + messages.map(m => `<li>${m}</li>`).join('') + '</ul>';
            } else {
                resultDiv.innerHTML = '<p style="color: green;">No non-empty worksheets found.</p>';
            }
        });
    </script>
</html>
```
