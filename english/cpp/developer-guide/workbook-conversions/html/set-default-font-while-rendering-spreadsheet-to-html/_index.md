---
title: Set Default Font while rendering spreadsheet to HTML with C++
linktitle: Set Default Font while rendering spreadsheet to HTML
type: docs
weight: 370
url: /cpp/set-default-font-while-rendering-spreadsheet-to/
description: Learn how to set default font while rendering spreadsheet to HTML using Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Aspose.Cells allows you to set the default font while rendering a spreadsheet to HTML. Please use the [**HtmlSaveOptions.DefaultFontName**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/defaultfontname/) for this purpose. This property is useful when there are some cells in a spreadsheet that have invalid or non-existing fonts. Then those cells will be rendered in a font specified with the [**HtmlSaveOptions.DefaultFontName**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/defaultfontname/) property.

{{% /alert %}}

## Set Default Font while rendering spreadsheet to HTML

The following sample code creates a workbook and adds some text in cell B4 of the first worksheet and sets its font to some unknown/non-existing font. Then it saves the workbook in HTML by setting different default font names like Courier New, Arial, Times New Roman, etc.

The screenshot shows the effect of setting different default font names via [**HtmlSaveOptions.DefaultFontName**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/defaultfontname/) property.

![todo:image_alt_text](set-default-font-while-rendering-spreadsheet-to-html_1.png)

The code generates the [output HTML file with Courier New](5115516), the [output HTML with Arial](5115518), and the [output HTML file with Times New Roman](5115517).

## Sample Code

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