---
title: Получить адрес, смещение, количество ячеек, охват всей колонки и всей строки диапазона с помощью JavaScript через C++
linktitle: Получить адрес ячейки, количество ячеек смещение, весь столбец и вся строка диапазона
type: docs
weight: 330
url: /ru/javascript-cpp/get-address-cell-count-offset-entire-column-and-entire-row-of-the-range/
---

## **Возможные сценарии использования**
Aspose.Cells for JavaScript через C++ предоставляет объект Range, который имеет различные вспомогательные методы для облегчения работы с диапазонами Excel. В этой статье иллюстрируется использование следующих методов или свойств объекта Range.

- **Адрес**

Получает адрес диапазона.

- **Количество ячеек**

Получает общее количество ячеек в диапазоне.

- **Смещение**

Получает диапазон смещения.

- **Весь столбец**

Получает объект Range, представляющий весь столбец (или столбцы), содержащий указанный диапазон.

- **Вся строка**

Получает объект Range, представляющий всю строку (или строки), содержащий указанный диапазон.

## **Получить адрес, количество ячеек, смещение, весь столбец и всю строку диапазона**
Приведенный ниже образец кода объясняет использование методов и свойств, описанных выше. Пожалуйста, обратитесь к выводу консоли приведенного ниже кода в качестве справки.

## **Образец кода**
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Example Title</h1>
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
            // This example creates ranges on a new empty workbook and prints info to the page.
            const resultEl = document.getElementById('result');
            resultEl.innerHTML = '';

            // Create empty workbook.
            const wb = new Workbook();

            // Access first worksheet.
            const ws = wb.worksheets.get(0);

            // Create range A1:B3.
            console.log("Creating Range A1:B3\n");
            let rng = ws.cells.createRange("A1:B3");

            // Print range address and cell count.
            const lines = [];
            lines.push("Range Address: " + rng.address);
            lines.push("Range row Count: " + rng.rowCount);
            lines.push("Range column Count: " + rng.columnCount);

            // Formatting console output.
            lines.push("----------------------");
            lines.push("");

            // Create range A1.
            console.log("Creating Range A1\n");
            rng = ws.cells.createRange("A1");

            // Print range offset, entire column and entire row.
            lines.push("Offset: " + rng.offset(2, 2).address);
            lines.push("Entire Column: " + rng.entireColumn.address);
            lines.push("Entire Row: " + rng.entireRow.address);

            // Formatting console output.
            lines.push("----------------------");
            lines.push("");

            // Display results
            resultEl.innerHTML = '<pre>' + lines.join("\n") + '</pre>';
        });
    </script>
</html>
```

## **Вывод в консоль**
{{< highlight javascript >}}
 Creating Range A1:B3

Range Address: A1:B3

Cell Count: 6

\----------------------

Creating Range A1

Offset: C3

Entire Column: A:A

Entire Row: 1:1

\----------------------

{{< /highlight >}}
