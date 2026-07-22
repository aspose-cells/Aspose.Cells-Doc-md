---
title: Поля страниц в сводных таблицах
linktitle: Поля страниц в сводных таблицах
description: Узнайте, как добавлять и настраивать поля страниц в сводных таблицах с помощью Aspose.Cells for Python via Java, включая добавление полей страниц, фильтрацию с одиночным выбором и фильтрацию с множественным выбором.
keywords: Aspose.Cells, Python, Java, сводная таблица, поле страницы, PivotFieldType.Page, PageFields, IsMultipleItemSelectionAllowed, CurrentPageItem, PivotItem, IsHidden, фильтр
type: docs
weight: 250
url: /ru/python-java/add-page-field-in-pivot-table/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells поддерживает полный жизненный цикл полей страниц в сводных таблицах. Вы можете добавить поле страницы через высокоуровневый удобный API или через низкоуровневую коллекцию `page_fields`, а также управлять фильтром страниц в режиме одиночного выбора, очищать его для отображения всех элементов страницы или переключать поле в режим множественного выбора, чтобы пользователи могли выбирать несколько элементов страницы одновременно через интерфейс с флажками в Excel.
{{% /alert %}}

## **Введение**

Поле страницы — это поле сводной таблицы, которое управляет тем, *какое подмножество* исходных данных отображается в теле сводной таблицы. Конечные пользователи видят его как раскрывающийся список в верхней части отображённой сводной таблицы в Excel, и выбор одного из доступных элементов страницы перестраивает тело сводной таблицы так, чтобы суммировались только записи, принадлежащие этому элементу страницы. Поле сводной таблицы становится полем страницы, когда оно зарегистрировано как `PivotFieldType.PAGE`, а не как `PivotFieldType.ROW`, `PivotFieldType.COLUMN` или `PivotFieldType.DATA`.

Поле страницы может работать в двух режимах. В режиме по умолчанию **одиночного выбора** одновременно виден только один элемент страницы, поэтому тело сводной таблицы суммирует ровно одно подмножество. В режиме **множественного выбора** поле отображает список с флажками, и тело сводной таблицы суммирует объединение всех отмеченных элементов страницы. Одно и то же исходное поле можно переключать между этими режимами, изменяя значение одного свойства.

Aspose.Cells for Python via Java предоставляет два эквивалентных способа регистрации поля страницы. Высокоуровневый API — это `PivotTable.add_field_to_area(PivotFieldType.PAGE, "fieldName")`, который принимает имя исходного столбца и добавляет поле одним вызовом. Низкоуровневый API — это `PivotTable.page_fields.add(PivotField)`, который используется, когда у вас уже есть ссылка на `PivotField` и нужно добавить тот же экземпляр поля в область страницы. Оба API в итоге заполняют одну и ту же коллекцию `page_fields`, и далее в этой статье показано, как выбирать между ними и как управлять каждым режимом фильтрации.

## **Добавление поля страницы**

Существует два способа зарегистрировать поле сводной таблицы в области страницы. Высокоуровневый вызов принимает имя исходного столбца в виде строки и является наиболее распространённым путём. Низкоуровневый вызов принимает существующий экземпляр `PivotField` и удобен, когда тот же объект поля должен использоваться в нескольких областях сводной таблицы. Оба вызова помещают поле в `PivotTable.page_fields`, после чего оно появляется как раскрывающийся список страницы в верхней части отображённой сводной таблицы.

### Добавление поля страницы с помощью add_field_to_area

В следующем примере создаётся небольшой набор данных Fruit / Year / Amount, сводная таблица размещается в ячейке E3 с полем `Fruit` в области строк, полем `Amount` в области данных и полем `Year` в области страницы, выполняется обновление сводной таблицы и сохранение рабочей книги.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, PivotFieldType

# Создание новой рабочей книги
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
worksheet.setName("Data")

# Настройка строки заголовка
worksheet.getCells().get("A1").putValue("Fruit")
worksheet.getCells().get("B1").putValue("Year")
worksheet.getCells().get("C1").putValue("Amount")

# Заполнение 9 строк примерами данных: Фрукт, Год, Количество
data = [
    ["apple", 2020, 100],
    ["banana", 2021, 200],
    ["apple", 2021, 150],
    ["grape", 2020, 120],
    ["orange", 2022, 180],
    ["banana", 2020, 90],
    ["grape", 2021, 130],
    ["apple", 2022, 170],
    ["orange", 2021, 110]
]

for i in range(len(data)):
    worksheet.getCells().get(i + 1, 0).putValue(data[i][0])
    worksheet.getCells().get(i + 1, 1).putValue(data[i][1])
    worksheet.getCells().get(i + 1, 2).putValue(data[i][2])

# Добавление сводной таблицы, привязанной к ячейке E3
pivotIndex = worksheet.getPivotTables().add("A1:C10", "E3", "PivotTable1")
pivotTable = worksheet.getPivotTables().get(pivotIndex)

# Добавление полей в их области: Фрукт как Строка, Количество как Данные, Год как Поле страницы
pivotTable.addFieldToArea(PivotFieldType.Row, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.Data, "Amount")
pivotTable.addFieldToArea(PivotFieldType.Page, "Year")

# Обновление и расчёт данных сводной таблицы
pivotTable.refreshData()
pivotTable.calculateData()

# Сохранение рабочей книги
workbook.save("pageFieldSample.xlsx")

jpype.shutdownJVM()
```

### Добавление поля страницы с помощью page_fields.add

Если вы уже работаете с экземпляром `PivotField`, вы можете передать его напрямую в `PivotTable.page_fields.add`. Сводная таблица и поле страницы создаются точно так же, как в предыдущем сценарии; только финальная регистрация в области страницы заменяется вызовом низкоуровневого API.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotTable, PivotField, PivotFieldType

# — Сводная таблица и поле страницы формируются точно так же, как в
#   Сценарии 1a (данные Fruit/Year/Amount, сводная в E3, Fruit→Строка,
#   Amount→Данные). Ниже мы получаем PivotField Year из
#   коллекции BaseFields и передаём его в PageFields.Add — это
#   низкоуровневая альтернатива AddFieldToArea. Результат
#   функционально идентичен Сценарию 1a.

workbook = Workbook()
sheet = workbook.getWorksheets().get(0)

# Заголовки
sheet.getCells().get("A1").putValue("Fruit")
sheet.getCells().get("B1").putValue("Year")
sheet.getCells().get("C1").putValue("Amount")

# Пример данных (9 строк)
sheet.getCells().get("A2").putValue("apple");    sheet.getCells().get("B2").putValue("2020"); sheet.getCells().get("C2").putValue(100)
sheet.getCells().get("A3").putValue("apple");    sheet.getCells().get("B3").putValue("2021"); sheet.getCells().get("C3").putValue(150)
sheet.getCells().get("A4").putValue("apple");    sheet.getCells().get("B4").putValue("2022"); sheet.getCells().get("C4").putValue(200)
sheet.getCells().get("A5").putValue("grape");    sheet.getCells().get("B5").putValue("2020"); sheet.getCells().get("C5").putValue(300)
sheet.getCells().get("A6").putValue("grape");    sheet.getCells().get("B6").putValue("2021"); sheet.getCells().get("C6").putValue(400)
sheet.getCells().get("A7").putValue("grape");    sheet.getCells().get("B7").putValue("2022"); sheet.getCells().get("C7").putValue(500)
sheet.getCells().get("A8").putValue("blueberry"); sheet.getCells().get("B8").putValue("2020"); sheet.getCells().get("C8").putValue(250)
sheet.getCells().get("A9").putValue("blueberry"); sheet.getCells().get("B9").putValue("2021"); sheet.getCells().get("C9").putValue(350)
sheet.getCells().get("A10").putValue("blueberry");sheet.getCells().get("B10").putValue("2022"); sheet.getCells().get("C10").putValue(450)

# Добавляем сводную таблицу в E3, охватывающую A1:C10
pivotIndex = sheet.getPivotTables().add("E3", "A1:C10", "PivotTable1")
pivotTable = sheet.getPivotTables().get(pivotIndex)

# Fruit -> Строка, Amount -> Данные (Year будет добавлено на страницу ниже)
pivotTable.addFieldToArea(PivotFieldType.Row, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.Data, "Amount")

# Низкоуровневый подход: извлекаем существующий PivotField Year из BaseFields
# и регистрируем его в области Страница через PageFields.Add(PivotField).
yearField = pivotTable.getBaseFields().get("Year")
pivotTable.getPageFields().add(yearField)

# Обновляем, чтобы новое поле страницы отразилось в сохранённой книге
pivotTable.refreshData()
pivotTable.calculateData()

workbook.save("output.xlsx")
jpype.shutdownJVM()
```

## **Фильтрация с одиночным выбором (отображение одного элемента страницы)**

В режиме одиночного выбора по умолчанию поле страницы отображается как одиночный раскрывающийся список, а целочисленное свойство `PivotField.current_page_item` выбирает, какой элемент страницы управляет телом сводной таблицы. Присвоение конкретного индекса выбирает именно этот элемент; присвоение специального контрольного значения `0x7FFD` (десятичное 32765) очищает фильтр, и тогда сразу суммируются все элементы страницы. Одиночный выбор является режимом по умолчанию; включать его явно не нужно.

### Отображение всех элементов

Присвоение `current_page_item` магического значения `0x7FFD` эквивалентно очистке фильтра страницы: тело сводной таблицы суммирует все элементы страницы так, как будто фильтр не применён.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotFieldType

# Создать новую рабочую книгу
workbook = Workbook()
sheet = workbook.getWorksheets().get(0)

# Заполнить данные Fruit/Year/Amount
sheet.getCells().get("A1").putValue("Fruit")
sheet.getCells().get("B1").putValue("Year")
sheet.getCells().get("C1").putValue("Amount")

data = [
    ["Apple", 2022, 100],
    ["Apple", 2023, 150],
    ["Banana", 2022, 80],
    ["Banana", 2023, 120],
    ["Cherry", 2022, 200],
    ["Cherry", 2023, 250]
]

for r in range(len(data)):
    for c in range(len(data[r])):
        sheet.getCells().get(r + 1, c).putValue(data[r][c])

# Создать сводную таблицу в E3
pivotTables = sheet.getPivotTables()
index = pivotTables.add("=A1:C7", "E3", "PivotTable1")
pivotTable = pivotTables.get(index)

# Настроить поля сводной таблицы: Fruit→Строка, Amount→Данные, Year→Страница
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount")
pivotTable.addFieldToArea(PivotFieldType.PAGE, "Year")

pivotTable.refreshData()
pivotTable.calculateData()

# Очистить фильтр страницы, чтобы каждый элемент поля страницы был виден.
# 0x7FFD (десятичное 32765) — это специальное контрольное значение, означающее «все элементы» —
# эквивалентно выбору «(Все)» в раскрывающемся списке поля страницы Excel.
pivotTable.getPageFields().get(0).setCurrentPageItem(0x7FFD)

workbook.save("output.xlsx")

jpype.shutdownJVM()
```

### Отображение одного конкретного элемента

Присвоение `current_page_item` реального индекса выбирает только этот один элемент страницы. Индекс — это позиция элемента в отсортированном списке элементов поля страницы, поэтому, например, `1` выбирает второй элемент после сортировки.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotFieldType

# Создать книгу
workbook = Workbook()
sheet = workbook.getWorksheets().get(0)
cells = sheet.getCells()

# Добавить образец данных (Фрукт/Год/Сумма)
cells.get("A1").putValue("Fruit")
cells.get("B1").putValue("Year")
cells.get("C1").putValue("Amount")

cells.get("A2").putValue("Apple")
cells.get("B2").putValue("2020")
cells.get("C2").putValue("100")

cells.get("A3").putValue("Apple")
cells.get("B3").putValue("2021")
cells.get("C3").putValue("150")

cells.get("A4").putValue("Banana")
cells.get("B4").putValue("2020")
cells.get("C4").putValue("200")

cells.get("A5").putValue("Banana")
cells.get("B5").putValue("2021")
cells.get("C5").putValue("250")

# Добавить сводную таблицу в E3
pivotTables = sheet.getPivotTables()
pivotIndex = pivotTables.add("A1:C5", "E3", "PivotTable1")
pivotTable = pivotTables.get(pivotIndex)

# Добавить поля: Фрукт→Строка, Сумма→Данные, Год→Страница
pivotTable.addFieldToArea(PivotFieldType.Row, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.Data, "Amount")
pivotTable.addFieldToArea(PivotFieldType.Page, "Year")

# Операции, специфичные для поля страницы
pivotTable.getPageFields().get(0).setCurrentPageItem(1) # 1 = второй элемент в отсортированном порядке (например, "2021")

# Обновить и вычислить сводную таблицу
pivotTable.refreshData()
pivotTable.calculateData()

workbook.save("output.xlsx")

jpype.shutdownJVM()
```

## **Фильтрация с множественным выбором**

Фильтрация с множественным выбором превращает раскрывающийся список страницы в список с флажками и позволяет конечному пользователю выбирать несколько элементов страницы одновременно. Aspose.Cells предоставляет два свойства, которые работают вместе. `PivotField.is_multiple_item_selection_allowed` должно быть установлено в `True`, прежде чем интерфейс множественного выбора начнёт действовать. После его включения `PivotItem.is_hidden` управляет тем, какие элементы отображаются в списке с флажками, поэтому вы можете либо показать все элементы, либо включить в белый список только конкретные элементы.

Код ниже включает множественный выбор для того же поля страницы Year, созданного в сценарии 1a, и затем демонстрирует два шаблона: Часть A раскрывает все элементы страницы, оставляя `is_hidden` равным `False` для каждой записи, тогда как Часть B включает в белый список только выбранные вами исходные значения и скрывает все остальные через блок `switch (pivot_items[i].get_string_value())`.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotFieldType
import os
import re

# — Сводная таблица и поле страницы построены точно так же, как в
#   Сценарии 1a (данные Fruit/Year/Amount, сводная в E3, Fruit→Row,
#   Amount→Data, Year→Page через AddFieldToArea).
#   Ниже мы применяем множественную фильтрацию на поле страницы.

workbook = Workbook()
sheet = workbook.getWorksheets().get(0)
cells = sheet.getCells()

# Пример данных: Fruit | Year | Amount
cells.get(0, 0).putValue("Fruit")
cells.get(0, 1).putValue("Year")
cells.get(0, 2).putValue("Amount")

data = [
    ["apple",  "2019", "100"],
    ["apple",  "2020", "150"],
    ["apple",  "2021", "200"],
    ["banana", "2019", "110"],
    ["banana", "2020", "160"],
    ["banana", "2021", "210"],
    ["grape",  "2019", "120"],
    ["grape",  "2020", "170"],
    ["grape",  "2021", "220"]
]

for i in range(len(data)):
    cells.get(i + 1, 0).putValue(data[i][0])
    cells.get(i + 1, 1).putValue(int(data[i][1]))
    cells.get(i + 1, 2).putValue(int(data[i][2]))

pivotSheet = workbook.getWorksheets().add("Pivot")
pivots = pivotSheet.getPivotTables()
pivotIndex = pivots.add("E3", "A1:C10", "PivotTable1")
pivotTable = pivots.get(pivotIndex)

pivotTable.addFieldToArea(PivotFieldType.Row, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.Data, "Amount")
pivotTable.addFieldToArea(PivotFieldType.Page, "Year")

# — Включить множественный выбор на поле страницы
pivotTable.getPageFields().get(0).setMultipleItemSelectionAllowed(True)

# Часть A — выбрать ВСЕ элементы (сделать каждый элемент видимым)
pivotItems = pivotTable.getPageFields().get(0).getPivotItems()
for i in range(pivotItems.getCount()):
    pivotItems.get(i).setHidden(False)

# Часть B — выбрать только определенные элементы по исходному значению
for i in range(pivotItems.getCount()):
    value = pivotItems.get(i).getStringValue()
    if value == "2020" or value == "grape" or value == "blueberry":
        pivotItems.get(i).setHidden(False)
    else:
        pivotItems.get(i).setHidden(True)

pivotTable.refreshData()
pivotTable.calculateData()

workbook.save("output.xlsx")

jpype.shutdownJVM()
```

> **Примечание:** При использовании фильтрации с множественным выбором через `PivotItem.is_hidden`, **хотя бы один `PivotItem` должен оставаться видимым** (`is_hidden == False`). Если все элементы скрыты, Excel либо аварийно завершает работу при открытии файла, либо отображает пустую сводную таблицу. Всегда проверяйте, что ваш белый список для множественного выбора включает хотя бы один элемент из исходных данных.

## **Какой API и какой режим следует использовать?**

Таблица ниже обобщает, когда использовать каждый API и режим, чтобы вы могли выбрать правильную комбинацию, не читая подробно каждый сценарий.

| Сценарий / Вариант использования | Рекомендуемый API | Используемое свойство | Примечания |
|---|---|---|---|
| Добавление поля страницы по имени исходного столбца (наиболее распространённый случай) | `PivotTable.add_field_to_area(PivotFieldType.PAGE, "fieldName")` | n/a | Высокоуровневый, однострочный. Используйте его, если вам не нужна ссылка на `PivotField`. |
| Добавление поля страницы, когда у вас уже есть объект `PivotField` | `PivotTable.page_fields.add(PivotField)` | n/a | Используйте, когда объект поля был получен в другом месте или должен быть переиспользован. |
| Фильтрация до одного элемента страницы (режим по умолчанию) | `PivotField.current_page_item` | установить в конкретный индекс | Например, `1` показывает второй элемент в отсортированном списке. |
| Отображение всех элементов / очистка фильтра страницы | `PivotField.current_page_item` | установить в `0x7FFD` | Магическое значение `0x7FFD` (десятичное 32765) — это контрольное значение для «всех элементов». |
| Включение интерфейса множественного выбора в Excel | `PivotField.is_multiple_item_selection_allowed` | установить в `True` | Требуется до того, как любые вызовы `is_hidden` начнут действовать. |
| Скрытие / отображение отдельных элементов в списке множественного выбора | `PivotItem.is_hidden` | устанавливается для каждого элемента | Хотя бы один элемент должен оставаться видимым (`is_hidden == False`). |

{{% alert color="primary" %}}
Всегда помните об ограничении видимости при настройке фильтрации с множественным выбором. Если все `PivotItem` в поле страницы с множественным выбором скрыты, Excel аварийно завершает работу при открытии или отображает пустую сводную таблицу. Создавайте свой белый список на основе исходных данных так, чтобы хотя бы один элемент оставался видимым, и ваши сохранённые рабочие книги будут надёжно открываться на любом компьютере.
{{% /alert %}}



{{< app/cells/assistant language="python" >}}