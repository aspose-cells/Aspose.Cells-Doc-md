---
title: Добавить поля фильтров в сводную таблицу в Aspose.Cells для .NET
linktitle: Добавить поля фильтров
description: Узнайте, как добавлять и настраивать поля фильтра в сводных таблицах с помощью Aspose.Cells for Python via .NET, включая добавление полей фильтра, фильтрацию с одиночным выбором и фильтрацию с множественным выбором.
keywords: Aspose.Cells, Python via .NET, сводная таблица, поле фильтра, PivotFieldType.Page, PageFields, IsMultipleItemSelectionAllowed, CurrentPageItem, PivotItem, IsHidden, фильтр
type: docs
weight: 250
url: /ru/python-net/add-filter-field-in-pivot-table/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells поддерживает полный жизненный цикл полей фильтра в сводных таблицах. Вы можете добавить поле фильтра через высокоуровневый удобный API или через низкоуровневую коллекцию `page_fields`, а также управлять фильтром страницы в режиме одиночного выбора, очищать его для отображения всех элементов страницы или переключать поле в режим множественного выбора, чтобы пользователи могли выбирать несколько элементов страницы одновременно через интерфейс с флажками в Excel.
{{% /alert %}}

## **Введение**

поле фильтра — это поле сводной таблицы, которое управляет тем, *какое подмножество* исходных данных отображается в теле сводной таблицы. Конечные пользователи видят его как выпадающий список в верхней части отображаемой сводной таблицы в Excel, и выбор одного из доступных элементов страницы перестраивает тело сводной таблицы таким образом, чтобы обобщались только записи, принадлежащие этому элементу страницы. Поле сводной таблицы становится полем страницы, когда оно зарегистрировано как `PivotFieldType.PAGE`, а не как `PivotFieldType.ROW`, `PivotFieldType.COLUMN` или `PivotFieldType.DATA`.

поле фильтра может работать в двух режимах. В режиме по умолчанию **одиночного выбора** одновременно виден только один элемент страницы, поэтому тело сводной таблицы обобщает ровно одно подмножество. В режиме **множественного выбора** поле отображает список с флажками, и тело сводной таблицы обобщает объединение каждого отмеченного элемента страницы. Одно и то же исходное поле можно переключать между этими режимами, изменяя одно свойство.

Aspose.Cells for Python via .NET предоставляет два эквивалентных способа регистрации поля фильтраы. Высокоуровневый API — это `PivotTable.add_field_to_area(PivotFieldType.PAGE, "field_name")`, который принимает имя исходного столбца и добавляет поле одним вызовом. Низкоуровневый API — это `PivotTable.page_fields.add(PivotField)`, который используется, когда у вас уже есть ссылка на `PivotField` и вы хотите добавить тот же экземпляр поля в область фильтраы. Оба API в итоге заполняют одну и ту же коллекцию `page_fields`, и далее в этой статье показано, как выбирать между ними и как управлять каждым режимом фильтрации.

## **Добавление поля фильтраы**

Существует два способа зарегистрировать поле сводной таблицы в области страницы. Высокоуровневый вызов принимает имя исходного столбца в виде строки и является наиболее распространённым способом. Низкоуровневый вызов принимает существующий экземпляр `PivotField` и удобен, когда тот же объект поля должен использоваться в нескольких областях сводной таблицы. Оба вызова помещают поле в `PivotTable.page_fields`, после чего оно появляется как выпадающий список страницы в верхней части отображаемой сводной таблицы.

### Добавление поля фильтраы с помощью add_field_to_area

Следующий пример создаёт небольшой набор данных Fruit / Year / Amount, размещает сводную таблицу в ячейке E3 с полем `Fruit` в области строк, `Amount` в области данных и `Year` в области страницы, обновляет сводную таблицу и сохраняет книгу.

```python
import aspose.cells as ac

# Создать новую книгу
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
worksheet.name = "Data"

# Настроить строку заголовка
worksheet.cells["A1"].put_value("Fruit")
worksheet.cells["B1"].put_value("Year")
worksheet.cells["C1"].put_value("Amount")

# Заполнить 9 строк образцов данных: Fruit, Year, Amount
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
    worksheet.cells[i + 1, 0].put_value(data[i][0])
    worksheet.cells[i + 1, 1].put_value(data[i][1])
    worksheet.cells[i + 1, 2].put_value(data[i][2])

# Добавить сводную таблицу, привязанную к ячейке E3
pivot_index = worksheet.pivot_tables.add("A1:C10", "E3", "PivotTable1")
pivot_table = worksheet.pivot_tables[pivot_index]

# Добавить поля в их области: Fruit как строка, Amount как данные, Year как поле страницы
pivot_table.add_field_to_area(ac.PivotFieldType.Row, "Fruit")
pivot_table.add_field_to_area(ac.PivotFieldType.Data, "Amount")
pivot_table.add_field_to_area(ac.PivotFieldType.Page, "Year")

# Обновить и вычислить данные сводной таблицы
pivot_table.refresh_data()
pivot_table.calculate_data()

# Сохранить книгу
workbook.save("pageFieldSample.xlsx")
```

### Добавление поля фильтраы с помощью page_fields.add

Когда вы уже работаете с экземпляром `PivotField`, вы можете передать его напрямую в `PivotTable.page_fields.add`. Сводная таблица и поле фильтра создаются точно так же, как в предыдущем сценарии; только финальная регистрация в области страницы заменяется вызовом низкоуровневого API.

```python
import aspose.cells as ac

# — Сводная таблица и поле страницы создаются точно так же, как в
#   Сценарии 1a (данные Фрукт/Год/Сумма, сводная в E3, Фрукт→Строка,
#   Сумма→Данные). Ниже мы получаем PivotField Год из коллекции
#   BaseFields и передаём его в PageFields.Add — низкоуровневую
#   альтернативу AddFieldToArea. Результат функционально
#   идентичен Сценарию 1a.

workbook = ac.Workbook()
sheet = workbook.worksheets[0]

# Заголовки
sheet.cells["A1"].put_value("Fruit")
sheet.cells["B1"].put_value("Year")
sheet.cells["C1"].put_value("Amount")

# Пример данных (9 строк)
sheet.cells["A2"].put_value("apple");    sheet.cells["B2"].put_value("2020"); sheet.cells["C2"].put_value(100)
sheet.cells["A3"].put_value("apple");    sheet.cells["B3"].put_value("2021"); sheet.cells["C3"].put_value(150)
sheet.cells["A4"].put_value("apple");    sheet.cells["B4"].put_value("2022"); sheet.cells["C4"].put_value(200)
sheet.cells["A5"].put_value("grape");    sheet.cells["B5"].put_value("2020"); sheet.cells["C5"].put_value(300)
sheet.cells["A6"].put_value("grape");    sheet.cells["B6"].put_value("2021"); sheet.cells["C6"].put_value(400)
sheet.cells["A7"].put_value("grape");    sheet.cells["B7"].put_value("2022"); sheet.cells["C7"].put_value(500)
sheet.cells["A8"].put_value("blueberry"); sheet.cells["B8"].put_value("2020"); sheet.cells["C8"].put_value(250)
sheet.cells["A9"].put_value("blueberry"); sheet.cells["B9"].put_value("2021"); sheet.cells["C9"].put_value(350)
sheet.cells["A10"].put_value("blueberry");sheet.cells["B10"].put_value("2022"); sheet.cells["C10"].put_value(450)

# Добавить сводную таблицу в E3, охватывающую A1:C10
pivot_index = sheet.pivot_tables.add("E3", "A1:C10", "PivotTable1")
pivot_table = sheet.pivot_tables[pivot_index]

# Фрукт -> Строка, Сумма -> Данные (Год будет добавлен на Страницу ниже)
pivot_table.add_field_to_area(ac.PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(ac.PivotFieldType.DATA, "Amount")

# Низкоуровневый подход: получить существующий PivotField Год из BaseFields
# и зарегистрировать его в области Страница через PageFields.Add(PivotField).
year_field = pivot_table.base_fields["Year"]
pivot_table.page_fields.add(year_field)

# Обновить, чтобы новое поле страницы отразилось в сохранённой книге
pivot_table.refresh_data()
pivot_table.calculate_data()

workbook.save("output.xlsx")
```

## **Фильтрация с одиночным выбором (отображение одного элемента страницы)**

В режиме одиночного выбора по умолчанию поле фильтра отображается как одиночный выпадающий список, а целочисленное значение `PivotField.current_page_item` выбирает, какой элемент страницы управляет телом сводной таблицы. Присвоение конкретного индекса выбирает этот единственный элемент; присвоение специального значения `0x7FFD` (десятичное 32765) очищает фильтр, так что все элементы страницы обобщаются одновременно. Одиночный выбор используется по умолчанию; его не нужно включать явно.

### Отображение всех элементов

Установка `current_page_item` на магическое значение `0x7FFD` эквивалентна очистке фильтра страницы: тело сводной таблицы обобщает все элементы страницы так, как если бы фильтр не был применён.

```python
import aspose.cells as ac

# Создать новую рабочую книгу
workbook = ac.Workbook()
sheet = workbook.worksheets[0]

# Заполнить данные Fruit/Year/Amount
sheet.cells["A1"].put_value("Fruit")
sheet.cells["B1"].put_value("Year")
sheet.cells["C1"].put_value("Amount")

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
        sheet.cells[r + 1, c].put_value(data[r][c])

# Создать сводную таблицу в E3
pivot_tables = sheet.pivot_tables
index = pivot_tables.add("=A1:C7", "E3", "PivotTable1")
pivot_table = pivot_tables[index]

# Настроить поля сводной таблицы: Fruit→Строка, Amount→Данные, Year→Страница
pivot_table.add_field_to_area(ac.PivotFieldType.Row, "Fruit")
pivot_table.add_field_to_area(ac.PivotFieldType.Data, "Amount")
pivot_table.add_field_to_area(ac.PivotFieldType.Page, "Year")

pivot_table.refresh_data()
pivot_table.calculate_data()

# Очистить фильтр страницы, чтобы каждый элемент в поле страницы был виден.
# 0x7FFD (десятичное 32765) — это специальное значение-маркер, означающее «все элементы» —
# эквивалентно выбору «(Все)» в раскрывающемся списке поля страницы Excel.
pivot_table.page_fields[0].current_page_item = 0x7FFD

workbook.save("output.xlsx")
```

### Отображение одного конкретного элемента

Установка `current_page_item` на реальный индекс выбирает только этот один элемент страницы. Индекс — это позиция элемента в отсортированном списке элементов поля фильтраы, поэтому, например, `1` выбирает второй элемент после сортировки.

```python
import aspose.cells as ac

# Создать рабочую книгу
workbook = ac.Workbook()
sheet = workbook.worksheets[0]
cells = sheet.cells

# Добавить образец данных (Фрукт/Год/Сумма)
cells["A1"].put_value("Fruit")
cells["B1"].put_value("Year")
cells["C1"].put_value("Amount")

cells["A2"].put_value("Apple")
cells["B2"].put_value("2020")
cells["C2"].put_value("100")

cells["A3"].put_value("Apple")
cells["B3"].put_value("2021")
cells["C3"].put_value("150")

cells["A4"].put_value("Banana")
cells["B4"].put_value("2020")
cells["C4"].put_value("200")

cells["A5"].put_value("Banana")
cells["B5"].put_value("2021")
cells["C5"].put_value("250")

# Добавить сводную таблицу в E3
pivot_tables = sheet.pivot_tables
pivot_index = pivot_tables.add("A1:C5", "E3", "PivotTable1")
pivot_table = pivot_tables[pivot_index]

# Добавить поля: Фрукт→Строка, Сумма→Данные, Год→Страница
pivot_table.add_field_to_area(ac.PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(ac.PivotFieldType.DATA, "Amount")
pivot_table.add_field_to_area(ac.PivotFieldType.PAGE, "Year")

# Операции, специфичные для поля страницы
pivot_table.page_fields[0].current_page_item = 1  # 1 = второй элемент в порядке сортировки (например, "2021")

# Обновить и вычислить сводную таблицу
pivot_table.refresh_data()
pivot_table.calculate_data()

workbook.save("output.xlsx")
```

## **Фильтрация с множественным выбором**

Фильтрация с множественным выбором превращает выпадающий список страницы в список с флажками и позволяет конечному пользователю выбирать несколько элементов страницы одновременно. Aspose.Cells предоставляет два свойства, которые работают вместе. `PivotField.is_multiple_item_selection_allowed` должно быть установлено в `True` до того, как интерфейс множественного выбора вообще начнёт действовать. После его включения `PivotItem.is_hidden` управляет тем, какие элементы отображаются в списке с флажками, поэтому вы можете либо показать все элементы, либо включить в белый список только конкретные элементы.

Приведённый ниже код включает множественный выбор для того же поля фильтраы Year, созданного в Сценарии 1a, а затем демонстрирует два шаблона: Часть A показывает каждый элемент страницы, оставляя `is_hidden` установленным в `False` для каждой записи, тогда как Часть B включает в белый список только выбранные вами исходные значения и скрывает всё остальное через блок `if` / `elif`, который проверяет `pivot_items[i].get_string_value()`.

```python
import aspose.cells as ac

# — Сводная таблица и поле страницы построены точно так же, как в
#   Сценарии 1a (данные Fruit/Year/Amount, сводная в E3, Fruit→Строка,
#   Amount→Данные, Year→Страница через AddFieldToArea).
#   Ниже мы применяем множественный выбор для фильтрации поля страницы.

workbook = ac.Workbook()
sheet = workbook.worksheets[0]
cells = sheet.cells

# Пример данных: Fruit | Year | Amount
cells[0, 0].put_value("Fruit")
cells[0, 1].put_value("Year")
cells[0, 2].put_value("Amount")

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
    cells[i + 1, 0].put_value(data[i][0])
    cells[i + 1, 1].put_value(int(data[i][1]))
    cells[i + 1, 2].put_value(int(data[i][2]))

pivot_sheet = workbook.worksheets.add("Pivot")
pivots = pivot_sheet.pivot_tables
pivot_index = pivots.add("E3", "A1:C10", "PivotTable1")
pivot_table = pivots[pivot_index]

pivot_table.add_field_to_area(ac.PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(ac.PivotFieldType.DATA, "Amount")
pivot_table.add_field_to_area(ac.PivotFieldType.PAGE, "Year")

# — Включить множественный выбор для поля страницы
pivot_table.page_fields[0].is_multiple_item_selection_allowed = True

# Часть A — выбрать ВСЕ элементы (сделать каждый элемент видимым)
pivot_items = pivot_table.page_fields[0].pivot_items
for i in range(pivot_items.count):
    pivot_items[i].is_hidden = False

# Часть B — выбрать только определённые элементы по исходному значению
for i in range(pivot_items.count):
    value = pivot_items[i].get_string_value()
    if value == "2020" or value == "grape" or value == "blueberry":
        pivot_items[i].is_hidden = False
    else:
        pivot_items[i].is_hidden = True

pivot_table.refresh_data()
pivot_table.calculate_data()

workbook.save("output.xlsx")
```

> **Примечание:** При использовании фильтрации с множественным выбором через `PivotItem.is_hidden` **хотя бы один `PivotItem` должен оставаться видимым** (`is_hidden == False`). Если все элементы скрыты, Excel либо аварийно завершает работу при открытии файла, либо отображает пустую сводную таблицу. Всегда проверяйте, что ваш белый список для множественного выбора включает хотя бы один элемент из ваших исходных данных.

## **Какой API и какой режим следует использовать?**

Приведённая ниже таблица обобщает, когда использовать каждый API и режим, чтобы вы могли выбрать правильную комбинацию, не читая подробно каждый сценарий.

| Сценарий / Вариант использования | Рекомендуемый API | Используемое свойство | Примечания |
|---|---|---|---|
| Добавление поля фильтраы по имени исходного столбца (наиболее распространённый случай) | `PivotTable.add_field_to_area(PivotFieldType.PAGE, "field_name")` | n/a | Высокоуровневый, однострочный. Используйте его, если вам не нужна ссылка на `PivotField`. |
| Добавление поля фильтраы, когда у вас уже есть объект `PivotField` | `PivotTable.page_fields.add(PivotField)` | n/a | Используйте, когда объект поля был получен в другом месте или должен быть повторно использован. |
| Фильтрация до одного элемента страницы (режим по умолчанию) | `PivotField.current_page_item` | установить в конкретный индекс | Например, `1` показывает второй элемент в отсортированном списке. |
| Отображение всех элементов / очистка фильтра страницы | `PivotField.current_page_item` | установить в `0x7FFD` | Магическое значение `0x7FFD` (десятичное 32765) является меткой-заполнителем для «всех элементов». |
| Включение интерфейса множественного выбора в Excel | `PivotField.is_multiple_item_selection_allowed` | установить в `True` | Требуется до того, как любые вызовы `is_hidden` вступят в силу. |
| Скрытие / отображение отдельных элементов в списке множественного выбора | `PivotItem.is_hidden` | установить для каждого элемента | Хотя бы один элемент должен оставаться видимым (`is_hidden == False`). |

{{% alert color="primary" %}}
Всегда помните об ограничении видимости при настройке фильтрации с множественным выбором. Если каждый `PivotItem` в поле фильтра с множественным выбором скрыт, Excel аварийно завершает работу при открытии или отображает пустую сводную таблицу. Создавайте свой белый список на основе исходных данных так, чтобы хотя бы один элемент оставался видимым, и ваши сохранённые книги будут надёжно открываться на любом компьютере.
{{% /alert %}}


{{< app/cells/assistant language="python" >}}