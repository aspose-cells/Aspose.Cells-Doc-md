---
title: Отображение значений как в сводной таблице
linktitle: Отображение значений как в сводной таблице
description: Отображайте значения полей данных сводной таблицы в виде процента от общего итога, разницы от базового элемента, скользящих итогов, рангов и прочего с Aspose.Cells for JavaScript via C++.
keywords: Aspose.Cells, JavaScript via C++, сводная таблица, отображение значений как, PivotShowValuesAsType, PercentageOfTotal, PivotShowValuesSetting, showValuesAs, BaseFieldIndex, BaseItemIndex
type: docs
weight: 145
url: /ru/javascript-cpp/show-values-as-in-pivot-table/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Возможные сценарии использования**
Сводная таблица обычно агрегирует каждое поле данных с помощью функции агрегирования, такой как `Sum` или `Count`. Функция **Show Values As** в Excel заменяет каждый отображаемый результат вторичным вычислением, полученным из этой агрегированной величины — например, процентом от общего итога, скользящим итогом, разницей от выбранного базового элемента или рангом, позволяя выполнять сравнительный анализ без вспомогательных формул или вычисляемых столбцов.  
Типичные применения включают анализ доли от общего итога (проценты по строке, столбце или общему итогу), кумулятивную отчетность с использованием скользящего итога в полевом периоде, анализ отклонений от базового элемента (разница или процентная разница) и ранжирование значений от наименьшего к наибольшему или наоборот.  
В Aspose.Cells for JavaScript via C++ перечисление `PivotShowValuesAsType` выбирает вторичное вычисление. Свойство только для чтения `PivotField.showValuesSetting` возвращает объект `PivotShowValuesSetting`, у которого записываемые свойства `showValuesAs`, `baseFieldIndex` и `baseItemIndex` задают поведение; удобный метод `PivotField.showValuesAs(...)` применяет те же настройки одним вызовом. Применяйте эти настройки к полю данных или значений, полученному из `PivotTable.dataFields`.

## **Члены перечисления PivotShowValuesAsType**
Поле данных сохраняет свою функцию агрегирования, такую как Sum или Count, тогда как Show Values As изменяет лишь способ отображения агрегированного значения.  
Помимо прямой записи свойств `PivotShowValuesSetting` (см. последний раздел), удобный метод одноразового вызова применяет ту же конфигурацию. Он доступен в двух формах — одна принимает базовое поле и базовый элемент по индексу, другая — по имени:

```html
function showValuesAs(pivotField, showValuesAsType, baseField, baseItem) {
    pivotField.showValuesAs(showValuesAsType, baseField, baseItem);
}
function showValuesAsByName(pivotField, showValuesAsType, baseField, baseItem) {
    pivotField.showValuesAs(showValuesAsType, baseField, baseItem);
}
// index form: AsposeCells.PivotShowValuesAsType.PercentageOfTotal, 0, 0
// name form:  AsposeCells.PivotShowValuesAsType.PercentageOf, "Fruit", "Apple"
```

| Параметр | Описание | Когда требуется |
| --- | --- | --- |
| `showValuesAsType` | Вторичное вычисление `PivotShowValuesAsType`, которое необходимо применить. | Всегда. |
| `baseField` | Нулевая индексация базового поля среди базовых полей сводной таблицы (например, индекс строкового поля, к которому относится базовый элемент), или — в форме по имени — имя базового поля. | Для восьми форматов, зависящих от базового поля (`DifferenceFrom`, `PercentageOf`, `PercentageDifferenceFrom`, `RunningTotalIn`, `PercentageOfParentTotal`, `PercentageOfRunningTotalIn`, `RankSmallestToLargest`, `RankLargestToSmallest`); для остальных форм передайте `0` (или `null` в форме по имени). |
| `baseItem` | Нулевая индексация базового элемента, с двумя метками‑sentinel: -1 выбирает предыдущий элемент и -2 — следующий (биндинг JavaScript via C++ не экспортирует именованные константы — передайте буквальные значения). В форме по имени указывается подпись базового элемента, а `null` используется, когда выбранный формат не требует базового элемента. | Только три формата, использующие базовый элемент (`DifferenceFrom`, `PercentageOf`, `PercentageDifferenceFrom`); остальные пять форматов, зависящих от поля (`RunningTotalIn`, `PercentageOfParentTotal`, `PercentageOfRunningTotalIn`, оба ранга), игнорируют его — передайте `0` или `null`. |

| Тип расчета | Поведение | Параметры базового элемента |
| --- | --- | --- |
| `Normal` | Без вторичного вычисления; агрегированное значение отображается как есть (по умолчанию). | — |
| `DifferenceFrom` | Отображает значение как разницу с значением базового элемента в базовом поле. | `baseField` + `baseItem` (индекс, подпись или одна из меток‑sentinel) |
| `PercentageOf` | Отображает значение как процент от значения базового элемента в базовом поле. | `baseField` + `baseItem` (индекс, подпись или одна из меток‑sentinel) |
| `PercentageDifferenceFrom` | Отображает значение как процентную разницу от значения базового элемента в базовом поле. | `baseField` + `baseItem` (индекс, подпись или одна из меток‑sentinel) |
| `RunningTotalIn` | Отображает значение как скользящий итог для последовательных элементов базового поля. | `baseField` (поле, определяющее порядок накопления) |
| `PercentageOfRow` | Отображает значение как процент от итога строки. | — |
| `PercentageOfColumn` | Отображает значение как процент от итога столбца. | — |
| `PercentageOfTotal` | Отображает значение как процент от общего итога. | — |
| `Index` | Отображает значение по формуле Excel Index ((value * grand total) / (row total * column total)). | — |
| `PercentageOfParentRowTotal` | Отображает значение как процент от итога родительской строки (для вложенных строковых полей). | — |
| `PercentageOfParentColumnTotal` | Отображает значение как процент от итога родительского столбца (для вложенных столбцовых полей). | — |
| `PercentageOfParentTotal` | Отображает значение как процент от итога родительского поля. | `baseField` (родительское поле, чей итог используется как ссылка) |
| `PercentageOfRunningTotalIn` | Отображает значение как процент от скользящего итога в базовом поле. | `baseField` (поле накопления) |
| `RankSmallestToLargest` | Ранжирует значение от наименьшего (1) к наибольшему. | `baseField` (поле, элементы которого определяют область ранжирования) |
| `RankLargestToSmallest` | Ранжирует значение от наибольшего (1) к наименьшему. | `baseField` (поле, элементы которого определяют область ранжирования) |

{{% alert color="primary" %}}
`showValuesAs(...)` записывает свойства объекта `PivotShowValuesSetting` (`showValuesAs`, `baseFieldIndex` и `baseItemIndex`) — метод и объект‑свойство представляют два способа настройки одного и того же состояния, аналогично элементам выбора базового поля и базового элемента в диалоговом окне Excel **Show Values As**.
{{% /alert %}}

## **Отображение значений в виде процента от общего итога**
Вызовите метод `PivotField.showValuesAs` с параметром `PivotShowValuesAsType.PercentageOfTotal`, чтобы преобразовать каждую ячейку поля данных, включая общий итог, в её долю от общего итога. Отображаемые числа тогда представляют собой часть от полного набора результатов. Этот формат измеряет каждое значение только относительно общего итога, поэтому не требует указания базового поля или базового элемента — конечные аргументы (`0`, `0`) являются заполняющими значениями, которые формат игнорирует, как указано в таблице параметров выше.

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
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

                // Load or create a workbook with source data
                const workbook = new Workbook();
                const dataSheet = workbook.worksheets.get(0);
                const cells = dataSheet.cells;
                cells.get("A1").value = "Fruit";
                cells.get("B1").value = "Amount";
                const fruits = ["Apple", "Banana", "Apple", "Cherry", "Banana", "Apple"];
                const amounts = [10, 20, 30, 40, 50, 60];
                for (let i = 0; i < fruits.length; i++) {
                    cells.get(i + 1, 0).value = fruits[i];
                    cells.get(i + 1, 1).value = amounts[i];
                }
                // Add a pivot table on a new worksheet
                const pivotSheetIndex = workbook.worksheets.add();
                const pivotSheet = workbook.worksheets.get(pivotSheetIndex);
                const pivotTable = pivotSheet.pivotTables.add("=Sheet1!A1:B7", 2, 2);
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
                pivotTable.calculateData();
                // Show the Amount data field as a percentage of the grand total with the
                // one-call method; PercentageOfTotal takes no base item, so the trailing
                // base arguments (0, 0) are placeholders the format ignores
                const dataField = pivotTable.dataFields.get(0);
                dataField.showValuesAs(AsposeCells.PivotShowValuesAsType.PercentageOfTotal, 0, 0);
                pivotTable.calculateData();
                // Body now reads (underlying values are fractions, shown with the
                // percentage format): Apple 47.62%, Banana 33.33%, Cherry 19.05%, Grand Total 100.00%
                const outputData = workbook.save(SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                const downloadLink = document.getElementById("downloadLink");
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "ShowValuesAsPercentageOfTotal.xlsx";
                downloadLink.style.display = "block";
                document.getElementById("result").innerHTML =
                    '<p style="color: green;">Done! Click the download link to get the result file.</p>';
            });
        </script>
    </body>
</html>
```

## **Получение и настройка PivotField.showValuesSetting**
Прочитайте текущую конфигурацию через `PivotField.showValuesSetting`: свойство только для чтения возвращает объект `PivotShowValuesSetting` поля, свойства которого описывают активное вычисление Show Values As. Чтобы изменить конфигурацию, вызовите метод `PivotField.showValuesAs` — он записывает все настройки одним вызовом, поэтому нет необходимости задавать свойства по отдельности.  
Объект `PivotShowValuesSetting` раскрывает состояние, записываемое `showValuesAs`:
- `showValuesAs` выбирает вторичное вычисление `PivotShowValuesAsType`.  
- `baseFieldIndex` задаёт нулевую индексацию базового поля среди полей сводной таблицы. Он используется в форматах, зависящих от базового поля.  
- `baseItemIndex` задаёт базовый элемент: нулевая индексация конкретного элемента сводной таблицы или одно из двух значений‑sentinel — -1 для предыдущего элемента, -2 для следующего (биндинг не экспортирует именованные константы). Он используется в форматах, зависящих от базового элемента.  
- `baseFieldName` и `baseItemCaption` — только для чтения, предоставляют разрешённые имена базового поля и подпись базового элемента; например, после выбора sentinel‑элемента «предыдущий» `baseItemCaption` возвращает `(previous)`.  
После вызова `showValuesAs` снова вызовите `PivotTable.calculateData()`, чтобы тело сводной таблицы пересчиталось и было отрисовано с обновлённой конфигурацией.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <input type="file" id="fileInput" accept=".xlsx" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>
    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;
        const ready = AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            try {
                await ready;
                const file = document.getElementById('fileInput').files[0];
                if (!file) {
                    throw new Error("Please select ShowValuesAsPercentageOfTotal.xlsx.");
                }
                const workbook = new Workbook(new Uint8Array(await file.arrayBuffer()));
                const worksheet = workbook.worksheets.get(1);
                const pivotTable = worksheet.pivotTables.get(0);
                const dataField = pivotTable.dataFields.get(0);
                // Read the current show-values settings
                const settings = dataField.showValuesSetting;
                const messages = [
                    `ShowValuesAs: ${settings.showValuesAs}`,
                    `BaseFieldIndex: ${settings.baseFieldIndex}`,
                    `BaseItemIndex: ${settings.baseItemIndex}`,
                    `BaseFieldName: ${settings.baseFieldName}`,
                    `BaseItemCaption: ${settings.baseItemCaption}`
                ];
                document.getElementById('result').innerHTML = messages
                    .map(message => `<p>${message}</p>`)
                    .join("");
                // Switch to a base-item calculation with the one-call method: difference
                // from the value of the previous item in the row field
                // (-1 is the previous-item sentinel; the binding does not export the constant)
                dataField.showValuesAs(
                    AsposeCells.PivotShowValuesAsType.DifferenceFrom,
                    pivotTable.rowFields.get(0).baseIndex,
                    -1
                );
                pivotTable.calculateData();
                // Note: the percentage number format saved by the previous example still
                // clings to the data field cells; the underlying values are now differences
                // Re-read the applied configuration
                messages.push(`ShowValuesAs now: ${dataField.showValuesSetting.showValuesAs}`);
                document.getElementById('result').innerHTML = messages
                    .map(message => `<p>${message}</p>`)
                    .join("");
                const outputData = workbook.save(SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                const downloadLink = document.getElementById('downloadLink');
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "ShowValuesAsDifferenceFrom.xlsx";
                downloadLink.style.display = "block";
            } catch (error) {
                document.getElementById('result').innerHTML =
                    `<p style="color: red;">${error.message}</p>`;
            }
        });
    </script>
</html>
```

## **Связанные статьи**
- [Управление полями значений в сводной таблице](/cells/ru/javascript-cpp/manage-value-fields/)
- [Обновление сводной таблицы](/cells/ru/javascript-cpp/refresh-pivot-table/)
- [Применение стиля к сводной таблице](/cells/ru/javascript-cpp/apply-style-to-pivot-table/)

{{< app/cells/assistant language="javascript-cpp" >}}