---
title: Форматирование части сводной таблицы
linktitle: Форматирование части сводной таблицы
description: Форматирование части сводной таблицы в Aspose.Cells for JavaScript via C++ путем применения стилей к семантическим регионам PivotArea или прямоугольникам CellArea через PivotTable.Format, при этом форматы хранятся в PivotTable.PivotFormats и сохраняются при обновлении сводной таблицы.
keywords: Aspose.Cells for JavaScript via C++, сводная таблица, формат, PivotArea, CellArea, PivotTable.Format, PivotFormats, PivotTableSelectionType, LabelOnly, DataOnly, SelectField, FormatAll, C++
type: docs
weight: 20
url: /ru/javascript-cpp/format-part-of-pivot-table/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Возможные сценарии использования**
`PivotTable.FormatAll` применяет один стиль ко всей сводной таблице и описан на родительской странице. Он не различает подписи, значения, итоги или отдельные области отчёта.  
На практике обычно требуется выделить лишь часть сводной таблицы. Распространённые цели включают подписи, принадлежащие полю строки, ячейки‑значения, полученные от одного поля, строку общего итога или произвольный прямоугольник, например первые две строки элементов.  
Применение стиля непосредственно к ячейкам листа, содержащим сводную таблицу, не эквивалентно. Excel сохраняет форматирование сводных таблиц как семантические записи `PivotArea`, а не как обычные записи стилей ячеек. Формат, привязанный к `PivotArea`, остаётся привязанным к такой области, как подписи поля или данные, и пересчитывается при перерасчёте, обновлении или расширении сводной таблицы. Стиль, записанный непосредственно в ячейку, принадлежит лишь этой позиции и не отслеживается моделью сводной таблицы.  
Aspose.Cells предоставляет полный набор перегрузок `PivotTable.Format`, позволяя использовать оба типа форматирования:
- `Format(PivotArea, Style)` привязывает стиль к семантической области, созданной с помощью `PivotArea.Select` или `PivotArea.SelectField`.
- `Format(CellArea, Style)` привязывает стиль к прямоугольнику листа внутри сводной таблицы.
- `Format(int row, int column, Style)` нацеливается на одну ячейку.
- `FormatAll(Style)` форматирует всю сводную таблицу.

## **Форматирование Pivot Area**
Семантический подход рекомендуется, когда выделение должно следовать за полем или областью отчёта.
1. Создайте `PivotArea` с помощью `new PivotArea(pivotTable)`. Объект описывает семантическую область, принадлежащую конкретной сводной таблице.  
2. Выберите поле по его нулевому индексу на заданной оси с помощью `PivotArea.Select(PivotFieldType axisType, int fieldPosition, PivotTableSelectionType selectionType)`.
   - `PivotTableSelectionType.DataAndLabel` выбирает как подписи, так и данные поля.  
   - `PivotTableSelectionType.LabelOnly` выбирает только подписи поля.  
   - `PivotTableSelectionType.DataOnly` выбирает только ячейки‑данные поля.  
3. Выберите поле по имени с помощью `PivotArea.SelectField(PivotFieldType axisType, string fieldName)`. При выборе строкового поля по имени область разрешается в ячейки‑значения, полученные от элементов этого поля.  
4. Создайте `Style` через `Workbook.CreateStyle()`, настройте шрифт, цвет переднего плана и сплошной фон, затем передайте стиль в `PivotTable.Format(area, style)`.  
5. Каждый вызов перегрузки `PivotArea` добавляет одну запись `PivotTableFormat` в `PivotTable.PivotFormats`.  
6. Форматы, привязанные к полю, отрисовываются при расчёте данных сводной таблицы. Поэтому вызовите `PivotTable.CalculateData()` после применения форматов, чтобы стили стали видимыми.  
Ниже приведён пример, создающий небольшую сводную таблицу продаж фруктов, оформляющий подписи строк `Fruit` с помощью `PivotArea.Select` и `PivotTableSelectionType.LabelOnly`, оформляющий ячейки‑значения того же поля с помощью `PivotArea.SelectField`, а затем перерассчитывающий сводную таблицу, чтобы оба стиля отобразились.

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
            const workbook = new Workbook();
            const sheet = workbook.worksheets.get(0);
            const cells = sheet.cells;
            // Fruit sales data
            const fruits = ["Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry"];
            const years = [2024, 2024, 2025, 2025, 2024, 2025];
            const amounts = [100, 150, 120, 180, 90, 110];
            cells.get("A1").value = "Fruit";
            cells.get("B1").value = "Year";
            cells.get("C1").value = "Amount";
            for (let i = 0; i < fruits.length; i++) {
                cells.get(i + 1, 0).value = fruits[i];
                cells.get(i + 1, 1).value = years[i];
                cells.get(i + 1, 2).value = amounts[i];
            }
            // Pivot table with its top-left corner at E3 (row 2, column 4)
            const pivotTable = sheet.pivotTables.add("=A1:C7", 2, 4);
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
            pivotTable.calculateData();
            // Bold yellow fill on the row field's label cells
            const labelStyle = workbook.createStyle();
            labelStyle.font.isBold = true;
            labelStyle.foregroundColor = AsposeCells.Color.Yellow;
            labelStyle.pattern = AsposeCells.BackgroundType.Solid;
            const labelArea = new AsposeCells.PivotArea(pivotTable);
            labelArea.select(
                AsposeCells.PivotFieldType.Row,
                0,
                AsposeCells.PivotTableSelectionType.LabelOnly
            );
            pivotTable.format(labelArea, labelStyle);
            // Light green fill on the value cells the row field produces
            const valueStyle = workbook.createStyle();
            valueStyle.foregroundColor = AsposeCells.Color.LightGreen;
            valueStyle.pattern = AsposeCells.BackgroundType.Solid;
            const valueArea = new AsposeCells.PivotArea(pivotTable);
            valueArea.selectField(AsposeCells.PivotFieldType.Row, "Fruit");
            pivotTable.format(valueArea, valueStyle);
            // Field-anchored formats are painted when the data is calculated
            pivotTable.calculateData();
            // Label cells E4:E6 are now bold on yellow, value cells F4:F6 are light green
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "FormatPivotArea.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML =
                '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

## **Форматирование Cell Area сводной таблицы**
Используйте `PivotTable.Format(CellArea, Style)`, когда интересующая область представляет собой обычный прямоугольник листа, а не семантическую область сводной таблицы.  
`CellArea` описывается полями `startRow`, `startColumn`, `endRow` и `endColumn`. Значения являются нулевыми координатами листа, а конечные координаты указывают последнюю строку и столбец, включённые в прямоугольник, поэтому область охватывает ячейки от начальной позиции до конечной включительно.  
В отличие от формата, привязанного к полю, формат `CellArea` применяется к ячейкам сразу. Повторный вызов `CalculateData()` не требуется для отображения стиля.  
Прямоугольник `CellArea` может содержать одновременно подписи и значения. Следующий раздел объясняет, как Aspose.Cells и Excel представляют такой прямоугольник внутренне.  
Ниже пример, который форматирует прямоугольник `E4:F5` сводной таблицы курсивным светло‑синим стилем и сохраняет рабочую книгу без дополнительного перерасчёта.

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
            const workbook = new Workbook();
            const sheet = workbook.worksheets.get(0);
            const cells = sheet.cells;
            const fruits = ["Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry"];
            const years = [2024, 2024, 2025, 2025, 2024, 2025];
            const amounts = [100, 150, 120, 180, 90, 110];
            cells.get("A1").value = "Fruit";
            cells.get("B1").value = "Year";
            cells.get("C1").value = "Amount";
            for (let i = 0; i < fruits.length; i++) {
                cells.get(i + 1, 0).value = fruits[i];
                cells.get(i + 1, 1).value = years[i];
                cells.get(i + 1, 2).value = amounts[i];
            }
            const pivotTable = sheet.pivotTables.add("=A1:C7", 2, 4);
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
            pivotTable.calculateData();
            // Highlight the first two fruit rows (the rectangle E4:F5)
            const highlightStyle = workbook.createStyle();
            highlightStyle.font.isItalic = true;
            highlightStyle.foregroundColor = AsposeCells.Color.LightBlue;
            highlightStyle.pattern = AsposeCells.BackgroundType.Solid;
            const rectangle = new AsposeCells.CellArea();
            rectangle.startRow = 3;
            rectangle.startColumn = 4;
            rectangle.endRow = 4;
            rectangle.endColumn = 5;
            pivotTable.format(rectangle, highlightStyle);
            // E4:F5 is italic on light blue immediately, no recalculation needed
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "FormatPivotCellArea.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

## **Соответствие Pivot Area и Cell Area**
Excel сохраняет форматирование сводных таблиц как записи `pivotArea`, а не как обычные записи стилей ячеек листа. Та же модель используется в Aspose.Cells, поэтому запросы на форматирование переводятся во внутренние pivot‑области при их сохранении.  
Отношения между `CellArea`, предоставляемой пользователем, и внутренними pivot‑областями являются многими‑ко‑многим в обоих направлениях.
- Один `CellArea` может порождать несколько pivot‑областей. Если прямоугольник охватывает и подписи, и значения, он разбивается на отдельные правила для подписей и данных, поскольку модель сводной таблицы обрабатывает форматирование подписей и данных независимо.  
- Одна pivot‑область может разрешаться в несколько разрозненных экземпляров `CellArea`. Семантическая область, например строка общего итога или поле, элементы которого не идут подряд, может покрывать несколько прямоугольников. Поэтому `PivotArea.GetCellAreas()` возвращает коллекцию, а не один прямоугольник.  
Каждая операция форматирования, выполненная через `PivotTable.Format`, записывается в `PivotTable.PivotFormats`. Каждая запись `PivotTableFormat` раскрывает связанный `PivotArea` и применённый к нему `Style`. Перегрузка `PivotArea` добавляет ровно одну запись за вызов, тогда как `CellArea`, содержащий разные семантические регионы, может добавить несколько записей.  
Чтобы различать сохранённые регионы, каждый `PivotArea` предоставляет флаги `OnlyLabel` и `OnlyData`. Пример ниже форматирует один прямоугольник, охватывающий и подписи, и значения, исследует `PivotTable.PivotFormats` и выводит координаты `CellArea`, к которым каждый сохранённый pivot‑область разрешается.

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
            const { Workbook, SaveFormat, CellArea, Color } = AsposeCells;
            AsposeCells.onReady({
                license: "/lic/aspose.cells.enc",
                fontPath: "/fonts/",
                fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
            }).then(() => {
                console.log("Aspose.Cells initialized");
            });
            document.getElementById("runExample").addEventListener("click", async () => {
                const result = document.getElementById("result");
                const downloadLink = document.getElementById("downloadLink");
                const workbook = new Workbook();
                const sheet = workbook.worksheets.get(0);
                const cells = sheet.cells;
                const fruits = ["Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry"];
                const years = [2024, 2024, 2025, 2025, 2024, 2025];
                const amounts = [100, 150, 120, 180, 90, 110];
                cells.get("A1").value = "Fruit";
                cells.get("B1").value = "Year";
                cells.get("C1").value = "Amount";
                for (let i = 0; i < fruits.length; i++) {
                    cells.get(i + 1, 0).value = fruits[i];
                    cells.get(i + 1, 1).value = years[i];
                    cells.get(i + 1, 2).value = amounts[i];
                }
                const pivotTable = sheet.pivotTables.add("=A1:C7", 2, 4);
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
                pivotTable.calculateData();
                const highlightStyle = workbook.createStyle();
                highlightStyle.font.isItalic = true;
                highlightStyle.foregroundColor = Color.LightBlue;
                highlightStyle.pattern = AsposeCells.BackgroundType.Solid;
                // ONE rectangle in...
                const rectangle = new CellArea();
                rectangle.startRow = 3;
                rectangle.startColumn = 4;
                rectangle.endRow = 4;
                rectangle.endColumn = 5;
                // ...TWO semantic pivot areas out: the label part and the data part are stored separately
                pivotTable.format(rectangle, highlightStyle);
                const pivotFormats = pivotTable.pivotFormats;
                const outputLines = [`Stored formats: ${pivotFormats.count}`];
                for (let i = 0; i < pivotFormats.count; i++) {
                    const pivotFormat = pivotFormats.get(i);
                    const storedArea = pivotFormat.pivotArea;
                    const onlyLabel = storedArea.onlyLabel ? "True" : "False";
                    const onlyData = storedArea.onlyData ? "True" : "False";
                    outputLines.push(`Format ${i}: OnlyLabel=${onlyLabel}, OnlyData=${onlyData}`);
                    const resolvedAreas = storedArea.cellAreas;
                    for (let j = 0; j < resolvedAreas.count; j++) {
                        const resolved = resolvedAreas.get(j);
                        outputLines.push(
                            `    rows ${resolved.startRow + 1}-${resolved.endRow + 1}, columns ${resolved.startColumn + 1}-${resolved.endColumn + 1}`
                        );
                    }
                }
                // This prints:
                // Stored formats: 2
                // Format 0: OnlyLabel=True, OnlyData=False
                //     rows 4-5, columns 5-5        (E4:E5, the label part)
                // Format 1: OnlyLabel=False, OnlyData=True
                //     rows 4-5, columns 6-6        (F4:F5, the data part)
                result.innerHTML =
                    `<pre>${outputLines.join("\n")}</pre>` +
                    `<p style="color: green;">Done! Click the download link to get the result file.</p>`;
                const outputData = workbook.save(SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "FormatPivotAreasMap.xlsx";
                downloadLink.style.display = "block";
            });
        </script>
    </body>
</html>
```

{{% alert color="primary" %}}
Поскольку форматы хранятся как pivot‑области, а не как обычные стили ячеек, они сохраняются при перерасчёте и обновлении. Когда сводная таблица обновляется с помощью `PivotTable.RefreshData`, перерасчитывается через `CalculateData` или сохраняется и заново загружается, каждая сохранённая pivot‑область переопределяется к текущей позиции своей области, и её стиль повторно применяется.
{{% /alert %}}

Используйте `PivotArea`, построенный через `Select` или `SelectField`, когда выделение должно оставаться привязанным к полю или семантической области при обновлениях, и используйте `CellArea`, когда достаточно отформатировать фиксированный прямоугольник текущего макета сводной таблицы. Перегрузка `Format(int row, int column, Style)` применяется к отдельной ячейке. Используйте `FormatAll`, описанный на родительской странице, когда необходимо перестилизовать всю сводную таблицу единовременно.

## **Связанные статьи**
- [Применение стиля к сводной таблице](/cells/ru/javascript-cpp/apply-style-to-pivot-table/)
- [Добавление строковых и столбцовых полей сводной таблицы](/cells/ru/javascript-cpp/pivot-table-add-row-and-column-fields/)
- [Управление полями значений в сводной таблице](/cells/ru/javascript-cpp/manage-value-fields/)
- [Обновление сводной таблицы](/cells/ru/javascript-cpp/refresh-pivot-table/)

{{< app/cells/assistant language="javascript-cpp" >}}