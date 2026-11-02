---
title: Добавление полей фильтра в сводную таблицу с помощью Aspose.Cells for JavaScript via C++
linktitle: Добавление полей фильтра в сводную таблицу с помощью Aspose.Cells for JavaScript via C++
description: Узнайте, как добавлять и настраивать поля фильтра в сводных таблицах с помощью Aspose.Cells for JavaScript via C++, включая фильтрацию с одиночным и множественным выбором.
keywords: Aspose.Cells, Aspose.Cells for JavaScript via C++, сводная таблица, поле фильтра, PivotFieldType.Page, PageFields, IsMultipleItemSelectionAllowed, CurrentPageItem, PivotItem, IsHidden, фильтр
type: docs
weight: 250
url: /ru/javascript-cpp/add-page-field-in-pivot-table/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells поддерживает полный цикл работы с полями фильтра в сводных таблицах. Поле фильтра можно добавить с помощью удобного API высокого уровня или коллекции `getPageFields()` низкого уровня. Aspose.Cells также поддерживает фильтрацию с одиночным выбором, очистку фильтра для отображения всех элементов и множественный выбор, при котором пользователи могут одновременно выбирать несколько элементов с помощью флажков в Excel.
{{% /alert %}}

## **Введение**
Поле фильтра — это поле сводной таблицы, которое определяет, *какое подмножество* исходных данных отображается в теле сводной таблицы. Конечные пользователи видят его в виде раскрывающегося списка в верхней части сформированной сводной таблицы в Excel. При выборе одного из доступных элементов фильтра тело сводной таблицы перестраивается, и в нем агрегируются только записи, относящиеся к выбранному элементу. Поле сводной таблицы становится полем фильтра, если оно зарегистрировано с типом `PivotFieldType.Page`, а не `PivotFieldType.Row`, `PivotFieldType.Column` или `PivotFieldType.Data`.

## **Добавление поля фильтра**

### Добавление поля фильтра с помощью `addFieldToArea`
В следующем примере создается небольшой набор данных `Fruit` / `Year` / `Amount`, сводная таблица размещается в ячейке E3, поле `Fruit` добавляется в область строк, `Amount` — в область данных, а `Year` — в область фильтра. Затем сводная таблица обновляется, а рабочая книга сохраняется.

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
            // Создать новую книгу
            const workbook = new Workbook();
            const worksheet = workbook.worksheets.get(0);
            worksheet.name = "Data";
            // Настроить строку заголовков
            const cells = worksheet.cells;
            cells.get("A1").value = "Fruit";
            cells.get("B1").value = "Year";
            cells.get("C1").value = "Amount";
            // Заполнить 9 строк примерами данных: Fruit, Year, Amount
            const data = [
                ["apple", 2020, 100],
                ["banana", 2021, 200],
                ["apple", 2021, 150],
                ["grape", 2020, 120],
                ["orange", 2022, 180],
                ["banana", 2020, 90],
                ["grape", 2021, 130],
                ["apple", 2022, 170],
                ["orange", 2021, 110]
            ];
            for (let i = 0; i < data.length; i++) {
                cells.get(i + 1, 0).value = data[i][0];
                cells.get(i + 1, 1).value = data[i][1];
                cells.get(i + 1, 2).value = data[i][2];
            }
            // Добавить сводную таблицу с ячейкой привязки E3
            const pivotTableIndex = worksheet.pivotTables.add("=A1:C10", "E3", "PivotTable1");
            const pivotTable = worksheet.pivotTables.get(pivotTableIndex);
            // Добавить поля в соответствующие области: Fruit как строка, Amount как данные, Year как поле страницы
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, "Year");
            // Обновить и вычислить данные сводной таблицы
            pivotTable.calculateData();
            // Сохранить книгу
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "pageFieldSample.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

### Добавление поля фильтра с помощью `getPageFields().add`
Если у вас уже есть экземпляр `PivotField`, его можно передать непосредственно в `pivotTable.getPageFields().add(pivotField)`. Сводная таблица и поле фильтра создаются точно так же, как в предыдущем сценарии; отличается только добавление поля в область фильтра: вместо `addFieldToArea` используется вызов API нижнего уровня.

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
            // — Сводная таблица и поле страницы создаются точно так же, как
            //   в сценарии 1a (данные Fruit/Year/Amount, сводная таблица в E3,
            //   Fruit→строка, Amount→данные). Ниже мы получаем поле PivotField
            //   Year из коллекции BaseFields и передаём его в PageFields.Add —
            //   низкоуровневую альтернативу AddFieldToArea. Результат
            //   функционально идентичен сценарию 1a.
            const workbook = new Workbook();
            const sheet = workbook.worksheets.get(0);
            // Заголовки
            sheet.cells.get("A1").value = "Fruit";
            sheet.cells.get("B1").value = "Year";
            sheet.cells.get("C1").value = "Amount";
            // Пример данных (9 строк)
            sheet.cells.get("A2").value = "apple";    sheet.cells.get("B2").value = "2020"; sheet.cells.get("C2").value = 100;
            sheet.cells.get("A3").value = "apple";    sheet.cells.get("B3").value = "2021"; sheet.cells.get("C3").value = 150;
            sheet.cells.get("A4").value = "apple";    sheet.cells.get("B4").value = "2022"; sheet.cells.get("C4").value = 200;
            sheet.cells.get("A5").value = "grape";    sheet.cells.get("B5").value = "2020"; sheet.cells.get("C5").value = 300;
            sheet.cells.get("A6").value = "grape";    sheet.cells.get("B6").value = "2021"; sheet.cells.get("C6").value = 400;
            sheet.cells.get("A7").value = "grape";    sheet.cells.get("B7").value = "2022"; sheet.cells.get("C7").value = 500;
            sheet.cells.get("A8").value = "blueberry"; sheet.cells.get("B8").value = "2020"; sheet.cells.get("C8").value = 250;
            sheet.cells.get("A9").value = "blueberry"; sheet.cells.get("B9").value = "2021"; sheet.cells.get("C9").value = 350;
            sheet.cells.get("A10").value = "blueberry"; sheet.cells.get("B10").value = "2022"; sheet.cells.get("C10").value = 450;
            // Добавляем сводную таблицу в E3 для диапазона A1:C10
            const pivotTableIndex = sheet.pivotTables.add("=A1:C10", "E3", "PivotTable1");
            const pivotTable = sheet.pivotTables.get(pivotTableIndex);
            // Fruit → строка, Amount → данные (Year будет добавлено в область страницы ниже)
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
            // Низкоуровневый подход: получаем существующее поле PivotField Year из BaseFields
            // и регистрируем его в области страницы через PageFields.Add(PivotField).
            const yearField = pivotTable.baseFields.get("Year");
            pivotTable.pageFields.add(yearField);
            // Обновляем данные, чтобы новое поле страницы было отражено в сохранённой книге
            pivotTable.calculateData();
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

## **Фильтрация с одиночным выбором (отображение одного элемента фильтра)**
По умолчанию для поля фильтра используется одиночный выбор: оно отображается в виде раскрывающегося списка, а целочисленное значение `pivotField.currentPageItem` определяет, какой элемент фильтра управляет телом сводной таблицы. Присвоение конкретного индекса выбирает один элемент; присвоение специального значения-маркера `0x7FFD` (десятичное значение 32765) очищает фильтр, поэтому одновременно агрегируются все элементы фильтра. Одиночный выбор является режимом по умолчанию, поэтому его не требуется включать явно.

### Отображение всех элементов
Присвоение `currentPageItem` специального значения `0x7FFD` эквивалентно очистке фильтра: тело сводной таблицы агрегирует все элементы фильтра, как если бы фильтр не применялся.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <button id="runExample" disabled>Run Example</button>
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
            document.getElementById('runExample').disabled = false;
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            // Создаем новую книгу
            const workbook = new Workbook();
            const sheet = workbook.worksheets.get(0);
            // Заполняем данные Fruit/Year/Amount
            const cells = sheet.cells;
            cells.get("A1").value = "Fruit";
            cells.get("B1").value = "Year";
            cells.get("C1").value = "Amount";
            const data = [
                ["Apple", 2022, 100],
                ["Apple", 2023, 150],
                ["Banana", 2022, 80],
                ["Banana", 2023, 120],
                ["Cherry", 2022, 200],
                ["Cherry", 2023, 250]
            ];
            for (let r = 0; r < data.length; r++) {
                for (let c = 0; c < data[r].length; c++) {
                    cells.get(r + 1, c).value = data[r][c];
                }
            }
            // Создаем сводную таблицу в ячейке E3
            const pivotTables = sheet.pivotTables;
            const pivotTableIndex = pivotTables.add("=A1:C7", "E3", "PivotTable1");
            const pivotTable = pivotTables.get(pivotTableIndex);
            // Настраиваем поля сводной таблицы: Fruit→Строка, Amount→Данные, Year→Страница
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, "Year");
            pivotTable.calculateData();
            // Сбрасываем фильтр страницы, чтобы были видны все элементы поля страницы.
            // 0x7FFD (десятичное 32765) — специальное значение-маркер, означающее "все элементы", —
            // эквивалент выбору "(Все)" в выпадающем списке полей страницы Excel.
            pivotTable.pageFields.get(0).currentPageItem = 0x7FFD;
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

### Отображение одного конкретного элемента
Присвоение `currentPageItem` действительного индекса выбирает только соответствующий элемент фильтра. Индекс задает положение элемента в отсортированном списке элементов поля фильтра, поэтому, например, `1` выбирает второй элемент после сортировки.

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
            document.getElementById("runExample").addEventListener("click", async () => {
                // Создать книгу
                const workbook = new Workbook();
                const sheet = workbook.worksheets.get(0);
                const cells = sheet.cells;
                // Добавить образец данных (Fruit/Year/Amount)
                cells.get("A1").value = "Fruit";
                cells.get("B1").value = "Year";
                cells.get("C1").value = "Amount";
                cells.get("A2").value = "Apple";
                cells.get("B2").value = "2020";
                cells.get("C2").value = "100";
                cells.get("A3").value = "Apple";
                cells.get("B3").value = "2021";
                cells.get("C3").value = "150";
                cells.get("A4").value = "Banana";
                cells.get("B4").value = "2020";
                cells.get("C4").value = "200";
                cells.get("A5").value = "Banana";
                cells.get("B5").value = "2021";
                cells.get("C5").value = "250";
                // Добавить сводную таблицу в E3
                const pivotTables = sheet.pivotTables;
                const pivotTableIndex = pivotTables.add("=A1:C5", "E3", "PivotTable1");
                const pivotTable = pivotTables.get(pivotTableIndex);
                // Добавить поля: Fruit→Строка, Amount→Данные, Year→Страница
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, "Year");
                // Операции, специфичные для поля страницы
                pivotTable.pageFields.get(0).currentPageItem = 1; // 1 = второй элемент в отсортированном порядке (например, «2021»)
                // Обновить и рассчитать сводную таблицу
                pivotTable.calculateData();
                const outputData = workbook.save(SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                const downloadLink = document.getElementById("downloadLink");
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "output.xlsx";
                downloadLink.style.display = "block";
                document.getElementById("result").innerHTML =
                    '<p style="color: green;">Done! Click the download link to get the result file.</p>';
            });
        </script>
    </body>
</html>
```

## **Фильтрация с множественным выбором**
Фильтрация с множественным выбором преобразует раскрывающийся список фильтра в список с флажками и позволяет конечному пользователю одновременно выбирать несколько элементов фильтра. Aspose.Cells предоставляет два взаимосвязанных свойства. Чтобы интерфейс множественного выбора стал доступен, сначала необходимо установить `pivotField.isMultipleItemSelectionAllowed` в `true`. После этого `pivotItem.isHidden` определяет, какие элементы отображаются в списке с флажками. Таким образом, можно отобразить все элементы или указать список разрешенных элементов.

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
            const { Workbook } = AsposeCells;
            const initializationPromise = AsposeCells.onReady({
                license: "/lic/aspose.cells.enc",
                fontPath: "/fonts/",
                fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
            }).then(() => {
                console.log("Aspose.Cells initialized");
            });
            document.getElementById('runExample').addEventListener('click', async () => {
                await initializationPromise;
                // — Сводная таблица и поле страницы создаются точно так же, как
                //   в сценарии 1a (данные Fruit/Year/Amount, сводная таблица в E3,
                //   Fruit→строка, Amount→данные, Year→страница через AddFieldToArea).
                //   Ниже применяется многоэлементная фильтрация поля страницы.
                const workbook = new Workbook();
                const sheet = workbook.worksheets.get(0);
                const cells = sheet.cells;
                // Пример данных: Fruit | Year | Amount
                cells.get(0, 0).value = "Fruit";
                cells.get(0, 1).value = "Year";
                cells.get(0, 2).value = "Amount";
                const data = [
                    ["apple", "2019", "100"],
                    ["apple", "2020", "150"],
                    ["apple", "2021", "200"],
                    ["banana", "2019", "110"],
                    ["banana", "2020", "160"],
                    ["banana", "2021", "210"],
                    ["grape", "2019", "120"],
                    ["grape", "2020", "170"],
                    ["grape", "2021", "220"]
                ];
                for (let i = 0; i < data.length; i++) {
                    cells.get(i + 1, 0).value = data[i][0];
                    cells.get(i + 1, 1).value = Number(data[i][1]);
                    cells.get(i + 1, 2).value = Number(data[i][2]);
                }
                const pivotSheet = workbook.worksheets.add("Pivot");
                const pivots = pivotSheet.pivotTables;
                const pivotTableIndex = pivots.add("=A1:C10", "E3", "PivotTable1");
                const pivotTable = pivots.get(pivotTableIndex);
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, "Year");
                // — Включение множественного выбора для поля страницы
                const pageField = pivotTable.pageFields.get(0);
                pageField.isMultipleItemSelectionAllowed = true;
                const pivotItems = pageField.pivotItems;
                // Часть A — выбор ВСЕХ элементов (сделать видимым каждый элемент)
                for (let i = 0; i < pivotItems.count; i++) {
                    pivotItems.get(i).isHidden = false;
                }
                // Часть B — выбор только определенных элементов по исходному значению
                for (let i = 0; i < pivotItems.count; i++) {
                    const pivotItem = pivotItems.get(i);
                    switch (pivotItem.getStringValue()) {
                        case "2020":
                        case "grape":
                        case "blueberry":
                            pivotItem.isHidden = false;
                            break;
                        default:
                            pivotItem.isHidden = true;
                            break;
                    }
                }
                pivotTable.calculateData();
                const outputData = workbook.save(AsposeCells.SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                const downloadLink = document.getElementById('downloadLink');
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "output.xlsx";
                downloadLink.style.display = "block";
                document.getElementById('result').innerHTML =
                    '<p style="color: green;">Done! Click the download link to get the result file.</p>';
            });
        </script>
    </body>
</html>
```

> **Примечание:** При использовании фильтрации с множественным выбором через `pivotItem.isHidden` **хотя бы один `PivotItem` должен оставаться видимым** (`isHidden === false`). Если скрыты все элементы, Excel либо аварийно завершает работу при открытии файла, либо отображает пустую сводную таблицу. Убедитесь, что список разрешенных элементов для множественного выбора включает хотя бы один элемент из исходных данных.

## **Какой API и какой режим следует использовать?**
В таблице ниже кратко указано, когда следует использовать каждый API и режим, чтобы выбрать подходящее сочетание, не читая описание каждого сценария.
| Сценарий / вариант использования | Рекомендуемый API | Используемое свойство | Примечания |
|---|---|---|---|
| Добавление поля фильтра по имени исходного столбца (наиболее распространенный случай) | `pivotTable.addFieldToArea(PivotFieldType.Page, "fieldName")` | н/д | Вызов API высокого уровня, умещающийся в одну строку. Используйте его, если не требуется ссылка на `PivotField`. |
| Добавление поля фильтра при наличии объекта `PivotField` | `pivotTable.getPageFields().add(pivotField)` | н/д | Используйте, если объект поля получен в другом месте или должен быть повторно использован. |
| Фильтрация по одному элементу фильтра (режим по умолчанию) | `pivotField.currentPageItem` | задается конкретный индекс | Например, `1` отображает второй элемент в отсортированном списке. |
| Отображение всех элементов / очистка фильтра | `pivotField.currentPageItem` | задается `0x7FFD` | Значение `0x7FFD` (десятичное значение 32765) служит маркером «все элементы». |
| Включение интерфейса множественного выбора в Excel | `pivotField.isMultipleItemSelectionAllowed` | задается `true` | Необходимо установить это значение, чтобы присвоения `isHidden` вступили в силу. |
| Скрытие/отображение отдельных элементов в списке с множественным выбором | `pivotItem.isHidden` | задается для каждого элемента | Хотя бы один элемент должен оставаться видимым (`isHidden === false`). |

{{% alert color="primary" %}}
При настройке фильтрации с множественным выбором всегда учитывайте ограничение на видимость. Если скрыты все элементы `PivotItem` поля фильтра с множественным выбором, Excel аварийно завершает работу при открытии файла или отображает пустую сводную таблицу. Сформируйте список разрешенных элементов на основе исходных данных так, чтобы хотя бы один элемент оставался видимым. Тогда сохраненные рабочие книги будут корректно открываться на любом компьютере.
{{% /alert %}}

{{< app/cells/assistant language="javascript-cpp" >}}