---
title: Вставка сводной таблицы
linktitle: Вставка сводной таблицы
description: Создание и форматирование сводных таблиц в файлах Excel.
keywords: Создание сводной таблицы, Вставка сводной таблицы, Форматирование сводной таблицы.
type: docs
weight: 160
url: /ru/net/create-pivot-table/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Что такое сводная таблица?**
Сводная таблица — это интерактивный отчет для обобщения данных: она сводит большой массив необработанных данных, расположенных построчно, в компактную матрицу без единой формулы. Вы выбираете, какие столбцы станут метками строк, какие — метками столбцов, а какие будут использоваться в качестве агрегируемых значений: сводная таблица выполняет группировку и расчеты:
- **Обобщение** — общий объем продаж по каждому продукту, региону или кварталу вместо длинных цепочек формул.
- **Сравнение** — категории в строках и периоды в столбцах превращают плоский список в перекрестный отчет, в котором тенденции видны с первого взгляда.
- **Детализация** — дважды щелкните по любому итоговому значению, чтобы изучить исходные строки, на основе которых оно рассчитано.
- **Обновление** — при изменении исходных данных одно обновление пересчитывает весь отчет.
Типичные сценарии применения — дашборды продаж, разбивка расходов и анализ запасов; с их помощью можно ответить на любой вопрос вида «как эти показатели распределяются по категориям и периодам?». Aspose.Cells for .NET программным способом создает аналогичные сводные таблицы, поэтому рабочие книги, формируемые вашим приложением, могут содержать готовые отчеты, а не только необработанные данные.

### **Объектная модель сводной таблицы**
Aspose.Cells предоставляет специальный набор классов в namespace [**Aspose.Cells.Pivot**](https://reference.aspose.com/cells/net/aspose.cells.pivot), которые используются для создания сводных таблиц и управления ими. Эти классы применяются для создания и настройки объектов [**PivotTable**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable), являющихся основными компонентами сводной таблицы. Эти объекты:
- [**PivotField**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfield) представляет поле объекта [**PivotTable**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable).
- [**PivotFieldCollection**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfieldcollection) представляет коллекцию всех объектов [**PivotField**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfield) в объекте [**PivotTable**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable).
- [**PivotTable**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable) представляет сводную таблицу на рабочем листе.
- [**PivotTableCollection**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottablecollection) представляет коллекцию всех объектов [**PivotTable**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable) на рабочем листе.

### **Создание простой сводной таблицы с помощью Aspose.Cells**
Создание сводной таблицы выполняется в три этапа: запись исходных данных в ячейки рабочего листа, добавление сводной таблицы в указанное место и размещение полей сводной таблицы в областях строк, столбцов и данных.
1. Добавьте данные в рабочий лист с помощью метода [**PutValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/putvalue/index) объекта [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell). Эти данные будут использоваться в качестве источника данных сводной таблицы.
2. Добавьте сводную таблицу в рабочий лист, вызвав метод [**Add**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottablecollection/methods/add/index) коллекции [**PivotTables**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottablecollection): `Add(sourceData, row, column)`. `sourceData` — исходный диапазон (например, "A1:C8"); `row` и `column` — координаты ячейки назначения в левом верхнем углу сводной таблицы с нулевым отсчетом (ячейка E3 соответствует строке 2 и столбцу 4). Метод напрямую возвращает новый объект [**PivotTable**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable).
3. Разместите поля сводной таблицы с помощью метода `AddFieldToArea` объекта [**PivotTable**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable): передайте имя поля в область строк (`PivotFieldType.Row`), область столбцов (`PivotFieldType.Column`) или область данных (`PivotFieldType.Data`).
4. Сохраните рабочую книгу — сводная таблица будет записана в сохраненный файл.
После выполнения примера кода в рабочий лист добавляется сводная таблица.

```csharp
using Aspose.Cells;
using Aspose.Cells.Pivot;

// Создать новую книгу и получить первый лист
Workbook workbook = new Workbook();
Worksheet sheet = workbook.Worksheets[0];

// Записать исходные данные: продажи по видам спорта и кварталам
sheet.Cells["A1"].PutValue("Sport");
sheet.Cells["B1"].PutValue("Quarter");
sheet.Cells["C1"].PutValue("Sales");
sheet.Cells["A2"].PutValue("Golf");
sheet.Cells["B2"].PutValue("Qtr3");
sheet.Cells["C2"].PutValue(1500);
sheet.Cells["A3"].PutValue("Golf");
sheet.Cells["B3"].PutValue("Qtr4");
sheet.Cells["C3"].PutValue(2000);
sheet.Cells["A4"].PutValue("Tennis");
sheet.Cells["B4"].PutValue("Qtr3");
sheet.Cells["C4"].PutValue(600);
sheet.Cells["A5"].PutValue("Tennis");
sheet.Cells["B5"].PutValue("Qtr4");
sheet.Cells["C5"].PutValue(1500);
sheet.Cells["A6"].PutValue("Tennis");
sheet.Cells["B6"].PutValue("Qtr3");
sheet.Cells["C6"].PutValue(4070);
sheet.Cells["A7"].PutValue("Tennis");
sheet.Cells["B7"].PutValue("Qtr4");
sheet.Cells["C7"].PutValue(5000);
sheet.Cells["A8"].PutValue("Golf");
sheet.Cells["B8"].PutValue("Qtr3");
sheet.Cells["C8"].PutValue(6430);

// Добавить сводную таблицу в ячейку назначения E3 на основе A1:C8
PivotTable pivotTable = sheet.PivotTables.Add("A1:C8", 2, 4);

// Назначить поля сводной таблицы: Sport в строки, Quarter в столбцы, Sales в данные
pivotTable.AddFieldToArea(PivotFieldType.Row, "Sport");
pivotTable.AddFieldToArea(PivotFieldType.Column, "Quarter");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Sales");

// Сохранить книгу
workbook.Save("pivotTable_test_out.xlsx");
```

{{% alert color="primary" %}}
При назначении диапазона ячеек в качестве источника данных диапазон должен проходить от левого верхнего угла к правому нижнему. Например, "A1:C3" корректен, а "C3:A1" — нет.
{{% /alert %}}

## Связанные статьи
- [Добавление полей фильтра в сводную таблицу в Aspose.Cells for .NET](/cells/ru/net/add-page-field-in-pivot-table/)
- [Применение стилей к сводным таблицам в Aspose.Cells for .NET](/cells/ru/net/apply-style-to-pivot-table/)
- [Изменение макета поля страницы в сводной таблице](/cells/ru/net/change-page-field-layout/)
- [Фильтрация сводных таблиц по метке или значению](/cells/ru/net/filter-by-label-or-value-of-pivot-table/)
- [Управление полями значений сводной таблицы в Aspose.Cells for .NET](/cells/ru/net/manage-value-fields/)

{{< app/cells/assistant language="csharp" >}}