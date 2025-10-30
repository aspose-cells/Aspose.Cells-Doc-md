---
title: Trova celle con stile specifico con C++
linktitle: Trova celle con uno stile specifico
type: docs
weight: 190
url: /it/cpp/find-cells-with-specific-style/
description: Scopri come trovare o cercare celle con uno stile particolare applicato attraverso l API Aspose.Cells for C++.
keywords: Trova celle con uno stile particolare applicato, Cerca celle con uno stile particolare applicato
---

{{% alert color="primary" %}}

A volte è necessario trovare celle con uno stile particolare applicato. Puoi usare Aspose.Cells per trovare tutte le celle con uno stile comune. Aspose.Cells fornisce la proprietà [**FindOptions.GetStyle()**](https://reference.aspose.com/cells/cpp/aspose.cells/findoptions/getstyle/) che puoi usare per specificare lo stile da cercare nelle celle.

{{% /alert %}}

Il codice in questo esempio trova tutte le celle che hanno lo stesso stile di quella della cella A1. Dopo che il codice è stato eseguito, tutte le celle che hanno lo stesso stile di A1 contengono il testo "Trovato".

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");
    U16String filePath = srcDir + u"TestBook.xlsx";

    Workbook workbook(filePath);
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    Style style = worksheet.GetCells().Get(u"A1").GetStyle();

    FindOptions options;
    options.SetStyle(style);

    Cell nextCell;

    do
    {
        nextCell = worksheet.GetCells().Find(U16String(), nextCell, options);
        if (nextCell.GetRow() == -1)
            break;
        nextCell.PutValue(u"Found");
    } while (true);

    U16String outputPath = outDir + u"output.out.xlsx";
    workbook.Save(outputPath);

    std::cout << "File saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
