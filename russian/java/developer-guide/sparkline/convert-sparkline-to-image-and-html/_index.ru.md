---
title: Преобразование спарклайнов в изображения и HTML в Aspose.Cells for Java
linktitle: Convert Sparkline to Image and HTML
description: Узнайте, как отображать спарклайны Aspose.Cells в отдельные изображения для встраивания в ячейки и экспортировать листы со спарклайнами в HTML с помощью HtmlSaveOptions.
keywords: Aspose.Cells, Java, sparkline, Sparkline.toImage, Cell.EmbeddedImage, HtmlSaveOptions, отображение спарклайна, преобразование спарклайна в изображение, экспорт спарклайна в HTML
type: docs
weight: 120
url: /ru/java/convert-sparkline-to-image-and-html/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Спарклайны — это миниатюрные диаграммы, размещаемые внутри ячеек рабочего листа. Aspose.Cells позволяет извлекать каждый спарклайн как отдельное изображение (для встраивания в другую ячейку или внешний отчёт), а также экспортировать весь рабочий лист со спарклайнами в HTML для распространения через браузер. Свойство `Cell.EmbeddedImage`, используемое в данной статье, доступно в **Aspose.Cells 26.5 и более поздних версиях**.
{{% /alert %}}

## **Введение**

Спарклайны — это компактный способ визуализации трендов непосредственно внутри рабочего листа. В то время как пользователи Excel видят их на месте, во многих реальных сценариях требуется, чтобы спарклайн покинул ячейку — например, чтобы быть встроенным в другую ячейку как статическое изображение, прикреплённым к автоматическому письму или отображённым в составе HTML-отчёта, публикуемого в Интернете.

Aspose.Cells поддерживает обе эти операции. Метод `Sparkline.toImage` отображает отдельный спарклайн в поток, а полученные байты могут быть присвоены свойству `Cell.EmbeddedImage` (через `setEmbeddedImage`), чтобы изображение хранилось внутри одной ячейки рабочей книги. Отдельно, `HtmlSaveOptions` позволяет преобразовать всю рабочую книгу — вместе со спарклайнами — в самодостаточный HTML-файл. В данной статье оба рабочих процесса рассматриваются от начала до конца.

## **Рабочий процесс 1 — Отображение спарклайнов в виде изображений и их встраивание в ячейки**

В этом рабочем процессе вы создадите рабочий лист, содержащий небольшой диапазон исходных значений, прикрепите три различные группы спарклайнов (линейную, столбчатую и стековую/win-loss) к этому диапазону, отобразите каждую группу как PNG и запишете эти байты PNG в соседние ячейки как встроенные изображения. Конечным результатом является единый файл `.xlsx`, содержащий как живые спарклайны, так и их отрендеренные изображения.

### **Пошаговые инструкции**

1. Определите рабочий каталог и убедитесь, что он существует на диске.
2. Создайте новый `Workbook` и получите ссылку на первый `Worksheet`.
3. Заполните ячейки с `A1` по `E1` пятью числовыми значениями (например, ежедневными продажами или показаниями температуры).
4. Добавьте три объекта `SparklineGroup` на рабочий лист, вызвав `worksheet.getSparklineGroups().add(...)`:
   - Группу `SparklineType.LINE`, привязанную к `F1`, с диапазоном данных `A1:E1`.
   - Группу `SparklineType.COLUMN`, привязанную к `G1`, с диапазоном данных `A1:E1`.
   - Группу `SparklineType.STACKED` (win/loss), привязанную к `H1`, с диапазоном данных `A1:E1`.
5. Создайте экземпляр `ImageOrPrintOptions` и вызовите `setImageType(ImageType.PNG)`, чтобы каждый спарклайн был отрендерен как прозрачный PNG.
6. Для каждой из трёх групп отрендерите её единственный спарклайн с помощью `group.getSparklines().get(0).toImage(byteArrayOutputStream, imageOptions)`, преобразуйте `ByteArrayOutputStream` в `byte[]` и присвойте массив через `worksheet.getCells().get("F2").setEmbeddedImage(...)`, `worksheet.getCells().get("G2").setEmbeddedImage(...)` и `worksheet.getCells().get("H2").setEmbeddedImage(...)` соответственно.
7. Вызовите `workbook.save("output_with_sparklines.xlsx")`, чтобы сохранить рабочую книгу на диск.

```java
import com.aspose.cells.*;
import java.io.*;

// Создать новую книгу и получить доступ к первому рабочему листу
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);

// Заполнить образец данных в ячейках A1:E1
worksheet.getCells().get("A1").putValue(5);
worksheet.getCells().get("B1").putValue(-3);
worksheet.getCells().get("C1").putValue(8);
worksheet.getCells().get("D1").putValue(-2);
worksheet.getCells().get("E1").putValue(6);

// Добавить группу линейных спарклайнов, привязанную к F1 (столбец 5, строка 0)
CellArea lineArea = CellArea.createCellArea(5, 0, 5, 0);
int lineIdx = worksheet.getSparklineGroups().add(SparklineType.LINE, "A1:E1", false, lineArea);

// Добавить группу столбчатых спарклайнов, привязанную к G1 (столбец 6, строка 0)
CellArea columnArea = CellArea.createCellArea(6, 0, 6, 0);
int columnIdx = worksheet.getSparklineGroups().add(SparklineType.COLUMN, "A1:E1", false, columnArea);

// Добавить группу спарклайнов Win/Loss (составных), привязанную к H1 (столбец 7, строка 0)
CellArea stackedArea = CellArea.createCellArea(7, 0, 7, 0);
int stackedIdx = worksheet.getSparklineGroups().add(SparklineType.STACKED, "A1:E1", false, stackedArea);

// Настроить параметры изображения для вывода в формате PNG
ImageOrPrintOptions imageOptions = new ImageOrPrintOptions();
imageOptions.setImageType(ImageType.PNG);

// Преобразовать линейный спарклайн в изображение и встроить его в ячейку F2
Sparkline lineSp = worksheet.getSparklineGroups().get(lineIdx).getSparklines().get(0);
ByteArrayOutputStream lineMs = new ByteArrayOutputStream();
lineSp.toImage(lineMs, imageOptions);
worksheet.getCells().get("F2").setEmbeddedImage(lineMs.toByteArray());

// Преобразовать столбчатый спарклайн в изображение и встроить его в ячейку G2
Sparkline columnSp = worksheet.getSparklineGroups().get(columnIdx).getSparklines().get(0);
ByteArrayOutputStream columnMs = new ByteArrayOutputStream();
columnSp.toImage(columnMs, imageOptions);
worksheet.getCells().get("G2").setEmbeddedImage(columnMs.toByteArray());

// Преобразовать спарклайн Win/Loss в изображение и встроить его в ячейку H2
Sparkline stackedSp = worksheet.getSparklineGroups().get(stackedIdx).getSparklines().get(0);
ByteArrayOutputStream stackedMs = new ByteArrayOutputStream();
stackedSp.toImage(stackedMs, imageOptions);
worksheet.getCells().get("H2").setEmbeddedImage(stackedMs.toByteArray());

// Сохранить книгу на диск
workbook.save("output_with_sparklines.xlsx");
```

Код выше создаёт рабочую книгу, в которой каждое визуальное представление спарклайна дублируется в двух формах: живой, нативный спарклайн, привязанный к строке 1, и статичное изображение PNG, встроенное непосредственно в соседнюю ячейку в строке 2. Поскольку изображения хранятся внутри самого файла, рабочая книга остаётся единым самодостаточным артефактом, который можно отправить по электронной почте или заархивировать без нарушения ссылок на встроенные изображения. Отрендерите каждую группу спарклайнов как PNG, преобразуйте `ByteArrayOutputStream` в `byte[]` и присвойте массив свойству `EmbeddedImage` целевой ячейки через `setEmbeddedImage(byte[])` — именно это присваивание делает изображение частью хранимого содержимого ячейки.

{{% alert color="primary" %}}
Поскольку каждая группа спарклайнов привязана к одной ячейке, вы можете обращаться к ней через индексатор `group.getSparklines().get(0)` вместо перебора в цикле `for`. Это делает код рендеринга коротким и соответствует типичному шаблону «один спарклайн на одну ячейку привязки». Сохранение байтов изображения через `Cell.EmbeddedImage` (устанавливается через `setEmbeddedImage`) требует Aspose.Cells версии 26.5 или более поздней.
{{% /alert %}}

## **Рабочий процесс 2 — Экспорт рабочего листа со спарклайнами в HTML**

После того как рабочая книга содержит живые спарклайны (и опционально встроенные изображения-аналоги), весь рабочий лист может быть опубликован в Интернете путём сохранения его в формате HTML. Класс `HtmlSaveOptions` предоставляет параметры, необходимые для управления этим экспортом; в данном рабочем процессе вы повторно используете файл `output_with_sparklines.xlsx`, созданный в Рабочем процессе 1, и преобразуете его в чистый одностраничный HTML-документ.

### **Пошаговые инструкции**

1. Убедитесь, что файл `output_with_sparklines.xlsx`, созданный в Рабочем процессе 1, доступен на диске в вашем рабочем каталоге.
2. Загрузите этот файл в новый экземпляр `Workbook`.
3. Создайте экземпляр `HtmlSaveOptions` и вызовите `setExportActiveWorksheetOnly(true)`, чтобы итоговый HTML-файл содержал только активный рабочий лист, а не всю рабочую книгу.
4. Вызовите `workbook.save("sparklines.html", htmlOptions)`, чтобы записать HTML-вывод на диск.

```java
import com.aspose.cells.*;

Workbook workbook = new Workbook("output_with_sparklines.xlsx");
HtmlSaveOptions htmlOptions = new HtmlSaveOptions();
htmlOptions.setExportActiveWorksheetOnly(true);
workbook.save("sparklines.html", htmlOptions);
```

Код выше берёт рабочую книгу со спарклайнами из Рабочего процесса 1 и превращает её в переносимый HTML-файл. Спарклайны сохраняются как встроенные SVG- или PNG-рендеринги внутри сгенерированного HTML (в зависимости от режима экспорта), поэтому конечные пользователи могут просматривать тренды в любом современном браузере без необходимости установки Excel. Установив `ExportActiveWorksheetOnly` в значение `true` через `setExportActiveWorksheetOnly(true)`, вы избежите случайной публикации скрытых листов или вспомогательных данных — экспортируется только рабочий лист, который в данный момент виден пользователю.

{{% alert color="primary" %}}
Класс `HtmlSaveOptions` предлагает дополнительные свойства для тонкой настройки вывода, такие как `ExportHiddenWorksheet`, `ExportImagesAsBase64` и `Encoding`. Настраивайте их по мере необходимости для вашей целевой среды развёртывания.
{{% /alert %}}

## **Сводка по API**

Описанные выше рабочие процессы опираются на небольшой набор API Aspose.Cells, работающих совместно.

- `SparklineGroup` и метод доступа к коллекции `worksheet.getSparklineGroups()` используются для объявления типа (Line, Column, Stacked), диапазона данных и ячейки привязки для каждой группы спарклайнов. В данной статье каждая группа привязана к одной ячейке, поэтому группа доступна через `worksheet.getSparklineGroups().get(i)`.
- `Sparkline` и индексатор `group.getSparklines().get(0)` возвращают отдельный спарклайн внутри группы. Поскольку каждая группа в примере содержит ровно один спарклайн, цикл `for` не требуется.
- `Sparkline.toImage(Stream, ImageOrPrintOptions)` — это метод рендеринга, который записывает изображение спарклайна в предоставленный `Stream`. Метод возвращает `void`; байты считываются из потока после вызова.
- `Cell.EmbeddedImage` — это свойство типа `byte[]` (присваивается через `cell.setEmbeddedImage(byte[])`), которое хранит изображение внутри одной ячейки. Оно доступно в **Aspose.Cells 26.5 и более поздних версиях** и является рекомендуемым способом обратного сохранения спарклайна, отрендеренного методом `toImage`, в ту же рабочую книгу.
- `HtmlSaveOptions.setExportActiveWorksheetOnly(boolean)` ограничивает экспорт в HTML только активным рабочим листом. Это одно из наиболее часто используемых свойств `HtmlSaveOptions` при создании одностраничных отчётов.
- `ImageOrPrintOptions.setImageType(ImageType)` находится в пакете `com.aspose.cells.drawing` и выбирает формат изображения (например, `ImageType.PNG`), используемый при рендеринге с помощью `toImage` и при печати рабочих листов в изображения.

## **Связанные статьи**

- [Спарклайны в Aspose.Cells для Aspose.Cells for Java](/cells/ru/java/sparkline/)
- [Вставка изображения в ячейку](/cells/ru/java/inserting-an-image-into-a-cell/)
- [Рендеринг массива одной ячейки SmartMarker | Aspose.Cells Java](/cells/ru/java/SmartMarker-Single-Cell-Array-Rendering/)

{{< app/cells/assistant language="java" >}}