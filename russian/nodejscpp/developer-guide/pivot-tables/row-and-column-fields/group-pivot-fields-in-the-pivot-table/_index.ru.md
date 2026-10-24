---
title: Группировка полей сводной таблицы
linktitle: Группировка полей сводной таблицы
description: Узнайте, как группировать поля строк и столбцов сводной таблицы по временным периодам, таким как месяцы и кварталы, и числовым диапазонам, используя PivotField.Group и PivotFieldGroupOptions в Aspose.Cells for Node.js via C++.
keywords: Aspose.Cells, сводная таблица, группировка полей сводной таблицы, PivotField.Group, PivotFieldGroupOptions, группировка по датам, группировка по числам, месяцы, кварталы, числовые диапазоны, JavaScript
type: docs
weight: 80
url: /ru/nodejs-cpp/group-pivot-fields-in-the-pivot-table/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Возможные сценарии использования**
- Группировка полей сводной таблицы полезна, когда поле строки или столбца сводной таблицы содержит много различных значений, например поле даты с сотнями дат или числовое поле с множеством разрозненных значений. Группировка объединяет эти значения в содержательные разделы: даты — в месяцы, кварталы и годы, а числа — в диапазоны, такие как 0–1, 2–3, 4–5. Это делает большую сводную таблицу компактной и удобной для анализа. Aspose.Cells предоставляет эту возможность через метод `pivotField.group()` (автоматическая группировка по типу данных) и `pivotField.group(PivotFieldGroupOptions)` (пользовательские параметры группировки).
- Группировка по датам сворачивает отдельные даты в более крупные периоды, такие как дни, месяцы, кварталы и годы, и формирует временную иерархию (например, Годы, Кварталы, Месяцы). Тенденции во времени становятся видны с первого взгляда, и каждый уровень периода становится отдельным полем сводной таблицы в области строк или столбцов сводной таблицы.
- Группировка доступна только для полей, размещённых в области СТРОК или СТОЛБЦОВ сводной таблицы. Поле данных (значения) нельзя сгруппировать напрямую. Чтобы сгруппировать такое поле, его сначала необходимо добавить в область строк или столбцов сводной таблицы.

## **Автоматическая группировка полей сводной таблицы**
Безпараметрическая перегрузка `pivotField.group()` определяет тип данных поля и группирует его автоматически. Поле, содержащее только даты (и пустые значения), группируется по месяцам. Поле, содержащее только числа (и пустые значения), группируется в числовые диапазоны с автоматическим интервалом.

```javascript
const AsposeCells = require("aspose.cells.node");
// Загрузить образец рабочей книги
const wb = new AsposeCells.Workbook("sampleGroupPivotFieldsInPivotTable.xlsx");
// Получить доступ ко второму рабочему листу и его сводной таблице
const pt = wb.getWorksheets().get(1).getPivotTables().get(0);
// Сгруппировать первое поле строки автоматически.
// Поле содержит даты, поэтому оно группируется по месяцам.
const field = pt.getRowFields().get(0);
field.group();
// Вычислить данные сводной таблицы и сохранить выходной файл
pt.calculateData();
wb.save("outputAutoGroupPivotField.xlsx");
```

## **Группировка полей сводной таблицы с пользовательскими параметрами**
Класс `PivotFieldGroupOptions` предоставляет пользовательскую конфигурацию группировки. Для полей дат задаются `startDate`, `endDate` и `groupTypes`. Для числовых полей задаются `startNumber`, `endNumber` и `interval`. Свойство `newPivotField` управляет тем, создаёт ли группировка новые поля сводной таблицы рядом с исходным (см. раздел «Примечание» в конце статьи).

### **Группировка поля даты по месяцам и кварталам**
Следующий пример группирует поле даты в строках образца сводной таблицы по месяцам и кварталам в пределах заданных начальной и конечной дат. Код загружает [образец Excel-файла](sampleGroupPivotFieldsInPivotTable.xlsx), выполняет группировку, вычисляет данные сводной таблицы и сохраняет результат группировки. На снимке экрана показан результат: поле даты в строках теперь сгруппировано по кварталам и месяцам.
Обратите внимание, что порядок значений в `options.groupTypes` игнорируется. Независимо от того, в каком порядке перечислены типы групп, сгруппированные поля всегда отображаются от наибольшего периода к наименьшему: годы, кварталы, месяцы, дни, часы, минуты, секунды. В данном примере месяцы перечислены раньше кварталов в `options.groupTypes`, однако кварталы отображаются как внешний уровень, а месяцы — как внутренний.

```javascript
const AsposeCells = require("aspose.cells.node");
let wb = new AsposeCells.Workbook("sampleGroupPivotFieldsInPivotTable.xlsx");
// Получить доступ ко второму рабочему листу и его сводной таблице
let pt = wb.getWorksheets().get(1).getPivotTables().get(0);
// Сгруппировать первое поле строки (поле даты) по месяцам и кварталам
let options = new AsposeCells.PivotFieldGroupOptions();
options.setStartDate(new Date(2008, 0, 1));
options.setEndDate(new Date(2008, 8, 5));
options.setGroupTypes([AsposeCells.PivotGroupByType.Months, AsposeCells.PivotGroupByType.Quarters]);
pt.getRowFields().get(0).group(options);
// Вычислить данные сводной таблицы и сохранить выходной файл
pt.calculateData();
wb.save("outputGroupPivotFieldsInPivotTable.xlsx");
```

![Сводная таблица, сгруппированная по месяцам и кварталам](group-pivot-fields-in-the-pivot-table_1.png)

### **Группировка числового поля в диапазоны**
`FieldTwo` в образце сводной таблицы изначально является полем данных (значения). Поскольку группировать можно только поля строк или столбцов, код сначала вызывает `pivotTable.addFieldToArea(PivotFieldType.Row, "FieldTwo")`, чтобы переместить `FieldTwo` в область строк, обновляет сводную таблицу, а затем группирует числовое поле в диапазоны 0–1, 2–3 и 4–5, используя `startNumber = 0`, `endNumber = 5` и `interval = 2`.

```javascript
const AsposeCells = require("aspose.cells.node");
let wb = new AsposeCells.Workbook("sampleGroupPivotFieldsInPivotTable.xlsx");
// Получить доступ ко второму листу и его сводной таблице
let pt = wb.getWorksheets().get(1).getPivotTables().get(0);
// FieldTwo - это поле данных: сначала переместим его в область строк,
// потому что группировать можно только поля строк/столбцов
pt.addFieldToArea(AsposeCells.PivotFieldType.Row, "FieldTwo");
pt.calculateData();
// Сгруппировать числовое поле в диапазоны 0-1, 2-3, 4-5
let options = new AsposeCells.PivotFieldGroupOptions();
options.setStartNumber(0);
options.setEndNumber(5);
options.setInterval(2);
pt.getRowFields().get(1).group(options);
// Пересчитать данные сводной таблицы и сохранить выходной файл
pt.calculateData();
wb.save("outputNumberGroupPivotField.xlsx");
```

## **Примечание**

{{% alert color="primary" %}}
- Перегрузки метода `pivotField.groupBy()` объявлены устаревшими и удалены из API. Их заменой являются `pivotField.group()` и `pivotField.group(PivotFieldGroupOptions)`.
- В Microsoft Excel группировка числового поля ЗАМЕНЯЕТ исходное поле сводной таблицы на сгруппированные диапазоны, тогда как группировка поля даты создаёт НОВЫЕ поля сводной таблицы (по одному на каждый уровень группировки, например Кварталы и Месяцы) рядом с исходным полем. Начиная с Aspose.Cells 26.10, методы `pivotField.group()` следуют тому же поведению, что и Excel. Свойство `pivotFieldGroupOptions.newPivotField` существует для совместимости со старыми версиями: по умолчанию оно равно false для числовой группировки и true для группировки по дате и времени; установите его в false, если хотите, чтобы группировка по датам заменяла исходное поле сводной таблицы вместо создания новых полей.
- Свойство `pivotFieldGroupOptions.interval` действует только для числовой группировки и для группировки дат по дням (например, группировка дат в 7-дневные периоды); оно игнорируется, когда даты группируются по месяцам, кварталам или годам.
{{% /alert %}}

## **Связанные статьи**
- [Добавление полей строк и столбцов в сводную таблицу](/cells/ru/nodejs-cpp/pivot-table-add-row-and-column-fields/)
- [Фильтрация сводных таблиц по метке или значению](/cells/ru/nodejs-cpp/filter-by-label-or-value-of-pivot-table/)
- [Добавление поля страницы в сводную таблицу](/cells/ru/nodejs-cpp/add-page-field-in-pivot-table/)
- [Применение стиля к сводной таблице](/cells/ru/nodejs-cpp/apply-style-to-pivot-table/)
- [Обновление сводной таблицы](/cells/ru/nodejs-cpp/refresh-pivot-table/)

{{< app/cells/assistant language="nodejs-cpp" >}}