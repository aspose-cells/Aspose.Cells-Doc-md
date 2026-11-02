---
title: Показать значения как в сводной таблице
linktitle: Показать значения как в сводной таблице
description: Отображать значения полей данных сводной таблицы в виде процента от общего итога, разницы от базового элемента, накопительных итогов, рангов и прочего с Aspose.Cells for JavaScript via C++.
keywords: Aspose.Cells, JavaScript via C++, сводная таблица, показать значения как, формат отображения данных, PivotFieldDataDisplayFormat, PercentageOfTotal, PivotShowValuesSetting, CalculationType, BaseFieldIndex
type: docs
weight: 145
url: /ru/javascript-cpp/show-values-as-in-pivot-table/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Возможные сценарии использования**
Сводная таблица обычно агрегирует каждое поле данных с помощью агрегирующей функции, такой как `Sum` или `Count`. Функция **Show Values As** в Excel заменяет каждый отображаемый результат вторичным расчётом, полученным из этой агрегатной функции — например, процентом от общего итога, накопительным итогом, разницей от выбранного базового элемента или рейтингом — что позволяет выполнять сравнительный анализ без вспомогательных формул или вычисляемых столбцов.  
Типичные применения включают анализ доли от общего итога (проценты по строке, столбцу или общему итогу), накопительные отчёты с использованием накопительного итога в поле периода, анализ отклонений от контрольного элемента (разница или процент разницы от базового элемента) и ранжирование значений от наименьшего к наибольшему или наоборот.  
В Aspose.Cells for JavaScript via C++ свойство `PivotFieldDataDisplayFormat` выбирает вторичный расчёт. Только для чтения свойство `PivotField.showValuesSetting` возвращает объект `PivotShowValuesSetting`, у которого записываемые свойства `calculationType`, `baseFieldIndex`, `baseItemPositionType` и `baseItemIndex` задают поведение; удобный метод `PivotField.showValuesAs(...)` применяет те же четыре параметра одним вызовом. Применяйте эти настройки к полю данных или значений, полученному из `PivotTable.dataFields`.

## **Перечисление PivotFieldDataDisplayFormat**
Поле данных сохраняет свою агрегатную функцию, например Sum или Count, тогда как Show Values As изменяет только способ отображения агрегированного значения.  
Помимо непосредственного задания свойств `PivotShowValuesSetting` (см. последний раздел), одноразовый удобный метод применяет ту же конфигурацию:

```html
dataField.showValuesAs(displayFormat, baseField, baseItemPositionType, baseItem);
```

| Параметр | Значение | Требуется когда |
| --- | --- | --- |
| `displayFormat` | Вторичный расчёт `PivotFieldDataDisplayFormat`, который будет применён. | Всегда. |
| `baseField` | Индекс базового поля (нумерация с нуля) среди базовых полей сводной таблицы (например, индекс строкового поля, к которому относится базовый элемент). | Только шесть базовых форматов ниже (`DifferenceFrom`, `PercentageOf`, `PercentageDifferenceFrom`, `RunningTotalIn`, `PercentageOfRunningTotalIn`, `PercentageOfParentTotal`); игнорируется всеми остальными форматами. |
| `baseItemPositionType` | Способ выбора базового элемента относительно текущего: `PivotItemPositionType.Previous`, `.Next` или `.Custom`. | Только три формата базового элемента (`DifferenceFrom`, `PercentageOf`, `PercentageDifferenceFrom`); игнорируется всеми остальными форматами. |
| `baseItem` | Индекс базового элемента (нумерация с нуля). | Только когда `baseItemPositionType` установлен в `Custom` (тогда индекс элемента выбирает точный базовый элемент); игнорируется для `Previous` / `Next` и всех форматов без базового элемента — указывайте `0`. |

| Тип расчёта | Поведение | Параметры базового элемента |
| --- | --- | --- |
| `Normal` | Без вторичного расчёта; агрегированное значение отображается как есть (по умолчанию). | — |
| `DifferenceFrom` | Отображает значение как разницу с значением базового элемента в базовом поле. | `baseField` + `Previous`/`Next`/`Custom` (`baseItem` только при `Custom`) |
| `PercentageOf` | Отображает значение как процент от значения базового элемента в базовом поле. | `baseField` + `Previous`/`Next`/`Custom` (`baseItem` только при `Custom`) |
| `PercentageDifferenceFrom` | Отображает значение как процентную разницу от значения базового элемента в базовом поле. | `baseField` + `Previous`/`Next`/`Custom` (`baseItem` только при `Custom`) |
| `RunningTotalIn` | Отображает значение как накопительный итог для последовательных элементов базового поля. | `baseField` (поле, определяющее порядок элементов для накопления) |
| `PercentageOfRow` | Отображает значение как процент от итога строки. | — |
| `PercentageOfColumn` | Отображает значение как процент от итога столбца. | — |
| `PercentageOfTotal` | Отображает значение как процент от общего итога. | — |
| `Index` | Отображает значение по формуле Excel Index ((value * grand total) / (row total * column total)). | — |
| `PercentageOfParentRowTotal` | Отображает значение как процент от итоговой суммы родительской строки (для вложенных строковых полей). | — |
| `PercentageOfParentColumnTotal` | Отображает значение как процент от итоговой суммы родительского столбца (для вложенных столбцовых полей). | — |
| `PercentageOfParentTotal` | Отображает значение как процент от итоговой суммы родителя. | `baseField` (базовое родительское поле) |
| `PercentageOfRunningTotalIn` | Отображает значение как процент от накопительного итога в базовом поле. | `baseField` (поле накопления) |
| `RankSmallestToLargest` | Ранжирует значение от наименьшего (1) к наибольшему. | — |
| `RankLargestToSmallest` | Ранжирует значение от наибольшего (1) к наименьшему. | — |

{{% alert color="primary" %}}
`showValuesAs(...)` записывает свойства объекта `PivotShowValuesSetting` (`calculationType`, `baseFieldIndex`, `baseItemPositionType`, `baseItemIndex`) — метод и объект‑свойство представляют два способа конфигурировать одно и то же состояние, аналогично выбору базового поля и базового элемента в диалоговом окне Excel **Show Values As**.
{{% /alert %}}

## **Показать значения как процент от общего итога**
Вызовите метод `PivotField.showValuesAs` с параметром `PivotFieldDataDisplayFormat.PercentageOfTotal`, чтобы преобразовать каждую ячейку поля данных, включая общий итог, в её долю от общего итога. Отображаемые числа тогда представляют собой доли от полного результирующего набора. Этот формат измеряет каждое значение только относительно общего итога, поэтому не требует указания базового поля или базового элемента — добавочные аргументы (`0`, `PivotItemPositionType.Previous`, `0`) являются заполнительными и игнорируются форматом, как указано в таблице параметров.

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
                // base arguments (0, Previous, 0) are placeholders the format ignores
                const dataField = pivotTable.dataFields.get(0);
                dataField.showValuesAs(
                    AsposeCells.PivotFieldDataDisplayFormat.PercentageOfTotal,
                    0,
                    AsposeCells.PivotItemPositionType.Previous,
                    0
                );
                pivotTable.calculateData();
                // Body now reads: Apple 47.62%, Banana 33.33%, Cherry 19.05%, Grand Total 100.00%
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

## **Чтение и настройка PivotField.showValuesSetting**
Получите текущую конфигурацию через `PivotField.showValuesSetting`: только‑для‑чтения свойство возвращает объект `PivotShowValuesSetting` поля, у которого четыре свойства описывают активный расчёт Show Values As. Чтобы изменить конфигурацию, вызовите метод `PivotField.showValuesAs` — он записывает все четыре настройки одним вызовом, поэтому задавать свойства по отдельности не требуется.  
Объект `PivotShowValuesSetting` раскрывает четыре свойства, которые записывает `showValuesAs`:
- `calculationType` выбирает вторичный расчёт `PivotFieldDataDisplayFormat`.
- `baseFieldIndex` задаёт индекс базового поля (нумерация с нуля) среди полей сводной таблицы. Используется базовыми форматами.
- `baseItemPositionType` определяет позицию базового элемента относительно текущего и принимает значения `PivotItemPositionType.Next`, `PivotItemPositionType.Previous` или `PivotItemPositionType.Custom`.
- `baseItemIndex` задаёт индекс базового элемента (нумерация с нуля) и используется, когда `baseItemPositionType` установлен в `Custom`.  
После вызова `showValuesAs` вызовите `PivotTable.calculateData()` заново, чтобы тело сводной таблицы пересчиталось и отобразилось с обновлённой конфигурацией.

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
                    `CalculationType: ${settings.calculationType}`,
                    `BaseFieldIndex: ${settings.baseFieldIndex}`,
                    `BaseItemPositionType: ${settings.baseItemPositionType}`,
                    `BaseItemIndex: ${settings.baseItemIndex}`
                ];
                document.getElementById('result').innerHTML = messages
                    .map(message => `<p>${message}</p>`)
                    .join("");
                // Switch to a base-item calculation with the one-call method: difference
                // from the value of the previous item in the row field
                dataField.showValuesAs(
                    AsposeCells.PivotFieldDataDisplayFormat.DifferenceFrom,
                    pivotTable.rowFields.get(0).baseIndex,
                    AsposeCells.PivotItemPositionType.Previous,
                    0
                );
                pivotTable.calculateData();
                // Note: the percentage number format saved by the previous example still
                // clings to the data field cells; the underlying values are now differences
                // Re-read the applied configuration
                messages.push(`CalculationType now: ${dataField.showValuesSetting.calculationType}`);
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