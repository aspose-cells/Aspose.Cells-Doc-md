---
title: Настройки границ
linktitle: Настройки границ
description: Как использовать библиотеку Aspose.Cells через JavaScript с использованием C++ для установки стиля границы и цвета ячеек. Регулируя ширину, стиль и цвет границы, вы получаете больший контроль над внешним видом ячеек.
keywords: Aspose.Cells, Настройки границы ячейки, JavaScript через C++, Толщина границы, Стиль границы, Цвет границы
type: docs
weight: 40
url: /ru/javascript-cpp/cells-border-settings/
---

## **Добавление границ в ячейки**

Microsoft Excel позволяет пользователям форматировать ячейки, добавляя границы. Тип границы зависит от её расположения. Например, верхняя граница добавляется к верхней стороне ячейки. Также можно изменить стиль линии и цвет границы.

С помощью Aspose.Cells for JavaScript через C++, разработчики могут добавлять границы и настраивать их внешний вид так же гибко, как в Microsoft Excel.

### **Добавление границ в ячейки**

Aspose.Cells предоставляет класс [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook), который представляет файл Microsoft Excel. Класс [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) содержит коллекцию [**worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--), позволяющую получить доступ к каждому листу в файле Excel. Лист представлен классом [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet). Класс [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) обеспечивает коллекцию [**cells**](https://reference.aspose.com/cells/javascript-cpp/cells). Каждый элемент коллекции [**cells**](https://reference.aspose.com/cells/javascript-cpp/cells) представляет объект класса [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell).

Aspose.Cells предоставляет свойство [**style**](https://reference.aspose.com/cells/javascript-cpp/cell/#style--) в классе [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell). [**style**](https://reference.aspose.com/cells/javascript-cpp/cell/#style-style-) используется для установки стиля форматирования ячейки. Класс [**Style**](https://reference.aspose.com/cells/javascript-cpp/style) предоставляет свойства для добавления границ к ячейкам.

#### **Добавление границ к ячейке**

Разработчики могут добавлять границы к ячейке, используя коллекцию [**borders**](https://reference.aspose.com/cells/javascript-cpp/style/#borders--) объекта [**Style**](https://reference.aspose.com/cells/javascript-cpp/style). Тип границы передается как индекс в коллекцию [**borders**](https://reference.aspose.com/cells/javascript-cpp/style/#borders--). Все типы границ предопределены в перечислении [**BorderType**](https://reference.aspose.com/cells/javascript-cpp/bordertype).

Перечисление границ

|**Типы границ**|**Описание**|
| :- | :- |
|BottomBorder|Линия нижней границы|
|DiagonalDown|Диагональная линия от верхнего левого до нижнего правого|
|DiagonalUp|Диагональная линия от нижнего левого до верхнего правого|
|LeftBorder|Линия левой границы|
|RightBorder|Линия правой границы|
|TopBorder|Линия верхней границы|

Коллекция [**borders**](https://reference.aspose.com/cells/javascript-cpp/style/#borders--) хранит все границы. Каждая граница в коллекции [**borders**](https://reference.aspose.com/cells/javascript-cpp/style/#borders--) представлена объектом [**Border**](https://reference.aspose.com/cells/javascript-cpp/border), который обеспечивает два свойства: [**color**](https://reference.aspose.com/cells/javascript-cpp/border/#color-color-) и [**lineStyle**](https://reference.aspose.com/cells/javascript-cpp/border/#lineStyle-cellbordertype-) для установки цвета линии границы и стиля соответственно.

Чтобы установить цвет линии границы, выберите цвет с помощью перечисления Color (часть JavaScript) и присвойте его свойству color объекта Border.

Стиль линии границы устанавливается выбором стиля линии из перечисления [**CellBorderType**](https://reference.aspose.com/cells/javascript-cpp/cellbordertype).

**Перечисление типов границ ячейки**

|**Стили линий**|**Описание**|
| :- | :- |
|DashDot|Тонкая пунктирная линия|
|DashDotDot|Тонкая штрих-пунктирная линия|
|Dashed|Пунктирная линия|
|Dotted|Точечная линия|
|Double|Двойная линия|
|Hair|Линия минимальной толщины|
|MediumDashDot|Средняя штрих-пунктирная линия|
|MediumDashDotDot|Средняя штрих-точечно-пунктирная линия|
|MediumDashed|Средняя пунктирная линия|
|None|Нет линии|
|Medium|Средняя линия|
|SlantedDashDot|Наклоненная средняя штрих-пунктирная линия|
|Thick|Толстая линия|
|Thin|Тонкая линия|
Выберите один из стилей линий и затем присвойте его свойству [**lineStyle**](https://reference.aspose.com/cells/javascript-cpp/border/#lineStyle-cellbordertype-) объекта [**Border**](https://reference.aspose.com/cells/javascript-cpp/border).

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Add Borders to A1 Cell Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell } = AsposeCells;

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
            // This example creates a new workbook and adds borders to cell A1.
            // No try/catch is used so errors propagate for testing.

            // Instantiating a Workbook object
            const workbook = new Workbook();

            // Obtaining the reference of the first (default) worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(0);

            // Accessing the "A1" cell from the worksheet
            const cell = worksheet.cells.get("A1");

            // Adding some value to the "A1" cell
            cell.value = "Visit Aspose!";

            // Create a style object
            const style = cell.style;

            // Setting the line style and color of the top border
            style.borders.get(AsposeCells.BorderType.TopBorder).lineStyle = AsposeCells.CellBorderType.Thick;
            style.borders.get(AsposeCells.BorderType.TopBorder).color = AsposeCells.Color.Black;

            // Setting the line style and color of the bottom border
            style.borders.get(AsposeCells.BorderType.BottomBorder).lineStyle = AsposeCells.CellBorderType.Thick;
            style.borders.get(AsposeCells.BorderType.BottomBorder).color = AsposeCells.Color.Black;

            // Setting the line style and color of the left border
            style.borders.get(AsposeCells.BorderType.LeftBorder).lineStyle = AsposeCells.CellBorderType.Thick;
            style.borders.get(AsposeCells.BorderType.LeftBorder).color = AsposeCells.Color.Black;

            // Setting the line style and color of the right border
            style.borders.get(AsposeCells.BorderType.RightBorder).lineStyle = AsposeCells.CellBorderType.Thick;
            style.borders.get(AsposeCells.BorderType.RightBorder).color = AsposeCells.Color.Black;

            // Apply the border styles to the cell
            cell.style = style;

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'book1.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and styled successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```

{{% alert color="primary" %}}
Следует одновременно устанавливать как стиль линии, так и цвет. Две диагональные линии границы должны иметь одинаковый стиль линии и цвет.
{{% /alert %}}

#### **Добавление границ для диапазона ячеек**

Также возможно добавлять границы к диапазону ячеек, а не только к одной ячейке. Для этого сначала создайте диапазон ячеек, вызвав метод [**createRange**](https://reference.aspose.com/cells/javascript-cpp/cells/#createRange-string-string-) коллекции [**cells**](https://reference.aspose.com/cells/javascript-cpp/cells). Он принимает следующие параметры:

- Первая строка, первая строка диапазона.
- Первый столбец, представляет первый столбец диапазона.
- Количество строк, количество строк в диапазоне.
- Количество столбцов, количество столбцов в диапазоне.

Метод [**createRange**](https://reference.aspose.com/cells/javascript-cpp/cells/#createRange-string-string-) возвращает объект [**Range**](https://reference.aspose.com/cells/javascript-cpp/range), который содержит указанный диапазон ячеек. Объект [**Range**](https://reference.aspose.com/cells/javascript-cpp/range) предоставляет метод [**outlineBorder**](https://reference.aspose.com/cells/javascript-cpp/range/#outlineBorder-bordertype-cellbordertype-cellscolor-), который принимает следующие параметры для добавления границы к диапазону ячеек:

- **Тип границы**, тип границы, выбранный из перечисления [**BorderType**](https://reference.aspose.com/cells/javascript-cpp/bordertype).
- **Стиль линии**, стиль линии границы, выбранный из перечисления [**CellBorderType**](https://reference.aspose.com/cells/javascript-cpp/cellbordertype).
- **Цвет**, цвет линии, выбранный из перечисления Color.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Create Workbook and Apply Borders</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, BorderType, CellBorderType, Color } = AsposeCells;

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
            // This example creates a new workbook, writes to A1, creates a range and applies borders, then offers the file for download.
            const workbook = new Workbook();

            const worksheet = workbook.worksheets.get(0);

            const cell = worksheet.cells.get("A1");

            cell.putValue("Hello World From Aspose");

            const range = worksheet.cells.createRange(0, 0, 1, 3);

            // Applying borders using property assignment conversions for setter methods
            range.outlineBorder = [BorderType.TopBorder, CellBorderType.Thick, Color.Blue];
            range.outlineBorder = [BorderType.BottomBorder, CellBorderType.Thick, Color.Blue];
            range.outlineBorder = [BorderType.LeftBorder, CellBorderType.Thick, Color.Blue];
            range.outlineBorder = [BorderType.RightBorder, CellBorderType.Thick, Color.Blue];

            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'book1.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and borders applied successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```
