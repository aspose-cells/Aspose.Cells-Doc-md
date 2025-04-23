---
title: Cerca e sostituisci dati in un intervallo con C++
linktitle: Cerca e Sostituisci Dati in un Intervallo
type: docs
weight: 170
url: /it/cpp/search-and-replace-data-in-a-range/
description: Questo articolo mostra come cercare e sostituire i dati in un intervallo in Excel usando codice C++.
keywords: c++ cerca e sostituisci dati in excel, c++ cerca dati in excel, c++ cerca e sostituisci dati in un intervallo, c++ cerca dati in un intervallo, c++ ricerca dati in un intervallo, c++ ricerca dati in intervallo, c++ ricerca dati in excel, c++ cerca dati in intervallo, cerca e sostituisci dati in excel con c++, cerca e sostituisci dati in un intervallo con c++, cerca e sostituisci dati in intervallo con c++
---

{{% alert color="primary" %}}

 A volte è necessario cercare e sostituire dati specifici in un intervallo, ignorando eventuali valori di cella al di fuori dell'intervallo desiderato. Aspose.Cells consente di limitare la ricerca a un intervallo specifico. Questo articolo spiega come.

{{% /alert %}}

 Aspose.Cells fornisce il metodo [**FindOptions::SetRange()**](https://reference.aspose.com/cells/cpp/aspose.cells/findoptions/setrange/) per specificare un intervallo durante la ricerca di dati. Il campione di codice di seguito dimostra come cercare e sostituire i dati in un intervallo.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of input excel file
    U16String filePath = srcDir + u"input.xlsx";

    // Create workbook
    Workbook workbook(filePath);

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Specify the range where you want to search
    // Here the range is E9:H15
    CellArea area = CellArea::CreateCellArea(u"E9", u"H15");

    // Specify Find options
    FindOptions opts;
    opts.SetLookInType(LookInType::Values);
    opts.SetLookAtType(LookAtType::EntireContent);
    opts.SetRange(area);

    Cell cell;
    do
    {
        // Search the cell with value search within range
        cell = worksheet.GetCells().Find(u"search", cell, opts);

        // If no such cell found, then break the loop
        if (!cell)
            break;

        // Replace the cell with value replace
        cell.PutValue(u"replace");

    } while (true);

    // Save the workbook
    U16String outputPath = srcDir + u"output.out.xlsx";
    workbook.Save(outputPath);

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
