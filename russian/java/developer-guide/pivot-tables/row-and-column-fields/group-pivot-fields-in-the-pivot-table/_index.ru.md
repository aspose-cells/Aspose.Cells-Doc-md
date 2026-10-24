---
title: Группировка полей в сводной таблице
linktitle: Группировка полей в сводной таблице
description: Узнайте, как группировать поля строк и столбцов в сводной таблице по временным периодам, таким как месяцы и кварталы, а также в числовые диапазоны с помощью PivotField.group и PivotFieldGroupOptions в Aspose.Cells for Java.
keywords: Aspose.Cells, сводная таблица, группировка поля сводной таблицы, PivotField.group, PivotFieldGroupOptions, группировка по дате, группировка по числам, месяцы, кварталы, числовой диапазон, Java
type: docs
weight: 80
url: /ru/java/group-pivot-fields-in-the-pivot-table/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Возможные сценарии использования**
- Группировка полей сводной таблицы полезна, когда поле строки или столбца сводной таблицы содержит множество различных элементов, например поле даты с сотнями дат или числовое поле со множеством разрозненных значений. Группировка объединяет эти элементы в осмысленные секции: даты — в месяцы, кварталы и годы, а числа — в диапазоны, такие как 0-1, 2-3, 4-5. Это делает большую сводную таблицу компактной и удобной для анализа. Aspose.Cells предоставляет эту возможность через метод `PivotField.group()` (автоматическая группировка по типу данных) и `PivotField.group(PivotFieldGroupOptions)` (пользовательские параметры группировки).
- Группировка по датам объединяет отдельные даты в более крупные периоды, такие как дни, месяцы, кварталы и годы, и формирует иерархию времени (например, Годы, Кварталы, Месяцы). Тенденции во времени становятся видны с одного взгляда, и каждый уровень периода становится отдельным полем сводной таблицы в области строк или столбцов сводной таблицы.
- Группировка доступна только для полей, размещённых в области СТРОК или СТОЛБЦОВ сводной таблицы. Поле данных (значения) нельзя сгруппировать напрямую. Чтобы сгруппировать такое поле, необходимо сначала добавить его в область строк или столбцов сводной таблицы.

## **Автоматическая группировка полей сводной таблицы**
Перегрузка `PivotField.group()` без параметров проверяет тип данных поля и группирует его автоматически. Поле, содержащее только даты (и пустые значения), группируется по месяцам. Поле, содержащее только числа (и пустые значения), группируется в числовые диапазоны с использованием автоматического интервала.

```java
import com.aspose.cells.*;
Workbook wb = new Workbook("sampleGroupPivotFieldsInPivotTable.xlsx");
PivotTable pt = wb.getWorksheets().get(1).getPivotTables().get(0);
PivotField field = pt.getRowFields().get(0);
field.group();
pt.calculateData();
wb.save("outputAutoGroupPivotField.xlsx");
```

## **Группировка полей сводной таблицы с пользовательскими параметрами**
Класс `PivotFieldGroupOptions` предоставляет пользовательскую конфигурацию группировки. Для полей дат задайте `startDate`, `endDate` и `groupTypes`. Для числовых полей задайте `startNumber`, `endNumber` и `interval`. Свойство `newPivotField` управляет тем, создаёт ли группировка новые поля сводной таблицы рядом с исходным (см. раздел Примечание в конце этой статьи).

### **Группировка поля даты по месяцам и кварталам**
Следующий пример группирует поле даты строки образца сводной таблицы по месяцам и кварталам между начальной и конечной датами. Код загружает [образец Excel-файла](sampleGroupPivotFieldsInPivotTable.xlsx), выполняет группировку, вычисляет данные сводной таблицы и сохраняет сгруппированный результат. Снимок экрана показывает эффект: поле даты строки теперь сгруппировано по кварталам и месяцам.
Обратите внимание, что порядок значений в `options.groupTypes` игнорируется. Независимо от того, в каком порядке перечислены типы групп, сгруппированные поля всегда отображаются от наибольшего периода к наименьшему: годы, кварталы, месяцы, дни, часы, минуты, секунды. В этом примере месяцы перечислены перед кварталами в `options.groupTypes`, однако кварталы отображаются как внешний уровень, а месяцы — как внутренний уровень.

```java
import com.aspose.cells.*;
Workbook wb = new Workbook("sampleGroupPivotFieldsInPivotTable.xlsx");
PivotTable pt = wb.getWorksheets().get(1).getPivotTables().get(0);
PivotFieldGroupOptions options = new PivotFieldGroupOptions();
options.setStartDate(new com.aspose.cells.DateTime(2008, 1, 1));
options.setEndDate(new com.aspose.cells.DateTime(2008, 9, 5));
options.setGroupTypes(new int[] { PivotGroupByType.MONTHS, PivotGroupByType.QUARTERS });
pt.getRowFields().get(0).group(options);
pt.calculateData();
wb.save("outputGroupPivotFieldsInPivotTable.xlsx");
```

![Сводная таблица, сгруппированная по месяцам и кварталам](group-pivot-fields-in-the-pivot-table_1.png)

### **Группировка числового поля в диапазоны**
`FieldTwo` образца сводной таблицы изначально является полем данных (значения). Поскольку группировать можно только поля строк или столбцов, код сначала вызывает `PivotTable.addFieldToArea(PivotFieldType.ROW, "FieldTwo")`, чтобы переместить `FieldTwo` в область строк, обновляет сводную таблицу, а затем группирует числовое поле в диапазоны 0-1, 2-3 и 4-5 с использованием `startNumber = 0`, `endNumber = 5` и `interval = 2`.

```java
import com.aspose.cells.*;
// Загружаем образец книги
Workbook wb = new Workbook("sampleGroupPivotFieldsInPivotTable.xlsx");
// Получаем доступ ко второму листу и его сводной таблице
PivotTable pt = wb.getWorksheets().get(1).getPivotTables().get(0);
// FieldTwo - это поле данных: сначала перемещаем его в область строк,
// поскольку группировать можно только поля строк/столбцов
pt.addFieldToArea(PivotFieldType.ROW, "FieldTwo");
pt.calculateData();
// Группируем числовое поле по диапазонам 0-1, 2-3, 4-5
PivotFieldGroupOptions options = new PivotFieldGroupOptions();
options.setStartNumber(0);
options.setEndNumber(5);
options.setInterval(2);
pt.getRowFields().get(1).group(options);
// Вычисляем данные сводной таблицы и сохраняем выходной файл
pt.calculateData();
wb.save("outputNumberGroupPivotField.xlsx");
```

## **Примечание**

{{% alert color="primary" %}}
- Перегрузки метода `PivotField.groupBy()` устарели и удалены из API. `PivotField.group()` и `PivotField.group(PivotFieldGroupOptions)` являются их заменой.
- В Microsoft Excel группировка числового поля ЗАМЕНЯЕТ исходное поле сводной таблицы на сгруппированные диапазоны, тогда как группировка поля даты создаёт НОВЫЕ поля сводной таблицы (по одному на каждый уровень группы, например Кварталы и Месяцы) рядом с исходным полем. Начиная с Aspose.Cells 26.10 методы `PivotField.group()` следуют тому же поведению, что и Excel. Свойство `PivotFieldGroupOptions.newPivotField` существует для совместимости со старыми версиями: по умолчанию оно равно false для числовой группировки и true для группировки по дате и времени; установите его в false, если хотите, чтобы группировка по дате заменяла исходное поле сводной таблицы вместо создания новых полей сводной таблицы.
- Свойство `PivotFieldGroupOptions.interval` действует только для числовой группировки и для группировки дат по дням (например, группировка дат в 7-дневные периоды); оно игнорируется, когда даты группируются по месяцам, кварталам или годам.
{{% /alert %}}

## **Связанные статьи**
- [Добавление полей строк и столбцов в сводной таблице](/cells/ru/java/pivot-table-add-row-and-column-fields/)
- [Фильтрация сводных таблиц по метке или значению](/cells/ru/java/filter-by-label-or-value-of-pivot-table/)
- [Добавление поля страницы в сводной таблице](/cells/ru/java/add-page-field-in-pivot-table/)
- [Применение стиля к сводной таблице](/cells/ru/java/apply-style-to-pivot-table/)
- [Обновление сводной таблицы](/cells/ru/java/refresh-pivot-table/)

{{< app/cells/assistant language="java" >}}