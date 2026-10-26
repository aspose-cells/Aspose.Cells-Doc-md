---
title: Применение стилей к сводным таблицам в Aspose.Cells for Python via .NET
description: Узнайте, как применять встроенные и пользовательские стили к сводным таблицам в Aspose.Cells for Python via .NET, включая устаревшие автоформаты XLS, современные именованные стили Excel 2007+, пользовательские стили сводных таблиц и сокращение _format_all.
linktitle: Применение стилей к сводной таблице
keywords: Aspose.Cells Python via .NET, стиль сводной таблицы, PivotTableStyleType, AutoFormatType, FormatAll, пользовательский стиль, PivotTableStyleName, TableStyles
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
Aspose.Cells предоставляет два параллельных API стилей для сводных таблиц. Выбор между ними определяется форматом файла, в который вы сохраняете рабочая книгу, а не форматом, из которого она была прочитана. Рабочая книга, загруженная из файла `.xls`, может быть сохранена как `.xlsx`, и в этом случае применяется современный API стилей, а не устаревший.
- `PivotTable.pivot_table_style_type` выбирает один из встроенных именованных стилей (светлые и тёмные темы, включая стили, добавленные в Excel 2017). Эти предустановки доступны только для чтения.
- `PivotTable.pivot_table_style_name` выбирает пользовательский стиль, который вы определяете самостоятельно с помощью `workbook.worksheets.table_styles.add_pivot_table_style(...)`. Пользовательские стили необходимы, когда требуется изменить цвета, границы или шрифты сверх того, что предлагают предустановки.
Кроме того, `PivotTable.format_all(Style)` — это сокращение, которое применяет один объект `Style` к каждой ячейке сводной таблицы, переопределяя всё, что было задано через любой из указанных выше API имён стилей. Это полезно, когда требуется единообразный внешний вид вне зависимости от базовой темы.

## **Применение устаревшего предустановленного автоформата XLS**
`PivotTable.auto_format_type` принимает значение из перечисления `aspose.cells.pivot.PivotTableAutoFormatType`. Доступные значения: `REPORT_1` — `REPORT_10`, `CLASSIC`, а также `TABLE_1` — `TABLE_10`.
В следующем примере загружается новая рабочая книга, заполняется примерными данными Fruit/Year/Amount, добавляется сводная таблица, применяется `PivotTableAutoFormatType.REPORT5`, и результат сохраняется в формате `.xls`.

{{% alert color="primary" %}}
**Почему нет полей столбцов?** Автоформаты серии Report (с `Report1` по `Report10`, с `Table1` по `Table10`) были разработаны в классическом Excel для **одномерных сводных таблиц**, содержащих только поля строк и значения, — у них нет встроенного оформления для заголовков полей столбцов. Если вашей сводной таблице нужны поля столбцов, используйте современные предустановки `PivotTableStyleType` из [Сценария 2](#apply-a-modern-named-preset-pivot-table-style), которые предназначены для двухмерной компоновки, применяемой в современном Excel.
{{% /alert %}}

```python
import aspose.cells as ac
from aspose.cells.pivot import PivotFieldType
from aspose.cells.pivot import PivotTableAutoFormatType
# Scenario 1: Apply a legacy XLS preset autoformat
# API in use: PivotTable.AutoFormatType
# Target file format: .xls (legacy)
# For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-.NET
# Create a new workbook
workbook = ac.Workbook()
# Get the first worksheet
sheet = workbook.worksheets[0]
# Populate the source data with header row (Fruit, Year, Amount)
# and 9 data rows covering grape, blueberry, kiwi, cherry across 2020 and 2021
sheet.cells.get(0, 0).put_value("Fruit")
sheet.cells.get(0, 1).put_value("Year")
sheet.cells.get(0, 2).put_value("Amount")
sheet.cells.get(1, 0).put_value("grape")
sheet.cells.get(1, 1).put_value(2020)
sheet.cells.get(1, 2).put_value(50)
sheet.cells.get(2, 0).put_value("blueberry")
sheet.cells.get(2, 1).put_value(2020)
sheet.cells.get(2, 2).put_value(30)
sheet.cells.get(3, 0).put_value("kiwi")
sheet.cells.get(3, 1).put_value(2020)
sheet.cells.get(3, 2).put_value(25)
sheet.cells.get(4, 0).put_value("cherry")
sheet.cells.get(4, 1).put_value(2020)
sheet.cells.get(4, 2).put_value(40)
sheet.cells.get(5, 0).put_value("grape")
sheet.cells.get(5, 1).put_value(2021)
sheet.cells.get(5, 2).put_value(60)
sheet.cells.get(6, 0).put_value("blueberry")
sheet.cells.get(6, 1).put_value(2021)
sheet.cells.get(6, 2).put_value(35)
sheet.cells.get(7, 0).put_value("kiwi")
sheet.cells.get(7, 1).put_value(2021)
sheet.cells.get(7, 2).put_value(28)
sheet.cells.get(8, 0).put_value("cherry")
sheet.cells.get(8, 1).put_value(2021)
sheet.cells.get(8, 2).put_value(45)
sheet.cells.get(9, 0).put_value("grape")
sheet.cells.get(9, 1).put_value(2020)
sheet.cells.get(9, 2).put_value(45)
# Add a pivot table at destination cell E3, using source range A1:C10
pivot_table = sheet.pivot_tables.add("A1:C10", 2, 4)
# Assign fields: Fruit -> Rows, Amount -> Data
pivot_table.add_field_to_area(PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Amount")
# Apply the legacy XLS preset autoformat "Report5"
# Note: This property is only meaningful when saving as .xls.
# When saved as .xlsx/.xlsm/.xlsb, Excel ignores AutoFormatType
# and uses whatever PivotTableStyleType / PivotTableStyleName specifies.
pivot_table.auto_format_type = PivotTableAutoFormatType.REPORT5
# Save the workbook in legacy .xls format
workbook.save("output.xls")
```

## **Применение современного именованного предустановленного стиля сводной таблицы**
`pivot_table.pivot_table_style_type` выбирает один из встроенных именованных стилей, представленных в Excel 2007 для сводных таблиц. Перечисление `PivotTableStyleType` предоставляет три семейства тем: светлое семейство от `PIVOT_TABLE_STYLE_LIGHT1` до `PIVOT_TABLE_STYLE_LIGHT28`, среднее семейство от `PIVOT_TABLE_STYLE_MEDIUM1` до `PIVOT_TABLE_STYLE_MEDIUM28` и темное семейство от `PIVOT_TABLE_STYLE_DARK1` до `PIVOT_TABLE_STYLE_DARK28`. Оно также определяет `None` и `Custom`. Элементы с более высоким номером в каждом семействе представляют собой стили, добавленные в Excel 2017.
Эти предустановки доступны только для чтения. Как только возникает необходимость изменить цвета, границы или шрифты за пределами возможностей предустановки, необходимо определить пользовательский стиль сводной таблицы, как показано в [Сценарии 3](#define-and-apply-a-custom-pivot-table-style).

{{% alert color="primary" %}}
**Почему используются современные предустановки, а не автоформаты серий отчетов?** Значения `Report1`–`Report10` и `Table1`–`Table10` перечисления `PivotTableAutoFormatType` существовали до появления полей столбцов сводных таблиц, поэтому они не включают оформление заголовков полей столбцов, и Excel отображает такие заголовки без оформления. Предустановки `PivotTableStyleType` разработаны для двумерной структуры, используемой современным Excel, и одинаково оформляют заголовки полей строк и полей столбцов.
{{% /alert %}}

В этом сценарии повторно используется набор данных Fruit/Year/Amount из сценария 1, поле `Year` добавляется в область столбцов рядом с полем строк `Fruit` с помощью `PivotFieldType.COLUMN`, применяется предустановка темной темы `PIVOT_TABLE_STYLE_DARK1` с помощью `pivot_table.pivot_table_style_type`, а результат сохраняется в формате `.xlsx` — формате, для которого `PivotTableStyleType` имеет смысл.

```python
import aspose.cells as ac
from aspose.cells.pivot import PivotFieldType, PivotTableStyleType
# Scenario 2: Apply a modern Excel 2007+ named preset style using PivotTableStyleType.
# Target file format: .xlsx. PivotTableStyleType lives in aspose.cells.pivot,
# so it is imported explicitly alongside PivotFieldType.
# GitHub reference: https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Examples/CSharp/PivotTables/ApplyStyleToPivotTable2.cs
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
# Header row: Fruit / Year / Amount
worksheet.cells.get("A1").put_value("Fruit")
worksheet.cells.get("B1").put_value("Year")
worksheet.cells.get("C1").put_value("Amount")
# 9 data rows of Fruit / Year / Amount
worksheet.cells.get("A2").put_value("Grape")
worksheet.cells.get("B2").put_value(2020)
worksheet.cells.get("C2").put_value(100)
worksheet.cells.get("A3").put_value("Blueberry")
worksheet.cells.get("B3").put_value(2020)
worksheet.cells.get("C3").put_value(150)
worksheet.cells.get("A4").put_value("Kiwi")
worksheet.cells.get("B4").put_value(2020)
worksheet.cells.get("C4").put_value(200)
worksheet.cells.get("A5").put_value("Cherry")
worksheet.cells.get("B5").put_value(2020)
worksheet.cells.get("C5").put_value(180)
worksheet.cells.get("A6").put_value("Grape")
worksheet.cells.get("B6").put_value(2021)
worksheet.cells.get("C6").put_value(120)
worksheet.cells.get("A7").put_value("Blueberry")
worksheet.cells.get("B7").put_value(2021)
worksheet.cells.get("C7").put_value(170)
worksheet.cells.get("A8").put_value("Kiwi")
worksheet.cells.get("B8").put_value(2021)
worksheet.cells.get("C8").put_value(210)
worksheet.cells.get("A9").put_value("Cherry")
worksheet.cells.get("B9").put_value(2021)
worksheet.cells.get("C9").put_value(190)
worksheet.cells.get("A10").put_value("Grape")
worksheet.cells.get("B10").put_value(2021)
worksheet.cells.get("C10").put_value(130)
# Add a pivot table at E3, sourced from A1:C10
pivot_table = worksheet.pivot_tables.add("A1:C10", 2, 4)
# Assign pivot fields: Fruit -> Row area, Year -> Column area, Amount -> Data area
pivot_table.add_field_to_area(PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Amount")
# Apply a modern Excel 2007+ named preset pivot style.
# PivotTableStyleType is the correct API for .xlsx / .xlsm / .xlsb files; AutoFormatType
# is ignored by Excel for those formats. PIVOT_TABLE_STYLE_DARK1 belongs to the dark-theme
# family (PIVOT_TABLE_STYLE_DARK1..PIVOT_TABLE_STYLE_DARK28), and the same enum also exposes
# the newer Excel 2017 themes (PIVOT_TABLE_STYLE_LIGHT1..LIGHT28 / DARK1..DARK28).
pivot_table.pivot_table_style_type = PivotTableStyleType.PIVOT_TABLE_STYLE_DARK1
# Save as modern .xlsx — this is the format for which PivotTableStyleType is meaningful.
workbook.save("output.xlsx")
```

## **Определение и применение пользовательского стиля сводной таблицы**
Встроенные предустановки не могут быть изменены. Если требуется переопределить цвета, границы или шрифты, необходимо определить пользовательский стиль сводной таблицы. Рабочий процесс состоит из трёх шагов:
1. Добавьте пользовательский стиль в коллекцию `table_styles` рабочей книги с помощью `workbook.worksheets.table_styles.add_pivot_table_style(name)`. Метод возвращает индекс только что созданного стиля.
2. Настройте стиль, добавляя элементы (например, `WHOLE_TABLE` или `GRAND_TOTAL_ROW`) через `table_style.table_style_elements.add(TableStyleElementType)`, затем назначьте объект `Style` каждому элементу с помощью `table_style_element.set_element_style(Style)`.
3. Примените пользовательский стиль к сводной таблице, задав свойству `PivotTable.pivot_table_style_name` имя стиля. Здесь не следует использовать `pivot_table_style_type`, поскольку это свойство выбирает встроенные предустановки.

{{% alert color="primary" %}}
`pivot_table_style_name` и `pivot_table_style_type` не являются взаимозаменяемыми. Используйте `pivot_table_style_type` для встроенных предустановок, а `pivot_table_style_name` — для пользовательских стилей, которые вы определили через `add_pivot_table_style`. Установка обоих свойств безвредна, но отображается только то, которое соответствует предполагаемому источнику.
Доступные значения `TableStyleElementType` включают `WHOLE_TABLE`, `FIRST_ROW`, `LAST_ROW`, `FIRST_COLUMN`, `LAST_COLUMN`, `GRAND_TOTAL_ROW`, `GRAND_TOTAL_COLUMN`, `PAGE_FIELD_LABELS` и `PAGE_FIELD_VALUES`.
В следующем примере определяется пользовательский стиль сводной таблицы с тонкой чёрной границей для `WHOLE_TABLE` и жирным красным шрифтом для `GRAND_TOTAL_ROW`, затем он назначается через `pivot_table_style_name` и сохраняется как `.xlsx`.
{{% /alert %}}

```python
import aspose.cells as ac
from aspose.cells.pivot import PivotFieldType
from aspose.cells.tables import TableStyleElementType
from aspose.pydrawing import Color
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
# Populate source data: header row + 9 data rows (A1:C10)
worksheet.cells.get("A1").put_value("Fruit")
worksheet.cells.get("B1").put_value("Year")
worksheet.cells.get("C1").put_value("Amount")
worksheet.cells.get("A2").put_value("Grape")
worksheet.cells.get("B2").put_value(2020)
worksheet.cells.get("C2").put_value(100)
worksheet.cells.get("A3").put_value("Blueberry")
worksheet.cells.get("B3").put_value(2020)
worksheet.cells.get("C3").put_value(200)
worksheet.cells.get("A4").put_value("Kiwi")
worksheet.cells.get("B4").put_value(2020)
worksheet.cells.get("C4").put_value(300)
worksheet.cells.get("A5").put_value("Cherry")
worksheet.cells.get("B5").put_value(2020)
worksheet.cells.get("C5").put_value(400)
worksheet.cells.get("A6").put_value("Grape")
worksheet.cells.get("B6").put_value(2021)
worksheet.cells.get("C6").put_value(500)
worksheet.cells.get("A7").put_value("Blueberry")
worksheet.cells.get("B7").put_value(2021)
worksheet.cells.get("C7").put_value(600)
worksheet.cells.get("A8").put_value("Kiwi")
worksheet.cells.get("B8").put_value(2021)
worksheet.cells.get("C8").put_value(700)
worksheet.cells.get("A9").put_value("Cherry")
worksheet.cells.get("B9").put_value(2021)
worksheet.cells.get("C9").put_value(800)
worksheet.cells.get("A10").put_value("Grape")
worksheet.cells.get("B10").put_value(2021)
worksheet.cells.get("C10").put_value(900)
# Add pivot table sourced from A1:C10, anchored at E3
pivot_table = worksheet.pivot_tables.add("A1:C10", 2, 4)
pivot_table.add_field_to_area(PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Amount")
# Step 1: register a new custom pivot table style and capture its index
style_index = workbook.worksheets.table_styles.add_pivot_table_style("CustomPivotStyle")
table_style = workbook.worksheets.table_styles[style_index]
# Step 2: add a WholeTable element and apply thin black borders on all four sides
whole_table_element_index = table_style.table_style_elements.add(TableStyleElementType.WHOLE_TABLE)
whole_table_element = table_style.table_style_elements[whole_table_element_index]
whole_table_style = workbook.create_style()
whole_table_style.borders.get(ac.BorderType.TOP_BORDER).line_style = ac.CellBorderType.THIN
whole_table_style.borders.get(ac.BorderType.TOP_BORDER).color = Color.black
whole_table_style.borders.get(ac.BorderType.BOTTOM_BORDER).line_style = ac.CellBorderType.THIN
whole_table_style.borders.get(ac.BorderType.BOTTOM_BORDER).color = Color.black
whole_table_style.borders.get(ac.BorderType.LEFT_BORDER).line_style = ac.CellBorderType.THIN
whole_table_style.borders.get(ac.BorderType.LEFT_BORDER).color = Color.black
whole_table_style.borders.get(ac.BorderType.RIGHT_BORDER).line_style = ac.CellBorderType.THIN
whole_table_style.borders.get(ac.BorderType.RIGHT_BORDER).color = Color.black
whole_table_element.set_element_style(whole_table_style)
# Step 3: add a GrandTotalRow element and apply bold red font
grand_total_element_index = table_style.table_style_elements.add(TableStyleElementType.GRAND_TOTAL_ROW)
grand_total_element = table_style.table_style_elements[grand_total_element_index]
grand_total_style = workbook.create_style()
grand_total_style.font.is_bold = True
grand_total_style.font.color = Color.red
grand_total_element.set_element_style(grand_total_style)
# Step 4: apply the custom style by name (NOT by PivotTableStyleType, which is for built-in presets)
pivot_table.pivot_table_style_name = "CustomPivotStyle"
workbook.save("output.xlsx")
```

## **Применение одного стиля ко всем ячейкам сводной таблицы с помощью format_all**
`PivotTable.format_all(Style)` — это сокращение, которое применяет один объект `Style` к каждой ячейке сводной таблицы, включая область данных, заголовки строк и столбцов, а также итоги. Всё, что было ранее установлено через `pivot_table_style_type` или `pivot_table_style_name`, переопределяется.

{{% alert color="primary" %}}
`format_all` переопределяет как `pivot_table_style_type`, так и `pivot_table_style_name`. Используйте его только в тех случаях, когда требуется единообразный, не зависящий от темы внешний вид по всей сводной таблице.
В следующем примере создаётся объект `Style` с жёлтой сплошной заливкой, жирным тёмно-синим шрифтом и тонкими чёрными границами со всех сторон, затем он применяется с помощью `format_all` и сохраняется как `.xlsx`.
{{% /alert %}}

```python
from aspose.pydrawing import Color
import aspose.cells as ac
from aspose.cells.pivot import PivotFieldType
from aspose.cells import BackgroundType, CellBorderType, BorderType
# Scenario 4: Apply a single Style to every pivot table cell using format_all
# API in use: PivotTable.format_all(Style)
# Target format: .xlsx
# GitHub reference: see Aspose.Cells-for-.NET repository — pivot table styling examples
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
# Populate source data: header row (row 1) + 9 data rows (rows 2-10)
worksheet.cells.get("A1").put_value("Fruit")
worksheet.cells.get("B1").put_value("Year")
worksheet.cells.get("C1").put_value("Amount")
worksheet.cells.get("A2").put_value("Grape")
worksheet.cells.get("B2").put_value(2020)
worksheet.cells.get("C2").put_value(5000)
worksheet.cells.get("A3").put_value("Blueberry")
worksheet.cells.get("B3").put_value(2020)
worksheet.cells.get("C3").put_value(3000)
worksheet.cells.get("A4").put_value("Kiwi")
worksheet.cells.get("B4").put_value(2020)
worksheet.cells.get("C4").put_value(4000)
worksheet.cells.get("A5").put_value("Cherry")
worksheet.cells.get("B5").put_value(2020)
worksheet.cells.get("C5").put_value(2000)
worksheet.cells.get("A6").put_value("Grape")
worksheet.cells.get("B6").put_value(2021)
worksheet.cells.get("C6").put_value(6000)
worksheet.cells.get("A7").put_value("Blueberry")
worksheet.cells.get("B7").put_value(2021)
worksheet.cells.get("C7").put_value(3500)
worksheet.cells.get("A8").put_value("Kiwi")
worksheet.cells.get("B8").put_value(2021)
worksheet.cells.get("C8").put_value(4500)
worksheet.cells.get("A9").put_value("Cherry")
worksheet.cells.get("B9").put_value(2021)
worksheet.cells.get("C9").put_value(2500)
worksheet.cells.get("A10").put_value("Grape")
worksheet.cells.get("B10").put_value(2021)
worksheet.cells.get("C10").put_value(5500)
# Add pivot table: source range A1:C10, destination cell E3
pivot_table = worksheet.pivot_tables.add("A1:C10", 2, 4)
# Assign pivot fields: Fruit -> Row area, Year -> Column area, Amount -> Data area
pivot_table.add_field_to_area(PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Amount")
# Build a Style that will be forced onto every cell of the pivot table
style = workbook.create_style()
style.foreground_color = Color.yellow
style.pattern = BackgroundType.SOLID
style.font.is_bold = True
style.font.color = Color.dark_blue
style.borders.get(BorderType.TOP_BORDER).line_style = CellBorderType.THIN
style.borders.get(BorderType.TOP_BORDER).color = Color.black
style.borders.get(BorderType.BOTTOM_BORDER).line_style = CellBorderType.THIN
style.borders.get(BorderType.BOTTOM_BORDER).color = Color.black
style.borders.get(BorderType.LEFT_BORDER).line_style = CellBorderType.THIN
style.borders.get(BorderType.LEFT_BORDER).color = Color.black
style.borders.get(BorderType.RIGHT_BORDER).line_style = CellBorderType.THIN
style.borders.get(BorderType.RIGHT_BORDER).color = Color.black
# Apply format_all: forces this single style onto every cell of the pivot table,
# overriding any PivotTableStyleType / PivotTableStyleName previously set
pivot_table.format_all(style)
# Save the workbook in the modern .xlsx format
workbook.save("output.xlsx")
```

## **Какой API стилей следует использовать?**
Выбор API стилей зависит от формата файла, в который вы сохраняете. Используйте приведённую ниже таблицу в качестве краткого справочника.
| Целевой формат файла | Используемый API | Примечания |
|---|---|---|
| `.xls` (устаревший) | `PivotTable.auto_format_type` | Значения из `aspose.cells.pivot.PivotTableAutoFormatType` (например, `REPORT_1`–`REPORT_10`, `CLASSIC`, `TABLE_1`–`TABLE_10`). Игнорируется при сохранении в современных форматах. |
| `.xlsx` / `.xlsm` / `.xlsb` (современный, встроенный стиль) | `PivotTable.pivot_table_style_type` | Значения из `aspose.cells.PivotTableStyleType` (светлые/тёмные темы, включая дополнения Excel 2017). |
| `.xlsx` / `.xlsm` / `.xlsb` (современный, пользовательский стиль) | `PivotTable.pivot_table_style_name` + `worksheets.table_styles.add_pivot_table_style(...)` | Используйте, когда встроенных предустановок недостаточно. Настройка выполняется через `table_style_element.set_element_style(...)`. |
| Любой формат (единообразное переопределение) | `PivotTable.format_all(Style)` | Сокращение, переопределяющее все остальные настройки стилей во всей сводной таблице. |
Если вы сомневаетесь, сохраняйте в формате `.xlsx` и используйте `pivot_table_style_type` для встроенных тем или `pivot_table_style_name` для пользовательских тем.

{{< app/cells/assistant language="python-net" >}}