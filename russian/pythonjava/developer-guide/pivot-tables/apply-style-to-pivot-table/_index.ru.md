---
title: Применение стилей к сводным таблицам в Aspose.Cells for Python via Java
linktitle: Применение стилей к сводным таблицам в Aspose.Cells for Python via Java
description: Узнайте, как применять встроенные и пользовательские стили к сводным таблицам в Aspose.Cells for Python via Java, включая устаревшие автоформаты XLS, современные именованные стили Excel 2007+, пользовательские стили сводных таблиц и вспомогательный метод formatAll.
keywords: Aspose.Cells Python via Java стиль сводной таблицы, PivotTableStyleType, AutoFormatType, FormatAll, пользовательский стиль, PivotTableStyleName, TableStyles
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
Aspose.Cells предоставляет два параллельных API стилей для сводных таблиц. Выбор между ними определяется форматом файла, в который сохраняется рабочая книга, а не форматом, из которого она была загружена. Рабочую книгу, загруженную из файла `.xls`, можно повторно сохранить как `.xlsx`, и в этом случае применяется современный API стилей, а не устаревший.
- `pivotTable.setPivotTableStyleType(int)` выбирает один из встроенных именованных стилей (светлые и тёмные темы, включая стили, добавленные в Excel 2017). Эти предустановки доступны только для чтения.
- `pivotTable.setPivotTableStyleName(String)` выбирает пользовательский стиль, который вы определяете самостоятельно через `workbook.getWorksheets().getTableStyles().addPivotTableStyle(String)`. Пользовательские стили требуются в тех случаях, когда необходимо изменить цвета, границы или шрифты за пределами возможностей предустановок.
Кроме того, `pivotTable.formatAll(Style)` — это вспомогательный метод, который применяет один объект `Style` к каждой ячейке сводной таблицы, переопределяя всё, что было задано через любой из API имени стиля выше. Это полезно, когда требуется единообразный внешний вид вне зависимости от базовой темы.

## **Применение устаревшего предустановленного автоформата XLS**
Метод `setAutoFormatType` для сводной таблицы принимает значение из перечисления `com.aspose.cells.pivot.PivotTableAutoFormatType`. Доступные значения: `REPORT_1`–`REPORT_10`, `CLASSIC` и `TABLE_1`–`TABLE_10`.
Следующий пример загружает новую рабочую книгу, заполняет исходные данные Fruit/Year/Amount, добавляет сводную таблицу, применяет `PivotTableAutoFormatType.REPORT_5` и сохраняет результат как `.xls`.

{{% alert color="primary" %}}
**Почему нет полей столбцов?** Автоформаты серии Report (`Report1`–`Report10`, `Table1`–`Table10`) были разработаны в классическом Excel для **одномерных сводных таблиц** только с полями строк и значениями — у них нет встроенного оформления для заголовков полей столбцов. Если вашей сводной таблице нужны поля столбцов, используйте современные предустановки `PivotTableStyleType` из [Сценария 2](#apply-a-modern-named-preset-pivot-table-style), которые предназначены для двухмерной компоновки, применяемой в современном Excel.
{{% /alert %}}

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, PivotFieldType, PivotTableAutoFormatType
# Сценарий 1: Применение предустановленного автоформата устаревшего формата XLS
# Используемый API: PivotTable.AutoFormatType
# Целевой формат файла: .xls (устаревший)
# Для полных примеров и файлов данных перейдите по ссылке https://github.com/aspose-cells/Aspose.Cells-for-.NET
# Создание новой рабочей книги
workbook = Workbook()
# Получение первого листа
sheet = workbook.getWorksheets().get(0)
# Заполнение исходных данных строкой заголовка (Fruit, Year, Amount)
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
# Добавление сводной таблицы в ячейку назначения E3 с именем, использующей исходный диапазон A1:C10
pivotTable = sheet.getPivotTables().add("A1:C10", 2, 4)
# Назначение полей: Fruit -> Строки, Amount -> Данные
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount")
# Применение предустановленного автоформата устаревшего формата XLS "Report5"
# Примечание: Это свойство имеет смысл только при сохранении в формате .xls.
# При сохранении в .xlsx/.xlsm/.xlsb Excel игнорирует AutoFormatType
# и использует то, что указано в PivotTableStyleType / PivotTableStyleName.
pivotTable.setAutoFormatType(PivotTableAutoFormatType.REPORT_5)
# Сохранение рабочей книги в устаревшем формате .xls
workbook.save("output.xls")
jpype.shutdownJVM()
```

## **Применение современного именованного предустановленного стиля сводной таблицы**
`pivotTable.setPivotTableStyleType(int)` выбирает один из встроенных именованных стилей, добавленных в Excel 2007 для сводных таблиц. Перечисление `PivotTableStyleType` включает три семейства тем: светлое — от `PIVOT_TABLE_STYLE_LIGHT1` до `PIVOT_TABLE_STYLE_LIGHT28`, среднее — от `PIVOT_TABLE_STYLE_MEDIUM1` до `PIVOT_TABLE_STYLE_MEDIUM28` и темное — от `PIVOT_TABLE_STYLE_DARK1` до `PIVOT_TABLE_STYLE_DARK_28`. Оно также определяет `None` и `Custom`. Элементы с более высокими номерами в каждом семействе — это стили, добавленные в Excel 2017.
Эти пресеты доступны только для чтения. Как только вам потребуется изменить цвета, границы или шрифты за пределами возможностей пресета, вместо него необходимо определить пользовательский стиль сводной таблицы, как показано в [Сценарии 3](#define-and-apply-a-custom-pivot-table-style).

{{% alert color="primary" %}}
**Почему современные пресеты, а не автоформаты для серий отчетов?** Значения `Report1`–`Report10` и `Table1`–`Table10` перечисления `PivotTableAutoFormatType` относятся к периоду до появления полей столбцов сводных таблиц, поэтому не содержат оформления заголовков полей столбцов, и Excel отображает такие заголовки без оформления. Пресеты `PivotTableStyleType` разработаны для двумерной компоновки, которую использует современный Excel, и одинаково оформляют заголовки полей строк и полей столбцов.
{{% /alert %}}

В этом сценарии повторно используется набор данных Fruit/Year/Amount из Сценария 1, `Year` добавляется в область столбцов рядом с полем строк `Fruit` с помощью `PivotFieldType.COLUMN`, применяется пресет темной темы `PIVOT_TABLE_STYLE_DARK1` с помощью `pivotTable.setPivotTableStyleType`, а результат сохраняется в формате `.xlsx` — формате, для которого `PivotTableStyleType` имеет смысл.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotTableStyleType, PivotFieldType
# Scenario 2: Apply a modern Excel 2007+ named preset style using PivotTableStyleType.
# Target file format: .xlsx. The PivotTableStyleType enum lives in the Aspose.Cells namespace
# GitHub reference: https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Examples/CSharp/PivotTables/ApplyStyleToPivotTable2.cs
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
# Header row: Fruit / Year / Amount
worksheet.getCells().get("A1").putValue("Fruit")
worksheet.getCells().get("B1").putValue("Year")
worksheet.getCells().get("C1").putValue("Amount")
# 9 data rows of Fruit / Year / Amount
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
# Add a pivot table at E3, sourced from A1:C10
pivotTable = worksheet.getPivotTables().add("A1:C10", 2, 4)
# Assign pivot fields: Fruit -> Row area, Year -> Column area, Amount -> Data area
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year")
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount")
# Apply a modern Excel 2007+ named preset pivot style.
# PivotTableStyleType is the correct API for .xlsx / .xlsm / .xlsb files; AutoFormatType
# is ignored by Excel for those formats. PivotTableStyleDark1 belongs to the dark-theme
# family (PivotTableStyleDark1..PivotTableStyleDark28), and the same enum also exposes the
# newer Excel 2017 light/dark themes (PivotTableStyleLight1..Light28 / Dark1..Dark28).
pivotTable.setPivotTableStyleType(PivotTableStyleType.PIVOT_TABLE_STYLE_DARK_1)
# Save as modern .xlsx — this is the format for which PivotTableStyleType is meaningful.
workbook.save("output.xlsx")
jpype.shutdownJVM()
```

## **Определение и применение пользовательского стиля сводной таблицы**
Встроенные предустановки не могут быть изменены. Всякий раз, когда требуется переопределить цвета, границы или шрифты, необходимо определить пользовательский стиль сводной таблицы. Рабочий процесс состоит из трёх шагов:
1. Добавьте пользовательский стиль в коллекцию `TableStyles` рабочей книги через `workbook.getWorksheets().getTableStyles().addPivotTableStyle(String name)`. Этот метод возвращает индекс только что созданного стиля.
2. Настройте стиль, добавляя элементы (например, `WHOLE_TABLE` или `GRAND_TOTAL_ROW`) через `tableStyle.getTableStyleElements().add(TableStyleElementType)`, затем назначьте каждому элементу `Style` через `tableStyleElement.setElementStyle(Style)`.
3. Примените пользовательский стиль к сводной таблице, вызвав `pivotTable.setPivotTableStyleName(String)` с именем стиля. Здесь не следует использовать `setPivotTableStyleType`, поскольку этот метод выбирает встроенные предустановки.

{{% alert color="primary" %}}
`setPivotTableStyleName` и `setPivotTableStyleType` не являются взаимозаменяемыми. Используйте `setPivotTableStyleType` для встроенных предустановок и `setPivotTableStyleName` для пользовательских стилей, определённых через `addPivotTableStyle`. Установка обоих безвредна, но отображается только тот, который соответствует предполагаемому источнику.
Доступные значения `TableStyleElementType` включают `WHOLE_TABLE`, `FIRST_ROW`, `LAST_ROW`, `FIRST_COLUMN`, `LAST_COLUMN`, `GRAND_TOTAL_ROW`, `GRAND_TOTAL_COLUMN`, `PAGE_FIELD_LABELS` и `PAGE_FIELD_VALUES`.
Следующий пример определяет пользовательский стиль сводной таблицы с тонкой чёрной границей для `WHOLE_TABLE` и жирным красным шрифтом для `GRAND_TOTAL_ROW`, затем применяет его через `setPivotTableStyleName` и сохраняет как `.xlsx`.
{{% /alert %}}

```python
import jpype
import jpype.imports
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat
from asposecells.api import PivotFieldType, TableStyleElementType, BorderType, CellBorderType
from asposecells.api import Color
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
# Добавление сводной таблицы из диапазона A1:C10, привязанная к ячейке E3, с именем
pivotTable = worksheet.getPivotTables().add("A1:C10", 2, 4)
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
wholeTableStyle.getBorders().getByBorderType(BorderType.TOP_BORDER).setLineStyle(CellBorderType.THIN)
wholeTableStyle.getBorders().getByBorderType(BorderType.TOP_BORDER).setColor(Color.getBlack())
wholeTableStyle.getBorders().getByBorderType(BorderType.BOTTOM_BORDER).setLineStyle(CellBorderType.THIN)
wholeTableStyle.getBorders().getByBorderType(BorderType.BOTTOM_BORDER).setColor(Color.getBlack())
wholeTableStyle.getBorders().getByBorderType(BorderType.LEFT_BORDER).setLineStyle(CellBorderType.THIN)
wholeTableStyle.getBorders().getByBorderType(BorderType.LEFT_BORDER).setColor(Color.getBlack())
wholeTableStyle.getBorders().getByBorderType(BorderType.RIGHT_BORDER).setLineStyle(CellBorderType.THIN)
wholeTableStyle.getBorders().getByBorderType(BorderType.RIGHT_BORDER).setColor(Color.getBlack())
wholeTableElement.setElementStyle(wholeTableStyle)
# Шаг 3: добавление элемента GrandTotalRow и применение жирного красного шрифта
grandTotalElementIndex = tableStyle.getTableStyleElements().add(TableStyleElementType.GRAND_TOTAL_ROW)
grandTotalElement = tableStyle.getTableStyleElements().get(grandTotalElementIndex)
grandTotalStyle = workbook.createStyle()
grandTotalStyle.getFont().setBold(True)
grandTotalStyle.getFont().setColor(Color.getRed())
grandTotalElement.setElementStyle(grandTotalStyle)
# Шаг 4: применение пользовательского стиля по имени (НЕ через PivotTableStyleType, который предназначен для встроенных предустановок)
pivotTable.setPivotTableStyleName("CustomPivotStyle")
workbook.save("output.xlsx")
jpype.shutdownJVM()
```

## **Применение одного стиля ко всем ячейкам сводной таблицы с помощью formatAll**
`pivotTable.formatAll(Style)` — это вспомогательный метод, который применяет один объект `Style` к каждой ячейке сводной таблицы, включая область данных, заголовки строк и столбцов, а также итоги. Всё, что ранее было задано через `setPivotTableStyleType` или `setPivotTableStyleName`, переопределяется.

{{% alert color="primary" %}}
`formatAll` переопределяет и `setPivotTableStyleType`, и `setPivotTableStyleName`. Используйте его только в тех случаях, когда требуется единообразный, не зависящий от темы внешний вид по всей сводной таблице.
Следующий пример создаёт `Style` с жёлтой сплошной заливкой, жирным тёмно-синим шрифтом и тонкими чёрными границами со всех сторон, затем применяет его с помощью `formatAll` и сохраняет как `.xlsx`.
{{% /alert %}}

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, Style
from asposecells.api import Color
from asposecells.api import PivotTable, PivotFieldType
from asposecells.api import BorderType, CellBorderType, BackgroundType
# Сценарий 4: Применение одного стиля к каждой ячейке сводной таблицы с помощью formatAll
# Используемый API: PivotTable.formatAll(Style)
# Целевой формат: .xlsx
# Ссылка на GitHub: см. репозиторий Aspose.Cells-for-.NET — примеры стилизации сводных таблиц
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
# Заполняем исходные данные: строка заголовка (строка 1) + 9 строк данных (строки 2-10)
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
# Добавляем сводную таблицу: исходный диапазон A1:C10, целевая ячейка E3, имя
pivotTable = worksheet.getPivotTables().add("A1:C10", 2, 4)
# Назначаем поля сводной таблицы: Fruit -> область строк, Year -> область столбцов, Amount -> область данных
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year")
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount")
# Создаём стиль, который будет принудительно применён к каждой ячейке сводной таблицы
style = workbook.createStyle()
style.setForegroundColor(Color.fromArgb(70, 130, 180))
style.setPattern(BackgroundType.SOLID)
style.getFont().setBold(True)
style.getFont().setColor(Color.getDarkBlue())
style.getBorders().getByBorderType(BorderType.TOP_BORDER).setLineStyle(CellBorderType.THIN)
style.getBorders().getByBorderType(BorderType.TOP_BORDER).setColor(Color.getBlack())
style.getBorders().getByBorderType(BorderType.BOTTOM_BORDER).setLineStyle(CellBorderType.THIN)
style.getBorders().getByBorderType(BorderType.BOTTOM_BORDER).setColor(Color.getBlack())
style.getBorders().getByBorderType(BorderType.LEFT_BORDER).setLineStyle(CellBorderType.THIN)
style.getBorders().getByBorderType(BorderType.LEFT_BORDER).setColor(Color.getBlack())
style.getBorders().getByBorderType(BorderType.RIGHT_BORDER).setLineStyle(CellBorderType.THIN)
style.getBorders().getByBorderType(BorderType.RIGHT_BORDER).setColor(Color.getBlack())
# Применяем formatAll: принудительно применяет этот единственный стиль к каждой ячейке сводной таблицы,
# переопределяя любой ранее установленный PivotTableStyleType / PivotTableStyleName
pivotTable.formatAll(style)
# Сохраняем книгу в современном формате .xlsx
workbook.save("output.xlsx")
jpype.shutdownJVM()
```

## **Какой API стилей следует использовать?**
Выбор API стилей зависит от формата файла, в который выполняется сохранение. Используйте приведённую ниже таблицу для быстрого ознакомления.
| Целевой формат файла | Используемый API | Примечания |
|---|---|---|
| `.xls` (устаревший) | `pivotTable.setAutoFormatType(int)` | Значения из `com.aspose.cells.pivot.PivotTableAutoFormatType` (например, `REPORT_1`–`REPORT_10`, `CLASSIC`, `TABLE_1`–`TABLE_10`). Игнорируется при сохранении в современных форматах. |
| `.xlsx` / `.xlsm` / `.xlsb` (современный, встроенный стиль) | `pivotTable.setPivotTableStyleType(int)` | Значения из `com.aspose.cells.PivotTableStyleType` (светлые/тёмные темы, включая дополнения Excel 2017). |
| `.xlsx` / `.xlsm` / `.xlsb` (современный, пользовательский стиль) | `pivotTable.setPivotTableStyleName(String)` + `tableStyles.addPivotTableStyle(String)` | Используйте, когда встроенных предустановок недостаточно. Настройка через `tableStyleElement.setElementStyle(Style)`. |
| Любой формат (единообразное переопределение) | `pivotTable.formatAll(Style)` | Вспомогательный метод, который переопределяет все остальные параметры стилей по всей сводной таблице. |
В случае сомнений сохраняйте как `.xlsx` и используйте `setPivotTableStyleType` для встроенных тем или `setPivotTableStyleName` для пользовательских тем.

{{< app/cells/assistant language="python" >}}