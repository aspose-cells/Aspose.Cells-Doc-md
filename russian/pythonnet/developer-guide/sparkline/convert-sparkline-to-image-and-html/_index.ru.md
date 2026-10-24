---
title: Преобразование спарклайна в изображение и HTML в Aspose.Cells for Python via .NET
linktitle: Преобразование спарклайна в изображение и HTML в Aspose.Cells for Python via .NET
description: Узнайте, как визуализировать спарклайны Aspose.Cells в отдельные изображения для встраивания в ячейки и экспортировать рабочие листы со спарклайнами в HTML с помощью HtmlSaveOptions в Python via .NET.
keywords: Aspose.Cells, Python via .NET, спарклайн, sparkline.to_image, cell.embedded_image, HtmlSaveOptions, рендеринг спарклайна, преобразование спарклайна в изображение, экспорт спарклайна в HTML
type: docs
weight: 120
url: /ru/python-net/convert-sparkline-to-image-and-html/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Спарклайны — миниатюрные диаграммы, размещаемые внутри ячеек рабочего листа. Aspose.Cells позволяет извлекать каждый спарклайн в виде отдельного изображения (для встраивания в другую ячейку или внешний отчёт), а также экспортировать весь рабочий лист со спарклайнами в HTML для публикации в Интернете и просмотра в браузере. Свойство `cell.embedded_image`, используемое в данной статье, доступно начиная с версии **Aspose.Cells 26.5**.
{{% /alert %}}

## **Введение**
Спарклайны представляют собой компактный способ визуализации тенденций непосредственно внутри рабочего листа. В Excel спарклайны отображаются в ячейках, однако во многих реальных сценариях требуется вынести их за пределы ячейки — например, встроить в другую ячейку как статическое изображение, вложить в автоматическое электронное письмо или отобразить в HTML-отчёте, опубликованном в Интернете. Aspose.Cells поддерживает обе эти операции. Метод `sparkline.to_image` формирует изображение отдельного спарклайна и записывает его в поток; полученные байты можно присвоить свойству `cell.embedded_image`, чтобы изображение хранилось внутри одной ячейки рабочей книги. Кроме того, `HtmlSaveOptions` позволяет преобразовать всю рабочую книгу — вместе со спарклайнами — в автономный HTML-файл. В этой статье оба сценария описаны от начала до конца.

## **Сценарий 1 — Рендеринг спарклайнов в изображения и встраивание их в ячейки**
В этом сценарии создаётся рабочий лист, содержащий небольшой диапазон исходных значений. К диапазону добавляются три различные группы спарклайнов (Line, Column и Stacked/Win-Loss), после чего для каждой группы формируется PNG-изображение. Полученные байты PNG записываются в соседние ячейки как встроенные изображения. В итоге создаётся единый файл `.xlsx`, содержащий как нативные спарклайны, так и их статические изображения.

### **Пошаговые инструкции**
1. Определите рабочий каталог и убедитесь, что он существует на диске.
2. Создайте новый экземпляр `Workbook` и получите ссылку на первый `Worksheet`.
3. Заполните ячейки с `A1` по `E1` пятью числовыми значениями (например, ежедневными продажами или показаниями температуры).
4. Добавьте на рабочий лист три объекта `SparklineGroup`, вызвав `worksheet.sparkline_groups.add(...)`:
   - Группа `SparklineType.LINE` с ячейкой привязки `F1` и диапазоном данных `A1:E1`.
   - Группа `SparklineType.COLUMN` с ячейкой привязки `G1` и диапазоном данных `A1:E1`.
   - Группа `SparklineType.STACKED` (win/loss) с ячейкой привязки `H1` и диапазоном данных `A1:E1`.
5. Создайте экземпляр `ImageOrPrintOptions` и установите его свойство `image_type` в значение `ImageType.PNG`, чтобы каждый спарклайн сохранялся как прозрачное изображение PNG.
7. Сохраните рабочую книгу в файл `output_with_sparklines.xlsx`.

```python
from io import BytesIO
import aspose.cells as ac
from aspose.cells.charts import SparklineType
from aspose.cells.drawing import ImageType
from aspose.cells.rendering import ImageOrPrintOptions
# Создать новую книгу и получить доступ к первому листу
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
# Заполнить ячейки A1:E1 примерными данными
worksheet.cells.get("A1").put_value(5)
worksheet.cells.get("B1").put_value(-3)
worksheet.cells.get("C1").put_value(8)
worksheet.cells.get("D1").put_value(-2)
worksheet.cells.get("E1").put_value(6)
# Добавить группу линейных спарклайнов, привязанную к F1 (столбец 5, строка 0)
line_area = ac.CellArea()
line_area.start_column = 5
line_area.end_column = 5
line_area.start_row = 0
line_area.end_row = 0
line_idx = worksheet.sparkline_groups.add(SparklineType.LINE, "A1:E1", False, line_area)
# Добавить группу гистограммных спарклайнов, привязанную к G1 (столбец 6, строка 0)
column_area = ac.CellArea()
column_area.start_column = 6
column_area.end_column = 6
column_area.start_row = 0
column_area.end_row = 0
column_idx = worksheet.sparkline_groups.add(SparklineType.COLUMN, "A1:E1", False, column_area)
# Добавить группу спарклайнов «Выигрыш/проигрыш (с накоплением)», привязанную к H1 (столбец 7, строка 0)
stacked_area = ac.CellArea()
stacked_area.start_column = 7
stacked_area.end_column = 7
stacked_area.start_row = 0
stacked_area.end_row = 0
stacked_idx = worksheet.sparkline_groups.add(SparklineType.STACKED, "A1:E1", False, stacked_area)
# Настроить параметры изображения для вывода PNG
image_options = ImageOrPrintOptions()
image_options.image_type = ImageType.PNG
# Преобразовать линейный спарклайн в изображение и встроить его в ячейку F2
line_sp = worksheet.sparkline_groups[line_idx].sparklines[0]
ms = BytesIO()
line_sp.to_image(ms, image_options)
worksheet.cells.get("F2").embedded_image = ms.getvalue()
# Преобразовать гистограммный спарклайн в изображение и встроить его в ячейку G2
column_sp = worksheet.sparkline_groups[column_idx].sparklines[0]
ms = BytesIO()
column_sp.to_image(ms, image_options)
worksheet.cells.get("G2").embedded_image = ms.getvalue()
# Преобразовать спарклайн «Выигрыш/проигрыш» в изображение и встроить его в ячейку H2
stacked_sp = worksheet.sparkline_groups[stacked_idx].sparklines[0]
ms = BytesIO()
stacked_sp.to_image(ms, image_options)
worksheet.cells.get("H2").embedded_image = ms.getvalue()
# Сохранить книгу на диск
workbook.save("output_with_sparklines.xlsx")
```

В приведённой выше рабочей книге для каждого спарклайна предусмотрены два варианта отображения: нативный спарклайн с ячейкой привязки в строке 1 и статическое изображение PNG, встроенное непосредственно в соседнюю ячейку строки 2. Поскольку изображения хранятся внутри самого файла, рабочая книга остаётся самодостаточной. Файл можно отправить по электронной почте или поместить в архив без нарушения ссылок на встроенные изображения. Сформируйте PNG-изображение для каждой группы спарклайнов, преобразуйте поток `BytesIO` в объект `bytes` и присвойте полученные байты свойству `embedded_image` целевой ячейки. Именно это присваивание делает изображение частью сохраняемого содержимого ячейки.

{{% alert color="primary" %}}
Поскольку каждая группа спарклайнов привязана к одной ячейке, можно обращаться к ней через индексатор `group.sparklines[0]` вместо перебора элементов с помощью цикла `for`. Такой подход делает код рендеринга компактным и соответствует типичной схеме «один спарклайн для каждой ячейки привязки». Сохранение байтов изображения с помощью `cell.embedded_image` доступно начиная с версии Aspose.Cells 26.5.
{{% /alert %}}

## **Сценарий 2 — Экспорт рабочего листа со спарклайнами в HTML**
Если рабочая книга содержит нативные спарклайны и, при необходимости, соответствующие встроенные изображения, рабочий лист можно сохранить в формате HTML для публикации в Интернете. Класс `HtmlSaveOptions` предоставляет параметры, необходимые для управления этим экспортом. В этом сценарии файл `output_with_sparklines.xlsx`, созданный в сценарии 1, повторно используется и преобразуется в компактный одностраничный HTML-документ.

### **Пошаговые инструкции**
1. Убедитесь, что файл `output_with_sparklines.xlsx`, созданный в сценарии 1, доступен на диске в рабочем каталоге.
2. Загрузите этот файл в новый экземпляр `Workbook`.
3. Создайте экземпляр `HtmlSaveOptions` и установите его свойство `export_active_worksheet_only` в значение `True`, чтобы итоговый HTML-файл содержал только активный рабочий лист, а не всю рабочую книгу.
4. Вызовите `workbook.save("sparklines.html", html_options)`, чтобы сохранить HTML-файл на диск.

```python
import aspose.cells as ac
workbook = ac.Workbook("output_with_sparklines.xlsx")
html_options = ac.HtmlSaveOptions()
html_options.export_active_worksheet_only = True
workbook.save("sparklines.html", html_options)
```

Приведённый выше код преобразует рабочую книгу со спарклайнами из сценария 1 в автономный HTML-файл. Спарклайны сохраняются как встроенные SVG- или PNG-изображения внутри сгенерированного HTML в зависимости от режима экспорта, поэтому пользователи могут просматривать тенденции в любом современном браузере, не требуя установки Excel. Если задать `export_active_worksheet_only` равным `True`, можно исключить случайную публикацию скрытых листов или вспомогательных данных: экспортируется только рабочий лист, который в данный момент виден пользователю.

{{% alert color="primary" %}}
Класс `HtmlSaveOptions` также предлагает дополнительные свойства для точной настройки вывода, например `export_hidden_worksheet`, `export_images_as_base64` и `encoding`. При необходимости настройте их с учётом требований целевой среды развёртывания.
{{% /alert %}}

## **Сводная информация по API**
В описанных выше сценариях используется небольшой набор API Aspose.Cells.
- Класс `SparklineGroup` и коллекция `worksheet.sparkline_groups` используются для задания типа (Line, Column, Stacked), диапазона данных и ячейки привязки для каждой группы спарклайнов. В этой статье каждая группа привязана к одной ячейке, поэтому доступ к ней осуществляется через `worksheet.sparkline_groups[i]`.
- Класс `Sparkline` и индексатор `group.sparklines[0]` обеспечивают доступ к отдельному спарклайну внутри группы. Поскольку каждая группа в примере содержит ровно один спарклайн, цикл `for` не требуется.
- `sparkline.to_image(Stream, ImageOrPrintOptions)` — метод рендеринга, который записывает изображение спарклайна в переданный поток. Метод возвращает `None`; после вызова необходимо прочитать байты из потока.
- `html_save_options.export_active_worksheet_only` (тип `bool`) ограничивает экспорт в HTML активным рабочим листом. Это одно из наиболее часто используемых свойств `HtmlSaveOptions` при создании одностраничных отчётов.
- `image_or_print_options.image_type` находится в namespace `aspose.cells.drawing` и задаёт формат изображения (например, `ImageType.PNG`), используемый при рендеринге с помощью `to_image`, а также при печати рабочих листов в виде изображений.

## **Связанные статьи**
- [Вставка изображения в ячейку](/cells/ru/python-net/inserting-an-image-into-a-cell/)

{{< app/cells/assistant language="python-net" >}}