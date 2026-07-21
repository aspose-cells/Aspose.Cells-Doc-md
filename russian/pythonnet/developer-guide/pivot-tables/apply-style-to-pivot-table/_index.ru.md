---
title: Применение стилей к сводным таблицам
linktitle: Применение стилей к сводным таблицам
description: Узнайте, как применять встроенные и пользовательские стили к сводным таблицам в Aspose.Cells for Python via .NET, включая устаревшие автоформаты XLS, современные именованные стили Excel 2007+, пользовательские стили сводных таблиц и удобный метод FormatAll.
keywords: Aspose.Cells Python via .NET стиль сводной таблицы, PivotTableStyleType, AutoFormatType, FormatAll, пользовательский стиль, PivotTableStyleName, TableStyles
type: docs
weight: 200
url: /ru/python-net/apply-style-to-pivot-table/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells поддерживает применение как устаревших автоформатов сводных таблиц (предназначенных для файлов `.xls`), так и современных именованных или пользовательских стилей сводных таблиц (предназначенных для файлов `.xlsx`, `.xlsm` и `.xlsb`). Какой API следует вызывать, зависит от формата файла, в который сохраняется рабочая книга, а не от формата, из которого она была загружена.

{{% /alert %}}

## **Введение**

Aspose.Cells предоставляет два параллельных API стилей для сводных таблиц. Выбор между ними определяется форматом файла, в который вы сохраняете рабочую книгу, а не форматом, из которого вы её читаете. Рабочая книга, загруженная из файла `.xls`, может быть повторно сохранена как `.xlsx`, и в этом случае применяется современный API стилей, а не устаревший.

Для устаревшего вывода в формате `.xls` используйте свойство `PivotTable.auto_format_type` вместе с перечислением `aspose.cells.pivot.PivotTableAutoFormatType`. Этот API соответствует выбору автоформата, который предлагал классический Excel для сводных таблиц.

Для современных форматов вывода `.xlsx`, `.xlsm` и `.xlsb` доступны два варианта API стилей:

- `PivotTable.pivot_table_style_type` выбирает один из встроенных именованных стилей (светлые и тёмные темы, включая стили, добавленные в Excel 2017). Эти предустановки доступны только для чтения.
- `PivotTable.pivot_table_style_name` выбирает пользовательский стиль, который вы определяете самостоятельно через `workbook.worksheets.table_styles.add_pivot_table_style(...)`. Пользовательские стили необходимы, когда требуется изменить цвета, границы или шрифты за пределы того, что предлагают предустановки.

Кроме того, `PivotTable.format_all(Style)` представляет собой удобный метод, который применяет единственный объект `Style` к каждой ячейке сводной таблицы, переопределяя всё, что было установлено через любой из API имён стилей выше. Это полезно, когда требуется единообразный внешний вид независимо от базовой темы.

## **Применение предустановленного автоформата устаревшего формата XLS**

`PivotTable.auto_format_type` принимает значение из перечисления `aspose.cells.pivot.PivotTableAutoFormatType`. Доступные значения: `REPORT_1` — `REPORT_10`, `CLASSIC` и `TABLE_1` — `TABLE_10`.

{{% alert color="primary" %}}

`auto_format_type` учитывается только при сохранении рабочей книги в формате `.xls`. Когда та же рабочая книга сохраняется в формате `.xlsx`, `.xlsm` или `.xlsb`, Excel игнорирует это свойство и возвращается к настройкам `pivot_table_style_type` и `pivot_table_style_name`.

{{% /alert %}}

Следующий пример загружает новую рабочую книгу, заполняет примерные данные Fruit/Year/Amount, добавляет сводную таблицу, применяет `PivotTableAutoFormatType.REPORT_5` и сохраняет результат в формате `.xls`.

{{% alert color="primary" %}}

**Почему нет полей столбцов?** Автоформаты серии Report (`Report1`–`Report10`, `Table1`–`Table10`) были разработаны в классическом Excel для **одномерных сводных таблиц** — только с полями строк и значениями, без встроенного оформления для заголовков полей столбцов. Если сводной таблице нужны поля столбцов, используйте современные предустановки `PivotTableStyleType` из Сценария 2 ниже — они рассчитаны на двумерную раскладку современного Excel.

{{% /alert %}}

```python
import aspose.cells as ac

# Сценарий 1: Применение предустановленного автоформата устаревшего XLS
# Используемый API: PivotTable.AutoFormatType
# Целевой формат файла: .xls (устаревший)
# Для полных примеров и файлов данных перейдите по ссылке https://github.com/aspose-cells/Aspose.Cells-for-.NET

# Создаём новую книгу
workbook = ac.Workbook()

# Получаем первый лист
sheet = workbook.worksheets[0]

# Заполняем исходные данные строкой заголовков (Fruit, Year, Amount)
# и 9 строками данных, охватывающими grape, blueberry, kiwi, cherry за 2020 и 2021 годы
sheet.cells[0, 0].put_value("Fruit")
sheet.cells[0, 1].put_value("Year")
sheet.cells[0, 2].put_value("Amount")

sheet.cells[1, 0].put_value("grape")
sheet.cells[1, 1].put_value(2020)
sheet.cells[1, 2].put_value(50)

sheet.cells[2, 0].put_value("blueberry")
sheet.cells[2, 1].put_value(2020)
sheet.cells[2, 2].put_value(30)

sheet.cells[3, 0].put_value("kiwi")
sheet.cells[3, 1].put_value(2020)
sheet.cells[3, 2].put_value(25)

sheet.cells[4, 0].put_value("cherry")
sheet.cells[4, 1].put_value(2020)
sheet.cells[4, 2].put_value(40)

sheet.cells[5, 0].put_value("grape")
sheet.cells[5, 1].put_value(2021)
sheet.cells[5, 2].put_value(60)

sheet.cells[6, 0].put_value("blueberry")
sheet.cells[6, 1].put_value(2021)
sheet.cells[6, 2].put_value(35)

sheet.cells[7, 0].put_value("kiwi")
sheet.cells[7, 1].put_value(2021)
sheet.cells[7, 2].put_value(28)

sheet.cells[8, 0].put_value("cherry")
sheet.cells[8, 1].put_value(2021)
sheet.cells[8, 2].put_value(45)

sheet.cells[9, 0].put_value("grape")
sheet.cells[9, 1].put_value(2020)
sheet.cells[9, 2].put_value(45)

# Добавляем сводную таблицу в ячейку назначения E3 с именем "Pivot1", используя исходный диапазон A1:C10
pivot_index = sheet.pivot_tables.add("A1:C10", "E3", "Pivot1")
pivot_table = sheet.pivot_tables[pivot_index]

# Назначаем поля: Fruit -> строки, Year -> столбцы, Amount -> данные
pivot_table.add_field_to_area(ac.PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(ac.PivotFieldType.DATA, "Amount")

# Применяем предустановленный автоформат устаревшего XLS "Report5"
# Примечание: Это свойство имеет смысл только при сохранении в формате .xls.
# При сохранении в формате .xlsx/.xlsm/.xlsb Excel игнорирует AutoFormatType
# и использует то, что указано в PivotTableStyleType / PivotTableStyleName.
pivot_table.auto_format_type = ac.PivotTableAutoFormatType.REPORT5

# Сохраняем книгу в устаревшем формате .xls
workbook.save("output.xls")
```

## **Применение современного именованного предустановленного стиля сводной таблицы**

`PivotTable.pivot_table_style_type` принимает значение из перечисления `aspose.cells.PivotTableStyleType`. Перечисление охватывает светлые темы `PIVOT_TABLE_STYLE_LIGHT_1` — `PIVOT_TABLE_STYLE_LIGHT_28` и тёмные темы `PIVOT_TABLE_STYLE_DARK_1` — `PIVOT_TABLE_STYLE_DARK_28`. Стили, добавленные в Excel 2017 (вторая волна светлых и тёмных тем), доступны через то же перечисление.

Это рекомендуемый API для любого современного формата файла. В отличие от устаревшего автоформата, выбранный здесь стиль корректно отображается в Excel и сохраняется при циклическом обмене данными через другие инструменты Office.

В следующем примере используются те же данные Fruit/Year/Amount, создаётся идентичная сводная таблица, применяется `PIVOT_TABLE_STYLE_DARK_1` и рабочая книга сохраняется в формате `.xlsx`.

```python
import aspose.cells as ac

# Сценарий 2: Применение современного именованного предустановленного стиля Excel 2007+ с помощью PivotTableStyleType.
# Целевой формат файла: .xlsx. Перечисление PivotTableStyleType находится в пространстве имён Aspose.Cells
# (не в Aspose.Cells.Pivot) — поэтому нам не нужны никакие дополнительные using для него.
# Ссылка на GitHub: https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Examples/CSharp/PivotTables/ApplyStyleToPivotTable2.cs

workbook = ac.Workbook()
worksheet = workbook.worksheets[0]

# Строка заголовков: Fruit / Year / Amount
worksheet.cells["A1"].put_value("Fruit")
worksheet.cells["B1"].put_value("Year")
worksheet.cells["C1"].put_value("Amount")

# 9 строк данных Fruit / Year / Amount
worksheet.cells["A2"].put_value("Grape")
worksheet.cells["B2"].put_value(2020)
worksheet.cells["C2"].put_value(100)

worksheet.cells["A3"].put_value("Blueberry")
worksheet.cells["B3"].put_value(2020)
worksheet.cells["C3"].put_value(150)

worksheet.cells["A4"].put_value("Kiwi")
worksheet.cells["B4"].put_value(2020)
worksheet.cells["C4"].put_value(200)

worksheet.cells["A5"].put_value("Cherry")
worksheet.cells["B5"].put_value(2020)
worksheet.cells["C5"].put_value(180)

worksheet.cells["A6"].put_value("Grape")
worksheet.cells["B6"].put_value(2021)
worksheet.cells["C6"].put_value(120)

worksheet.cells["A7"].put_value("Blueberry")
worksheet.cells["B7"].put_value(2021)
worksheet.cells["C7"].put_value(170)

worksheet.cells["A8"].put_value("Kiwi")
worksheet.cells["B8"].put_value(2021)
worksheet.cells["C8"].put_value(210)

worksheet.cells["A9"].put_value("Cherry")
worksheet.cells["B9"].put_value(2021)
worksheet.cells["C9"].put_value(190)

worksheet.cells["A10"].put_value("Grape")
worksheet.cells["B10"].put_value(2021)
worksheet.cells["C10"].put_value(130)

# Добавление сводной таблицы в E3 с именем "Pivot1", источник данных — A1:C10
pivot_index = worksheet.pivot_tables.add("A1:C10", "E3", "Pivot1")
pivot_table = worksheet.pivot_tables[pivot_index]

# Назначение полей сводной таблицы: Fruit -> область строк, Year -> область столбцов, Amount -> область данных
pivot_table.add_field_to_area(ac.PivotFieldType.Row, "Fruit")
pivot_table.add_field_to_area(ac.PivotFieldType.Column, "Year")
pivot_table.add_field_to_area(ac.PivotFieldType.Data, "Amount")

# Применение современного именованного предустановленного стиля сводной таблицы Excel 2007+.
# PivotTableStyleType — это правильный API для файлов .xlsx / .xlsm / .xlsb; AutoFormatType
# игнорируется Excel для этих форматов. PivotTableStyleDark1 принадлежит семейству тёмных тем
# (PivotTableStyleDark1..PivotTableStyleDark28), и то же перечисление также предоставляет
# новые светлые/тёмные темы Excel 2017 (PivotTableStyleLight1..Light28 / Dark1..Dark28).
pivot_table.pivot_table_style_type = ac.PivotTableStyleType.PivotTableStyleDark1

# Сохранение в современном формате .xlsx — это формат, для которого PivotTableStyleType имеет значение.
workbook.save("output.xlsx")
```

## **Определение и применение пользовательского стиля сводной таблицы**

Встроенные предустановки не могут быть изменены. Каждый раз, когда вам нужно переопределить цвета, границы или шрифты, вы должны определить пользовательский стиль сводной таблицы. Рабочий процесс состоит из трёх шагов:

1. Добавьте пользовательский стиль в коллекцию `table_styles` рабочей книги через `workbook.worksheets.table_styles.add_pivot_table_style(name)`. Это вернёт индекс вновь созданного стиля.
2. Настройте стиль, добавляя элементы (такие как `WHOLE_TABLE` или `GRAND_TOTAL_ROW`) через `table_style.table_style_elements.add(TableStyleElementType)`, затем назначьте `Style` каждому элементу через `table_style_element.set_element_style(Style)`.
3. Примените пользовательский стиль к сводной таблице, установив `PivotTable.pivot_table_style_name` равным имени стиля. Не используйте здесь `pivot_table_style_type`, поскольку это свойство выбирает встроенные предустановки.

{{% alert color="primary" %}}

`pivot_table_style_name` и `pivot_table_style_type` не взаимозаменяемы. Используйте `pivot_table_style_type` для встроенных предустановок и `pivot_table_style_name` для пользовательских стилей, определённых через `add_pivot_table_style`. Установка обоих свойств безвредна, но отображается только то, которое соответствует предполагаемому источнику.

{{% /alert %}}

Доступные значения `TableStyleElementType` включают `WHOLE_TABLE`, `FIRST_ROW`, `LAST_ROW`, `FIRST_COLUMN`, `LAST_COLUMN`, `GRAND_TOTAL_ROW`, `GRAND_TOTAL_COLUMN`, `PAGE_FIELD_LABELS` и `PAGE_FIELD_VALUES`.

В следующем примере определяется пользовательский стиль сводной таблицы с тонкой чёрной границей для `WHOLE_TABLE` и жирным красным шрифтом для `GRAND_TOTAL_ROW`, затем он применяется через `pivot_table_style_name` и сохраняется в формате `.xlsx`.

```python
import aspose.cells as ac
import System.Drawing

workbook = ac.Workbook()
worksheet = workbook.worksheets[0]

# Заполняем исходные данные: строка заголовка + 9 строк данных (A1:C10)
worksheet.cells["A1"].put_value("Fruit")
worksheet.cells["B1"].put_value("Year")
worksheet.cells["C1"].put_value("Amount")

worksheet.cells["A2"].put_value("Grape")
worksheet.cells["B2"].put_value(2020)
worksheet.cells["C2"].put_value(100)

worksheet.cells["A3"].put_value("Blueberry")
worksheet.cells["B3"].put_value(2020)
worksheet.cells["C3"].put_value(200)

worksheet.cells["A4"].put_value("Kiwi")
worksheet.cells["B4"].put_value(2020)
worksheet.cells["C4"].put_value(300)

worksheet.cells["A5"].put_value("Cherry")
worksheet.cells["B5"].put_value(2020)
worksheet.cells["C5"].put_value(400)

worksheet.cells["A6"].put_value("Grape")
worksheet.cells["B6"].put_value(2021)
worksheet.cells["C6"].put_value(500)

worksheet.cells["A7"].put_value("Blueberry")
worksheet.cells["B7"].put_value(2021)
worksheet.cells["C7"].put_value(600)

worksheet.cells["A8"].put_value("Kiwi")
worksheet.cells["B8"].put_value(2021)
worksheet.cells["C8"].put_value(700)

worksheet.cells["A9"].put_value("Cherry")
worksheet.cells["B9"].put_value(2021)
worksheet.cells["C9"].put_value(800)

worksheet.cells["A10"].put_value("Grape")
worksheet.cells["B10"].put_value(2021)
worksheet.cells["C10"].put_value(900)

# Добавляем сводную таблицу с источником A1:C10, привязанную к E3, с именем "Pivot1"
pivot_index = worksheet.pivot_tables.add("A1:C10", "E3", "Pivot1")
pivot_table = worksheet.pivot_tables[pivot_index]

pivot_table.add_field_to_area(ac.PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(ac.PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(ac.PivotFieldType.DATA, "Amount")

# Шаг 1: регистрируем новый пользовательский стиль сводной таблицы и сохраняем его индекс
style_index = workbook.worksheets.table_styles.add_pivot_table_style("CustomPivotStyle")
table_style = workbook.worksheets.table_styles[style_index]

# Шаг 2: добавляем элемент WholeTable и применяем тонкие чёрные границы со всех четырёх сторон
whole_table_element_index = table_style.table_style_elements.add(ac.TableStyleElementType.WHOLE_TABLE)
whole_table_element = table_style.table_style_elements[whole_table_element_index]
whole_table_style = workbook.create_style()
whole_table_style.borders[ac.BorderType.TOP_BORDER].line_style = ac.CellBorderType.THIN
whole_table_style.borders[ac.BorderType.TOP_BORDER].color = System.Drawing.Color.Black
whole_table_style.borders[ac.BorderType.BOTTOM_BORDER].line_style = ac.CellBorderType.THIN
whole_table_style.borders[ac.BorderType.BOTTOM_BORDER].color = System.Drawing.Color.Black
whole_table_style.borders[ac.BorderType.LEFT_BORDER].line_style = ac.CellBorderType.THIN
whole_table_style.borders[ac.BorderType.LEFT_BORDER].color = System.Drawing.Color.Black
whole_table_style.borders[ac.BorderType.RIGHT_BORDER].line_style = ac.CellBorderType.THIN
whole_table_style.borders[ac.BorderType.RIGHT_BORDER].color = System.Drawing.Color.Black
whole_table_element.set_element_style(whole_table_style)

# Шаг 3: добавляем элемент GrandTotalRow и применяем жирный красный шрифт
grand_total_element_index = table_style.table_style_elements.add(ac.TableStyleElementType.GRAND_TOTAL_ROW)
grand_total_element = table_style.table_style_elements[grand_total_element_index]
grand_total_style = workbook.create_style()
grand_total_style.font.is_bold = True
grand_total_style.font.color = System.Drawing.Color.Red
grand_total_element.set_element_style(grand_total_style)

# Шаг 4: применяем пользовательский стиль по имени (НЕ через PivotTableStyleType, который предназначен для встроенных предустановок)
pivot_table.pivot_table_style_name = "CustomPivotStyle"

workbook.save("output.xlsx")
```

## **Применение одного стиля ко всем ячейкам сводной таблицы с помощью FormatAll**

`PivotTable.format_all(Style)` представляет собой удобный метод, который применяет единственный объект `Style` к каждой ячейке сводной таблицы, включая область данных, заголовки строк и столбцов, а также итоги. Всё, что ранее было установлено через `pivot_table_style_type` или `pivot_table_style_name`, переопределяется.

{{% alert color="primary" %}}

`format_all` переопределяет и `pivot_table_style_type`, и `pivot_table_style_name`. Используйте его только тогда, когда требуется единообразный, не зависящий от темы внешний вид для всей сводной таблицы.

{{% /alert %}}

В следующем примере создаётся `Style` с жёлтой сплошной заливкой, жирным тёмно-синим шрифтом и тонкими чёрными границами со всех сторон, затем он применяется с помощью `format_all` и сохраняется в формате `.xlsx`.

```python
from System.Drawing import Color
import aspose.cells as ac
from aspose.cells.pivot import PivotFieldType
from aspose.cells import BackgroundType, CellBorderType, BorderType

# Сценарий 4: Применение единого стиля ко всем ячейкам сводной таблицы с помощью FormatAll
# Используемый API: PivotTable.FormatAll(Style)
# Целевой формат: .xlsx
# Ссылка на GitHub: см. репозиторий Aspose.Cells-for-.NET — примеры стилизации сводных таблиц

workbook = ac.Workbook()
worksheet = workbook.worksheets[0]

# Заполнение исходных данных: строка заголовков (строка 1) + 9 строк данных (строки 2-10)
worksheet.cells["A1"].put_value("Fruit")
worksheet.cells["B1"].put_value("Year")
worksheet.cells["C1"].put_value("Amount")

worksheet.cells["A2"].put_value("Grape")
worksheet.cells["B2"].put_value(2020)
worksheet.cells["C2"].put_value(5000)

worksheet.cells["A3"].put_value("Blueberry")
worksheet.cells["B3"].put_value(2020)
worksheet.cells["C3"].put_value(3000)

worksheet.cells["A4"].put_value("Kiwi")
worksheet.cells["B4"].put_value(2020)
worksheet.cells["C4"].put_value(4000)

worksheet.cells["A5"].put_value("Cherry")
worksheet.cells["B5"].put_value(2020)
worksheet.cells["C5"].put_value(2000)

worksheet.cells["A6"].put_value("Grape")
worksheet.cells["B6"].put_value(2021)
worksheet.cells["C6"].put_value(6000)

worksheet.cells["A7"].put_value("Blueberry")
worksheet.cells["B7"].put_value(2021)
worksheet.cells["C7"].put_value(3500)

worksheet.cells["A8"].put_value("Kiwi")
worksheet.cells["B8"].put_value(2021)
worksheet.cells["C8"].put_value(4500)

worksheet.cells["A9"].put_value("Cherry")
worksheet.cells["B9"].put_value(2021)
worksheet.cells["C9"].put_value(2500)

worksheet.cells["A10"].put_value("Grape")
worksheet.cells["B10"].put_value(2021)
worksheet.cells["C10"].put_value(5500)

# Добавление сводной таблицы: исходный диапазон A1:C10, целевая ячейка E3, имя "Pivot1"
pivot_index = worksheet.pivot_tables.add("A1:C10", "E3", "Pivot1")
pivot_table = worksheet.pivot_tables[pivot_index]

# Назначение полей сводной таблицы: Fruit -> область строк, Year -> область столбцов, Amount -> область данных
pivot_table.add_field_to_area(PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Amount")

# Создание стиля, который будет принудительно применён к каждой ячейке сводной таблицы
style = workbook.create_style()
style.foreground_color = Color.Yellow
style.pattern = BackgroundType.SOLID
style.font.is_bold = True
style.font.color = Color.DarkBlue
style.borders[BorderType.TOP_BORDER].line_style = CellBorderType.THIN
style.borders[BorderType.TOP_BORDER].color = Color.Black
style.borders[BorderType.BOTTOM_BORDER].line_style = CellBorderType.THIN
style.borders[BorderType.BOTTOM_BORDER].color = Color.Black
style.borders[BorderType.LEFT_BORDER].line_style = CellBorderType.THIN
style.borders[BorderType.LEFT_BORDER].color = Color.Black
style.borders[BorderType.RIGHT_BORDER].line_style = CellBorderType.THIN
style.borders[BorderType.RIGHT_BORDER].color = Color.Black

# Применение FormatAll: принудительно применяет единый стиль к каждой ячейке сводной таблицы,
# переопределяя любые ранее установленные PivotTableStyleType / PivotTableStyleName
pivot_table.format_all(style)

# Сохранение книги в современном формате .xlsx
workbook.save("output.xlsx")
```

## **Какой API стилей мне следует использовать?**

Выбор API стилей зависит от формата файла, в который вы сохраняете. Используйте таблицу ниже как краткий справочник.

| Целевой формат файла | Используемый API | Примечания |
|---|---|---|
| `.xls` (устаревший) | `PivotTable.auto_format_type` | Значения из `aspose.cells.pivot.PivotTableAutoFormatType` (например, `REPORT_1`–`REPORT_10`, `CLASSIC`, `TABLE_1`–`TABLE_10`). Игнорируется при сохранении в современных форматах. |
| `.xlsx` / `.xlsm` / `.xlsb` (современный, встроенный стиль) | `PivotTable.pivot_table_style_type` | Значения из `aspose.cells.PivotTableStyleType` (светлые/тёмные темы, включая дополнения Excel 2017). |
| `.xlsx` / `.xlsm` / `.xlsb` (современный, пользовательский стиль) | `PivotTable.pivot_table_style_name` + `worksheets.table_styles.add_pivot_table_style(...)` | Используйте, когда встроенных предустановок недостаточно. Настройка через `table_style_element.set_element_style(...)`. |
| Любой формат (единообразное переопределение) | `PivotTable.format_all(Style)` | Удобный метод, который переопределяет все остальные настройки стилей для всей сводной таблицы. |

В случае сомнений сохраняйте в формате `.xlsx` и используйте `pivot_table_style_type` для встроенных тем или `pivot_table_style_name` для пользовательских тем.

## **Связанные статьи**

- [Обновление сводных таблиц в Aspose.Cells for Python via .NET](/cells/ru/python-net/refresh-pivot-table/)

{{< app/cells/assistant language="python" >}}