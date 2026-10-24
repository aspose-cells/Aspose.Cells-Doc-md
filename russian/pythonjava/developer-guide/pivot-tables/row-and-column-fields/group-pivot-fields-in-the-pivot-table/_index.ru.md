---
title: Группировка полей сводной таблицы
linktitle: Группировка полей сводной таблицы
description: Узнайте, как группировать поля строк и столбцов сводной таблицы по временным периодам, таким как месяцы и кварталы, а также по числовым диапазонам с помощью PivotField.group и PivotFieldGroupOptions в Aspose.Cells for Python via Java.
keywords: Aspose.Cells, сводная таблица, группировка поля сводной таблицы, PivotField.group, PivotFieldGroupOptions, группировка по дате, группировка по числам, месяцы, кварталы, числовой диапазон, Python
type: docs
weight: 80
url: /ru/python-java/group-pivot-fields-in-the-pivot-table/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Возможные сценарии использования**
- Группировка полей сводной таблицы полезна, когда поле строки или столбца сводной таблицы содержит множество различных элементов, например поле даты с сотнями дат или числовое поле с множеством разрозненных значений. Группировка объединяет эти элементы в значимые разделы: даты — в месяцы, кварталы и годы, а числа — в диапазоны, такие как 0–1, 2–3, 4–5. Это делает большую сводную таблицу компактной и удобной для анализа. Aspose.Cells предоставляет такую возможность через метод `PivotField.group()` (автоматическая группировка по типу данных) и `PivotField.group(PivotFieldGroupOptions)` (пользовательские параметры группировки).
- Группировка по датам сводит отдельные даты к более крупным периодам, таким как дни, месяцы, кварталы и годы, и формирует иерархию времени (например, Годы, Кварталы, Месяцы). Тенденции во времени становятся видны с первого взгляда, и каждый уровень периода становится отдельным полем сводной таблицы в области строк или столбцов.
- Группировка доступна только для полей, размещённых в области СТРОК или СТОЛБЦОВ сводной таблицы. Поле данных (значений) нельзя сгруппировать напрямую. Чтобы сгруппировать такое поле, его необходимо сначала добавить в область строк или столбцов сводной таблицы.

## **Автоматическая группировка полей сводной таблицы**
Перегрузка `PivotField.group()` без параметров определяет тип данных поля и группирует его автоматически. Поле, содержащее только даты (и пустые значения), группируется по месяцам. Поле, содержащее только числа (и пустые значения), группируется в числовые диапазоны с использованием автоматического интервала.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
# Загрузить образец рабочей книги
wb = Workbook("sampleGroupPivotFieldsInPivotTable.xlsx")
# Получить доступ ко второму рабочему листу и его сводной таблице
pt = wb.getWorksheets().get(1).getPivotTables().get(0)
# Сгруппировать первое поле строки автоматически.
# Поле содержит даты, поэтому оно группируется по месяцам.
field = pt.getRowFields().get(0)
field.group()
# Вычислить данные сводной таблицы и сохранить выходной файл
pt.calculateData()
wb.save("outputAutoGroupPivotField.xlsx")
jpype.shutdownJVM()
```

## **Группировка полей сводной таблицы с пользовательскими параметрами**
Класс `PivotFieldGroupOptions` предоставляет пользовательскую конфигурацию группировки. Для полей с датами задайте `StartDate`, `EndDate` и `GroupTypes`. Для числовых полей задайте `StartNumber`, `EndNumber` и `Interval`. Свойство `NewPivotField` управляет тем, создаёт ли группировка новые поля сводной таблицы рядом с исходным (см. раздел Примечание в конце статьи).

### **Группировка поля даты по месяцам и кварталам**
Следующий пример группирует поле строки с датами в образце сводной таблицы по месяцам и кварталам в пределах начальной и конечной даты. Код загружает [образец файла Excel](sampleGroupPivotFieldsInPivotTable.xlsx), выполняет группировку, вычисляет данные сводной таблицы и сохраняет результат группировки. На снимке экрана показан результат: поле строки с датами теперь сгруппировано по кварталам и месяцам.
Обратите внимание, что порядок значений в `options.GroupTypes` игнорируется. Независимо от того, в каком порядке перечислены типы групп, сгруппированные поля всегда отображаются от самого крупного периода к самому мелкому: годы, кварталы, месяцы, дни, часы, минуты, секунды. В этом примере месяцы указаны раньше кварталов в `options.GroupTypes`, однако кварталы отображаются как внешний уровень, а месяцы — как внутренний.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, PivotFieldGroupOptions, PivotGroupByType, DateTime
# Загрузить образец книги
wb = Workbook("sampleGroupPivotFieldsInPivotTable.xlsx")
# Получить доступ ко второму рабочему листу и его сводной таблице
pt = wb.getWorksheets().get(1).getPivotTables().get(0)
# Сгруппировать первое поле строки (поле даты) по месяцам и кварталам
options = PivotFieldGroupOptions()
options.setStartDate(DateTime(2008, 1, 1))
options.setEndDate(DateTime(2008, 9, 5))
options.setGroupTypes([PivotGroupByType.MONTHS, PivotGroupByType.QUARTERS])
pt.getRowFields().get(0).group(options)
# Вычислить данные сводной таблицы и сохранить выходной файл
pt.calculateData()
wb.save("outputGroupPivotFieldsInPivotTable.xlsx")
jpype.shutdownJVM()
```

![Сводная таблица сгруппирована по месяцам и кварталам](group-pivot-fields-in-the-pivot-table_1.png)

### **Группировка числового поля в диапазоны**
`FieldTwo` в образце сводной таблицы изначально является полем данных (значений). Поскольку группировать можно только поля строк или столбцов, код сначала вызывает `pivotTable.addFieldToArea(PivotFieldType.ROW, "FieldTwo")`, чтобы переместить `FieldTwo` в область строк, обновляет сводную таблицу, а затем группирует числовое поле в диапазоны 0–1, 2–3 и 4–5, используя `StartNumber = 0`, `EndNumber = 5` и `Interval = 2`.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, PivotFieldType, PivotFieldGroupOptions
# Загрузить образец книги
wb = Workbook("sampleGroupPivotFieldsInPivotTable.xlsx")
# Получить доступ ко второму рабочему листу и его сводной таблице
pt = wb.getWorksheets().get(1).getPivotTables().get(0)
# FieldTwo является полем данных: сначала переместите его в область строк,
# поскольку группировать можно только поля строк/столбцов
pt.addFieldToArea(PivotFieldType.ROW, "FieldTwo")
pt.calculateData()
# Сгруппировать числовое поле в диапазоны 0-1, 2-3, 4-5
options = PivotFieldGroupOptions()
options.setStartNumber(0)
options.setEndNumber(5)
options.setInterval(2)
pt.getRowFields().get(1).group(options)
# Рассчитать данные сводной таблицы и сохранить выходной файл
pt.calculateData()
wb.save("outputNumberGroupPivotField.xlsx")
jpype.shutdownJVM()
```

## **Примечание**

{{% alert color="primary" %}}
- Перегрузки метода `PivotField.groupBy()` устарели и удалены из API. Заменой служат `PivotField.group()` и `PivotField.group(PivotFieldGroupOptions)`.
- В Microsoft Excel при группировке числового поля исходное поле сводной таблицы ЗАМЕНЯЕТСЯ сгруппированными диапазонами, тогда как при группировке поля даты рядом с исходным полем создаются НОВЫЕ поля сводной таблицы (по одному на каждый уровень группы, например Кварталы и Месяцы). Начиная с Aspose.Cells 26.10 методы `PivotField.group()` следуют тому же поведению, что и Excel. Свойство `PivotFieldGroupOptions.NewPivotField` существует для совместимости со старыми версиями: по умолчанию оно равно false для числовой группировки и true для группировки по дате и времени; установите его в false, если хотите, чтобы группировка по дате заменяла исходное поле сводной таблицы вместо создания новых полей.
- Свойство `PivotFieldGroupOptions.Interval` действует только для числовой группировки и для группировки дат по дням (например, группировка дат в 7-дневные периоды); оно игнорируется при группировке дат по месяцам, кварталам или годам.
{{% /alert %}}

## **Связанные статьи**
- [Добавление полей строк и столбцов в сводную таблицу](/cells/ru/python-java/pivot-table-add-row-and-column-fields/)
- [Фильтрация сводных таблиц по метке или значению](/cells/ru/python-java/filter-by-label-or-value-of-pivot-table/)
- [Добавление поля страницы в сводную таблицу](/cells/ru/python-java/add-page-field-in-pivot-table/)
- [Применение стиля к сводной таблице](/cells/ru/python-java/apply-style-to-pivot-table/)
- [Обновление сводной таблицы](/cells/ru/python-java/refresh-pivot-table/)

{{< app/cells/assistant language="python" >}}