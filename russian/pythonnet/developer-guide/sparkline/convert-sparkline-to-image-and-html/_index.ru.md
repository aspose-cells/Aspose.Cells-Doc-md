---
title: Преобразование спарклайнов в изображение и HTML в Aspose.Cells for Python via .NET
linktitle: Convert Sparkline to Image and HTML
description: Узнайте, как отрисовать спарклайны Aspose.Cells в отдельные изображения для встраивания в ячейки и экспортировать рабочие листы со спарклайнами в HTML с помощью HtmlSaveOptions в Python via .NET.
keywords: Aspose.Cells, Python via .NET, sparkline, sparkline.to_image, cell.embedded_image, HtmlSaveOptions, render sparkline, convert sparkline to image, export sparkline to HTML
type: docs
weight: 120
url: /ru/python-net/convert-sparkline-to-image-and-html/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Спарклайны — это миниатюрные диаграммы, размещаемые внутри ячеек рабочего листа. Aspose.Cells позволяет извлекать каждый спарклайн в виде отдельного изображения (для встраивания в другую ячейку или внешний отчёт), а также экспортировать весь рабочий лист со спарклайнами в HTML для распространения через браузер. Свойство `cell.embedded_image`, используемое в данной статье, доступно в **Aspose.Cells 26.5 и более поздних версиях**.
{{% /alert %}}

## **Введение**

Спарклайны — это компактный способ визуализации трендов непосредственно внутри рабочего листа. В то время как пользователи Excel видят их на месте, во многих реальных сценариях требуется, чтобы спарклайн покидал ячейку — например, чтобы быть встроенным в другую ячейку как статичная картинка, прикреплённым к автоматическому письму или отображённым в составе HTML-отчёта, публикуемого в Интернете.

Aspose.Cells поддерживает обе эти операции. Метод `sparkline.to_image` отрисовывает отдельный спарклайн в поток, и полученные байты могут быть присвоены свойству `cell.embedded_image`, чтобы картинка хранилась внутри одной ячейки рабочей книги. Отдельно, `HtmlSaveOptions` позволяет преобразовать всю рабочую книгу — включая спарклайны — в самодостаточный HTML-файл. В данной статье оба рабочих процесса рассмотрены от начала до конца.

## **Рабочий процесс 1 — Отрисовка спарклайнов в изображения и их встраивание в ячейки**

В этом рабочем процессе вы создадите рабочий лист, содержащий небольшой диапазон исходных значений, прикрепите к этому диапазону три разные группы спарклайнов (Линейная, Столбцовая и Стопочная/Win-Loss), отобразите каждую группу как PNG и запишете эти байты PNG в соседние ячейки как встроенные изображения. Конечный результат — единый файл `.xlsx`, который содержит как живые спарклайны, так и их отрендеренные графические аналоги.

### **Пошаговые инструкции**

1. Определите рабочую директорию и убедитесь, что она существует на диске.
2. Создайте новый объект `Workbook` и получите ссылку на первый `Worksheet`.
3. Заполните ячейки `A1`–`E1` пятью числовыми значениями-примерами (например, ежедневными продажами или показаниями температуры).
4. Добавьте три объекта `SparklineGroup` на рабочий лист, вызывая `worksheet.sparkline_groups.add(...)`:
   - Группа `SparklineType.LINE`, привязанная к `F1`, с диапазоном данных `A1:E1`.
   - Группа `SparklineType.COLUMN`, привязанная к `G1`, с диапазоном данных `A1:E1`.
   - Группа `SparklineType.STACKED` (win/loss), привязанная к `H1`, с диапазоном данных `A1:E1`.
5. Создайте экземпляр `ImageOrPrintOptions` и установите его свойство `image_type` в значение `ImageType.PNG`, чтобы каждый спарклайн отрисовывался как прозрачный PNG.
6. Для каждой из трёх групп отобразите её единственный спарклайн с помощью `group.sparklines[0].to_image(memory_stream, image_options)`, преобразуйте поток `BytesIO` в объект `bytes` и присвойте массив соответственно свойствам `worksheet.cells["F2"].embedded_image`, `worksheet.cells["G2"].embedded_image` и `worksheet.cells["H2"].embedded_image`.
7. Сохраните рабочую книгу как `output_with_sparklines.xlsx`.

```python
import aspose.cells as ac

# Создаём новую книгу и получаем доступ к первому рабочему листу
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]

# Заполняем образцы данных в ячейках A1:E1
worksheet.cells["A1"].put_value(5)
worksheet.cells["B1"].put_value(-3)
worksheet.cells["C1"].put_value(8)
worksheet.cells["D1"].put_value(-2)
worksheet.cells["E1"].put_value(6)

# Добавляем группу линейных спарклайнов, привязанную к ячейке F1 (столбец 5, строка 0)
line_area = ac.CellArea()
line_area.start_column = 5
line_area.end_column = 5
line_area.start_row = 0
line_area.end_row = 0
line_idx = worksheet.sparkline_groups.add(ac.SparklineType.LINE, "A1:E1", False, line_area)

# Добавляем группу столбчатых спарклайнов, привязанную к ячейке G1 (столбец 6, строка 0)
column_area = ac.CellArea()
column_area.start_column = 6
column_area.end_column = 6
column_area.start_row = 0
column_area.end_row = 0
column_idx = worksheet.sparkline_groups.add(ac.SparklineType.COLUMN, "A1:E1", False, column_area)

# Добавляем группу спарклайнов «Выигрыш/Проигрыш» (стек), привязанную к ячейке H1 (столбец 7, строка 0)
stacked_area = ac.CellArea()
stacked_area.start_column = 7
stacked_area.end_column = 7
stacked_area.start_row = 0
stacked_area.end_row = 0
stacked_idx = worksheet.sparkline_groups.add(ac.SparklineType.STACKED, "A1:E1", False, stacked_area)

# Настраиваем параметры изображения для вывода в формате PNG
image_options = ac.ImageOrPrintOptions()
image_options.image_type = ac.ImageType.PNG

# Преобразуем линейный спарклайн в изображение и встраиваем его в ячейку F2
line_sp = worksheet.sparkline_groups[line_idx].sparklines[0]
ms = ac.MemoryStream()
line_sp.to_image(ms, image_options)
worksheet.cells["F2"].embedded_image = ms.to_array()

# Преобразуем столбчатый спарклайн в изображение и встраиваем его в ячейку G2
column_sp = worksheet.sparkline_groups[column_idx].sparklines[0]
ms = ac.MemoryStream()
column_sp.to_image(ms, image_options)
worksheet.cells["G2"].embedded_image = ms.to_array()

# Преобразуем спарклайн «Выигрыш/Проигрыш» в изображение и встраиваем его в ячейку H2
stacked_sp = worksheet.sparkline_groups[stacked_idx].sparklines[0]
ms = ac.MemoryStream()
stacked_sp.to_image(ms, image_options)
worksheet.cells["H2"].embedded_image = ms.to_array()

# Сохраняем книгу на диск
workbook.save("output_with_sparklines.xlsx")
```

Приведённый выше код создаёт рабочую книгу, в которой каждое визуальное представление спарклайна дублируется в двух формах: живой, нативный спарклайн, привязанный к строке 1, и статичная PNG-картинка, встроенная непосредственно в соседнюю ячейку в строке 2. Поскольку картинки хранятся внутри самого файла, рабочая книга остаётся единым самодостаточным артефактом, который можно отправить по электронной почте или архивировать без нарушения ссылок на встроенные изображения. Отрисуйте каждую группу спарклайнов как PNG, преобразуйте поток `BytesIO` в объект `bytes` и присвойте байты свойству `embedded_image` целевой ячейки — именно это присваивание делает картинку частью хранимого содержимого ячейки.

{{% alert color="primary" %}}
Поскольку каждая группа спарклайнов привязана к одной ячейке, вы можете обращаться к ней через индексатор `group.sparklines[0]` вместо перебора с помощью цикла `for`. Это позволяет сохранить код отрисовки кратким и соответствует типичному шаблону «один спарклайн на одну ячейку-привязку». Для сохранения байтов картинки через `cell.embedded_image` требуется Aspose.Cells 26.5 или более поздней версии.
{{% /alert %}}

## **Рабочий процесс 2 — Экспорт рабочего листа со спарклайнами в HTML**

После того как рабочая книга содержит живые спарклайны (и, опционально, встроенные графические аналоги), весь рабочий лист может быть опубликован в Интернете путём сохранения его как HTML. Класс `HtmlSaveOptions` предоставляет необходимые настройки для управления этим экспортом; в данном рабочем процессе вы повторно используете файл `output_with_sparklines.xlsx`, созданный в Рабочем процессе 1, и преобразуете его в чистый одностраничный HTML-документ.

### **Пошаговые инструкции**

1. Убедитесь, что файл `output_with_sparklines.xlsx`, созданный в Рабочем процессе 1, доступен на диске в вашей рабочей директории.
2. Загрузите этот файл в новый экземпляр `Workbook`.
3. Создайте экземпляр `HtmlSaveOptions` и установите его свойство `export_active_worksheet_only` в значение `True`, чтобы итоговый HTML-файл содержал только активный рабочий лист, а не всю рабочую книгу.
4. Вызовите `workbook.save("sparklines.html", html_options)` для записи HTML-результата на диск.

```python
import aspose.cells as ac

workbook = ac.Workbook("output_with_sparklines.xlsx")
html_options = ac.HtmlSaveOptions()
html_options.export_active_worksheet_only = True
workbook.save("sparklines.html", html_options)
```

Приведённый выше код берёт рабочую книгу со спарклайнами из Рабочего процесса 1 и превращает её в переносимый HTML-файл. Спарклайны сохраняются как встроенные SVG- или PNG-изображения в сгенерированном HTML (в зависимости от режима экспорта), так что конечные пользователи могут просматривать тренды в любом современном браузере без необходимости установки Excel. Устанавливая `export_active_worksheet_only` в `True`, вы избегаете случайной публикации скрытых листов или вспомогательных данных — экспортируется только рабочий лист, видимый пользователю в данный момент.

{{% alert color="primary" %}}
Класс `HtmlSaveOptions` предлагает дополнительные свойства для тонкой настройки результата, такие как `export_hidden_worksheet`, `export_images_as_base64` и `encoding`. Настраивайте их по мере необходимости в зависимости от целевого окружения развёртывания.
{{% /alert %}}

## **Сводка по API**

Описанные выше рабочие процессы опираются на небольшой набор API Aspose.Cells, работающих совместно.

- `SparklineGroup` и метод доступа к коллекции `worksheet.sparkline_groups` используются для объявления типа (Line, Column, Stacked), диапазона данных и ячейки-привязки для каждой группы спарклайнов. В данной статье каждая группа привязана к одной ячейке, поэтому к группе обращаются через `worksheet.sparkline_groups[i]`.
- `Sparkline` и индексатор `group.sparklines[0]` возвращают отдельный спарклайн внутри группы. Поскольку каждая группа в примере содержит ровно один спарклайн, цикл `for` не требуется.
- `sparkline.to_image(Stream, ImageOrPrintOptions)` — это метод отрисовки, который записывает изображение спарклайна в предоставленный поток. Метод возвращает `None`; после вызова вы считываете байты из потока.
- `cell.embedded_image` — это свойство типа `bytes`, которое хранит изображение внутри одной ячейки. Оно доступно в **Aspose.Cells 26.5 и более поздних версиях** и является рекомендуемым способом обратного сохранения спарклайна, отрендеренного через `to_image`, в ту же рабочую книгу.
- `html_save_options.export_active_worksheet_only` (тип `bool`) ограничивает экспорт в HTML активным рабочим листом. Это одно из наиболее часто используемых свойств `HtmlSaveOptions` при генерации одностраничных отчётов.
- `image_or_print_options.image_type` находится в пространстве имён `aspose.cells.drawing` и выбирает формат изображения (например, `ImageType.PNG`), используемый при отрисовке через `to_image` и при печати рабочих листов в изображения.

## **Связанные статьи**

- [Спарклайны в Aspose.Cells for Aspose.Cells for Python via .NET](/cells/ru/python-net/sparkline/)
- [Вставка изображения в ячейку](/cells/ru/python-net/inserting-an-image-into-a-cell/)
- [Отрисовка массива одной ячейки SmartMarker | Aspose.Cells for Aspose.Cells for Python via .NET](/cells/ru/python-net/SmartMarker-Single-Cell-Array-Rendering/)

{{< app/cells/assistant language="python" >}}