---
title: Сводные таблицы
linktitle: Сводные таблицы
description: Создание и форматирование сводных таблиц с помощью Aspose.Cells for Python via Java.
keywords: Создание сводной таблицы, Вставка сводной таблицы, Форматирование сводной таблицы.
type: docs
weight: 160
url: /ru/python-java/create-pivot-table/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Что такое сводная таблица?**
Сводная таблица — это интерактивный сводный отчет: она сжимает большой объем необработанных данных, расположенных построчно, в компактную матрицу без единой формулы. Вы выбираете, какие столбцы станут метками строк, какие — метками столбцов, а какие будут агрегированы в качестве значений; сводная таблица выполняет группировку и вычисления:
- **Подведение итогов** — итоговый объем продаж по каждому продукту, региону или кварталу вместо длинных цепочек формул.
- **Сравнение** — категории в строках и периоды в столбцах превращают плоский список в перекрестный отчет, в котором тенденции видны сразу.
- **Переход к деталям** — дважды щелкните по любому итоговому значению, чтобы изучить исходные строки, на основе которых оно рассчитано.
- **Обновление** — при изменении исходных данных одно обновление пересчитывает весь отчет.
Типичные сценарии — панели продаж, анализ структуры расходов и анализ запасов, то есть любые вопросы вида «как эти показатели распределяются по категориям и периодам?». Aspose.Cells for Python via Java позволяет программно создавать такие же сводные таблицы, поэтому рабочие книги, создаваемые вашим приложением, могут содержать готовые отчеты, а не только необработанные данные.

### **Объектная модель сводной таблицы**
Aspose.Cells предоставляет набор классов, предназначенных для создания сводных таблиц и управления ими. Основные элементы:
- `PivotField` представляет поле в `PivotTable`.
- `PivotFieldCollection` представляет коллекцию всех объектов `PivotField` в `PivotTable`.
- `PivotTable` представляет сводную таблицу на рабочем листе.
- `PivotTableCollection` представляет коллекцию всех объектов `PivotTable` на рабочем листе.

### **Создание простой сводной таблицы с помощью Aspose.Cells**
Создание простой сводной таблицы состоит из трех этапов: запись исходных данных в ячейки рабочего листа, добавление сводной таблицы в целевую позицию и размещение полей сводной таблицы в областях строк, столбцов и данных.
1. Добавьте данные в рабочий лист с помощью метода `putValue` ячейки. Эти данные будут использоваться как источник данных сводной таблицы.
2. Добавьте сводную таблицу в рабочий лист, вызвав метод `add` коллекции `PivotTables`: `add(sourceData, row, column)`. `sourceData` — исходный диапазон (например, «A1:C8»); `row` и `column` — координаты целевой ячейки в левом верхнем углу сводной таблицы, отсчитываемые от нуля (ячейка E3 соответствует строке 2 и столбцу 4). Метод напрямую возвращает новый объект `PivotTable`.
3. Разместите поля сводной таблицы с помощью метода `addFieldToArea` объекта `PivotTable`: передайте имя поля в область строк (`PivotFieldType.ROW`), область столбцов (`PivotFieldType.COLUMN`) или область данных (`PivotFieldType.DATA`).
4. Сохраните рабочую книгу — сводная таблица будет записана в сохраненный файл.
После выполнения примера кода на рабочий лист будет добавлена сводная таблица.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, PivotFieldType

# Создать новую книгу и получить первый рабочий лист
workbook = Workbook()
sheet = workbook.getWorksheets().get(0)
cells = sheet.getCells()

# Записать исходные данные: продажи по видам спорта и кварталам
cells.get("A1").putValue("Sport")
cells.get("B1").putValue("Quarter")
cells.get("C1").putValue("Sales")
cells.get("A2").putValue("Golf")
cells.get("B2").putValue("Qtr3")
cells.get("C2").putValue(1500)
cells.get("A3").putValue("Golf")
cells.get("B3").putValue("Qtr4")
cells.get("C3").putValue(2000)
cells.get("A4").putValue("Tennis")
cells.get("B4").putValue("Qtr3")
cells.get("C4").putValue(600)
cells.get("A5").putValue("Tennis")
cells.get("B5").putValue("Qtr4")
cells.get("C5").putValue(1500)
cells.get("A6").putValue("Tennis")
cells.get("B6").putValue("Qtr3")
cells.get("C6").putValue(4070)
cells.get("A7").putValue("Tennis")
cells.get("B7").putValue("Qtr4")
cells.get("C7").putValue(5000)
cells.get("A8").putValue("Golf")
cells.get("B8").putValue("Qtr3")
cells.get("C8").putValue(6430)

# Добавить сводную таблицу в ячейку назначения E3 на основе данных из A1:C8
pivotTable = sheet.getPivotTables().add("A1:C8", 2, 4)

# Назначить поля сводной таблицы: Sport в строки, Quarter в столбцы, Sales в данные
pivotTable.addFieldToArea(PivotFieldType.ROW, "Sport")
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Quarter")
pivotTable.addFieldToArea(PivotFieldType.DATA, "Sales")

# Сохранить книгу
workbook.save("pivotTable_test_out.xlsx")
```

{{% alert color="primary" %}}
При указании диапазона ячеек в качестве источника данных он должен быть задан от левого верхнего угла к правому нижнему. Например, «A1:C3» — допустимый диапазон, а «C3:A1» — нет.
{{% /alert %}}

## Связанные статьи
- [Добавление полей фильтра в сводную таблицу в Aspose.Cells for Python via Java](/cells/ru/python-java/add-page-field-in-pivot-table/)
- [Применение стилей к сводным таблицам в Aspose.Cells for Python via Java](/cells/ru/python-java/apply-style-to-pivot-table/)
- [Изменение макета поля страницы в сводной таблице](/cells/ru/python-java/change-page-field-layout/)
- [Фильтрация сводных таблиц по метке или значению](/cells/ru/python-java/filter-by-label-or-value-of-pivot-table/)
- [Управление полями значений сводной таблицы в Aspose.Cells for Python via Java](/cells/ru/python-java/manage-value-fields/)

{{< app/cells/assistant language="python" >}}