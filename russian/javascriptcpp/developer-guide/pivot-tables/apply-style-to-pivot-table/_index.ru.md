---
title: Применение стилей к сводным таблицам в Aspose.Cells for JavaScript via C++
linktitle: Применение стилей к сводным таблицам в Aspose.Cells for JavaScript via C++
description: Узнайте, как применять встроенные и пользовательские стили к сводным таблицам в Aspose.Cells for JavaScript via C++, включая устаревшие автоформаты XLS, современные именованные стили Excel 2007+, пользовательские стили сводных таблиц и сокращенный способ FormatAll.
keywords: Aspose.Cells for JavaScript via C++ стиль сводной таблицы, PivotTableStyleType, AutoFormatType, FormatAll, пользовательский стиль, PivotTableStyleName, TableStyles
type: docs
weight: 200
url: /ru/javascript-cpp/apply-style-to-pivot-table/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells поддерживает применение как устаревших автоформатов сводных таблиц (предназначенных для файлов `.xls`), так и современных именованных или пользовательских стилей сводных таблиц (предназначенных для файлов `.xlsx`, `.xlsm` и `.xlsb`). Выбор API зависит от формата файла, в который сохраняется рабочая книга, а не от формата, из которого она была загружена.
{{% /alert %}}

## **Введение**
Aspose.Cells предоставляет два параллельных API для работы со стилями сводных таблиц. Выбор между ними определяется форматом файла, в который вы сохраняете рабочую книгу, а не форматом, из которого вы её загружаете. Рабочая книга, загруженная из файла `.xls`, может быть повторно сохранена как `.xlsx`; в этом случае применяется современный API стилей, а не устаревший.
- `pivotTable.pivotTableStyleType` выбирает один из встроенных именованных стилей (светлые и тёмные темы, включая стили, добавленные в Excel 2017). Эти предустановки доступны только для чтения.
- `pivotTable.pivotTableStyleName` выбирает пользовательский стиль, который вы определяете самостоятельно через `workbook.worksheets.tableStyles.addPivotTableStyle(...)`. Пользовательские стили необходимы, если требуется изменить цвета, границы или шрифты сверх возможностей предустановок.
Кроме того, `pivotTable.formatAll(style)` — это сокращенный способ, который применяет один объект `style` к каждой ячейке сводной таблицы и переопределяет параметры, заданные через любой из двух API для имен стилей, описанных выше. Это полезно, если требуется единообразный вид независимо от основной темы.

## **Применение устаревшего предустановленного автоформата XLS**
`pivotTable.autoFormatType` принимает значение из перечисления `Aspose.Cells.Pivot.PivotTableAutoFormatType`. Доступные значения: `Report1`–`Report10`, `Classic` и `Table1`–`Table10`.
В следующем примере создаётся новая рабочая книга, она заполняется демонстрационными данными Fruit/Year/Amount, затем добавляется сводная таблица, применяется `PivotTableAutoFormatType.Report5`, а результат сохраняется как `.xls`.

{{% alert color="primary" %}}
**Почему нет полей столбцов?** Автоформаты серии Report (`Report1`–`Report10`, `Table1`–`Table10`) были разработаны в классическом Excel для **одномерных сводных таблиц**, содержащих только поля строк и значения, поэтому они не предусматривают встроенного стиля оформления для заголовков полей столбцов. Если в сводной таблице требуются поля столбцов, используйте современные предустановки `PivotTableStyleType` из [Сценария 2](#apply-a-modern-named-preset-pivot-table-style), разработанные для двумерной компоновки, применяемой в современном Excel.
{{% /alert %}}

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
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
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            // Scenario 1: Apply a legacy XLS preset autoformat
            // API in use: PivotTable.AutoFormatType
            // Target file format: .xls (legacy)
            // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-.NET
            // Create a new workbook
            const workbook = new Workbook();
            // Get the first worksheet
            const sheet = workbook.worksheets.get(0);
            const cells = sheet.cells;
            // Populate the source data with header row (Fruit, Year, Amount)
            // and 9 data rows covering grape, blueberry, kiwi, cherry across 2020 and 2021
            cells.get(0, 0).value = "Fruit";
            cells.get(0, 1).value = "Year";
            cells.get(0, 2).value = "Amount";
            cells.get(1, 0).value = "grape";
            cells.get(1, 1).value = 2020;
            cells.get(1, 2).value = 50;
            cells.get(2, 0).value = "blueberry";
            cells.get(2, 1).value = 2020;
            cells.get(2, 2).value = 30;
            cells.get(3, 0).value = "kiwi";
            cells.get(3, 1).value = 2020;
            cells.get(3, 2).value = 25;
            cells.get(4, 0).value = "cherry";
            cells.get(4, 1).value = 2020;
            cells.get(4, 2).value = 40;
            cells.get(5, 0).value = "grape";
            cells.get(5, 1).value = 2021;
            cells.get(5, 2).value = 60;
            cells.get(6, 0).value = "blueberry";
            cells.get(6, 1).value = 2021;
            cells.get(6, 2).value = 35;
            cells.get(7, 0).value = "kiwi";
            cells.get(7, 1).value = 2021;
            cells.get(7, 2).value = 28;
            cells.get(8, 0).value = "cherry";
            cells.get(8, 1).value = 2021;
            cells.get(8, 2).value = 45;
            cells.get(9, 0).value = "grape";
            cells.get(9, 1).value = 2020;
            cells.get(9, 2).value = 45;
            // Add a pivot table at destination cell E3, using source range A1:C10
            const pivotTable = sheet.pivotTables.add("=A1:C10", 2, 4);
            // Assign fields: Fruit -> Rows, Amount -> Data
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
            // Apply the legacy XLS preset autoformat "Report5"
            // Note: This property is only meaningful when saving as .xls.
            // When saved as .xlsx/.xlsm/.xlsb, Excel ignores AutoFormatType
            // and uses whatever PivotTableStyleType / PivotTableStyleName specifies.
            pivotTable.autoFormatType = AsposeCells.PivotTableAutoFormatType.Report5;
            // Save the workbook in legacy .xls format
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData], { type: "application/vnd.ms-excel" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output.xls";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

## **Применение современного именованного предустановленного стиля сводной таблицы**
`pivotTable.pivotTableStyleType` выбирает один из встроенных именованных стилей, которые Excel 2007 ввёл для сводных таблиц. Перечисление `PivotTableStyleType` содержит три семейства тем: светлое семейство (`PivotTableStyleLight1`–`PivotTableStyleLight28`), среднее семейство (`PivotTableStyleMedium1`–`PivotTableStyleMedium28`) и тёмное семейство (`PivotTableStyleDark1`–`PivotTableStyleDark28`). Кроме того, в перечислении определены `None` и `Custom`. Элементы с более высокими номерами в каждом семействе — это стили, добавленные в Excel 2017.
Эти предустановки доступны только для чтения. Если необходимо изменить цвета, границы или шрифты сверх возможностей предустановки, следует определить пользовательский стиль сводной таблицы, как показано в [Сценарии 3](#define-and-apply-a-custom-pivot-table-style).

{{% alert color="primary" %}}
**Почему следует использовать современные предустановки, а не автоформаты серии Report?** Значения `Report1`–`Report10` и `Table1`–`Table10` перечисления `PivotTableAutoFormatType` появились до появления полей столбцов в сводных таблицах, поэтому для них не предусмотрено оформление заголовков полей столбцов, и Excel отображает такие заголовки без оформления. Предустановки `PivotTableStyleType` разработаны для двумерной компоновки, которую использует современный Excel, и одинаково оформляют заголовки полей строк и полей столбцов.
{{% /alert %}}

В этом сценарии повторно используется набор данных Fruit/Year/Amount из Сценария 1. Поле `Year` добавляется в область столбцов вместе с полем строк `Fruit` с помощью `PivotFieldType.Column`. Затем с помощью `pivotTable.pivotTableStyleType` применяется предустановка тёмной темы `PivotTableStyleDark1`, а результат сохраняется как `.xlsx` — формат, для которого предназначен `PivotTableStyleType`.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
        <script src="aspose.cells.js.min.js"></script>
        <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;
        const readyPromise = AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            // Scenario 2: Apply a modern Excel 2007+ named preset style using PivotTableStyleType.
            // Target file format: .xlsx. The PivotTableStyleType enum lives in the Aspose.Cells namespace
            // (not in Aspose.Cells.Pivot) -- that is why we do not need any extra using for it.
            // GitHub reference: https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Examples/CSharp/PivotTables/ApplyStyleToPivotTable2.cs
            const workbook = new Workbook();
            const worksheet = workbook.worksheets.get(0);
            const cells = worksheet.cells;
            // Header row: Fruit / Year / Amount
            cells.get("A1").value = "Fruit";
            cells.get("B1").value = "Year";
            cells.get("C1").value = "Amount";
            // 9 data rows of Fruit / Year / Amount
            cells.get("A2").value = "Grape";
            cells.get("B2").value = 2020;
            cells.get("C2").value = 100;
            cells.get("A3").value = "Blueberry";
            cells.get("B3").value = 2020;
            cells.get("C3").value = 150;
            cells.get("A4").value = "Kiwi";
            cells.get("B4").value = 2020;
            cells.get("C4").value = 200;
            cells.get("A5").value = "Cherry";
            cells.get("B5").value = 2020;
            cells.get("C5").value = 180;
            cells.get("A6").value = "Grape";
            cells.get("B6").value = 2021;
            cells.get("C6").value = 120;
            cells.get("A7").value = "Blueberry";
            cells.get("B7").value = 2021;
            cells.get("C7").value = 170;
            cells.get("A8").value = "Kiwi";
            cells.get("B8").value = 2021;
            cells.get("C8").value = 210;
            cells.get("A9").value = "Cherry";
            cells.get("B9").value = 2021;
            cells.get("C9").value = 190;
            cells.get("A10").value = "Grape";
            cells.get("B10").value = 2021;
            cells.get("C10").value = 130;
            // Add a pivot table at E3, sourced from A1:C10
            const pivotTable = worksheet.pivotTables.add("=A1:C10", 2, 4);
            // Assign pivot fields: Fruit -> Row area, Year -> Column area, Amount -> Data area
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
            // Apply a modern Excel 2007+ named preset pivot style.
            // PivotTableStyleType is the correct API for .xlsx / .xlsm / .xlsb files; AutoFormatType
            // is ignored by Excel for those formats. PivotTableStyleDark1 belongs to the dark-theme
            // family (PivotTableStyleDark1..PivotTableStyleDark28), and the same enum also exposes the
            // newer Excel 2017 light/dark themes (PivotTableStyleLight1..Light28 / Dark1..Dark28).
            pivotTable.pivotTableStyleType = AsposeCells.PivotTableStyleType.PivotTableStyleDark1;
            // Save as modern .xlsx -- this is the format for which PivotTableStyleType is meaningful.
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
        </script>
    </body>
</html>
```

## **Определение и применение пользовательского стиля сводной таблицы**
Встроенные предустановки нельзя изменять. Если необходимо переопределить цвета, границы или шрифты, следует определить пользовательский стиль сводной таблицы. Процесс состоит из трех шагов:
1. Добавьте пользовательский стиль в коллекцию `tableStyles` рабочей книги с помощью `workbook.worksheets.tableStyles.addPivotTableStyle(name)`. Этот вызов возвращает индекс созданного стиля.
2. Настройте стиль, добавив элементы (например, `WholeTable` или `GrandTotalRow`) с помощью `tableStyle.tableStyleElements.add(tableStyleElementType)`, а затем назначьте каждому элементу объект `style` с помощью `tableStyleElement.setElementStyle(style)`.
3. Примените пользовательский стиль к сводной таблице, указав имя стиля в `pivotTable.pivotTableStyleName`. Не используйте `pivotTable.pivotTableStyleType`, поскольку это свойство выбирает встроенные предустановки.

{{% alert color="primary" %}}
`pivotTable.pivotTableStyleName` и `pivotTable.pivotTableStyleType` не взаимозаменяемы. Используйте `pivotTable.pivotTableStyleType` для встроенных предустановок и `pivotTable.pivotTableStyleName` для пользовательских стилей, которые вы определили с помощью `addPivotTableStyle`. Установка обоих свойств не приводит к ошибке, но применяется только стиль, соответствующий предполагаемому источнику.
Доступные значения `TableStyleElementType` включают `WholeTable`, `FirstRow`, `LastRow`, `FirstColumn`, `LastColumn`, `GrandTotalRow`, `GrandTotalColumn`, `PageFieldLabels` и `PageFieldValues`.
В следующем примере определяется пользовательский стиль сводной таблицы с тонкой чёрной границей для `WholeTable` и полужирным красным шрифтом для `GrandTotalRow`, после чего он применяется с помощью `pivotTable.pivotTableStyleName`, а результат сохраняется как `.xlsx`.
{{% /alert %}}

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>
    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook } = AsposeCells;
        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            const workbook = new Workbook();
            const worksheet = workbook.worksheets.get(0);
            const cells = worksheet.cells;
            // Populate source data: header row + 9 data rows (A1:C10)
            cells.get("A1").value = "Fruit";
            cells.get("B1").value = "Year";
            cells.get("C1").value = "Amount";
            cells.get("A2").value = "Grape";
            cells.get("B2").value = 2020;
            cells.get("C2").value = 100;
            cells.get("A3").value = "Blueberry";
            cells.get("B3").value = 2020;
            cells.get("C3").value = 200;
            cells.get("A4").value = "Kiwi";
            cells.get("B4").value = 2020;
            cells.get("C4").value = 300;
            cells.get("A5").value = "Cherry";
            cells.get("B5").value = 2020;
            cells.get("C5").value = 400;
            cells.get("A6").value = "Grape";
            cells.get("B6").value = 2021;
            cells.get("C6").value = 500;
            cells.get("A7").value = "Blueberry";
            cells.get("B7").value = 2021;
            cells.get("C7").value = 600;
            cells.get("A8").value = "Kiwi";
            cells.get("B8").value = 2021;
            cells.get("C8").value = 700;
            cells.get("A9").value = "Cherry";
            cells.get("B9").value = 2021;
            cells.get("C9").value = 800;
            cells.get("A10").value = "Grape";
            cells.get("B10").value = 2021;
            cells.get("C10").value = 900;
            // Add pivot table sourced from A1:C10, anchored at E3
            const pivotTable = worksheet.pivotTables.add("=A1:C10", 2, 4);
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
            // Step 1: register a new custom pivot table style and capture its index
            const styleIndex = workbook.worksheets.tableStyles.addPivotTableStyle("CustomPivotStyle");
            const tableStyle = workbook.worksheets.tableStyles.get(styleIndex);
            // Step 2: add a WholeTable element and apply thin black borders on all four sides
            const wholeTableElementIndex = tableStyle.tableStyleElements.add(AsposeCells.TableStyleElementType.WholeTable);
            const wholeTableElement = tableStyle.tableStyleElements.get(wholeTableElementIndex);
            const wholeTableStyle = workbook.createStyle();
            const topBorder = wholeTableStyle.borders.get(AsposeCells.BorderType.TopBorder);
            topBorder.lineStyle = AsposeCells.CellBorderType.Thin;
            topBorder.color = "black";
            const bottomBorder = wholeTableStyle.borders.get(AsposeCells.BorderType.BottomBorder);
            bottomBorder.lineStyle = AsposeCells.CellBorderType.Thin;
            bottomBorder.color = "black";
            const leftBorder = wholeTableStyle.borders.get(AsposeCells.BorderType.LeftBorder);
            leftBorder.lineStyle = AsposeCells.CellBorderType.Thin;
            leftBorder.color = "black";
            const rightBorder = wholeTableStyle.borders.get(AsposeCells.BorderType.RightBorder);
            rightBorder.lineStyle = AsposeCells.CellBorderType.Thin;
            rightBorder.color = "black";
            wholeTableElement.setElementStyle(wholeTableStyle);
            // Step 3: add a GrandTotalRow element and apply bold red font
            const grandTotalElementIndex = tableStyle.tableStyleElements.add(AsposeCells.TableStyleElementType.GrandTotalRow);
            const grandTotalElement = tableStyle.tableStyleElements.get(grandTotalElementIndex);
            const grandTotalStyle = workbook.createStyle();
            grandTotalStyle.font.isBold = true;
            grandTotalStyle.font.color = "red";
            grandTotalElement.setElementStyle(grandTotalStyle);
            // Step 4: apply the custom style by name (NOT by PivotTableStyleType, which is for built-in presets)
            pivotTable.pivotTableStyleName = "CustomPivotStyle";
            const outputData = workbook.save(AsposeCells.SaveFormat.Xlsx);
            const blob = new Blob([outputData], {
                type: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

## **Применение одного стиля к каждой ячейке сводной таблицы с помощью formatAll**
`pivotTable.formatAll(style)` — это сокращенный способ, который применяет один объект `style` к каждой ячейке сводной таблицы, включая область данных, заголовки строк и столбцов, а также итоговые значения. Все параметры, ранее заданные через `pivotTable.pivotTableStyleType` или `pivotTable.pivotTableStyleName`, переопределяются.

{{% alert color="primary" %}}
`formatAll` переопределяет и `pivotTable.pivotTableStyleType`, и `pivotTable.pivotTableStyleName`. Используйте его только тогда, когда требуется единообразный вид, независимый от темы, для всей сводной таблицы.
В следующем примере создаётся объект `style` с жёлтой сплошной заливкой, полужирным тёмно-синим шрифтом и тонкими чёрными границами со всех сторон, затем применяется с помощью `formatAll`, а результат сохраняется как `.xlsx`.
{{% /alert %}}

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
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
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            // Scenario 4: Apply a single Style to every pivot table cell using FormatAll
            // API in use: PivotTable.FormatAll(Style)
            // Target format: .xlsx
            // GitHub reference: see Aspose.Cells-for-.NET repository — pivot table styling examples
            const workbook = new Workbook();
            const worksheet = workbook.worksheets.get(0);
            // Populate source data: header row (row 1) + 9 data rows (rows 2-10)
            const cells = worksheet.cells;
            cells.get("A1").value = "Fruit";
            cells.get("B1").value = "Year";
            cells.get("C1").value = "Amount";
            cells.get("A2").value = "Grape";
            cells.get("B2").value = 2020;
            cells.get("C2").value = 5000;
            cells.get("A3").value = "Blueberry";
            cells.get("B3").value = 2020;
            cells.get("C3").value = 3000;
            cells.get("A4").value = "Kiwi";
            cells.get("B4").value = 2020;
            cells.get("C4").value = 4000;
            cells.get("A5").value = "Cherry";
            cells.get("B5").value = 2020;
            cells.get("C5").value = 2000;
            cells.get("A6").value = "Grape";
            cells.get("B6").value = 2021;
            cells.get("C6").value = 6000;
            cells.get("A7").value = "Blueberry";
            cells.get("B7").value = 2021;
            cells.get("C7").value = 3500;
            cells.get("A8").value = "Kiwi";
            cells.get("B8").value = 2021;
            cells.get("C8").value = 4500;
            cells.get("A9").value = "Cherry";
            cells.get("B9").value = 2021;
            cells.get("C9").value = 2500;
            cells.get("A10").value = "Grape";
            cells.get("B10").value = 2021;
            cells.get("C10").value = 5500;
            // Add pivot table: source range A1:C10, destination cell E3
            const pivotTable = worksheet.pivotTables.add("=A1:C10", 2, 4);
            // Assign pivot fields: Fruit -> Row area, Year -> Column area, Amount -> Data area
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
            // Build a Style that will be forced onto every cell of the pivot table
            const style = workbook.createStyle();
            style.foregroundColor = AsposeCells.Color.Yellow;
            style.pattern = AsposeCells.BackgroundType.Solid;
            style.font.isBold = true;
            style.font.color = AsposeCells.Color.DarkBlue;
            style.borders.get(AsposeCells.BorderType.TopBorder).lineStyle = AsposeCells.CellBorderType.Thin;
            style.borders.get(AsposeCells.BorderType.TopBorder).color = AsposeCells.Color.Black;
            style.borders.get(AsposeCells.BorderType.BottomBorder).lineStyle = AsposeCells.CellBorderType.Thin;
            style.borders.get(AsposeCells.BorderType.BottomBorder).color = AsposeCells.Color.Black;
            style.borders.get(AsposeCells.BorderType.LeftBorder).lineStyle = AsposeCells.CellBorderType.Thin;
            style.borders.get(AsposeCells.BorderType.LeftBorder).color = AsposeCells.Color.Black;
            style.borders.get(AsposeCells.BorderType.RightBorder).lineStyle = AsposeCells.CellBorderType.Thin;
            style.borders.get(AsposeCells.BorderType.RightBorder).color = AsposeCells.Color.Black;
            // Apply FormatAll: forces this single style onto every cell of the pivot table,
            // overriding any PivotTableStyleType / PivotTableStyleName previously set
            pivotTable.formatAll(style);
            // Save the workbook in the modern .xlsx format
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

## **Какой API для стилей следует использовать?**
Выбор API для стилей зависит от формата файла, в который сохраняется рабочая книга. Используйте приведённую ниже таблицу в качестве краткого справочника.
| Целевой формат файла | Используемый API | Примечания |
|---|---|---|
| `.xls` (устаревший) | `pivotTable.autoFormatType` | Значения из `Aspose.Cells.Pivot.PivotTableAutoFormatType` (например, `Report1`–`Report10`, `Classic`, `Table1`–`Table10`). Игнорируется при сохранении в современные форматы. |
| `.xlsx` / `.xlsm` / `.xlsb` (современный формат, встроенный стиль) | `pivotTable.pivotTableStyleType` | Значения из `Aspose.Cells.PivotTableStyleType` (светлые и тёмные темы, включая стили, добавленные в Excel 2017). |
| `.xlsx` / `.xlsm` / `.xlsb` (современный формат, пользовательский стиль) | `pivotTable.pivotTableStyleName` + `workbook.worksheets.tableStyles.addPivotTableStyle(...)` | Используйте, когда встроенных предустановок недостаточно. Настройка выполняется через `tableStyleElement.setElementStyle(...)`. |
| Любой формат (единообразное переопределение) | `pivotTable.formatAll(style)` | Сокращенный способ, переопределяющий все остальные параметры стилей для всей сводной таблицы. |
Если есть сомнения, сохраняйте как `.xlsx` и используйте `pivotTable.pivotTableStyleType` для встроенных тем или `pivotTable.pivotTableStyleName` для пользовательских стилей.

{{< app/cells/assistant language="javascript-cpp" >}}