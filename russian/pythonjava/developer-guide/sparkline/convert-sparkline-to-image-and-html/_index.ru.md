---
title: Преобразование спарклайнов в изображения и HTML в Aspose.Cells for Python via Java
linktitle: Convert Sparkline to Image and HTML
description: Узнайте, как преобразовать спарклайны Aspose.Cells в отдельные изображения для встраивания в ячейки и экспортировать рабочие листы со спарклайнами в HTML с помощью HtmlSaveOptions.
keywords: Aspose.Cells, Python via Java, спарклайн, Sparkline.toImage, Cell.embeddedImage, HtmlSaveOptions, отрисовка спарклайна, преобразование спарклайна в изображение, экспорт спарклайна в HTML
type: docs
weight: 120
url: /ru/python-java/convert-sparkline-to-image-and-html/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Спарклайны — это миниатюрные диаграммы, размещаемые внутри ячеек рабочего листа. Aspose.Cells позволяет извлекать каждый спарклайн как отдельное изображение (для встраивания в другую ячейку или внешний отчёт), а также экспортировать весь рабочий лист со спарклайнами в HTML для распространения через браузер. Свойство `Cell.embedded_image`, используемое в данной статье, доступно в **Aspose.Cells 26.5 и более поздних версиях**.
{{% /alert %}}

## **Введение**

Спарклайны представляют собой компактный способ визуализации трендов непосредственно внутри рабочего листа. В то время как пользователи Excel видят их на месте, во многих реальных сценариях требуется, чтобы спарклайн покинул ячейку — например, чтобы быть встроенным в другую ячейку как статичное изображение, прикреплённым к автоматически формируемому письму или отрендеренным как часть HTML-отчёта, публикуемого в Интернете.

Aspose.Cells поддерживает обе эти операции. Метод `Sparkline.to_image` отрисовывает отдельный спарклайн в поток, а полученные байты могут быть присвоены свойству `Cell.embedded_image`, благодаря чему изображение сохраняется внутри одной ячейки рабочей книги. Отдельно, `HtmlSaveOptions` позволяет преобразовать всю рабочую книгу — включая спарклайны — в самодостаточный HTML-файл. В данной статье оба рабочих процесса рассматриваются от начала до конца.

## **Рабочий процесс 1 — Отрисовка спарклайнов в изображения и встраивание их в ячейки**

В этом рабочем процессе вы создадите рабочий лист, содержащий небольшой диапазон исходных значений, прикрепите к этому диапазону три разные группы спарклайнов (Line, Column и Stacked/Win-Loss), отрендерите каждую группу в формат PNG и запишете полученные байты PNG в соседние ячейки как встроенные изображения. Конечным результатом является единый файл `.xlsx`, который содержит как «живые» спарклайны, так и их отрендеренные изображения-аналоги.

### **Пошаговая инструкция**

1. Определите рабочую директорию и убедитесь, что она существует на диске.
2. Создайте новый объект `Workbook` и получите ссылку на первый `Worksheet`.
3. Заполните ячейки с `A1` по `E1` пятью числовыми значениями-примерами (например, ежедневные продажи или показания температуры).
4. Добавьте три объекта `SparklineGroup` в рабочий лист, вызывая `worksheet.sparkline_groups.add(...)`:
   - Группа `SparklineType.LINE`, привязанная к `F1`, с диапазоном данных `A1:E1`.
   - Группа `SparklineType.COLUMN`, привязанная к `G1`, с диапазоном данных `A1:E1`.
   - Группа `SparklineType.STACKED` (win/loss), привязанная к `H1`, с диапазоном данных `A1:E1`.
5. Создайте экземпляр `ImageOrPrintOptions` и установите его свойство `image_type` в значение `ImageType.PNG`, чтобы каждый спарклайн был отрендерен как прозрачный PNG.
6. Для каждой из трёх групп отрендерите её единственный спарклайн с помощью `group.sparklines[0].to_image(byte_array_output_stream, image_options)`, преобразуйте `ByteArrayOutputStream` в `byte[]` (или прочитайте его `to_byte_array()` в Python `bytes`) и присвойте байты соответственно `worksheet.cells["F2"].embedded_image`, `worksheet.cells["G2"].embedded_image` и `worksheet.cells["H2"].embedded_image`.
7. Сохраните рабочую книгу как `output_with_sparklines.xlsx`.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, CellArea, SparklineType, ImageType, ImageOrPrintOptions, Sparkline
from jpype import JClass

ByteArrayOutputStream = JClass('java.io.ByteArrayOutputStream')

# Создаём новую книгу и обращаемся к первому листу
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)

# Заполняем образцы данных в ячейках A1:E1
worksheet.getCells().get("A1").putValue(5)
worksheet.getCells().get("B1").putValue(-3)
worksheet.getCells().get("C1").putValue(8)
worksheet.getCells().get("D1").putValue(-2)
worksheet.getCells().get("E1").putValue(6)

# Добавляем группу линейных спарклайнов с привязкой к F1 (столбец 5, строка 0)
lineArea = CellArea()
lineArea.setStartColumn(5)
lineArea.setEndColumn(5)
lineArea.setStartRow(0)
lineArea.setEndRow(0)
lineIdx = worksheet.getSparklineGroups().add(SparklineType.Line, "A1:E1", False, lineArea)

# Добавляем группу столбчатых спарклайнов с привязкой к G1 (столбец 6, строка 0)
columnArea = CellArea()
columnArea.setStartColumn(6)
columnArea.setEndColumn(6)
columnArea.setStartRow(0)
columnArea.setEndRow(0)
columnIdx = worksheet.getSparklineGroups().add(SparklineType.Column, "A1:E1", False, columnArea)

# Добавляем группу спарклайнов Win/Loss (с накоплением) с привязкой к H1 (столбец 7, строка 0)
stackedArea = CellArea()
stackedArea.setStartColumn(7)
stackedArea.setEndColumn(7)
stackedArea.setStartRow(0)
stackedArea.setEndRow(0)
stackedIdx = worksheet.getSparklineGroups().add(SparklineType.Stacked, "A1:E1", False, stackedArea)

# Настраиваем параметры изображения для вывода в формате PNG
imageOptions = ImageOrPrintOptions()
imageOptions.setImageType(ImageType.Png)

# Преобразуем линейный спарклайн в изображение и встраиваем его в ячейку F2
lineSp = worksheet.getSparklineGroups().get(lineIdx).getSparklines().get(0)
ms = ByteArrayOutputStream()
lineSp.toImage(ms, imageOptions)
worksheet.getCells().get("F2").setEmbeddedImage(ms.toByteArray())

# Преобразуем столбчатый спарклайн в изображение и встраиваем его в ячейку G2
columnSp = worksheet.getSparklineGroups().get(columnIdx).getSparklines().get(0)
ms = ByteArrayOutputStream()
columnSp.toImage(ms, imageOptions)
worksheet.getCells().get("G2").setEmbeddedImage(ms.toByteArray())

# Преобразуем спарклайн Win/Loss в изображение и встраиваем его в ячейку H2
stackedSp = worksheet.getSparklineGroups().get(stackedIdx).getSparklines().get(0)
ms = ByteArrayOutputStream()
stackedSp.toImage(ms, imageOptions)
worksheet.getCells().get("H2").setEmbeddedImage(ms.toByteArray())

# Сохраняем книгу на диск
workbook.save("output_with_sparklines.xlsx")

jpype.shutdownJVM()
```

Приведённый выше код создаёт рабочую книгу, в которой каждое визуальное представление спарклайна дублируется в двух формах: «живой» нативный спарклайн, привязанный к строке 1, и статичное изображение PNG, встроенное непосредственно в соседнюю ячейку строки 2. Поскольку изображения хранятся внутри самого файла, рабочая книга остаётся единым самодостаточным артефактом, который можно отправить по электронной почте или заархивировать без нарушения ссылок на встроенные изображения. Отрендерите каждую группу спарклайнов в формат PNG, преобразуйте `ByteArrayOutputStream` в `byte[]` (или используйте `to_byte_array()` для получения объекта Python `bytes`) и присвойте массив свойству `embedded_image` целевой ячейки — именно это присваивание делает изображение частью хранимого содержимого ячейки.

{{% alert color="primary" %}}
Поскольку каждая группа спарклайнов привязана к одной ячейке, вы можете обращаться к ней через индексатор `group.sparklines[0]` вместо перебора в цикле `for`. Это делает код отрисовки компактным и соответствует типичному шаблону «один спарклайн на одну ячейку-якорь». Сохранение байтов изображения через `Cell.embedded_image` требует Aspose.Cells 26.5 или более поздней версии.
{{% /alert %}}

## **Рабочий процесс 2 — Экспорт рабочего листа со спарклайнами в HTML**

Когда рабочая книга содержит «живые» спарклайны (и опционально встроенные изображения-аналоги), весь рабочий лист может быть опубликован в Интернете путём сохранения его в формат HTML. Класс `HtmlSaveOptions` предоставляет необходимые настройки для управления этим экспортом; в данном рабочем процессе вы повторно используете файл `output_with_sparklines.xlsx`, созданный в Рабочем процессе 1, и преобразуете его в чистый одностраничный HTML-документ.

### **Пошаговая инструкция**

1. Убедитесь, что файл `output_with_sparklines.xlsx`, созданный в Рабочем процессе 1, доступен на диске в вашей рабочей директории.
2. Загрузите этот файл в новый экземпляр `Workbook`.
3. Создайте экземпляр `HtmlSaveOptions` и установите его свойство `export_active_worksheet_only` в значение `True`, чтобы результирующий HTML-файл содержал только активный рабочий лист, а не всю рабочую книгу.
4. Вызовите `workbook.save("sparklines.html", html_options)` для записи HTML-результата на диск.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, HtmlSaveOptions

workbook = Workbook("output_with_sparklines.xlsx")
htmlOptions = HtmlSaveOptions()
htmlOptions.setExportActiveWorksheetOnly(True)
workbook.save("sparklines.html", htmlOptions)

jpype.shutdownJVM()
```

Приведённый выше код берёт рабочую книгу со спарклайнами из Рабочего процесса 1 и превращает её в переносимый HTML-файл. Спарклайны сохраняются как встроенные SVG- или PNG-рендеры внутри сгенерированного HTML в зависимости от режима экспорта, поэтому конечные пользователи могут просматривать тренды в любом современном браузере без необходимости установки Excel. Устанавливая `export_active_worksheet_only` в значение `True`, вы избегаете случайной публикации скрытых листов или вспомогательных данных — экспортируется только рабочий лист, который в данный момент виден пользователю.

{{% alert color="primary" %}}
Класс `HtmlSaveOptions` предлагает дополнительные свойства для тонкой настройки вывода, такие как `export_hidden_worksheet`, `export_images_as_base64` и `encoding`. Настраивайте их по мере необходимости в соответствии с целевой средой развёртывания.
{{% /alert %}}

## **Сводная информация об API**

Описанные выше рабочие процессы опираются на небольшой набор API Aspose.Cells, работающих совместно.

- `SparklineGroup` и метод доступа к коллекции `worksheet.sparkline_groups` используются для объявления типа (Line, Column, Stacked), диапазона данных и ячейки-якоря для каждой группы спарклайнов. В данной статье каждая группа привязана к одной ячейке, поэтому доступ к группе осуществляется через `worksheet.sparkline_groups[i]`.
- `Sparkline` и индексатор `group.sparklines[0]` возвращают отдельный спарклайн внутри группы. Поскольку каждая группа в примере содержит ровно один спарклайн, цикл `for` не требуется.
- `Sparkline.to_image(OutputStream, ImageOrPrintOptions)` — это метод отрисовки, который записывает изображение спарклайна в переданный `OutputStream` (например, `ByteArrayOutputStream`). Метод возвращает `void`; байты считываются из потока после вызова.
- `Cell.embedded_image` — это свойство типа `byte[]`, которое хранит изображение внутри одной ячейки. Оно доступно в **Aspose.Cells 26.5 и более поздних версиях** и является рекомендуемым способом обратной записи спарклайна, отрендеренного методом `to_image`, в ту же рабочую книгу.
- `HtmlSaveOptions.export_active_worksheet_only` (тип `bool`) ограничивает экспорт в HTML только активным рабочим листом. Это одно из наиболее часто используемых свойств `HtmlSaveOptions` при формировании одностраничных отчётов.
- `ImageOrPrintOptions.image_type` находится в пространстве имён `com.aspose.cells.drawing` и задаёт формат изображения (например, `ImageType.PNG`), используемый при отрисовке методом `to_image` и при печати рабочих листов в изображения.

## **Связанные статьи**

- [Спарклайны в Aspose.Cells for Python via Java](/cells/ru/python-java/sparkline/)
- [Вставка изображения в ячейку](/cells/ru/python-java/inserting-an-image-into-a-cell/)

{{< app/cells/assistant language="python" >}}