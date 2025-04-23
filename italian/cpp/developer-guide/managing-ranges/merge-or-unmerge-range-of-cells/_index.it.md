---
title: Unisci o disunisci un intervallo di celle con C++
linktitle: Unisci o separa un intervallo di celle
type: docs
weight: 190
url: /it/cpp/merge-or-unmerge-range-of-cells/
description: Unisci e disunisci celle in un intervallo in Excel con codice C++.
keywords: merge e unmerge celle in C++, merge e unmerge celle in intervallo, unisci e disunisci celle in intervallo con C++, unisci e disunisci celle in intervallo usando C++, unisci e disunisci celle in Excel usando C++, unisci e disunisci celle in Excel con C++, merge e unmerge celle in Excel, unisci celle in Excel, disunisci celle in Excel
---

{{% alert color="primary" %}}

Puoi utilizzare Aspose.Cells per unire o dividere un intervallo di celle. Aspose.Cells fornisce i metodi [**Range.Merge()**](https://reference.aspose.com/cells/cpp/aspose.cells/range/merge/) e [**Range.UnMerge()**](https://reference.aspose.com/cells/cpp/aspose.cells/range/unmerge/) a questo scopo. Questo articolo spiega come unire un intervallo di celle in una singola cella.

{{% /alert %}}

## **Esempio**

Il seguente esempio di codice crea prima un intervallo - A1:D4 - quindi unisce le celle dell'intervallo in una singola cella usando il metodo [**Range.Merge()**](https://reference.aspose.com/cells/cpp/aspose.cells/range/merge/). Analogamente, puoi suddividere le celle creando un intervallo e chiamando il metodo [**Range.UnMerge()**](https://reference.aspose.com/cells/cpp/aspose.cells/range/unmerge/).

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of output excel file
    U16String outputPath = srcDir + u"output.out.xlsx";

    // Create a workbook
    Workbook workbook;

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Create a range
    Range range = worksheet.GetCells().CreateRange(u"A1:D4");

    // Merge range into a single cell
    range.Merge();

    // Save the workbook
    workbook.Save(outputPath);

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
