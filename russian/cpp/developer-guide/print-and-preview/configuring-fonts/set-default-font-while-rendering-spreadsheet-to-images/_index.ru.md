---
title: Установка шрифта по умолчанию при рендеринге таблицы в изображения с помощью C++
linktitle: Установить Шрифт по умолчанию
type: docs
weight: 360
url: /ru/cpp/set-default-font-while-rendering-spreadsheet-to-images/
description: Узнайте, как задавать шрифт по умолчанию при рендеринге таблиц в изображения с помощью Aspose.Cells и C++.
---

{{% alert color="primary" %}}

Используйте свойство [**ImageOrPrintOptions.GetDefaultFont()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getdefaultfont/), чтобы установить шрифт по умолчанию при рендеринге электронных таблиц в изображения. Это свойство будет действительным только в том случае, если шрифт по умолчанию книги не может отобразить ваши символы. Шрифт по умолчанию, указанный с помощью свойства [**ImageOrPrintOptions.GetDefaultFont()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getdefaultfont/), используется для всех тех ячеек, которые имеют недопустимые или отсутствующие шрифты.

{{% /alert %}}

## Установка шрифта по умолчанию при рендеринге электронных таблиц в изображения

Приведенный ниже образец кода создает книгу, добавляет текст в ячейку A4 первого рабочего листа и устанавливает его шрифт на недопустимый или отсутствующий шрифт. Затем он создает два изображения рабочего листа. Первое изображение создается, установив свойство [**ImageOrPrintOptions.GetDefaultFont()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getdefaultfont/) на *Courier New* и второе изображение создается, установив свойство [**ImageOrPrintOptions.GetDefaultFont()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getdefaultfont/) на *Times New Roman*.

Это выходное изображение после установки свойства [**ImageOrPrintOptions.GetDefaultFont()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getdefaultfont/) на *Courier New*.

![todo:image_alt_text](set-default-font-while-rendering-spreadsheet-to-images_1.png)

Это выходное изображение после установки свойства [**ImageOrPrintOptions.GetDefaultFont()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getdefaultfont/) на *Times New Roman*.

![todo:image_alt_text](set-default-font-while-rendering-spreadsheet-to-images_2.png)

## Образец кода

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main() {
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create workbook object
    Workbook wb;

    // Set default font of the workbook to none
    Style s = wb.GetDefaultStyle();
    s.GetFont().SetName(u"");
    wb.SetDefaultStyle(s);

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access cell A4 and add some text inside it
    Cell cell = ws.GetCells().Get(u"A4");
    cell.PutValue(u"This text has some unknown or invalid font which does not exist.");

    // Set the font of cell A4 which is unknown
    Style st = cell.GetStyle();
    st.GetFont().SetName(u"UnknownNotExist");
    st.GetFont().SetSize(20);
    st.SetIsTextWrapped(true);
    cell.SetStyle(st);

    // Set first column width and fourth column height
    ws.GetCells().SetColumnWidth(0, 80);
    ws.GetCells().SetRowHeight(3, 60);

    // Create image or print options
    ImageOrPrintOptions opts;
    opts.SetOnePagePerSheet(true);
    opts.SetImageType(ImageType::Png);

    // Render worksheet image with Courier New as default font
    opts.SetDefaultFont(u"Courier New");
    SheetRender sr(ws, opts);
    sr.ToImage(0, outDir + u"out_courier_new_out.png");

    // Render worksheet image again with Times New Roman as default font
    opts.SetDefaultFont(u"Times New Roman");
    SheetRender sr2(ws, opts);
    sr2.ToImage(0, outDir + u"times_new_roman_out.png");

    Aspose::Cells::Cleanup();
    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
