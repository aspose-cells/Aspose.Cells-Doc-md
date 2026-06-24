---
title: Преобразование спарклайна в изображение и HTML в Aspose.Cells for C++
linktitle: Convert Sparkline to Image and HTML
description: Узнайте, как преобразовать спарклайны Aspose.Cells в отдельные изображения для встраивания в ячейки и экспортировать рабочие листы со спарклайнами в HTML с помощью HtmlSaveOptions.
keywords: Aspose.Cells, C++, спарклайн, Sparkline.ToImage, Cell.EmbeddedImage, HtmlSaveOptions, рендеринг спарклайна, преобразование спарклайна в изображение, экспорт спарклайна в HTML
type: docs
weight: 120
url: /ru/cpp/convert-sparkline-to-image-and-html/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Спарклайны — это миниатюрные диаграммы, размещаемые внутри ячеек рабочего листа. Aspose.Cells позволяет извлекать каждый спарклайн как отдельное изображение (для встраивания в другую ячейку или внешний отчёт), а также экспортировать весь рабочий лист со спарклайнами в HTML для распространения через браузер. Свойство `Cell.EmbeddedImage`, используемое в этой статье, доступно в **Aspose.Cells версии 26.5 и более поздних**.
{{% /alert %}}

## **Введение**

Спарклайны — это компактный способ визуализации трендов непосредственно внутри рабочего листа. В то время как пользователи Excel видят их на месте, во многих реальных сценариях требуется, чтобы спарклайн покинул ячейку — например, чтобы быть встроенным в другую ячейку как статическое изображение, прикреплённым к автоматическому электронному письму или отображённым в составе HTML-отчёта, опубликованного в Интернете.

Aspose.Cells поддерживает обе эти операции. Метод `Sparkline.ToImage` преобразует отдельный спарклайн в поток, и полученные байты могут быть присвоены свойству `Cell.EmbeddedImage`, чтобы изображение сохранялось внутри одной ячейки рабочей книги. Отдельно класс `HtmlSaveOptions` позволяет преобразовать всю рабочую книгу — вместе со спарклайнами — в самостоятельный HTML-файл. В этой статье оба рабочих процесса рассматриваются от начала до конца.

## **Рабочий процесс 1 — рендеринг спарклайнов в изображения и встраивание их в ячейки**

В этом рабочем процессе вы создадите рабочий лист, содержащий небольшой диапазон исходных значений, прикрепите к этому диапазону три разные группы спарклайнов (Line, Column и Stacked/Win-Loss), отрендерите каждую группу в формат PNG и запишете байты PNG в соседние ячейки как встроенные изображения. Конечный результат — один файл `.xlsx`, который содержит как живые спарклайны, так и их отрендеренные изображения.

### **Пошаговые инструкции**

1. Определите рабочий каталог и убедитесь, что он существует на диске.
2. Создайте новый объект `Workbook` и получите ссылку на первый `Worksheet`.
3. Заполните ячейки с `A1` по `E1` пятью числовыми значениями (например, ежедневными продажами или показаниями температуры).
4. Добавьте три объекта `SparklineGroup` на рабочий лист, вызвав `worksheet.SparklineGroups.Add(...)`:
   - Группа `SparklineType.Line`, привязанная к `F1`, с диапазоном данных `A1:E1`.
   - Группа `SparklineType.Column`, привязанная к `G1`, с диапазоном данных `A1:E1`.
   - Группа `SparklineType.Stacked` (win/loss), привязанная к `H1`, с диапазоном данных `A1:E1`.
5. Создайте экземпляр `ImageOrPrintOptions` и установите его свойство `ImageType` в значение `ImageType.Png`, чтобы каждый спарклайн был отрендерен как прозрачный PNG.
6. Для каждой из трёх групп отрендерите её единственный спарклайн с помощью `group.Sparklines[0].ToImage(memoryStream, imageOptions)`, преобразуйте `MemoryStream` в `Vector<uint8_t>` и присвойте массив свойствам `worksheet.Cells["F2"].EmbeddedImage`, `worksheet.Cells["G2"].EmbeddedImage` и `worksheet.Cells["H2"].EmbeddedImage` соответственно.
7. Сохраните рабочую книгу как `output_with_sparklines.xlsx`.

```cpp
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    worksheet.GetCells().Get(u"A1").PutValue(5);
    worksheet.GetCells().Get(u"B1").PutValue(-3);
    worksheet.GetCells().Get(u"C1").PutValue(8);
    worksheet.GetCells().Get(u"D1").PutValue(-2);
    worksheet.GetCells().Get(u"E1").PutValue(6);

    CellArea lineArea;
    lineArea.StartColumn = 5;
    lineArea.EndColumn = 5;
    lineArea.StartRow = 0;
    lineArea.EndRow = 0;
    int lineIdx = worksheet.GetSparklineGroups().Add(SparklineType::Line, U16String("A1:E1"), false, lineArea);

    CellArea columnArea;
    columnArea.StartColumn = 6;
    columnArea.EndColumn = 6;
    columnArea.StartRow = 0;
    columnArea.EndRow = 0;
    int columnIdx = worksheet.GetSparklineGroups().Add(SparklineType::Column, U16String("A1:E1"), false, columnArea);

    CellArea stackedArea;
    stackedArea.StartColumn = 7;
    stackedArea.EndColumn = 7;
    stackedArea.StartRow = 0;
    stackedArea.EndRow = 0;
    int stackedIdx = worksheet.GetSparklineGroups().Add(SparklineType::Stacked, U16String("A1:E1"), false, stackedArea);

    ImageOrPrintOptions imageOptions;
    imageOptions.SetImageType(ImageType::Png);

    Sparkline lineSp = worksheet.GetSparklineGroups().Get(lineIdx).GetSparklines().Get(0);
    Vector<uint8_t> lineImg = lineSp.ToImage(imageOptions);
    worksheet.GetCells().Get(u"F2").SetEmbeddedImage(lineImg);

    Sparkline columnSp = worksheet.GetSparklineGroups().Get(columnIdx).GetSparklines().Get(0);
    Vector<uint8_t> columnImg = columnSp.ToImage(imageOptions);
    worksheet.GetCells().Get(u"G2").SetEmbeddedImage(columnImg);

    Sparkline stackedSp = worksheet.GetSparklineGroups().Get(stackedIdx).GetSparklines().Get(0);
    Vector<uint8_t> stackedImg = stackedSp.ToImage(imageOptions);
    worksheet.GetCells().Get(u"H2").SetEmbeddedImage(stackedImg);

    workbook.Save(u"output_with_sparklines.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

Приведённый выше код создаёт рабочую книгу, в которой каждое визуальное представление спарклайна дублируется в двух формах: живой, нативный спарклайн, привязанный к строке 1, и статическое изображение PNG, встроенное непосредственно в соседнюю ячейку в строке 2. Поскольку изображения хранятся внутри самого файла, рабочая книга остаётся единым самодостаточным артефактом, который можно отправить по электронной почте или заархивировать без нарушения ссылок на встроенные изображения. Отрендерите каждую группу спарклайнов в формат PNG, преобразуйте `MemoryStream` в `Vector<uint8_t>` и присвойте массив свойству `EmbeddedImage` целевой ячейки — именно это присваивание делает изображение частью сохранённого содержимого ячейки.

{{% alert color="primary" %}}
Поскольку каждая группа спарклайнов привязана к одной ячейке, вы можете обращаться к ней через индексатор `group.Sparklines[0]` вместо перечисления с помощью `foreach`. Это сохраняет код рендеринга коротким и соответствует типичному шаблону «один спарклайн на одну ячейку привязки». Сохранение байтов изображения через `Cell.EmbeddedImage` требует Aspose.Cells версии 26.5 или более поздней.
{{% /alert %}}

## **Рабочий процесс 2 — экспорт рабочего листа со спарклайнами в HTML**

После того как рабочая книга содержит живые спарклайны (и, при необходимости, встроенные изображения), весь рабочий лист может быть опубликован в Интернете путём сохранения его в формате HTML. Класс `HtmlSaveOptions` предоставляет параметры, необходимые для управления этим экспортом; в этом рабочем процессе вы повторно используете файл `output_with_sparklines.xlsx`, созданный в рабочем процессе 1, и преобразуете его в чистый одностраничный HTML-документ.

### **Пошаговые инструкции**

1. Убедитесь, что файл `output_with_sparklines.xlsx`, созданный в рабочем процессе 1, доступен на диске в вашем рабочем каталоге.
2. Загрузите этот файл в новый экземпляр `Workbook`.
3. Создайте экземпляр `HtmlSaveOptions` и установите его свойство `ExportActiveWorksheetOnly` в значение `true`, чтобы итоговый HTML-файл содержал только активный рабочий лист, а не всю рабочую книгу.
4. Вызовите `workbook.Save("sparklines.html", htmlOptions)` для записи HTML-вывода на диск.

```cpp
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    Workbook workbook(u"output_with_sparklines.xlsx");
    HtmlSaveOptions htmlOptions;
    htmlOptions.SetExportActiveWorksheetOnly(true);
    workbook.Save(u"sparklines.html", htmlOptions);

    Aspose::Cells::Cleanup();
    return 0;
}
```

Приведённый выше код берёт рабочую книгу со спарклайнами из рабочего процесса 1 и превращает её в переносимый HTML-файл. Спарклайны сохраняются как встроенные SVG- или PNG-рендеринги внутри сгенерированного HTML в зависимости от режима экспорта, поэтому конечные пользователи могут просматривать тренды в любом современном браузере без необходимости установки Excel. Установив `ExportActiveWorksheetOnly` в значение `true`, вы избегаете случайной публикации скрытых листов или вспомогательных данных — экспортируется только рабочий лист, видимый пользователю в данный момент.

{{% alert color="primary" %}}
Класс `HtmlSaveOptions` предлагает дополнительные свойства для тонкой настройки вывода, такие как `ExportHiddenWorksheet`, `ExportImagesAsBase64` и `Encoding`. Настраивайте их по мере необходимости для вашей целевой среды развёртывания.
{{% /alert %}}

## **Сводка по API**

Описанные выше рабочие процессы опираются на небольшой набор API Aspose.Cells, работающих совместно.

- `SparklineGroup` и средство доступа к коллекции `worksheet.SparklineGroups` используются для объявления типа (Line, Column, Stacked), диапазона данных и ячейки привязки для каждой группы спарклайнов. В этой статье каждая группа привязана к одной ячейке, поэтому группа доступна через `worksheet.SparklineGroups[i]`.
- `Sparkline` и индексатор `group.Sparklines[0]` возвращают отдельный спарклайн внутри группы. Поскольку каждая группа в примере содержит ровно один спарклайн, цикл `foreach` не требуется.
- `Sparkline.ToImage(Stream, ImageOrPrintOptions)` — это метод рендеринга, который записывает изображение спарклайна в предоставленный `Stream`. Метод возвращает `void`; байты считываются из потока после вызова.
- `Cell.EmbeddedImage` — это свойство типа `Vector<uint8_t>`, которое сохраняет изображение внутри одной ячейки. Оно доступно в **Aspose.Cells версии 26.5 и более поздних** и является рекомендуемым способом обратного сохранения спарклайна, отрендеренного с помощью `ToImage`, в ту же рабочую книгу.
- `HtmlSaveOptions.ExportActiveWorksheetOnly` (тип `bool`) ограничивает экспорт HTML активным рабочим листом. Это одно из наиболее часто используемых свойств `HtmlSaveOptions` при создании одностраничных отчётов.
- `ImageOrPrintOptions.ImageType` находится в пространстве имён `Aspose.Cells.Drawing` и выбирает формат изображения (например, `ImageType.Png`), используемый при рендеринге с помощью `ToImage` и при печати рабочих листов в изображения.

## **Связанные статьи**

- [Спарклайны в Aspose.Cells для Aspose.Cells for C++](/cells/ru/cpp/sparkline/)
- [Вставка изображения в ячейку](/cells/ru/cpp/inserting-an-image-into-a-cell/)
- [Рендеринг массива одиночной ячейки SmartMarker | Aspose.Cells for C++](/cells/ru/cpp/SmartMarker-Single-Cell-Array-Rendering/)

{{< app/cells/assistant language="cpp" >}}