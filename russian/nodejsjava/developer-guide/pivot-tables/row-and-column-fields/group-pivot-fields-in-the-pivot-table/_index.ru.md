---
title: Группировка полей в сводной таблице
linktitle: Группировка полей в сводной таблице
description: Узнайте, как группировать поля строк и столбцов сводной таблицы в периоды дат, такие как месяцы и кварталы, и числовые диапазоны с помощью PivotField.group и PivotFieldGroupOptions в Aspose.Cells for Node.js via Java.
keywords: Aspose.Cells, сводная таблица, группировка полей сводной таблицы, PivotField.group, PivotFieldGroupOptions, группировка по датам, группировка по числам, месяцы, кварталы, числовые диапазоны, Node.js
type: docs
weight: 80
url: /ru/nodejs-java/group-pivot-fields-in-the-pivot-table/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Возможные сценарии использования**
- Группировка полей сводной таблицы полезна, когда поле строки или столбца сводной таблицы содержит много различных элементов, например поле дат с сотнями дат или числовое поле с множеством разрозненных значений. Группировка объединяет эти элементы в осмысленные секции: даты — в месяцы, кварталы и годы, а числа — в диапазоны, такие как 0-1, 2-3, 4-5. Это делает большую сводную таблицу компактной и более удобной для анализа. Aspose.Cells for Node.js via Java предоставляет эту возможность через метод `PivotField.group()` (автоматическая группировка по типу данных) и `PivotField.group(PivotFieldGroupOptions)` (пользовательские параметры группировки).
- Группировка по датам объединяет отдельные даты в более крупные периоды, такие как дни, месяцы, кварталы и годы, и формирует иерархию времени (например, Годы, Кварталы, Месяцы). Тенденции во времени становятся видны с первого взгляда, и каждый уровень периода становится отдельным полем сводной таблицы в области строк или столбцов сводной таблицы.
- Группировка доступна только для полей, размещённых в области СТРОК или СТОЛБЦОВ сводной таблицы. Поле данных (значения) не может быть сгруппировано напрямую. Чтобы сгруппировать такое поле, его необходимо сначала добавить в область строк или столбцов сводной таблицы.

## **Автоматическая группировка полей сводной таблицы**
Перегрузка `PivotField.group()` без параметров проверяет тип данных поля и группирует его автоматически. Поле, содержащее только даты (и пустые значения), группируется по месяцам. Поле, содержащее только числа (и пустые значения), группируется в числовые диапазоны с использованием автоматического интервала.

```javascript
const AsposeCells = require("aspose.cells");
let wb = new AsposeCells.Workbook("sampleGroupPivotFieldsInPivotTable.xlsx");
// Получаем доступ ко второму рабочему листу и его сводной таблице
let pt = wb.getWorksheets().get(1).getPivotTables().get(0);
// Автоматически группируем первое поле строки.
// Поле содержит даты, поэтому оно группируется по месяцам.
let field = pt.getRowFields().get(0);
field.group();
// Вычисляем данные сводной таблицы и сохраняем выходной файл
pt.calculateData();
wb.save("outputAutoGroupPivotField.xlsx");
```

## **Группировка полей сводной таблицы с пользовательскими параметрами**
Класс `PivotFieldGroupOptions` предоставляет пользовательскую конфигурацию группировки. Для полей дат задайте `StartDate`, `EndDate` и `GroupTypes`. Для числовых полей задайте `StartNumber`, `EndNumber` и `Interval`. Свойство `NewPivotField` управляет тем, создаёт ли группировка новые поля сводной таблицы рядом с исходным (см. раздел Примечание в конце этой статьи).

### **Группировка поля дат по месяцам и кварталам**
Следующий пример группирует поле дат строки образца сводной таблицы по месяцам и кварталам между начальной и конечной датами. Код загружает [образец файла Excel](sampleGroupPivotFieldsInPivotTable.xlsx), выполняет группировку, вычисляет данные сводной таблицы и сохраняет сгруппированный результат. Снимок экрана показывает эффект: поле дат строки теперь сгруппировано по кварталам и месяцам.
Обратите внимание, что порядок значений в `options.GroupTypes` игнорируется. Независимо от того, в каком порядке перечислены типы групп, сгруппированные поля всегда отображаются от самого крупного периода к самому мелкому: годы, кварталы, месяцы, дни, часы, минуты, секунды. В этом примере месяцы перечислены перед кварталами в `options.GroupTypes`, однако кварталы отображаются как внешний уровень, а месяцы — как внутренний уровень.

```javascript
const AsposeCells = require("aspose.cells");
// Загрузить образец книги
const wb = new AsposeCells.Workbook("sampleGroupPivotFieldsInPivotTable.xlsx");
// Получить доступ ко второму рабочему листу и его сводной таблице
const pt = wb.getWorksheets().get(1).getPivotTables().get(0);
// Сгруппировать первое поле строки (поле даты) по месяцам и кварталам
const options = new AsposeCells.PivotFieldGroupOptions();
options.setStartDate(new Date(2008, 0, 1));
options.setEndDate(new Date(2008, 8, 5));
options.setGroupTypes([AsposeCells.PivotGroupByType.MONTHS, AsposeCells.PivotGroupByType.QUARTERS]);
pt.getRowFields().get(0).group(options);
// Рассчитать данные сводной таблицы и сохранить выходной файл
pt.calculateData();
wb.save("outputGroupPivotFieldsInPivotTable.xlsx");
```

![Сводная таблица, сгруппированная по месяцам и кварталам](group-pivot-fields-in-the-pivot-table_1.png)

### **Группировка числового поля в диапазоны**
`FieldTwo` образца сводной таблицы изначально является полем данных (значения). Поскольку группировать можно только поля строк или столбцов, код сначала вызывает `pivotTable.addFieldToArea(PivotFieldType.Row, "FieldTwo")`, чтобы переместить `FieldTwo` в область строк, обновляет сводную таблицу, а затем группирует числовое поле в диапазоны 0-1, 2-3 и 4-5, используя `StartNumber = 0`, `EndNumber = 5` и `Interval = 2`.

```javascript
const AsposeCells = require("aspose.cells");
// Загрузить образец книги
const wb = new AsposeCells.Workbook("sampleGroupPivotFieldsInPivotTable.xlsx");
// Получить доступ ко второму листу и его сводной таблице
const pt = wb.getWorksheets().get(1).getPivotTables().get(0);
// FieldTwo — поле данных: сначала переместить его в область строк,
// поскольку группировать можно только поля строк/столбцов
pt.addFieldToArea(AsposeCells.PivotFieldType.ROW, "FieldTwo");
pt.calculateData();
// Сгруппировать числовое поле в диапазоны 0-1, 2-3, 4-5
const options = new AsposeCells.PivotFieldGroupOptions();
options.setStartNumber(0);
options.setEndNumber(5);
options.setInterval(2);
pt.getRowFields().get(1).group(options);
// Вычислить данные сводной таблицы и сохранить выходной файл
pt.calculateData();
wb.save("outputNumberGroupPivotField.xlsx");
```

## **Примечание**

{{% alert color="primary" %}}
- Перегрузки метода `PivotField.GroupBy()` устарели и удалены из поверхности API. Их заменили `PivotField.group()` и `PivotField.group(PivotFieldGroupOptions)`.
- В Microsoft Excel группировка числового поля ЗАМЕНЯЕТ исходное поле сводной таблицы сгруппированными диапазонами, тогда как группировка поля дат создаёт НОВЫЕ поля сводной таблицы (по одному на каждый уровень группы, например Кварталы и Месяцы) рядом с исходным полем. Начиная с Aspose.Cells for Node.js via Java 26.10, методы `PivotField.group()` следуют тому же поведению, что и Excel. Свойство `PivotFieldGroupOptions.NewPivotField` существует для совместимости со старыми версиями: по умолчанию оно равно false для числовой группировки и true для группировки по дате и времени; установите его в false, если хотите, чтобы группировка по датам заменяла исходное поле сводной таблицы вместо создания новых полей сводной таблицы.
- Свойство `PivotFieldGroupOptions.Interval` действует только для числовой группировки и для группировки дат по дням (например, группировка дат в 7-дневные периоды); оно игнорируется, когда даты группируются по месяцам, кварталам или годам.
{{% /alert %}}

## **Связанные статьи**
- [Добавление полей строк и столбцов в сводной таблице](/cells/ru/nodejs-java/pivot-table-add-row-and-column-fields/)
- [Фильтрация сводных таблиц по метке или значению](/cells/ru/nodejs-java/filter-by-label-or-value-of-pivot-table/)
- [Добавление поля страницы в сводной таблице](/cells/ru/nodejs-java/add-page-field-in-pivot-table/)
- [Применение стиля к сводной таблице](/cells/ru/nodejs-java/apply-style-to-pivot-table/)
- [Обновление сводной таблицы](/cells/ru/nodejs-java/refresh-pivot-table/)

{{< app/cells/assistant language="nodejs-java" >}}