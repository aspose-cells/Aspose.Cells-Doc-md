---
title: Standardschriftart beim Rendern von Tabellenkalkulationen in Bilder mit C++ festlegen
linktitle: Standardschriftart festlegen
type: docs
weight: 360
url: /de/cpp/set-default-font-while-rendering-spreadsheet-to-images/
description: Erfahren Sie, wie Sie die Standardschriftart beim Rendern von Tabellenkalkulationen in Bilder mit Aspose.Cells und C++ setzen.
---

{{% alert color="primary" %}}

Bitte verwenden Sie die Eigenschaft [**ImageOrPrintOptions.GetDefaultFont()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getdefaultfont/), um die Standard-Schriftart beim Rendern von Tabellenkalkulationen als Bilder festzulegen. Diese Eigenschaft ist nur wirksam, wenn die Standard-Schriftart der Arbeitsmappe Ihre Zeichen nicht rendern kann. Die mit der Eigenschaft [**ImageOrPrintOptions.GetDefaultFont()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getdefaultfont/) festgelegte Standard-Schriftart wird für alle Zellen verwendet, die ungültige oder nicht vorhandene Schriftarten haben.

{{% /alert %}}

## Standard-Schriftart beim Rendern von Tabellenkalkulationen als Bilder festlegen

Der folgende Beispielcode erstellt eine Arbeitsmappe, fügt Text in Zelle A4 des ersten Arbeitsblatts ein und legt die Schriftart auf ungültig oder nicht vorhanden fest. Dann werden zwei Bilder des Arbeitsblatts aufgenommen. Das erste Bild wird durch Festlegen der Eigenschaft [**ImageOrPrintOptions.GetDefaultFont()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getdefaultfont/) auf *Courier New* aufgenommen und das zweite Bild wird durch Festlegen der Eigenschaft [**ImageOrPrintOptions.GetDefaultFont()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getdefaultfont/) auf *Times New Roman* aufgenommen.

Dies ist das Ausgabebild nach Festlegen der Eigenschaft [**ImageOrPrintOptions.GetDefaultFont()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getdefaultfont/) auf *Courier New*.

![todo:image_alt_text](set-default-font-while-rendering-spreadsheet-to-images_1.png)

Dies ist das Ausgabebild nach Festlegen der Eigenschaft [**ImageOrPrintOptions.GetDefaultFont()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getdefaultfont/) auf *Times New Roman*.

![todo:image_alt_text](set-default-font-while-rendering-spreadsheet-to-images_2.png)

## Beispielcode

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
