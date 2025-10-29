---
title: Установить шрифт по умолчанию при отображении таблицы в HTML с помощью C++
linktitle: Установить шрифт по умолчанию при рендеринге электронных таблиц в HTML
type: docs
weight: 370
url: /ru/cpp/set-default-font-while-rendering-spreadsheet-to/
description: Узнайте, как устанавливать шрифт по умолчанию при отображении таблицы в HTML с помощью Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Aspose.Cells позволяет устанавливать шрифт по умолчанию при преобразовании таблицы в HTML. Пожалуйста, используйте [**HtmlSaveOptions.GetDefaultFontName()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getdefaultfontname/) для этой цели. Эта характеристика полезна, когда в таблице есть ячейки с недопустимыми или несуществующими шрифтами. Тогда такие ячейки будут отображаться в шрифте, указанном с помощью свойства [**HtmlSaveOptions.GetDefaultFontName()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getdefaultfontname/).

{{% /alert %}}

## Установить шрифт по умолчанию при рендеринге электронной таблицы в HTML

Следующий образец кода создает книгу и добавляет некоторый текст в ячейку B4 первого листа и устанавливает ее шрифт на неизвестный/не существующий шрифт. Затем он сохраняет книгу в HTML, устанавливая разные имена шрифтов по умолчанию, такие как Courier New, Arial, Times New Roman, и т. д.

На снимке экрана показан эффект установки разных шрифтов по умолчанию через свойство [**HtmlSaveOptions.GetDefaultFontName()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getdefaultfontname/).

![todo:image_alt_text](set-default-font-while-rendering-spreadsheet-to-html_1.png)

Код генерирует [выходной файл HTML с Courier New](5115516), [выходной HTML с Arial](5115518) и [выходной файл HTML с Times New Roman](5115517).

## Образец кода

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create workbook object and access first worksheet
    Workbook wb;
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access cell B4 and add some text inside it
    Cell cell = ws.GetCells().Get(u"B4");
    cell.PutValue(u"This text has some unknown or invalid font which does not exist.");

    // Set the font of cell B4 which is unknown
    Style st = cell.GetStyle();
    st.GetFont().SetName(u"UnknownNotExist");
    st.GetFont().SetSize(20);
    cell.SetStyle(st);

    // Now save the workbook in html format and set the default font to Courier New
    HtmlSaveOptions opts;
    opts.SetDefaultFontName(u"Courier New");
    wb.Save(outDir + u"out_courier_new_out.htm", opts);

    // Now save the workbook in html format once again but set the default font to Arial
    opts.SetDefaultFontName(u"Arial");
    wb.Save(outDir + u"out_arial_out.htm", opts);

    // Now save the workbook in html format once again but set the default font to Times New Roman
    opts.SetDefaultFontName(u"Times New Roman");
    wb.Save(outDir + u"times_new_roman_out.htm", opts);

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
