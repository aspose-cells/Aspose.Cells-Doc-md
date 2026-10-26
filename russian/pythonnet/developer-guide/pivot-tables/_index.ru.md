---
title: Вставка сводной таблицы
linktitle: Вставка сводной таблицы
description: Создавайте и форматируйте сводные таблицы с помощью Aspose.Cells for Python via .NET.
keywords: Создание сводной таблицы, Вставка сводной таблицы, Форматирование сводной таблицы.
type: docs
weight: 160
url: /ru/python-net/create-pivot-table/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Что такое сводная таблица?**
Сводная таблица — это интерактивный сводный отчет: она сжимает большой объем необработанных данных, представленных построчно, в компактную матрицу без единой формулы. Вы выбираете, какие столбцы станут метками строк, какие — метками столбцов, а какие будут использованы для агрегации значений; сводная таблица выполняет группировку и вычисления:
- **Подведение итогов** — общий объем продаж по каждому продукту, региону или кварталу вместо длинных цепочек формул.
- **Сравнение** — категории в строках и периоды в столбцах превращают плоский список в перекрестный отчет, в котором тенденции видны сразу.
- **Детализация** — дважды щелкните по любому итоговому значению, чтобы изучить исходные строки, из которых оно сформировано.
- **Обновление** — при изменении исходных данных одно обновление пересчитывает весь отчет.
Типичные сценарии — дашборды продаж, разбивка расходов и анализ запасов, а также любой вопрос вида «как разбиваются эти числа по категориям и периодам времени?». Aspose.Cells for Python via .NET программно создает те же сводные таблицы, поэтому рабочие книги, формируемые вашим приложением, могут содержать готовые отчеты вместо одних только необработанных данных.

### **Объектная модель сводной таблицы**
Aspose.Cells for Python via .NET предоставляет специальный набор классов в namespace [**aspose.cells.pivot**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/), предназначенных для создания сводных таблиц и управления ими. Эти классы используются для создания и настройки объектов [**PivotTable**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/), являющихся строительными блоками сводной таблицы. Объекты представлены следующими классами:
- [**PivotField**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivotfield/) представляет поле в [**PivotTable**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/).
- [**PivotFieldCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivotfieldcollection) представляет коллекцию всех объектов [**PivotField**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivotfield/) в [**PivotTable**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable).
- [**PivotTable**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable) представляет объект PivotTable на рабочем листе.
- [**PivotTableCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottablecollection) представляет коллекцию всех объектов [**PivotTable**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable) на рабочем листе.

### **Создание простой сводной таблицы с помощью Aspose.Cells**
Создание сводной таблицы состоит из трех этапов: записи исходных данных в ячейки рабочего листа, добавления сводной таблицы в позицию назначения и размещения полей сводной таблицы в областях строк, столбцов и данных.
1. Добавьте данные в рабочий лист с помощью метода [**put_value**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/put_value/#str) объекта [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell). Эти данные будут использоваться в качестве источника данных сводной таблицы.
2. Добавьте сводную таблицу в рабочий лист, вызвав метод [**add**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottablecollection/add/#str-str-str) коллекции [**PivotTables**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottablecollection): `add(source_data, row, column)`. `source_data` — исходный диапазон (например, "A1:C8"); `row` и `column` — координаты ячейки назначения в левом верхнем углу сводной таблицы, нумеруемые с нуля (ячейка E3 означает строку 2 и столбец 4). Метод напрямую возвращает новый объект [**PivotTable**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable).
3. Разместите поля сводной таблицы с помощью метода `add_field_to_area` объекта [**PivotTable**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable): имя поля добавляется в область строк (`PivotFieldType.ROW`), область столбцов (`PivotFieldType.COLUMN`) или область данных (`PivotFieldType.DATA`).
4. Сохраните рабочую книгу — сводная таблица будет записана в сохраненный файл.
После выполнения примера кода в рабочий лист добавляется сводная таблица.

```python
import aspose.cells as ac
from aspose.cells.pivot import PivotFieldType

# Создать новую книгу и получить первый рабочий лист
workbook = ac.Workbook()
sheet = workbook.worksheets[0]

# Записать исходные данные: продажи по видам спорта и кварталам
sheet.cells.get("A1").put_value("Sport")
sheet.cells.get("B1").put_value("Quarter")
sheet.cells.get("C1").put_value("Sales")
sheet.cells.get("A2").put_value("Golf")
sheet.cells.get("B2").put_value("Qtr3")
sheet.cells.get("C2").put_value(1500)
sheet.cells.get("A3").put_value("Golf")
sheet.cells.get("B3").put_value("Qtr4")
sheet.cells.get("C3").put_value(2000)
sheet.cells.get("A4").put_value("Tennis")
sheet.cells.get("B4").put_value("Qtr3")
sheet.cells.get("C4").put_value(600)
sheet.cells.get("A5").put_value("Tennis")
sheet.cells.get("B5").put_value("Qtr4")
sheet.cells.get("C5").put_value(1500)
sheet.cells.get("A6").put_value("Tennis")
sheet.cells.get("B6").put_value("Qtr3")
sheet.cells.get("C6").put_value(4070)
sheet.cells.get("A7").put_value("Tennis")
sheet.cells.get("B7").put_value("Qtr4")
sheet.cells.get("C7").put_value(5000)
sheet.cells.get("A8").put_value("Golf")
sheet.cells.get("B8").put_value("Qtr3")
sheet.cells.get("C8").put_value(6430)

# Добавить сводную таблицу в ячейку назначения E3 на основе A1:C8
pivot_table = sheet.pivot_tables.add("A1:C8", 2, 4)

# Назначить поля сводной таблицы: Sport — строки, Quarter — столбцы, Sales — данные
pivot_table.add_field_to_area(PivotFieldType.ROW, "Sport")
pivot_table.add_field_to_area(PivotFieldType.COLUMN, "Quarter")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Sales")

# Сохранить книгу
workbook.save("pivotTable_test_out.xlsx")
```

{{% alert color="primary" %}}
При назначении диапазона ячеек в качестве источника данных диапазон должен проходить от левого верхнего угла к правому нижнему. Например, "A1:C3" допустим, а "C3:A1" — нет.
{{% /alert %}}

## Связанные статьи
- [Добавление полей фильтрации в сводную таблицу с помощью Aspose.Cells for Python via .NET](/cells/ru/python-net/add-page-field-in-pivot-table/)
- [Применение стилей к сводным таблицам с помощью Aspose.Cells for Python via .NET](/cells/ru/python-net/apply-style-to-pivot-table/)
- [Изменение макета поля страницы в сводной таблице](/cells/ru/python-net/change-page-field-layout/)
- [Фильтрация сводных таблиц по метке или значению](/cells/ru/python-net/filter-by-label-or-value-of-pivot-table/)
- [Управление полями значений сводной таблицы с помощью Aspose.Cells for Python via .NET](/cells/ru/python-net/manage-value-fields/)

{{< app/cells/assistant language="python-net" >}}