---
title: Форматирование ячеек с помощью JavaScript через C++
description: Узнайте, как форматировать и стилизовать ячейки в Aspose.Cells for JavaScript через C++, включая форматирование чисел, даты, стили шрифтов и другие параметры стилей ячеек. Наше руководство поможет вам создавать привлекательные и профессиональные таблицы.
keywords: Aspose.Cells for JavaScript через C++, форматирование ячеек, стилизация, форматирование чисел, форматирование дат, стиль шрифта, параметры стилей ячеек, таблицы, создание, профессиональный внешний вид, форматировать строки и столбцы.
linktitle: Форматировать ячейки
type: docs
weight: 120
url: /ru/javascript-cpp/cells-formatting/
---

## **Введение**

{{% alert color="primary" %}}

Aspose.Cells предоставляет методы [**style**](https://reference.aspose.com/cells/javascript-cpp/cell/#style--) и [**style**](https://reference.aspose.com/cells/javascript-cpp/cell/#style-style-) класса [Cell](https://reference.aspose.com/cells/javascript-cpp/cell), используемые для получения/установки стиля форматирования ячейки. Aspose.Cells также предоставляет класс [**Style**](https://reference.aspose.com/cells/javascript-cpp/style).

{{% /alert %}}

## **Как форматировать ячейки с помощью методов стиля**

Применить различные виды стилей форматирования на ячейки для установки цветов фона или переднего плана, границ, шрифтов, горизонтальных и вертикальных выравниваний, уровня отступа, направления текста, угла поворота и многое другое.

### **Как использовать методы стиля**

Если разработчикам нужно применять разные стили форматирования к разным ячейкам, то лучше получить [**Style**](https://reference.aspose.com/cells/javascript-cpp/style) ячейки с помощью метода [**Cell.style**](https://reference.aspose.com/cells/javascript-cpp/cell/#style--), указать атрибуты стиля и затем применить форматирование с помощью метода [**Cell.style**](https://reference.aspose.com/cells/javascript-cpp/cell/#style-style-). Ниже приведён пример, демонстрирующий этот подход для различных форматов ячейки.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Styling Example</h1>
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

            // Instantiate or load workbook
            let workbook;
            if (fileInput.files && fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Obtaining the reference of the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Accessing the "A1" cell from the worksheet
            const cell = worksheet.cells.get("A1");

            // Adding some value to the "A1" cell
            cell.value = "Hello Aspose!";

            // Defining a Style object
            let style;

            // Get the style from A1 cell
            style = cell.style;

            // Setting the vertical alignment
            style.verticalAlignment = AsposeCells.TextAlignmentType.Center;

            // Setting the horizontal alignment
            style.horizontalAlignment = AsposeCells.TextAlignmentType.Center;

            // Setting the font color of the text
            style.font.color = AsposeCells.Color.Green;

            // Setting to shrink according to the text contained in it
            style.shrinkToFit = true;

            // Setting the bottom border color to red
            style.borders.get(AsposeCells.BorderType.BottomBorder).color = AsposeCells.Color.Red;

            // Setting the bottom border type to medium
            style.borders.get(AsposeCells.BorderType.BottomBorder).lineStyle = AsposeCells.CellBorderType.Medium;

            // Applying the style to A1 cell
            cell.style = style;

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'book1.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

### **Как использовать объект стиля для форматирования различных ячеек**

Если разработчикам нужно применять одинаковый стиль оформления к разным ячейкам, они могут использовать объект [**Style**](https://reference.aspose.com/cells/javascript-cpp/style). Следуйте приведённым ниже шагам для использования объекта [**Style**](https://reference.aspose.com/cells/javascript-cpp/style):

1. Добавьте объект [**Style**](https://reference.aspose.com/cells/javascript-cpp/style), вызвав его метод [**createStyle()**](https://reference.aspose.com/cells/javascript-cpp/workbook/#createStyle--) класса [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)
2. Получите доступ к новосозданному объекту [**Style**](https://reference.aspose.com/cells/javascript-cpp/style)
3. Установите желаемые свойства/атрибуты объекта [**Style**](https://reference.aspose.com/cells/javascript-cpp/style) для применения нужных настроек форматирования
4. Назначьте сконфигурированный объект [**Style**](https://reference.aspose.com/cells/javascript-cpp/style) нужным ячейкам

Этот подход может значительно повысить эффективность ваших приложений и сэкономить память.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Create Workbook and Style Cells</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, TextAlignmentType, Color, BorderType, CellBorderType } = AsposeCells;

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
            // Instantiate a new Workbook
            const workbook = new Workbook();

            // Add a new worksheet to the workbook
            const i = workbook.worksheets.add();

            // Obtain the newly added worksheet by index
            const worksheet = workbook.worksheets.get(i);

            // Access cell A1
            const cell = worksheet.cells.get("A1");

            // Set value of A1
            cell.value = "Hello Aspose!";

            // Create a new style
            const style = workbook.createStyle();

            // Set vertical and horizontal alignment
            style.verticalAlignment = TextAlignmentType.Center;
            style.horizontalAlignment = TextAlignmentType.Center;

            // Set font color
            style.font.color = Color.Green;

            // Shrink to fit
            style.shrinkToFit = true;

            // Set bottom border color and style
            style.borders.get(BorderType.BottomBorder).color = Color.Red;
            style.borders.get(BorderType.BottomBorder).lineStyle = CellBorderType.Medium;

            // Apply style to A1
            cell.style = style;

            // Apply same style to B1, C1, D1
            worksheet.cells.get("B1").style = style;
            worksheet.cells.get("C1").style = style;
            worksheet.cells.get("D1").style = style;

            // Save workbook to XLS format and provide download link
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

### **Как использовать предопределенные стили Microsoft Excel 2007**

Если вам необходимо применить различные стили форматирования для Microsoft Excel 2007, примените стили с использованием API Aspose.Cells. Приведен пример, демонстрирующий этот подход к применению предопределенного стиля к ячейке.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Create Workbook and Set Cell Style Example</h1>
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
            // Instantiate a new Workbook.
            const workbook = new Workbook();

            // Create a style object.
            const style = workbook.createStyle();

            // Access the first worksheet in the workbook
            const worksheet = workbook.worksheets.get(0);

            // Access cell A1
            const cell = worksheet.cells.get("A1");

            // Input a value to A1 cell.
            cell.putValue("Test");

            // Apply the style to the cell.
            cell.style = style;

            // Saving the Excel 2007 file.
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'book1.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```



## **Как форматировать выбранные символы в ячейке**

Работа со настройками шрифта объясняет, как форматировать текст в ячейках, но это объясняет только, как форматировать весь содержимое ячейки. Что, если вы хотите отформатировать только выбранные символы?

Это также поддерживается в Aspose.Cells. В этой теме объясняется, как эффективно использовать эту функцию.

### **Как форматировать выбранные символы**

Aspose.Cells предоставляет класс [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook), который представляет файл Microsoft Excel. Класс [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) содержит коллекцию [**worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--), которая позволяет получать доступ к каждому листу Excel. Лист Excel представлен классом [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet). Класс [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) предоставляет коллекцию [**cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--). Каждый элемент коллекции [**cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--) представляет объект класса [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell).

Класс [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell) предоставляет метод [**characters(number, number)**](https://reference.aspose.com/cells/javascript-cpp/cell/#characters-number-number-), который имеет следующие параметры для выбора диапазона символов внутри ячейки:

- **Индекс начала**, индекс символа, с которого начинается выбор.
- **Количество символов**, количество выбираемых символов.

Метод [**characters(number, number)**](https://reference.aspose.com/cells/javascript-cpp/cell/#characters-number-number-) возвращает экземпляр класса [**FontSetting**](https://reference.aspose.com/cells/javascript-cpp/fontsetting), что позволяет разработчикам форматировать символы аналогично ячейке, как показано в примере кода ниже. В выходном файле, в ячейке A1, слово 'Visit' будет отформатировано шрифтом по умолчанию, а 'Aspose!' — жирным и синим цветом.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
        <meta charset="utf-8" />
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

            // If a file is provided, open it; otherwise create a new workbook
            let workbook;
            if (fileInput.files && fileInput.files.length > 0) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Obtaining the reference of the first (default) worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(0);

            // Accessing the "A1" cell from the worksheet
            const cell = worksheet.cells.get("A1");

            // Adding some value to the "A1" cell
            cell.value = "Visit Aspose!";

            // Setting the font of selected characters to bold and color to blue
            const charRange = cell.characters(6, 7);
            charRange.font.isBold = true;
            charRange.font.color = AsposeCells.Color.Blue;

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'book1.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

{{% alert color="primary" %}}

Если вы заинтересованы в форматировании части богатого текста в ячейке, используйте методы [**Cell.characters**](https://reference.aspose.com/cells/javascript-cpp/cell/#characters--) и [**Cell.characters**](https://reference.aspose.com/cells/javascript-cpp/cell/#characters-fontsettingarray-). Метод [**Cell.characters**](https://reference.aspose.com/cells/javascript-cpp/cell/#characters--) предназначен для доступа к частям текста, а затем исправления могут выполняться с помощью метода [**Cell.characters**](https://reference.aspose.com/cells/javascript-cpp/cell/#characters-fontsettingarray-), в то время как метод **Get** возвращает массив объектов [**FontSetting**](https://reference.aspose.com/cells/javascript-cpp/fontsetting), которые можно редактировать для задания различных свойств, таких как имя шрифта, цвет шрифта, жирность и т. д., а **Set** можно использовать для применения изменений.

{{% /alert %}}

## **Как форматировать строки и столбцы**

Иногда разработчику требуется применить одно и то же форматирование на строки или столбцы. Применение форматирования к ячейкам одну за другой часто занимает больше времени и не является хорошим решением.
Для решения этой проблемы Aspose.Cells предоставляет простой и быстрый способ, который подробно рассматривается в данной статье.

### **Форматирование строк и столбцов**

Aspose.Cells предоставляет класс [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook), который представляет файл Microsoft Excel. Класс [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) содержит коллекцию [**worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--), которая позволяет получать доступ к каждому листу Excel. Лист Excel представлен классом [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet). Класс [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) предоставляет коллекцию [**cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--). Коллекция [**cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--) содержит коллекцию [**rows**](https://reference.aspose.com/cells/javascript-cpp/cells/#rows--).

### **Как форматировать строку**

Каждый элемент коллекции [**rows**](https://reference.aspose.com/cells/javascript-cpp/cells/#rows--) представляет объект [**Row**](https://reference.aspose.com/cells/javascript-cpp/row). Объект [**Row**](https://reference.aspose.com/cells/javascript-cpp/row) предлагает метод [**applyStyle(Style, StyleFlag)**](https://reference.aspose.com/cells/javascript-cpp/row/#applyStyle-style-styleflag-), используемый для установки форматирования строки. Для применения одинакового форматирования к строке используйте объект [**Style**](https://reference.aspose.com/cells/javascript-cpp/style). Ниже показаны шаги, как это сделать.

1. Добавьте объект [**Style**](https://reference.aspose.com/cells/javascript-cpp/style) в класс [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook), вызвав его метод [**createStyle()**](https://reference.aspose.com/cells/javascript-cpp/workbook/#createStyle--).
2. Установите свойства объекта [**Style**](https://reference.aspose.com/cells/javascript-cpp/style) для применения настроек форматирования.
3. Включите соответствующие атрибуты для объекта [**StyleFlag**](https://reference.aspose.com/cells/javascript-cpp/styleflag).
4. Назначьте сконфигурированный объект [**Style**](https://reference.aspose.com/cells/javascript-cpp/style) объекту [**Row**](https://reference.aspose.com/cells/javascript-cpp/row).

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
            // Instantiating a Workbook object
            const workbook = new Workbook();

            // Obtaining the reference of the first (default) worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(0);

            // Adding a new Style to the styles
            const style = workbook.createStyle();

            // Setting the vertical alignment of the text in the "A1" cell
            style.verticalAlignment = AsposeCells.TextAlignmentType.Center;

            // Setting the horizontal alignment of the text in the "A1" cell
            style.horizontalAlignment = AsposeCells.TextAlignmentType.Center;

            // Setting the font color of the text in the "A1" cell
            style.font.color = AsposeCells.Color.Green;

            // Shrinking the text to fit in the cell
            style.shrinkToFit = true;

            // Setting the bottom border color of the cell to red
            style.borders.get(AsposeCells.BorderType.BottomBorder).color = AsposeCells.Color.Red;

            // Setting the bottom border type of the cell to medium
            style.borders.get(AsposeCells.BorderType.BottomBorder).lineStyle = AsposeCells.CellBorderType.Medium;

            // Creating StyleFlag
            const styleFlag = new AsposeCells.StyleFlag();
            styleFlag.horizontalAlignment = true;
            styleFlag.verticalAlignment = true;
            styleFlag.shrinkToFit = true;
            styleFlag.borders = true;
            styleFlag.fontColor = true;

            // Accessing a row from the Rows collection
            const row = worksheet.cells.rows.get(0);

            // Assigning the Style object to the Style property of the row
            row.applyStyle(style, styleFlag);

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'book1.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

### **Как форматировать столбец**

Коллекция [**cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--) также предоставляет коллекцию [**columns**](https://reference.aspose.com/cells/javascript-cpp/cells/#columns--). Каждый элемент в коллекции [**columns**](https://reference.aspose.com/cells/javascript-cpp/cells/#columns--) представляет объект [**Column**](https://reference.aspose.com/cells/javascript-cpp/column). Аналогично объекту [**Row**](https://reference.aspose.com/cells/javascript-cpp/row), объект [**Column**](https://reference.aspose.com/cells/javascript-cpp/column) также предлагает метод [**applyStyle(Style, StyleFlag)**](https://reference.aspose.com/cells/javascript-cpp/row/#applyStyle-style-styleflag-) для форматирования столбца.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Style and Column Apply Example</h1>
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
            // Instantiate a new Workbook
            const workbook = new Workbook();

            // Obtain the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Add a new Style to the styles
            const style = workbook.createStyle();

            // Set vertical and horizontal alignment
            style.verticalAlignment = AsposeCells.TextAlignmentType.Center;
            style.horizontalAlignment = AsposeCells.TextAlignmentType.Center;

            // Set font color
            style.font.color = AsposeCells.Color.Green;

            // Shrink to fit
            style.shrinkToFit = true;

            // Set bottom border color and style
            style.borders.get(AsposeCells.BorderType.BottomBorder).color = AsposeCells.Color.Red;
            style.borders.get(AsposeCells.BorderType.BottomBorder).lineStyle = AsposeCells.CellBorderType.Medium;

            // Create and configure StyleFlag
            const styleFlag = new AsposeCells.StyleFlag();
            styleFlag.horizontalAlignment = true;
            styleFlag.verticalAlignment = true;
            styleFlag.shrinkToFit = true;
            styleFlag.borders = true;
            styleFlag.fontColor = true;

            // Access first column and apply style
            const column = worksheet.cells.getColumns().get(0);
            column.applyStyle(style, styleFlag);

            // Save the workbook and provide download link
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'book1.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Style applied to column successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **Продвинутые темы**
- [Настройки выравнивания](/cells/ru/javascript-cpp/cells-alignment-settings/)
- [Настройки границ](/cells/ru/javascript-cpp/cells-border-settings/)
- [Установить условные форматы для файлов Excel и ODS.](/cells/ru/javascript-cpp/conditional-formatting/)
- [Темы и цвета Excel](/cells/ru/javascript-cpp/excel-themes-and-colors/)
- [Настройки заливки](/cells/ru/javascript-cpp/cells-fill-settings/)
- [Настройки шрифта](/cells/ru/javascript-cpp/cells-font-settings/)
- [Форматирование ячеек листа в книге Excel](/cells/ru/javascript-cpp/format-worksheet-cells-in-a-workbook/)
- [Реализация системы дат 1904 года](/cells/ru/javascript-cpp/implement-1904-date-system/)
- [Объединение и разъединение ячеек](/cells/ru/javascript-cpp/merging-and-unmerging-cells/)
- [Настройки чисел](/cells/ru/javascript-cpp/cells-number-settings/)
- [Получение и установка стиля ячеек](/cells/ru/javascript-cpp/evaluating-cell-getstyle-and-setstyle-methods-against-cell-style-property/)
