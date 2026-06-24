---
title: Преобразование спарклайнов в изображения и HTML в Aspose.Cells for Node.js via Java
linktitle: Convert Sparkline to Image and HTML
description: Узнайте, как преобразовывать спарклайны Aspose.Cells в отдельные изображения для встраивания в ячейки и экспортировать рабочие листы со спарклайнами в HTML с помощью HtmlSaveOptions.
keywords: Aspose.Cells, Node.js via Java, спарклайн, Sparkline.toImage, Cell.EmbeddedImage, HtmlSaveOptions, отрисовка спарклайна, преобразование спарклайна в изображение, экспорт спарклайна в HTML
type: docs
weight: 120
url: /ru/nodejs-java/convert-sparkline-to-image-and-html/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Спарклайны — это миниатюрные диаграммы, размещаемые внутри ячеек рабочего листа. Aspose.Cells позволяет извлекать каждый спарклайн в виде отдельного изображения (для встраивания в другую ячейку или внешний отчёт), а также экспортировать весь рабочий лист со спарклайнами в HTML для распространения через браузер. Свойство `Cell.EmbeddedImage`, используемое в этой статье, доступно в **Aspose.Cells 26.5 и более поздних версиях**.
{{% /alert %}}

## **Введение**

Спарклайны — это компактный способ визуализации тенденций непосредственно внутри рабочего листа. В то время как пользователи Excel видят их на месте, многие реальные сценарии требуют, чтобы спарклайн покинул ячейку — например, для встраивания в другую ячейку в виде статического изображения, для прикрепления к автоматическому email-сообщению или для отображения в составе HTML-отчёта, опубликованного в Интернете.

Aspose.Cells поддерживает обе эти операции. Метод `Sparkline.toImage` отрисовывает отдельный спарклайн в поток, и полученные байты могут быть присвоены свойству `Cell.EmbeddedImage`, чтобы изображение хранилось внутри одной ячейки рабочей книги. Отдельно `HtmlSaveOptions` позволяет преобразовать всю рабочую книгу — вместе со спарклайнами — в автономный HTML-файл. В этой статье подробно рассматриваются оба рабочих процесса.

## **Рабочий процесс 1 — Отрисовка спарклайнов в изображения и встраивание их в ячейки**

В этом рабочем процессе вы создадите рабочий лист, содержащий небольшой диапазон исходных значений, прикрепите к этому диапазону три разные группы спарклайнов (Line, Column и Stacked/Win-Loss), отобразите каждую группу в формате PNG и запишете эти байты PNG в соседние ячейки как встроенные изображения. Конечный результат — это единый файл `.xlsx`, который содержит как живые спарклайны, так и их отрендеренные изображения.

### **Пошаговые инструкции**

1. Определите рабочий каталог и убедитесь, что он существует на диске.
2. Создайте новый `Workbook` и получите ссылку на первый `Worksheet`.
3. Заполните ячейки с `A1` по `E1` пятью числовыми значениями (например, ежедневными продажами или показаниями температуры).
4. Добавьте три объекта `SparklineGroup` на рабочий лист, вызвав `worksheet.sparklineGroups.add(...)`:
   - Группа `SparklineType.Line`, привязанная к `F1`, с диапазоном данных `A1:E1`.
   - Группа `SparklineType.Column`, привязанная к `G1`, с диапазоном данных `A1:E1`.
   - Группа `SparklineType.Stacked` (win/loss), привязанная к `H1`, с диапазоном данных `A1:E1`.
5. Создайте экземпляр `ImageOrPrintOptions` и установите его свойство `ImageType` в `ImageType.Png`, чтобы каждый спарклайн отрисовывался как прозрачный PNG.
6. Для каждой из трёх групп отобразите её единственный спарклайн с помощью `group.sparklines[0].toImage(outputStream, imageOptions)`, преобразуйте `ByteArrayOutputStream` в `byte[]` и присвойте массив свойствам `worksheet.cells.get("F2").setEmbeddedImage(...)`, `worksheet.cells.get("G2").setEmbeddedImage(...)` и `worksheet.cells.get("H2").setEmbeddedImage(...)` соответственно.
7. Сохраните рабочую книгу как `output_with_sparklines.xlsx`.

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);

// Заполнение образцов данных в ячейках A1:E1
worksheet.getCells().get("A1").putValue(5);
worksheet.getCells().get("B1").putValue(-3);
worksheet.getCells().get("C1").putValue(8);
worksheet.getCells().get("D1").putValue(-2);
worksheet.getCells().get("E1").putValue(6);

// Добавление группы спарклайнов "Линия" с привязкой к F1 (столбец 5, строка 0)
let lineArea = new AsposeCells.CellArea();
lineArea.setStartColumn(5);
lineArea.setEndColumn(5);
lineArea.setStartRow(0);
lineArea.setEndRow(0);
let lineIdx = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.Line, "A1:E1", false, lineArea);

// Добавление группы спарклайнов "Столбец" с привязкой к G1 (столбец 6, строка 0)
let columnArea = new AsposeCells.CellArea();
columnArea.setStartColumn(6);
columnArea.setEndColumn(6);
columnArea.setStartRow(0);
columnArea.setEndRow(0);
let columnIdx = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.Column, "A1:E1", false, columnArea);

// Добавление группы спарклайнов "Победа/Поражение" (С накоплением) с привязкой к H1 (столбец 7, строка 0)
let stackedArea = new AsposeCells.CellArea();
stackedArea.setStartColumn(7);
stackedArea.setEndColumn(7);
stackedArea.setStartRow(0);
stackedArea.setEndRow(0);
let stackedIdx = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.Stacked, "A1:E1", false, stackedArea);

// Настройка параметров изображения для вывода в формате PNG
let imageOptions = new AsposeCells.ImageOrPrintOptions();
imageOptions.setImageType(AsposeCells.ImageType.Png);

// Преобразование спарклайна "Линия" в изображение и встраивание его в ячейку F2
let lineSp = worksheet.getSparklineGroups().get(lineIdx).getSparklines().get(0);
let lineMs = new java.io.ByteArrayOutputStream();
lineSp.toImage(lineMs, imageOptions);
worksheet.getCells().get("F2").setEmbeddedImage(lineMs.toByteArray());

// Преобразование спарклайна "Столбец" в изображение и встраивание его в ячейку G2
let columnSp = worksheet.getSparklineGroups().get(columnIdx).getSparklines().get(0);
let columnMs = new java.io.ByteArrayOutputStream();
columnSp.toImage(columnMs, imageOptions);
worksheet.getCells().get("G2").setEmbeddedImage(columnMs.toByteArray());

// Преобразование спарклайна "Победа/Поражение" в изображение и встраивание его в ячейку H2
let stackedSp = worksheet.getSparklineGroups().get(stackedIdx).getSparklines().get(0);
let stackedMs = new java.io.ByteArrayOutputStream();
stackedSp.toImage(stackedMs, imageOptions);
worksheet.getCells().get("H2").setEmbeddedImage(stackedMs.toByteArray());

// Сохранение книги на диск
workbook.save("output_with_sparklines.xlsx");
```

Код, приведённый выше, создаёт рабочую книгу, в которой каждое визуальное представление спарклайна продублировано в двух формах: живой нативный спарклайн, привязанный к строке 1, и статическое изображение PNG, встроенное непосредственно в соседнюю ячейку в строке 2. Поскольку изображения хранятся внутри самого файла, рабочая книга остаётся единым автономным артефактом, который можно отправлять по электронной почте или архивировать без нарушения ссылок на встроенные изображения. Отобразите каждую группу спарклайнов в формате PNG, преобразуйте `ByteArrayOutputStream` в `byte[]` и присвойте массив свойству `setEmbeddedImage` целевой ячейки — именно это присваивание делает изображение частью хранимого содержимого ячейки.

{{% alert color="primary" %}}
Поскольку каждая группа спарклайнов привязана к одной ячейке, вы можете обращаться к ней через индексатор `group.sparklines[0]` вместо перечисления с помощью `forEach`. Это позволяет сохранить код отрисовки коротким и соответствует типичному шаблону «один спарклайн на одну ячейку привязки». Для сохранения байтов изображения через `Cell.EmbeddedImage` требуется Aspose.Cells 26.5 или более поздней версии.
{{% /alert %}}

## **Рабочий процесс 2 — Экспорт рабочего листа со спарклайнами в HTML**

После того как рабочая книга содержит живые спарклайны (и, опционально, встроенные изображения), весь рабочий лист может быть опубликован в Интернете путём сохранения в формате HTML. Класс `HtmlSaveOptions` предоставляет параметры, необходимые для управления этим экспортом; в этом рабочем процессе вы будете повторно использовать файл `output_with_sparklines.xlsx`, созданный в Рабочем процессе 1, и преобразуете его в чистый одностраничный HTML-документ.

### **Пошаговые инструкции**

1. Убедитесь, что файл `output_with_sparklines.xlsx`, созданный в Рабочем процессе 1, доступен на диске в вашем рабочем каталоге.
2. Загрузите этот файл в новый экземпляр `Workbook`.
3. Создайте экземпляр `HtmlSaveOptions` и установите его свойство `ExportActiveWorksheetOnly` в `true`, чтобы результирующий HTML-файл содержал только активный рабочий лист, а не всю рабочую книгу.
4. Вызовите `workbook.save("sparklines.html", htmlOptions)` для записи HTML-вывода на диск.

```javascript
let workbook = new AsposeCells.Workbook("output_with_sparklines.xlsx");
let htmlOptions = new AsposeCells.HtmlSaveOptions();
htmlOptions.setExportActiveWorksheetOnly(true);
workbook.save("sparklines.html", htmlOptions);
```

Код, приведённый выше, берёт рабочую книгу со спарклайнами из Рабочего процесса 1 и превращает её в переносимый HTML-файл. Спарклайны сохраняются как встроенные SVG- или PNG-изображения в сгенерированном HTML (в зависимости от режима экспорта), поэтому конечные пользователи могут просматривать тенденции в любом современном браузере без необходимости установки Excel. Установив `ExportActiveWorksheetOnly` в `true`, вы избежите случайной публикации скрытых листов или вспомогательных данных — экспортируется только рабочий лист, видимый пользователю в данный момент.

{{% alert color="primary" %}}
Класс `HtmlSaveOptions` предлагает дополнительные свойства для тонкой настройки вывода, такие как `ExportHiddenWorksheet`, `ExportImagesAsBase64` и `Encoding`. Настройте их по мере необходимости для вашей целевой среды развёртывания.
{{% /alert %}}

## **Сводная информация по API**

Рабочие процессы, описанные выше, опираются на небольшой набор API Aspose.Cells, работающих совместно.

- `SparklineGroup` и метод доступа к коллекции `worksheet.sparklineGroups` используются для объявления типа (Line, Column, Stacked), диапазона данных и ячейки привязки для каждой группы спарклайнов. В этой статье каждая группа привязана к одной ячейке, поэтому группа доступна через `worksheet.sparklineGroups[i]`.
- `Sparkline` и индексатор `group.sparklines[0]` возвращают отдельный спарклайн внутри группы. Поскольку каждая группа в примере содержит ровно один спарклайн, цикл `forEach` не требуется.
- `Sparkline.toImage(OutputStream, ImageOrPrintOptions)` — это метод отрисовки, который записывает изображение спарклайна в предоставленный `OutputStream`. Метод возвращает `void`; байты считываются из потока после вызова.
- `Cell.EmbeddedImage` — это свойство типа `byte[]`, которое хранит изображение внутри одной ячейки. Оно доступно в **Aspose.Cells 26.5 и более поздних версиях** и является рекомендуемым способом обратной записи спарклайна, отрендеренного методом `toImage`, в ту же рабочую книгу.
- `HtmlSaveOptions.ExportActiveWorksheetOnly` (тип `boolean`) ограничивает экспорт в HTML только активным рабочим листом. Это одно из наиболее часто используемых свойств `HtmlSaveOptions` при создании одностраничных отчётов.
- `ImageOrPrintOptions.ImageType` находится в пространстве имён `com.aspose.cells.drawing` и выбирает формат изображения (например, `ImageType.Png`), используемый при отрисовке с помощью `toImage` и при печати рабочих листов в изображения.

## **Связанные статьи**

- [Спарклайны в Aspose.Cells для Aspose.Cells for Node.js via Java](/cells/ru/nodejs-java/sparkline/)
- [Вставка изображения в ячейку](/cells/ru/nodejs-java/inserting-an-image-into-a-cell/)
- [Рендеринг массива в одной ячейке SmartMarker | Aspose.Cells для Aspose.Cells for Node.js via Java](/cells/ru/nodejs-java/SmartMarker-Single-Cell-Array-Rendering/)

{{< app/cells/assistant language="javascript" >}}