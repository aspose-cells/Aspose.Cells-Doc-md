---
title: Zeile Höhen vom Quellbereich zum Zielbereich mit C++ kopieren
linktitle: Quellenbereichszeilenhöhen in Zielbereich kopieren
type: docs
weight: 590
url: /de/cpp/copy-row-heights-of-source-range-to-destination-range/
description: Lernen Sie, wie Sie Zeilenhöhen von einem Quellbereich auf einen Zielbereich mit Aspose.Cells for C++ kopieren.
---

{{% alert color="primary" %}}

Manchmal müssen Benutzer Zeilenhöhen von einem Quellbereich auf einen Zielbereich kopieren. Aspose.Cells bietet dafür den [**PasteType::RowHeights**](https://reference.aspose.com/cells/cpp/aspose.cells/pastetype/)-Aufzählungstyp. Wenn Sie die Eigenschaft [**GetPasteType()**](https://reference.aspose.com/cells/cpp/aspose.cells/pasteoptions/getpastetype/) mit dem [**PasteType::RowHeights**](https://reference.aspose.com/cells/cpp/aspose.cells/pastetype/)-Aufzählungstyp setzen, werden die Höhen aller Zeilen im Quellbereich in den Zielbereich kopiert.

{{% /alert %}}

 Das folgende Beispiel erklärt, wie man die [**PasteType::RowHeights**](https://reference.aspose.com/cells/cpp/aspose.cells/pastetype/)-Aufzählung verwendet, um Zeilenhöhen von einem Quellbereich in einen Zielbereich zu kopieren. Wenn Sie die erzeugte Excel-Datei in Microsoft Excel öffnen, sehen Sie, dass die Zeilenhöhen im Zielbereich genau die gleichen sind wie im Quellbereich.

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

    // Create workbook object
    Workbook workbook;

    // Source worksheet
    Worksheet srcSheet = workbook.GetWorksheets().Get(0);

    // Add destination worksheet
    Worksheet dstSheet = workbook.GetWorksheets().Add(u"Destination Sheet");

    // Set the row height of the 4th row. This row height will be copied to destination range
    srcSheet.GetCells().SetRowHeight(3, 50);

    // Create source range to be copied
    Range srcRange = srcSheet.GetCells().CreateRange(u"A1:D10");

    // Create destination range in destination worksheet
    Range dstRange = dstSheet.GetCells().CreateRange(u"A1:D10");

    // PasteOptions, we want to copy row heights of source range to destination range
    PasteOptions opts;
    opts.SetPasteType(PasteType::RowHeights);

    // Copy source range to destination range with paste options
    dstRange.Copy(srcRange, opts);

    // Write informative message in cell D4 of destination worksheet
    dstSheet.GetCells().Get(u"D4").PutValue(u"Row heights of source range copied to destination range");

    // Save the workbook in xlsx format
    workbook.Save(outDir + u"output_out.xlsx", SaveFormat::Xlsx);

    std::cout << "Row heights copied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
