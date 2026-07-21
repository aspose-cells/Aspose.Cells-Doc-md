---
title: Применение стилей к сводным таблицам
linktitle: Применение стилей к сводным таблицам
description: Узнайте, как применять встроенные и пользовательские стили к сводным таблицам в Aspose.Cells for Python via Java, включая устаревшие автоформаты XLS, современные именованные стили Excel 2007+, пользовательские стили сводных таблиц и вспомогательный метод FormatAll.
keywords: Aspose.Cells, Python via Java, сводная таблица, стиль, PivotTableStyleType, AutoFormatType, FormatAll, пользовательский стиль, PivotTableStyleName, TableStyles
type: docs
weight: 200
url: /ru/python-java/apply-style-to-pivot-table/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells поддерживает применение как устаревших автоформатов сводных таблиц (предназначенных для файлов `.xls`), так и современных именованных или пользовательских стилей сводных таблиц (предназначенных для файлов `.xlsx`, `.xlsm` и `.xlsb`). Вызываемый API зависит от формата файла, в который сохраняется рабочая книга, а не от формата, из которого она была загружена.

{{% /alert %}}

## **Введение**

Aspose.Cells предоставляет два параллельных API стилей для сводных таблиц. Выбор между ними определяется форматом файла, в который сохраняется рабочая книга, а не форматом, из которого она была считана. Рабочую книгу, загруженную из файла `.xls`, можно повторно сохранить как `.xlsx`, и в этом случае применяется современный API стилей, а не устаревший.

Для устаревшего вывода в формате `.xls` используйте метод `pivotTable.setAutoFormatType(int)` вместе с перечислением `com.aspose.cells.pivot.PivotTableAutoFormatType`. Этот API соответствует средству выбора автоформата, которое предлагал классический Excel для сводных таблиц.

Для современного вывода в форматах `.xlsx`, `.xlsm` и `.xlsb` доступны две разновидности API стилей:

- `pivotTable.setPivotTableStyleType(int)` выбирает один из встроенных именованных стилей (светлые и тёмные темы, включая стили, добавленные в Excel 2017). Эти предустановки доступны только для чтения.
- `pivotTable.setPivotTableStyleName(String)` выбирает пользовательский стиль, который вы определяете самостоятельно через `workbook.getWorksheets().getTableStyles().addPivotTableStyle(String)`. Пользовательские стили необходимы, когда требуется изменить цвета, границы или шрифты сверх того, что предлагают предустановки.

Кроме того, `pivotTable.formatAll(Style)` — это вспомогательный метод, который применяет один объект `Style` к каждой ячейке сводной таблицы, переопределяя всё, что было установлено с помощью любого из API имён стилей выше. Это полезно, когда требуется единообразное оформление вне зависимости от базовой темы.

## **Применение устаревшего предустановленного автоформата XLS**

Метод `setAutoFormatType` сводной таблицы принимает значение из перечисления `com.aspose.cells.pivot.PivotTableAutoFormatType`. Доступные значения: `REPORT_1` — `REPORT_10`, `CLASSIC` и `TABLE_1` — `TABLE_10`.

{{% alert color="primary" %}}

`setAutoFormatType` учитывается только в том случае, когда рабочая книга сохраняется в формате `.xls`. Когда та же рабочая книга сохраняется как `.xlsx`, `.xlsm` или `.xlsb`, Excel игнорирует эту настройку и использует настройки `setPivotTableStyleType` и `setPivotTableStyleName`.

{{% /alert %}}

В следующем примере загружается новая рабочая книга, заполняются тестовые данные Fruit/Year/Amount, добавляется сводная таблица, применяется `PivotTableAutoFormatType.REPORT_5`, и результат сохраняется в формате `.xls`.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, PivotFieldType, PivotTableAutoFormatType

# Сценарий 1: Применение предустановленного автоформата устаревшего XLS
# Используемый API: PivotTable.AutoFormatType
# Целевой формат файла: .xls (устаревший)
# Для полных примеров и файлов данных перейдите по ссылке https://github.com/aspose-cells/Aspose.Cells-for-.NET

# Создаём новую рабочую книгу
workbook = Workbook()

# Получаем первый рабочий лист
sheet = workbook.getWorksheets().get(0)

# Заполняем исходные данные строкой заголовка (Fruit, Year, Amount)
# и 9 строками данных, охватывающими grape, blueberry, kiwi, cherry за 2020 и 2021 годы
sheet.getCells().get(0, 0).putValue("Fruit")
sheet.getCells().get(0, 1).putValue("Year")
sheet.getCells().get(0, 2).putValue("Amount")

sheet.getCells().get(1, 0).putValue("grape")
sheet.getCells().get(1, 1).putValue(2020)
sheet.getCells().get(1, 2).putValue(50)

sheet.getCells().get(2, 0).putValue("blueberry")
sheet.getCells().get(2, 1).putValue(2020)
sheet.getCells().get(2, 2).putValue(30)

sheet.getCells().get(3, 0).putValue("kiwi")
sheet.getCells().get(3, 1).putValue(2020)
sheet.getCells().get(3, 2).putValue(25)

sheet.getCells().get(4, 0).putValue("cherry")
sheet.getCells().get(4, 1).putValue(2020)
sheet.getCells().get(4, 2).putValue(40)

sheet.getCells().get(5, 0).putValue("grape")
sheet.getCells().get(5, 1).putValue(2021)
sheet.getCells().get(5, 2).putValue(60)

sheet.getCells().get(6, 0).putValue("blueberry")
sheet.getCells().get(6, 1).putValue(2021)
sheet.getCells().get(6, 2).putValue(35)

sheet.getCells().get(7, 0).putValue("kiwi")
sheet.getCells().get(7, 1).putValue(2021)
sheet.getCells().get(7, 2).putValue(28)

sheet.getCells().get(8, 0).putValue("cherry")
sheet.getCells().get(8, 1).putValue(2021)
sheet.getCells().get(8, 2).putValue(45)

sheet.getCells().get(9, 0).putValue("grape")
sheet.getCells().get(9, 1).putValue(2020)
sheet.getCells().get(9, 2).putValue(45)

# Добавляем сводную таблицу в ячейку назначения E3 с именем "Pivot1", используя исходный диапазон A1:C10
pivotIndex = sheet.getPivotTables().add("A1:C10", "E3", "Pivot1")
pivotTable = sheet.getPivotTables().get(pivotIndex)

# Назначаем поля: Fruit -> Строки, Year -> Столбцы, Amount -> Данные
pivotTable.addFieldToArea(PivotFieldType.Row, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.Data, "Amount")

# Применяем предустановленный автоформат устаревшего XLS "Report5"
# Примечание: Это свойство имеет смысл только при сохранении в формате .xls.
# При сохранении в формате .xlsx/.xlsm/.xlsb Excel игнорирует AutoFormatType
# и использует то, что указано в PivotTableStyleType / PivotTableStyleName.
pivotTable.setAutoFormatType(PivotTableAutoFormatType.Report5)

# Сохраняем рабочую книгу в устаревшем формате .xls
workbook.save("output.xls")

jpype.shutdownJVM()
```

## **Применение современного именованного предустановленного стиля сводной таблицы**

Метод `setPivotTableStyleType` сводной таблицы принимает значение из перечисления `com.aspose.cells.PivotTableStyleType`. Перечисление охватывает светлые темы `PIVOT_TABLE_STYLE_LIGHT_1` — `PIVOT_TABLE_STYLE_LIGHT_28` и тёмные темы `PIVOT_TABLE_STYLE_DARK_1` — `PIVOT_TABLE_STYLE_DARK_28`. Стили, добавленные в Excel 2017 (вторая волна светлых и тёмных тем), доступны через то же перечисление.

Это рекомендуемый API для любого современного формата файла. В отличие от устаревшего автоформата, выбранный здесь стиль точно отображается в Excel и сохраняется при передаче через другие инструменты Office.

В следующем примере используются те же данные Fruit/Year/Amount, создаётся идентичная сводная таблица, применяется `PivotTableStyleType.PIVOT_TABLE_STYLE_DARK_1`, и рабочая книга сохраняется в формате `.xlsx`.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotTableStyleType, PivotFieldType

# Сценарий 2: Применение современного именованного стиля-пресета Excel 2007+ с помощью PivotTableStyleType.
# Целевой формат файла: .xlsx. Перечисление PivotTableStyleType находится в пространстве имён Aspose.Cells
# (а не в Aspose.Cells.Pivot) — именно поэтому нам не нужны никакие дополнительные using для него.
# Ссылка на GitHub: https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Examples/CSharp/PivotTables/ApplyStyleToPivotTable2.cs

workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)

# Строка заголовков: Fruit / Year / Amount
worksheet.getCells().get("A1").putValue("Fruit")
worksheet.getCells().get("B1").putValue("Year")
worksheet.getCells().get("C1").putValue("Amount")

# 9 строк данных Fruit / Year / Amount
worksheet.getCells().get("A2").putValue("Grape")
worksheet.getCells().get("B2").putValue(2020)
worksheet.getCells().get("C2").putValue(100)

worksheet.getCells().get("A3").putValue("Blueberry")
worksheet.getCells().get("B3").putValue(2020)
worksheet.getCells().get("C3").putValue(150)

worksheet.getCells().get("A4").putValue("Kiwi")
worksheet.getCells().get("B4").putValue(2020)
worksheet.getCells().get("C4").putValue(200)

worksheet.getCells().get("A5").putValue("Cherry")
worksheet.getCells().get("B5").putValue(2020)
worksheet.getCells().get("C5").putValue(180)

worksheet.getCells().get("A6").putValue("Grape")
worksheet.getCells().get("B6").putValue(2021)
worksheet.getCells().get("C6").putValue(120)

worksheet.getCells().get("A7").putValue("Blueberry")
worksheet.getCells().get("B7").putValue(2021)
worksheet.getCells().get("C7").putValue(170)

worksheet.getCells().get("A8").putValue("Kiwi")
worksheet.getCells().get("B8").putValue(2021)
worksheet.getCells().get("C8").putValue(210)

worksheet.getCells().get("A9").putValue("Cherry")
worksheet.getCells().get("B9").putValue(2021)
worksheet.getCells().get("C9").putValue(190)

worksheet.getCells().get("A10").putValue("Grape")
worksheet.getCells().get("B10").putValue(2021)
worksheet.getCells().get("C10").putValue(130)

# Добавление сводной таблицы в ячейке E3 с именем "Pivot1" на основе диапазона A1:C10
pivotIndex = worksheet.getPivotTables().add("A1:C10", "E3", "Pivot1")
pivotTable = worksheet.getPivotTables().get(pivotIndex)

# Назначение полей сводной таблицы: Fruit -> область строк, Year -> область столбцов, Amount -> область данных
pivotTable.addFieldToArea(PivotFieldType.Row, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.Column, "Year")
pivotTable.addFieldToArea(PivotFieldType.Data, "Amount")

# Применение современного именованного стиля-пресета сводной таблицы Excel 2007+.
# PivotTableStyleType — это корректный API для файлов .xlsx / .xlsm / .xlsb; AutoFormatType
# игнорируется Excel для этих форматов. PivotTableStyleDark1 принадлежит семейству тёмных тем
# (PivotTableStyleDark1..PivotTableStyleDark28), и то же перечисление также предоставляет
# более новые светлые/тёмные темы Excel 2017 (PivotTableStyleLight1..Light28 / Dark1..Dark28).
pivotTable.setPivotTableStyleType(PivotTableStyleType.PivotTableStyleDark1)

# Сохранение в современном формате .xlsx — это формат, для которого PivotTableStyleType имеет значение.
workbook.save("output.xlsx")

jpype.shutdownJVM()
```

## **Определение и применение пользовательского стиля сводной таблицы**

Встроенные предустановки не могут быть изменены. Когда требуется переопределить цвета, границы или шрифты, необходимо определить пользовательский стиль сводной таблицы. Рабочий процесс состоит из трёх шагов:

1. Добавьте пользовательский стиль в коллекцию `TableStyles` рабочей книги с помощью `workbook.getWorksheets().getTableStyles().addPivotTableStyle(String name)`. Этот метод возвращает индекс вновь созданного стиля.
2. Настройте стиль, добавляя элементы (такие как `WHOLE_TABLE` или `GRAND_TOTAL_ROW`) через `tableStyle.getTableStyleElements().add(TableStyleElementType)`, затем назначьте `Style` каждому элементу через `tableStyleElement.setElementStyle(Style)`.
3. Примените пользовательский стиль к сводной таблице, вызвав `pivotTable.setPivotTableStyleName(String)` с именем стиля. Не используйте здесь `setPivotTableStyleType`, поскольку этот метод выбирает встроенные предустановки.

{{% alert color="primary" %}}

`setPivotTableStyleName` и `setPivotTableStyleType` не являются взаимозаменяемыми. Используйте `setPivotTableStyleType` для встроенных предустановок, а `setPivotTableStyleName` — для пользовательских стилей, определённых через `addPivotTableStyle`. Установка обоих безопасна, но отображается только тот, который соответствует предполагаемому источнику.

{{% /alert %}}

Доступные значения `TableStyleElementType` включают `WHOLE_TABLE`, `FIRST_ROW`, `LAST_ROW`, `FIRST_COLUMN`, `LAST_COLUMN`, `GRAND_TOTAL_ROW`, `GRAND_TOTAL_COLUMN`, `PAGE_FIELD_LABELS` и `PAGE_FIELD_VALUES`.

В следующем примере определяется пользовательский стиль сводной таблицы с тонкой чёрной границей для `WHOLE_TABLE` и жирным красным шрифтом для `GRAND_TOTAL_ROW`, затем он применяется через `setPivotTableStyleName`, и результат сохраняется в формате `.xlsx`.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat
from asposecells.api import PivotFieldType, TableStyleElementType, BorderType, CellBorderType
from java.awt import Color

workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)

# Заполнение исходных данных: строка заголовка + 9 строк данных (A1:C10)
worksheet.getCells().get("A1").putValue("Fruit")
worksheet.getCells().get("B1").putValue("Year")
worksheet.getCells().get("C1").putValue("Amount")

worksheet.getCells().get("A2").putValue("Grape")
worksheet.getCells().get("B2").putValue(2020)
worksheet.getCells().get("C2").putValue(100)

worksheet.getCells().get("A3").putValue("Blueberry")
worksheet.getCells().get("B3").putValue(2020)
worksheet.getCells().get("C3").putValue(200)

worksheet.getCells().get("A4").putValue("Kiwi")
worksheet.getCells().get("B4").putValue(2020)
worksheet.getCells().get("C4").putValue(300)

worksheet.getCells().get("A5").putValue("Cherry")
worksheet.getCells().get("B5").putValue(2020)
worksheet.getCells().get("C5").putValue(400)

worksheet.getCells().get("A6").putValue("Grape")
worksheet.getCells().get("B6").putValue(2021)
worksheet.getCells().get("C6").putValue(500)

worksheet.getCells().get("A7").putValue("Blueberry")
worksheet.getCells().get("B7").putValue(2021)
worksheet.getCells().get("C7").putValue(600)

worksheet.getCells().get("A8").putValue("Kiwi")
worksheet.getCells().get("B8").putValue(2021)
worksheet.getCells().get("C8").putValue(700)

worksheet.getCells().get("A9").putValue("Cherry")
worksheet.getCells().get("B9").putValue(2021)
worksheet.getCells().get("C9").putValue(800)

worksheet.getCells().get("A10").putValue("Grape")
worksheet.getCells().get("B10").putValue(2021)
worksheet.getCells().get("C10").putValue(900)

# Добавление сводной таблицы на основе A1:C10, привязанной к E3, с именем "Pivot1"
pivotIndex = worksheet.getPivotTables().add("A1:C10", "E3", "Pivot1")
pivotTable = worksheet.getPivotTables().get(pivotIndex)

pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year")
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount")

# Шаг 1: регистрация нового пользовательского стиля сводной таблицы и сохранение его индекса
styleIndex = workbook.getWorksheets().getTableStyles().addPivotTableStyle("CustomPivotStyle")
tableStyle = workbook.getWorksheets().getTableStyles().get(styleIndex)

# Шаг 2: добавление элемента WholeTable и применение тонких черных границ со всех четырех сторон
wholeTableElementIndex = tableStyle.getTableStyleElements().add(TableStyleElementType.WHOLE_TABLE)
wholeTableElement = tableStyle.getTableStyleElements().get(wholeTableElementIndex)
wholeTableStyle = workbook.createStyle()
wholeTableStyle.getBorders().get(BorderType.TOP_BORDER).setLineStyle(CellBorderType.THIN)
wholeTableStyle.getBorders().get(BorderType.TOP_BORDER).setColor(Color.BLACK)
wholeTableStyle.getBorders().get(BorderType.BOTTOM_BORDER).setLineStyle(CellBorderType.THIN)
wholeTableStyle.getBorders().get(BorderType.BOTTOM_BORDER).setColor(Color.BLACK)
wholeTableStyle.getBorders().get(BorderType.LEFT_BORDER).setLineStyle(CellBorderType.THIN)
wholeTableStyle.getBorders().get(BorderType.LEFT_BORDER).setColor(Color.BLACK)
wholeTableStyle.getBorders().get(BorderType.RIGHT_BORDER).setLineStyle(CellBorderType.THIN)
wholeTableStyle.getBorders().get(BorderType.RIGHT_BORDER).setColor(Color.BLACK)
wholeTableElement.setElementStyle(wholeTableStyle)

# Шаг 3: добавление элемента GrandTotalRow и применение жирного красного шрифта
grandTotalElementIndex = tableStyle.getTableStyleElements().add(TableStyleElementType.GRAND_TOTAL_ROW)
grandTotalElement = tableStyle.getTableStyleElements().get(grandTotalElementIndex)
grandTotalStyle = workbook.createStyle()
grandTotalStyle.getFont().setBold(True)
grandTotalStyle.getFont().setColor(Color.RED)
grandTotalElement.setElementStyle(grandTotalStyle)

# Шаг 4: применение пользовательского стиля по имени (НЕ через PivotTableStyleType, который предназначен для встроенных предустановок)
pivotTable.setPivotTableStyleName("CustomPivotStyle")

workbook.save("output.xlsx")

jpype.shutdownJVM()
```

## **Применение одного стиля ко всем ячейкам сводной таблицы с помощью FormatAll**

`pivotTable.formatAll(Style)` — это вспомогательный метод, который применяет один объект `Style` к каждой ячейке сводной таблицы, включая область данных, заголовки строк и столбцов, а также итоги. Всё, что было ранее установлено через `setPivotTableStyleType` или `setPivotTableStyleName`, переопределяется.

{{% alert color="primary" %}}

`formatAll` переопределяет и `setPivotTableStyleType`, и `setPivotTableStyleName`. Используйте его только тогда, когда требуется единообразное, не зависящее от темы оформление всей сводной таблицы.

{{% /alert %}}

В следующем примере создаётся `Style` с жёлтой сплошной заливкой, жирным тёмно-синим шрифтом и тонкими чёрными границами со всех сторон, затем он применяется через `formatAll`, и результат сохраняется в формате `.xlsx`.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, Style
from asposecells.api import Color
from asposecells.api import PivotTable, PivotFieldType
from asposecells.api import BorderType, CellBorderType, BackgroundType

# Сценарий 4: Применение единого стиля ко всем ячейкам сводной таблицы с помощью FormatAll
# Используемый API: PivotTable.FormatAll(Style)
# Целевой формат: .xlsx
# Ссылка на GitHub: см. репозиторий Aspose.Cells-for-.NET — примеры стилизации сводных таблиц

workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)

# Заполнение исходных данных: строка заголовка (строка 1) + 9 строк данных (строки 2-10)
worksheet.getCells().get("A1").putValue("Fruit")
worksheet.getCells().get("B1").putValue("Year")
worksheet.getCells().get("C1").putValue("Amount")

worksheet.getCells().get("A2").putValue("Grape")
worksheet.getCells().get("B2").putValue(2020)
worksheet.getCells().get("C2").putValue(5000)

worksheet.getCells().get("A3").putValue("Blueberry")
worksheet.getCells().get("B3").putValue(2020)
worksheet.getCells().get("C3").putValue(3000)

worksheet.getCells().get("A4").putValue("Kiwi")
worksheet.getCells().get("B4").putValue(2020)
worksheet.getCells().get("C4").putValue(4000)

worksheet.getCells().get("A5").putValue("Cherry")
worksheet.getCells().get("B5").putValue(2020)
worksheet.getCells().get("C5").putValue(2000)

worksheet.getCells().get("A6").putValue("Grape")
worksheet.getCells().get("B6").putValue(2021)
worksheet.getCells().get("C6").putValue(6000)

worksheet.getCells().get("A7").putValue("Blueberry")
worksheet.getCells().get("B7").putValue(2021)
worksheet.getCells().get("C7").putValue(3500)

worksheet.getCells().get("A8").putValue("Kiwi")
worksheet.getCells().get("B8").putValue(2021)
worksheet.getCells().get("C8").putValue(4500)

worksheet.getCells().get("A9").putValue("Cherry")
worksheet.getCells().get("B9").putValue(2021)
worksheet.getCells().get("C9").putValue(2500)

worksheet.getCells().get("A10").putValue("Grape")
worksheet.getCells().get("B10").putValue(2021)
worksheet.getCells().get("C10").putValue(5500)

# Добавление сводной таблицы: исходный диапазон A1:C10, целевая ячейка E3, имя "Pivot1"
pivotIndex = worksheet.getPivotTables().add("A1:C10", "E3", "Pivot1")
pivotTable = worksheet.getPivotTables().get(pivotIndex)

# Назначение полей сводной таблицы: Fruit -> область строк, Year -> область столбцов, Amount -> область данных
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year")
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount")

# Создание стиля, который будет принудительно применён к каждой ячейке сводной таблицы
style = workbook.createStyle()
style.setForegroundColor(Color.YELLOW)
style.setPattern(BackgroundType.SOLID)
style.getFont().setIsBold(True)
style.getFont().setColor(Color.DARK_BLUE)
style.getBorders().get(BorderType.TOP_BORDER).setLineStyle(CellBorderType.THIN)
style.getBorders().get(BorderType.TOP_BORDER).setColor(Color.BLACK)
style.getBorders().get(BorderType.BOTTOM_BORDER).setLineStyle(CellBorderType.THIN)
style.getBorders().get(BorderType.BOTTOM_BORDER).setColor(Color.BLACK)
style.getBorders().get(BorderType.LEFT_BORDER).setLineStyle(CellBorderType.THIN)
style.getBorders().get(BorderType.LEFT_BORDER).setColor(Color.BLACK)
style.getBorders().get(BorderType.RIGHT_BORDER).setLineStyle(CellBorderType.THIN)
style.getBorders().get(BorderType.RIGHT_BORDER).setColor(Color.BLACK)

# Применение FormatAll: принудительно применяет этот единый стиль ко всем ячейкам сводной таблицы,
# переопределяя любые ранее установленные PivotTableStyleType / PivotTableStyleName
pivotTable.formatAll(style)

# Сохранение книги в современном формате .xlsx
workbook.save("output.xlsx")

jpype.shutdownJVM()
```

## **Какой API стилей следует использовать?**

Выбор API стилей зависит от формата файла, в который выполняется сохранение. Используйте приведённую ниже таблицу в качестве краткого справочника.

| Целевой формат файла | Используемый API | Примечания |
|---|---|---|
| `.xls` (устаревший) | `pivotTable.setAutoFormatType(int)` | Значения из `com.aspose.cells.pivot.PivotTableAutoFormatType` (например, `REPORT_1`–`REPORT_10`, `CLASSIC`, `TABLE_1`–`TABLE_10`). Игнорируются при сохранении в современных форматах. |
| `.xlsx` / `.xlsm` / `.xlsb` (современный, встроенный стиль) | `pivotTable.setPivotTableStyleType(int)` | Значения из `com.aspose.cells.PivotTableStyleType` (светлые/тёмные темы, включая добавленные в Excel 2017). |
| `.xlsx` / `.xlsm` / `.xlsb` (современный, пользовательский стиль) | `pivotTable.setPivotTableStyleName(String)` + `tableStyles.addPivotTableStyle(String)` | Используйте, когда встроенных предустановок недостаточно. Настройка через `tableStyleElement.setElementStyle(Style)`. |
| Любой формат (равномерное переопределение) | `pivotTable.formatAll(Style)` | Вспомогательный метод, переопределяющий все остальные настройки стилей по всей сводной таблице. |

При возникновении сомнений сохраняйте в формате `.xlsx` и используйте `setPivotTableStyleType` для встроенных тем или `setPivotTableStyleName` для пользовательских тем.

## **Связанные статьи**

- [Обновление сводных таблиц в Aspose.Cells for Aspose.Cells for Python via Java](/cells/ru/python-java/refresh-pivot-table/)

{{< app/cells/assistant language="python" >}}