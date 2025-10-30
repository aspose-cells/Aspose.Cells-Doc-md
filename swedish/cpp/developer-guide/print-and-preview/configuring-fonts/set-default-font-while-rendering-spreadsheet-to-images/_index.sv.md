---
title: Ställ in standardteckensnitt vid rendering av kalkylblad till bilder med C++
linktitle: Ställ in Standardteckensnitt
type: docs
weight: 360
url: /sv/cpp/set-default-font-while-rendering-spreadsheet-to-images/
description: Lär dig hur du ställer in standardteckensnittet vid rendering av kalkylblad till bilder med Aspose.Cells och C++.
---

{{% alert color="primary" %}}

Använd egenskapen [**ImageOrPrintOptions.GetDefaultFont()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getdefaultfont/) för att ange standardfont medan du renderar kalkylblad till bilder. Denna egenskap kommer bara att vara effektiv när arbetsbokens standardfont inte kan rendera dina tecken. Den standardfont som anges med egenskapen [**ImageOrPrintOptions.GetDefaultFont()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getdefaultfont/) används för alla de celler som har ogiltiga eller obefintliga teckensnitt.

{{% /alert %}}

## Ange standardfont medan du renderar kalkylblad till bilder

Följande kodexempel skapar en arbetsbok, lägger till någon text i cell A4 på den första arbetsbladet och anger dess font till ogiltig eller icke-existerande font. Sedan tar den två bilder av arbetsbladet. Den första bilden tas genom att ange egenskapen [**ImageOrPrintOptions.GetDefaultFont()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getdefaultfont/) till *Courier New* och den andra bilden tas genom att ange egenskapen [**ImageOrPrintOptions.GetDefaultFont()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getdefaultfont/) till *Times New Roman*.

Detta är utdataavbildningen efter att ha satt egenskapen [**ImageOrPrintOptions.GetDefaultFont()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getdefaultfont/) till *Courier New*.

![todo:image_alt_text](set-default-font-while-rendering-spreadsheet-to-images_1.png)

Detta är utmatningsbilden efter att ha ställt in egenskapen [**ImageOrPrintOptions.GetDefaultFont()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getdefaultfont/) till *Times New Roman*.

![todo:image_alt_text](set-default-font-while-rendering-spreadsheet-to-images_2.png)

## Exempelkod

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
