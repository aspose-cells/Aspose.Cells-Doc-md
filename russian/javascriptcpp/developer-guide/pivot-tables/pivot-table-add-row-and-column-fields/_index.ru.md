---
title: Добавление полей строк и столбцов сводной таблицы в Aspose.Cells for JavaScript via C++
linktitle: Добавление полей строк и столбцов сводной таблицы в Aspose.Cells for JavaScript via C++
description: Узнайте, как добавлять поля строк и столбцов в сводную таблицу и управлять подытогами ее полей с помощью PivotField.SetSubtotals и PivotFieldSubtotalType в Aspose.Cells for JavaScript via C++
keywords: Aspose.Cells, JavaScript via C++, сводная таблица, поле строки, поле столбца, PivotField, setSubtotals, PivotFieldSubtotalType, подытоги, JavaScript, сводная таблица Excel
type: docs
weight: 220
url: /ru/javascript-cpp/pivot-table-add-row-and-column-fields/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Добавление поля в область строк или столбцов**
Метод `pivotTable.addFieldToArea(fieldType, fieldName)` переносит базовое поле из исходных данных в одну из четырех областей сводной таблицы. Аргумент `fieldType` принимает одно из следующих значений `PivotFieldType`.
- `Row` — поля, расположенные вертикально слева
- `Column` — поля, расположенные горизонтально в верхней части
- `Data` — поля, значения которых агрегируются
- `Page` — поля, используемые в качестве фильтров отчета
Порядок вложения полей важен. Если сначала добавить `Category` в область строк, а затем `Item`, получится сводная таблица, в которой внешней группировкой будет `Category`, а внутренней — `Item`. Изменение порядка добавления полей меняет иерархию.

## **Подытоги полей сводной таблицы**
Метод `pivotField.setSubtotals(subtotalType, shown)` управляет отображением строк подытогов для поля сводной таблицы. Каждый вызов независимо включает или отключает один тип подытога. Если `shown = true`, подытог отображается, а если `shown = false` — скрывается. Поскольку каждый вызов затрагивает только один тип, повторные вызовы с различными значениями `subtotalType` позволяют сформировать пользовательский набор подытогов.
Перечисление `PivotFieldSubtotalType` определяет доступные типы подытогов.
- `Automatic` — Aspose.Cells выбирает значение по умолчанию (обычно `Sum` для числовых полей)
- `None` — подавляет все строки подытогов
- `Sum`
- `Count`
- `Average`
- `Max`
- `Min`
- `Product`
- `StdDev`
- `StdDevp`
- `Var`
- `Varp`

{{% alert color="primary" %}}
Подытоги отображаются, только если в области строк (или области столбцов) есть два или более полей сводной таблицы. При наличии одного поля промежуточные группы, для которых можно рассчитать подытог, отсутствуют, поэтому вызовы `setSubtotals` не дают видимого эффекта. Поэтому в каждом примере этой статьи в область строк добавляются два поля (`Category` — внешнее, `Item` — внутреннее), чтобы была видна граница подытога внутри каждой группы `Category`.
{{% /alert %}}

## **Сценарий 1 — автоматические подытоги (по умолчанию)**
Если `setSubtotals` вообще не вызывается, Aspose.Cells применяет значение `Automatic` к числовым полям. В следующем примере это поведение явно подтверждается вызовом `setSubtotals(PivotFieldSubtotalType.Automatic, true)` для внешнего поля `Category`, добавленного в область строк.

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
        const readyPromise = AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            const workbook = new Workbook();
            const worksheet = workbook.worksheets.get(0);
            worksheet.name = "Data";
            const cells = worksheet.cells;
            cells.get(0, 0).value = "Category";
            cells.get(0, 1).value = "Item";
            cells.get(0, 2).value = "Year";
            cells.get(0, 3).value = "Amount";
            cells.get(1, 0).value = "Fruit";
            cells.get(1, 1).value = "Apple";
            cells.get(1, 2).value = 2020;
            cells.get(1, 3).value = 100;
            cells.get(2, 0).value = "Fruit";
            cells.get(2, 1).value = "Apple";
            cells.get(2, 2).value = 2021;
            cells.get(2, 3).value = 150;
            cells.get(3, 0).value = "Fruit";
            cells.get(3, 1).value = "Banana";
            cells.get(3, 2).value = 2020;
            cells.get(3, 3).value = 80;
            cells.get(4, 0).value = "Fruit";
            cells.get(4, 1).value = "Banana";
            cells.get(4, 2).value = 2021;
            cells.get(4, 3).value = 90;
            cells.get(5, 0).value = "Vegetable";
            cells.get(5, 1).value = "Carrot";
            cells.get(5, 2).value = 2020;
            cells.get(5, 3).value = 50;
            cells.get(6, 0).value = "Vegetable";
            cells.get(6, 1).value = "Carrot";
            cells.get(6, 2).value = 2021;
            cells.get(6, 3).value = 60;
            cells.get(7, 0).value = "Vegetable";
            cells.get(7, 1).value = "Daikon";
            cells.get(7, 2).value = 2020;
            cells.get(7, 3).value = 40;
            cells.get(8, 0).value = "Vegetable";
            cells.get(8, 1).value = "Daikon";
            cells.get(8, 2).value = 2021;
            cells.get(8, 3).value = 45;
            const pivotTable = worksheet.pivotTables.add("=A1:D9", 2, 5);
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Category");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Item");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
            const categoryField = pivotTable.rowFields.get(0);
            categoryField.setSubtotals(AsposeCells.PivotFieldSubtotalType.Automatic, true);
            pivotTable.calculateData();
            const outputData = workbook.save(AsposeCells.SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output_automatic.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

## **Сценарий 2 — подавление всех подытогов (None)**
Вызов `setSubtotals(PivotFieldSubtotalType.None, true)` удаляет из сводной таблицы все строки подытогов, оставляя только строки полей и общий итог в нижней части. Это полезно, когда требуется отображать исходные сгруппированные данные без дополнительных строк сводки.

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
            const worksheet = workbook.worksheets.get(0);
            worksheet.name = "Data";
            const headers = ["Category", "Item", "Year", "Amount"];
            for (let j = 0; j < headers.length; j++) {
                worksheet.cells.get(0, j).value = headers[j];
            }
            const data = [
                ["Fruit", "Apple", 2020, 100],
                ["Fruit", "Apple", 2021, 150],
                ["Fruit", "Banana", 2020, 80],
                ["Fruit", "Banana", 2021, 90],
                ["Vegetable", "Carrot", 2020, 50],
                ["Vegetable", "Carrot", 2021, 60],
                ["Vegetable", "Daikon", 2020, 40],
                ["Vegetable", "Daikon", 2021, 45]
            ];
            for (let i = 0; i < data.length; i++) {
                for (let j = 0; j < data[i].length; j++) {
                    worksheet.cells.get(i + 1, j).value = data[i][j];
                }
            }
            const pivotTable = worksheet.pivotTables.add("=A1:D9", 2, 5);
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Category");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Item");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
            const categoryField = pivotTable.rowFields.get(0);
            categoryField.setSubtotals(AsposeCells.PivotFieldSubtotalType.None, true);
            pivotTable.calculateData();
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output_none.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

## **Сценарий 3 — пользовательский набор подытогов (Sum + Average)**
Использование не ограничено одним типом подытога. Каждый вызов `setSubtotals` применяется только к одному типу, поэтому два вызова — один с `Sum`, другой с `Average` — формируют пользовательский набор из двух строк подытогов для каждой группы `Category`.

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
            const worksheet = workbook.worksheets.get(0);
            worksheet.name = "Data";
            const cells = worksheet.cells;
            cells.get("A1").value = "Category";
            cells.get("B1").value = "Item";
            cells.get("C1").value = "Year";
            cells.get("D1").value = "Amount";
            cells.get(1, 0).value = "Fruit";
            cells.get(1, 1).value = "Apple";
            cells.get(1, 2).value = 2020;
            cells.get(1, 3).value = 100;
            cells.get(2, 0).value = "Fruit";
            cells.get(2, 1).value = "Apple";
            cells.get(2, 2).value = 2021;
            cells.get(2, 3).value = 150;
            cells.get(3, 0).value = "Fruit";
            cells.get(3, 1).value = "Banana";
            cells.get(3, 2).value = 2020;
            cells.get(3, 3).value = 80;
            cells.get(4, 0).value = "Fruit";
            cells.get(4, 1).value = "Banana";
            cells.get(4, 2).value = 2021;
            cells.get(4, 3).value = 90;
            cells.get(5, 0).value = "Vegetable";
            cells.get(5, 1).value = "Carrot";
            cells.get(5, 2).value = 2020;
            cells.get(5, 3).value = 50;
            cells.get(6, 0).value = "Vegetable";
            cells.get(6, 1).value = "Carrot";
            cells.get(6, 2).value = 2021;
            cells.get(6, 3).value = 60;
            cells.get(7, 0).value = "Vegetable";
            cells.get(7, 1).value = "Daikon";
            cells.get(7, 2).value = 2020;
            cells.get(7, 3).value = 40;
            cells.get(8, 0).value = "Vegetable";
            cells.get(8, 1).value = "Daikon";
            cells.get(8, 2).value = 2021;
            cells.get(8, 3).value = 45;
            const pivotTables = worksheet.pivotTables;
            const pivotTable = pivotTables.add("=A1:D9", 2, 5);
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Category");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Item");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
            const categoryField = pivotTable.rowFields.get(0);
            categoryField.setSubtotals(AsposeCells.PivotFieldSubtotalType.Sum, true);
            categoryField.setSubtotals(AsposeCells.PivotFieldSubtotalType.Average, true);
            pivotTable.calculateData();
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output_custom.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

## **Краткие выводы**
Три сценария отличаются только вызовами `setSubtotals`. Всё остальное — набор данных, поля и назначенные им области — идентично, что позволяет напрямую сравнивать макеты.
- **Размещение полей.** Метод `pivotTable.addFieldToArea(PivotFieldType.Row, fieldName)` перемещает исходный столбец в указанную область. В пределах одной области порядок вызовов определяет порядок отображения, поэтому первый вызов создает самую внешнюю группу. Для формирования подытогов в одной области требуются два или более полей: при одном поле отсутствуют промежуточные группы, для которых можно рассчитать подытог.
- **Сценарий 1 — автоматические подытоги.** Если `setSubtotals` не вызывается, выбор остается за Excel, который применяет собственный подытог по умолчанию для числовых полей. Вызов `setSubtotals` с `PivotFieldSubtotalType.Automatic` явно фиксирует этот выбор вместо того, чтобы оставлять его неявным.
- **Сценарий 2 — отсутствие подытогов.** Вызов `setSubtotals` с `PivotFieldSubtotalType.None` отключает подытог по умолчанию, поэтому сводная таблица сохраняет строки полей и общий итог, но исключает строки подытогов, которые Excel иначе добавил бы между ними.
- **Сценарий 3 — выбранный набор.** Каждый вызов переключает ровно один тип подытога, при этом параметры разных вызовов накапливаются, а не сбрасывают друг друга. Поэтому после одного вызова с `PivotFieldSubtotalType.Sum` и одного с `PivotFieldSubtotalType.Average` остаются включены оба типа, и сводная таблица отображает подытог `Sum`, подытог `Average` и общий итог.

{{% alert color="primary" %}}
Подытоги применяются не только в области строк. Те же вызовы `setSubtotals` для поля, полученного из `pivotTable.getColumnFields()`, создают те же три макета на оси столбцов, поскольку настройка принадлежит полю сводной таблицы, а не оси, на котором оно расположено.
{{% /alert %}}

## **Связанные статьи**
- [Поля страницы в сводных таблицах](/cells/ru/javascript-cpp/add-page-field-in-pivot-table/)
- [Обновление сводных таблиц в Aspose.Cells for JavaScript via C++](/cells/ru/javascript-cpp/refresh-pivot-table/)
- [Применение стилей к сводным таблицам](/cells/ru/javascript-cpp/apply-style-to-pivot-table/)

{{< app/cells/assistant language="javascript-cpp" >}}