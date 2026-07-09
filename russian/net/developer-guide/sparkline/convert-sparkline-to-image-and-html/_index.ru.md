---
title: Преобразование спарклайнов в изображение и HTML в Aspose.Cells for .NET
linktitle: Convert Sparkline to Image and HTML
description: Узнайте, как преобразовать спарклайны Aspose.Cells в отдельные изображения для встраивания в ячейки и экспортировать рабочие листы со спарклайнами в HTML с помощью HtmlSaveOptions.
keywords: Aspose.Cells, .NET, спарклайн, Sparkline.ToImage, Cell.EmbeddedImage, HtmlSaveOptions, рендеринг спарклайна, преобразование спарклайна в изображение, экспорт спарклайна в HTML
type: docs
weight: 120
url: /ru/net/convert-sparkline-to-image-and-html/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Спарклайны — это миниатюрные диаграммы, размещаемые внутри ячеек рабочего листа. Aspose.Cells позволяет извлекать каждый спарклайн в виде отдельного изображения (для встраивания в другую ячейку или внешний отчёт), а также экспортировать весь рабочий лист со спарклайнами в HTML для распространения через браузер. Свойство `Cell.EmbeddedImage`, используемое в этой статье, доступно в **Aspose.Cells 26.5 и более поздних версиях**.
{{% /alert %}}

## **Введение**

Спарклайны — это компактный способ визуализации трендов непосредственно внутри рабочего листа. Пользователи Excel видят их на месте, но многие реальные сценарии требуют, чтобы спарклайн покинул ячейку — например, для встраивания в другую ячейку в виде статического изображения, прикрепления к автоматическому электронному письму или отображения в составе HTML-отчёта, опубликованного в интернете.

Aspose.Cells поддерживает обе эти операции. Метод `Sparkline.ToImage` отображает отдельный спарклайн в поток, и полученные байты могут быть присвоены свойству `Cell.EmbeddedImage`, чтобы изображение сохранялось внутри одной ячейки рабочей книги. Кроме того, `HtmlSaveOptions` позволяет преобразовать всю рабочую книгу — вместе со спарклайнами — в автономный HTML-файл. В этой статье подробно рассматриваются оба рабочих процесса.

## **Рабочий процесс 1 — Рендеринг спарклайнов в изображения и их встраивание в ячейки**

В этом рабочем процессе вы создадите рабочий лист, содержащий небольшой диапазон исходных значений, прикрепите к этому диапазону три разные группы спарклайнов (Линейная, Столбцовая и Со стопкой/Выигрыш-Проигрыш), отобразите каждую группу в формате PNG и запишете эти байты PNG в соседние ячейки как встроенные изображения. Конечным результатом является единый файл `.xlsx`, который содержит как активные спарклайны, так и их отрендеренные изображения-аналоги.

### **Пошаговые инструкции**

1. Определите рабочий каталог и убедитесь, что он существует на диске.
2. Создайте новую `Workbook` и получите ссылку на первый `Worksheet`.
3. Заполните ячейки с `A1` по `E1` пятью числовыми значениями (например, ежедневные продажи или показания температуры).
4. Добавьте три объекта `SparklineGroup` на рабочий лист, вызвав `worksheet.SparklineGroups.Add(...)`:
   - Группа `SparklineType.Line`, привязанная к `F1`, с диапазоном данных `A1:E1`.
   - Группа `SparklineType.Column`, привязанная к `G1`, с диапазоном данных `A1:E1`.
   - Группа `SparklineType.Stacked` (выигрыш/проигрыш), привязанная к `H1`, с диапазоном данных `A1:E1`.
5. Создайте экземпляр `ImageOrPrintOptions` и установите его свойство `ImageType` в значение `ImageType.Png`, чтобы каждый спарклайн отображался как прозрачный PNG.
6. Для каждой из трёх групп отобразите её единственный спарклайн с помощью `group.Sparklines[0].ToImage(memoryStream, imageOptions)`, преобразуйте `MemoryStream` в `byte[]` и присвойте массив свойствам `worksheet.Cells["F2"].EmbeddedImage`, `worksheet.Cells["G2"].EmbeddedImage` и `worksheet.Cells["H2"].EmbeddedImage` соответственно.
7. Сохраните рабочую книгу как `output_with_sparklines.xlsx`.

```csharp
using System;
using System.IO;
using Aspose.Cells;
using Aspose.Cells.Charts;
using Aspose.Cells.Drawing;
using Aspose.Cells.Rendering;

// Создайте новую рабочую книгу и откройте доступ к первому рабочему листу
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];

// Заполните образец данных в ячейках A1:E1
worksheet.Cells["A1"].PutValue(5);
worksheet.Cells["B1"].PutValue(-3);
worksheet.Cells["C1"].PutValue(8);
worksheet.Cells["D1"].PutValue(-2);
worksheet.Cells["E1"].PutValue(6);

// Добавьте группу спарклайнов типа Line, привязанную к F1 (столбец 5, строка 0)
CellArea lineArea = new CellArea();
lineArea.StartColumn = 5;
lineArea.EndColumn = 5;
lineArea.StartRow = 0;
lineArea.EndRow = 0;
int lineIdx = worksheet.SparklineGroups.Add(SparklineType.Line, "A1:E1", false, lineArea);

// Добавьте группу спарклайнов типа Column, привязанную к G1 (столбец 6, строка 0)
CellArea columnArea = new CellArea();
columnArea.StartColumn = 6;
columnArea.EndColumn = 6;
columnArea.StartRow = 0;
columnArea.EndRow = 0;
int columnIdx = worksheet.SparklineGroups.Add(SparklineType.Column, "A1:E1", false, columnArea);

// Добавьте группу спарклайнов типа Win/Loss (Stacked), привязанную к H1 (столбец 7, строка 0)
CellArea stackedArea = new CellArea();
stackedArea.StartColumn = 7;
stackedArea.EndColumn = 7;
stackedArea.StartRow = 0;
stackedArea.EndRow = 0;
int stackedIdx = worksheet.SparklineGroups.Add(SparklineType.Stacked, "A1:E1", false, stackedArea);

// Настройте параметры изображения для вывода в формате PNG
ImageOrPrintOptions imageOptions = new ImageOrPrintOptions();
imageOptions.ImageType = ImageType.Png;

// Преобразуйте спарклайн Line в изображение и встройте его в ячейку F2
Sparkline lineSp = worksheet.SparklineGroups[lineIdx].Sparklines[0];
using (MemoryStream ms = new MemoryStream())
{
    lineSp.ToImage(ms, imageOptions);
    worksheet.Cells["F2"].EmbeddedImage = ms.ToArray();
}

// Преобразуйте спарклайн Column в изображение и встройте его в ячейку G2
Sparkline columnSp = worksheet.SparklineGroups[columnIdx].Sparklines[0];
using (MemoryStream ms = new MemoryStream())
{
    columnSp.ToImage(ms, imageOptions);
    worksheet.Cells["G2"].EmbeddedImage = ms.ToArray();
}

// Преобразуйте спарклайн Win/Loss в изображение и встройте его в ячейку H2
Sparkline stackedSp = worksheet.SparklineGroups[stackedIdx].Sparklines[0];
using (MemoryStream ms = new MemoryStream())
{
    stackedSp.ToImage(ms, imageOptions);
    worksheet.Cells["H2"].EmbeddedImage = ms.ToArray();
}

// Сохраните рабочую книгу на диск
workbook.Save("output_with_sparklines.xlsx");
```

Приведённый выше код создаёт рабочую книгу, в которой каждое визуальное представление спарклайна дублируется в двух формах: активный собственный спарклайн, привязанный к строке 1, и статическое изображение PNG, встроенное непосредственно в соседнюю ячейку в строке 2. Поскольку изображения хранятся внутри самого файла, рабочая книга остаётся единым автономным артефактом, который можно отправлять по электронной почте или архивировать без нарушения ссылок на встроенные изображения. Отобразите каждую группу спарклайнов в формате PNG, преобразуйте `MemoryStream` в `byte[]` и присвойте массив свойству `EmbeddedImage` целевой ячейки — именно это присвоение делает изображение частью хранимого содержимого ячейки.

{{% alert color="primary" %}}
Поскольку каждая группа спарклайнов привязана к одной ячейке, вы можете обращаться к ней через индексатор `group.Sparklines[0]` вместо перечисления с помощью `foreach`. Это позволяет сохранить код рендеринга кратким и соответствует типичному шаблону «один спарклайн на одну ячейку привязки». Сохранение байтов изображения через `Cell.EmbeddedImage` требует Aspose.Cells 26.5 или более поздней версии.
{{% /alert %}}

## **Рабочий процесс 2 — Экспорт рабочего листа со спарклайнами в HTML**

После того как рабочая книга содержит активные спарклайны (и, при необходимости, встроенные изображения-аналоги), весь рабочий лист можно опубликовать в интернете, сохранив его в формате HTML. Класс `HtmlSaveOptions` предоставляет необходимые параметры для управления этим экспортом; в этом рабочем процессе вы повторно используете файл `output_with_sparklines.xlsx`, созданный в Рабочем процессе 1, и преобразуете его в чистый одностраничный HTML-документ.

### **Пошаговые инструкции**

1. Убедитесь, что файл `output_with_sparklines.xlsx`, созданный в Рабочем процессе 1, доступен на диске в вашем рабочем каталоге.
2. Загрузите этот файл в новый экземпляр `Workbook`.
3. Создайте экземпляр `HtmlSaveOptions` и установите его свойство `ExportActiveWorksheetOnly` в значение `true`, чтобы итоговый HTML-файл содержал только активный рабочий лист, а не всю рабочую книгу.
4. Вызовите `workbook.Save("sparklines.html", htmlOptions)` для записи HTML-вывода на диск.

```csharp
using System;
using System.IO;
using Aspose.Cells;

Workbook workbook = new Workbook("output_with_sparklines.xlsx");
HtmlSaveOptions htmlOptions = new HtmlSaveOptions();
htmlOptions.ExportActiveWorksheetOnly = true;
workbook.Save("sparklines.html", htmlOptions);
```

Приведённый выше код берёт рабочую книгу со спарклайнами из Рабочего процесса 1 и превращает её в переносимый HTML-файл. Спарклайны сохраняются как встроенные SVG- или PNG-изображения внутри сгенерированного HTML в зависимости от режима экспорта, поэтому конечные пользователи могут просматривать тренды в любом современном браузере без установленного Excel. Установив `ExportActiveWorksheetOnly` в `true`, вы избегаете случайной публикации скрытых листов или вспомогательных данных — экспортируется только рабочий лист, видимый пользователю в данный момент.

{{% alert color="primary" %}}
Класс `HtmlSaveOptions` предлагает дополнительные свойства для точной настройки вывода, такие как `ExportHiddenWorksheet`, `ExportImagesAsBase64` и `Encoding`. Настраивайте их по мере необходимости для вашего целевого развёртывания.
{{% /alert %}}

## **Сводка по API**

Описанные выше рабочие процессы опираются на небольшой набор API Aspose.Cells, работающих вместе.

- `SparklineGroup` и метод доступа к коллекции `worksheet.SparklineGroups` используются для объявления типа (Линейная, Столбцовая, Со стопкой), диапазона данных и ячейки привязки для каждой группы спарклайнов. В этой статье каждая группа привязана к одной ячейке, поэтому к группе обращаются через `worksheet.SparklineGroups[i]`.
- `Sparkline` и индексатор `group.Sparklines[0]` возвращают отдельный спарклайн внутри группы. Поскольку каждая группа в примере содержит ровно один спарклайн, цикл `foreach` не требуется.
- `Sparkline.ToImage(Stream, ImageOrPrintOptions)` — это метод рендеринга, который записывает изображение спарклайна в предоставленный `Stream`. Метод возвращает `void`; байты считываются из потока после вызова.
- `Cell.EmbeddedImage` — это свойство типа `byte[]`, которое хранит изображение внутри одной ячейки. Оно доступно в **Aspose.Cells 26.5 и более поздних версиях** и является рекомендуемым способом обратной передачи спарклайна, отрендеренного с помощью `ToImage`, в ту же рабочую книгу.
- `HtmlSaveOptions.ExportActiveWorksheetOnly` (тип `bool`) ограничивает экспорт HTML только активным рабочим листом. Это одно из наиболее часто используемых свойств `HtmlSaveOptions` при создании одностраничных отчётов.
- `ImageOrPrintOptions.ImageType` находится в пространстве имён `Aspose.Cells.Drawing` и выбирает формат изображения (например, `ImageType.Png`), используемый при рендеринге с помощью `ToImage` и при печати рабочих листов в изображения.

## **Связанные статьи**

- [Спарклайны в Aspose.Cells for .NET](/cells/ru/net/sparkline/)
- [Вставка изображения в ячейку](/cells/ru/net/inserting-an-image-into-a-cell/)
- [Рендеринг массива одной ячейки SmartMarker | Aspose.Cells .NET](/cells/ru/net/SmartMarker-Single-Cell-Array-Rendering/)

{{< app/cells/assistant language="csharp" >}}