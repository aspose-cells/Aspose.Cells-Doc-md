---
title: Copia altezza righe dell intervallo di origine nell intervallo di destinazione con C++
linktitle: Copia l altezza delle righe dell intervallo di origine nell intervallo di destinazione
type: docs
weight: 590
url: /it/cpp/copy-row-heights-of-source-range-to-destination-range/
description: Impara come copiare l altezza delle righe da un intervallo di origine a uno di destinazione usando Aspose.Cells for C++.
---

{{% alert color="primary" %}}

A volte, gli utenti devono copiare l'altezza delle righe da un intervallo di origine a uno di destinazione. Aspose.Cells fornisce l'enumerazione [**PasteType::RowHeights**](https://reference.aspose.com/cells/cpp/aspose.cells/pastetype/) per questo scopo. Quando imposti la proprietà [**GetPasteType()**](https://reference.aspose.com/cells/cpp/aspose.cells/pasteoptions/getpastetype/) con l'enumerazione [**PasteType::RowHeights**](https://reference.aspose.com/cells/cpp/aspose.cells/pastetype/), le altezze di tutte le righe all'interno dell'intervallo di origine verranno copiate nell'intervallo di destinazione.

{{% /alert %}}

Il codice di esempio seguente spiega come usare l'enumerazione [**PasteType::RowHeights**](https://reference.aspose.com/cells/cpp/aspose.cells/pastetype/) per copiare le altezze delle righe da un intervallo di origine a uno di destinazione. Una volta aperto il file Excel di output generato da questo codice in Microsoft Excel, vedrai che le altezze delle righe dell'intervallo di destinazione sono esattamente le stesse delle righe dell'intervallo di origine.

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
{{< app/cells/assistant language="cpp" >}}
