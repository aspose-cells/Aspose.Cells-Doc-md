---
title: Преобразование спарклайнов в изображения и HTML в Aspose.Cells for Node.js via C++
linktitle: Convert Sparkline to Image and HTML
description: Узнайте, как отображать спарклайны Aspose.Cells в виде отдельных изображений для встраивания в ячейки и экспортировать рабочие листы со спарклайнами в HTML с помощью HtmlSaveOptions.
keywords: Aspose.Cells, Node.js via C++, спарклайн, Sparkline.toImage, cell.embeddedImage, HtmlSaveOptions, отображение спарклайнов, преобразование спарклайна в изображение, экспорт спарклайна в HTML
type: docs
weight: 120
url: /ru/nodejs-cpp/convert-sparkline-to-image-and-html/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Спарклайны — это миниатюрные диаграммы, размещаемые внутри ячеек рабочего листа. Aspose.Cells позволяет извлекать каждый спарклайн как отдельное изображение (для встраивания в другую ячейку или внешний отчёт), а также экспортировать весь рабочий лист со спарклайнами в HTML для распространения через браузер. Свойство `cell.embeddedImage`, используемое в этой статье, доступно в **Aspose.Cells 26.5 и более поздних версиях**.
{{% /alert %}}

## **Введение**

Спарклайны — это компактный способ визуализации трендов непосредственно внутри рабочего листа. В то время как пользователи Excel видят их на месте, многие реальные сценарии требуют, чтобы спарклайн покинул ячейку — например, чтобы быть встроенным в другую ячейку как статичное изображение, прикреплённым к автоматическому email-сообщению или отображённым как часть HTML-отчёта, опубликованного в интернете.

Aspose.Cells поддерживает обе эти операции. Метод `Sparkline.toImage` отображает отдельный спарклайн в поток, и полученные байты могут быть присвоены свойству `cell.embeddedImage`, чтобы изображение сохранялось внутри одной ячейки рабочей книги. Отдельно класс `HtmlSaveOptions` позволяет преобразовать всю рабочую книгу — вместе со спарклайнами — в автономный HTML-файл. В этой статье оба рабочих процесса рассматриваются шаг за шагом.

## **Рабочий процесс 1 — Отображение спарклайнов в виде изображений и их встраивание в ячейки**

В этом рабочем процессе вы создадите рабочий лист, содержащий небольшой диапазон исходных значений, прикрепите к этому диапазону три различные группы спарклайнов (Line, Column и Stacked/Win-Loss), отобразите каждую группу в виде PNG и запишете эти байты PNG в соседние ячейки как встроенные изображения. Конечный результат — это единый файл `.xlsx`, который содержит как живые спарклайны, так и их отрендеренные изображения-аналоги.

### **Пошаговые инструкции**

1. Определите рабочий каталог и убедитесь, что он существует на диске.
2. Создайте новый объект `Workbook` и получите ссылку на первый `Worksheet`.
3. Заполните ячейки от `A1` до `E1` пятью числовыми значениями-примерами (например, ежедневными продажами или показаниями температуры).
4. Добавьте три объекта `SparklineGroup` на рабочий лист, вызвав `worksheet.sparklineGroups.add(...)`:
   - Группа `SparklineType.Line`, привязанная к `F1`, с диапазоном данных `A1:E1`.
   - Группа `SparklineType.Column`, привязанная к `G1`, с диапазоном данных `A1:E1`.
   - Группа `SparklineType.Stacked` (win/loss), привязанная к `H1`, с диапазоном данных `A1:E1`.
5. Создайте экземпляр `ImageOrPrintOptions` и установите его свойство `ImageType` в значение `ImageType.Png`, чтобы каждый спарклайн отображался как прозрачный PNG.
6. Для каждой из трёх групп отобразите её единственный спарклайн, используя `group.sparklines[0].toImage(memoryStream, imageOrPrintOptions)`, преобразуйте поток в `Buffer` (или `Uint8Array`) и присвойте байты свойствам `worksheet.cells["F2"].embeddedImage`, `worksheet.cells["G2"].embeddedImage` и `worksheet.cells["H2"].embeddedImage` соответственно.
7. Сохраните рабочую книгу как `output_with_sparklines.xlsx`.

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);

// Заполнить образец данных в ячейках A1:E1
worksheet.getCells().get("A1").putValue(5);
worksheet.getCells().get("B1").putValue(-3);
worksheet.getCells().get("C1").putValue(8);
worksheet.getCells().get("D1").putValue(-2);
worksheet.getCells().get("E1").putValue(6);

// Добавить группу линейных спарклайнов, привязанную к F1 (столбец 5, строка 0)
let lineArea = new AsposeCells.CellArea();
lineArea.setStartColumn(5);
lineArea.setEndColumn(5);
lineArea.setStartRow(0);
lineArea.setEndRow(0);
let lineIdx = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.Line, "A1:E1", false, lineArea);

// Добавить группу столбчатых спарклайнов, привязанную к G1 (столбец 6, строка 0)
let columnArea = new AsposeCells.CellArea();
columnArea.setStartColumn(6);
columnArea.setEndColumn(6);
columnArea.setStartRow(0);
columnArea.setEndRow(0);
let columnIdx = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.Column, "A1:E1", false, columnArea);

// Добавить группу спарклайнов Выигрыш/Проигрыш (стек), привязанную к H1 (столбец 7, строка 0)
let stackedArea = new AsposeCells.CellArea();
stackedArea.setStartColumn(7);
stackedArea.setEndColumn(7);
stackedArea.setStartRow(0);
stackedArea.setEndRow(0);
let stackedIdx = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.Stacked, "A1:E1", false, stackedArea);

// Настроить параметры изображения для вывода в формате PNG
let imageOptions = new AsposeCells.ImageOrPrintOptions();
imageOptions.setImageType(AsposeCells.ImageType.Png);

// Преобразовать линейный спарклайн в изображение и встроить его в ячейку F2
let lineSp = worksheet.getSparklineGroups().get(lineIdx).getSparklines().get(0);
let linePath = "line_sparkline.png";
lineSp.toImage(linePath, imageOptions);
worksheet.getCells().get("F2").setEmbeddedImage(fs.readFileSync(linePath));

// Преобразовать столбчатый спарклайн в изображение и встроить его в ячейку G2
let columnSp = worksheet.getSparklineGroups().get(columnIdx).getSparklines().get(0);
let columnPath = "column_sparkline.png";
columnSp.toImage(columnPath, imageOptions);
worksheet.getCells().get("G2").setEmbeddedImage(fs.readFileSync(columnPath));

// Преобразовать спарклайн Выигрыш/Проигрыш в изображение и встроить его в ячейку H2
let stackedSp = worksheet.getSparklineGroups().get(stackedIdx).getSparklines().get(0);
let stackedPath = "stacked_sparkline.png";
stackedSp.toImage(stackedPath, imageOptions);
worksheet.getCells().get("H2").setEmbeddedImage(fs.readFileSync(stackedPath));

// Сохранить книгу на диск
workbook.save("output_with_sparklines.xlsx");
```

Приведённый выше код создаёт рабочую книгу, в которой каждое визуальное представление спарклайна дублируется в двух формах: живой, нативный спарклайн, привязанный к строке 1, и статичное изображение PNG, встроенное непосредственно в соседнюю ячейку в строке 2. Поскольку изображения хранятся внутри самого файла, рабочая книга остаётся единым самодостаточным артефактом, который можно отправить по электронной почте или архивировать без нарушения ссылок на встроенные изображения. Отобразите каждую группу спарклайнов в виде PNG, преобразуйте поток в `Buffer` и присвойте массив свойству `embeddedImage` целевой ячейки — именно это присваивание делает изображение частью сохранённого содержимого ячейки.

{{% alert color="primary" %}}
Поскольку каждая группа спарклайнов привязана к одной ячейке, вы можете обращаться к ней через индексатор `group.sparklines[0]` вместо перечисления с помощью `forEach`. Это делает код рендеринга коротким и соответствует типичному шаблону «один спарклайн на одну ячейку привязки». Для сохранения байтов изображения через `cell.embeddedImage` требуется Aspose.Cells 26.5 или более поздней версии.
{{% /alert %}}

## **Рабочий процесс 2 — Экспорт рабочего листа со спарклайнами в HTML**

После того как рабочая книга содержит живые спарклайны (и, при необходимости, встроенные изображения-аналоги), весь рабочий лист может быть опубликован в интернете путём его сохранения как HTML. Класс `HtmlSaveOptions` предоставляет параметры, необходимые для управления этим экспортом; в данном рабочем процессе вы будете повторно использовать файл `output_with_sparklines.xlsx`, созданный в Рабочем процессе 1, и преобразуете его в чистый одностраничный HTML-документ.

### **Пошаговые инструкции**

1. Убедитесь, что файл `output_with_sparklines.xlsx`, созданный в Рабочем процессе 1, доступен на диске в вашем рабочем каталоге.
2. Загрузите этот файл в новый экземпляр `Workbook`.
3. Создайте экземпляр `HtmlSaveOptions` и установите его свойство `exportActiveWorksheetOnly` в значение `true`, чтобы итоговый HTML-файл содержал только активный рабочий лист, а не всю рабочую книгу.
4. Вызовите `workbook.save("sparklines.html", htmlOptions)` для записи HTML-вывода на диск.

```javascript
let workbook = new AsposeCells.Workbook("output_with_sparklines.xlsx");
let htmlOptions = new AsposeCells.HtmlSaveOptions();
htmlOptions.setExportActiveWorksheetOnly(true);
workbook.save("sparklines.html", htmlOptions);
```

Приведённый выше код берёт рабочую книгу со спарклайнами из Рабочего процесса 1 и превращает её в переносимый HTML-файл. Спарклайны сохраняются как встроенные SVG или PNG-рендеринги внутри сгенерированного HTML, в зависимости от режима экспорта, поэтому конечные пользователи могут просматривать тренды в любом современном браузере без необходимости установки Excel. Установив `exportActiveWorksheetOnly` в значение `true`, вы избегаете случайной публикации скрытых листов или вспомогательных данных — экспортируется только тот рабочий лист, который в данный момент виден пользователю.

{{% alert color="primary" %}}
Класс `HtmlSaveOptions` предлагает дополнительные свойства для тонкой настройки вывода, такие как `exportHiddenWorksheet`, `exportImagesAsBase64` и `encoding`. Настраивайте их по мере необходимости для вашей целевой среды развёртывания.
{{% /alert %}}

## **Сводка по API**

Описанные выше рабочие процессы опираются на небольшой набор API Aspose.Cells, работающих совместно.

- `SparklineGroup` и метод доступа к коллекции `worksheet.sparklineGroups` используются для объявления типа (Line, Column, Stacked), диапазона данных и ячейки привязки для каждой группы спарклайнов. В этой статье каждая группа привязана к одной ячейке, поэтому к группе обращаются через `worksheet.sparklineGroups[i]`.
- `Sparkline` и индексатор `group.sparklines[0]` возвращают отдельный спарклайн внутри группы. Поскольку каждая группа в примере содержит ровно один спарклайн, цикл `forEach` не требуется.
- `Sparkline.toImage(Stream, ImageOrPrintOptions)` — это метод рендеринга, который записывает изображение спарклайна в предоставленный `Stream`. Метод возвращает `void`; байты считываются из потока после вызова.
- `cell.embeddedImage` — это свойство типа `Buffer` (или `Uint8Array`), которое хранит изображение внутри одной ячейки. Оно доступно в **Aspose.Cells 26.5 и более поздних версиях** и является рекомендуемым способом обратного сохранения спарклайна, отрендеренного через `toImage`, в ту же рабочую книгу.
- `htmlSaveOptions.exportActiveWorksheetOnly` (тип `bool`) ограничивает экспорт в HTML только активным рабочим листом. Это одно из наиболее часто используемых свойств класса `HtmlSaveOptions` при создании одностраничных отчётов.
- `imageOrPrintOptions.imageType` находится в пространстве имён `Aspose.Cells.Drawing` и выбирает формат изображения (например, `ImageType.Png`), используемый при рендеринге через `toImage` и при печати рабочих листов в изображения.

## **Связанные статьи**

- [Спарклайны в Aspose.Cells для Aspose.Cells для Node.js via C++](/cells/ru/nodejs-cpp/sparkline/)
- [Вставка изображения в ячейку](/cells/ru/nodejs-cpp/inserting-an-image-into-a-cell/)
- [Рендеринг массива одиночной ячейки SmartMarker | Aspose.Cells Node.js via C++](/cells/ru/nodejs-cpp/SmartMarker-Single-Cell-Array-Rendering/)

{{< app/cells/assistant language="javascript" >}}