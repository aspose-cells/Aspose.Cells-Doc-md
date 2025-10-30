---
title: Legen Sie die Standardschriftart beim Rendern von Tabellen nach HTML mit C++ fest
linktitle: Legen Sie die Standardschriftart beim Rendern der Tabellenkalkulation in HTML fest
type: docs
weight: 370
url: /de/cpp/set-default-font-while-rendering-spreadsheet-to/
description: Lernen Sie, wie man die Standard Schriftart beim Rendern von Tabellen nach HTML mit Aspose.Cells for C++ festlegt.
---

{{% alert color="primary" %}}

Aspose.Cells ermöglicht es Ihnen, die Standardschriftart beim Rendern einer Tabelle nach HTML festzulegen. Verwenden Sie dazu [**HtmlSaveOptions.GetDefaultFontName()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getdefaultfontname/). Diese Eigenschaft ist nützlich, wenn einige Zellen in einer Tabelle ungültige oder nicht vorhandene Schriftarten haben. Diese Zellen werden dann in einer mit [**HtmlSaveOptions.GetDefaultFontName()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getdefaultfontname/) festgelegten Schriftart gerendert.

{{% /alert %}}

## Festlegen der Standardschriftart beim Rendern von Tabellenkalkulationen in HTML

Der folgende Beispielscode erstellt eine Arbeitsmappe und fügt einen Text in Zelle B4 des ersten Arbeitsblatts hinzu und legt die Schriftart auf eine unbekannte/nicht vorhandene Schriftart fest. Dann speichert er die Arbeitsmappe in HTML, indem er verschiedene Standardschriftart-Namen wie Courier New, Arial, Times New Roman usw. festlegt.

Das Screenshot zeigt die Auswirkung der Einstellung verschiedener Standard-Schriftartnamen über die Eigenschaft [**HtmlSaveOptions.GetDefaultFontName()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getdefaultfontname/).

![todo:image_alt_text](set-default-font-while-rendering-spreadsheet-to-html_1.png)

Der Code generiert die [Ausgabe-HTML-Datei mit Courier New](5115516), die [Ausgabe-HTML mit Arial](5115518) und die [Ausgabe-HTML-Datei mit Times New Roman](5115517).

## Beispielcode

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
