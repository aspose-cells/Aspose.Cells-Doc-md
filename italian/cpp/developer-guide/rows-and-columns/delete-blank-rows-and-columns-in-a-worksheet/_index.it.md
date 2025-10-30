---
title: Elimina righe e colonne vuote in un foglio di lavoro con C++
linktitle: Eliminare Righe e Colonne Vuote in un Foglio di Lavoro
type: docs
weight: 300
url: /it/cpp/delete-blank-rows-and-columns-in-a-worksheet/
description: Elimina righe e colonne vuote in un foglio di lavoro utilizzando Aspose.Cells con C++.
---

{{% alert color="primary" %}}

È possibile eliminare tutte le righe e colonne vuote da un foglio di lavoro. Questo è utile quando, ad esempio, si genera un file PDF da un file Microsoft Excel e si desidera convertire solo le righe e colonne che contengono dati o oggetti correlati.

Utilizzare i seguenti metodi Aspose.Cells per eliminare le righe e le colonne vuote:

1. Per eliminare le righe vuote, utilizzare il metodo [**Cells.DeleteBlankRows()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/deleteblankrows/). Si prega di notare che, per le righe vuote che verranno eliminate, non è solo richiesto che [**Row.IsBlank**](https://reference.aspose.com/cells/cpp/aspose.cells/row/isblank/) sia vero, ma non deve essere definito alcun commento visibile per qualsiasi cella in quelle righe e non deve esserci alcuna tabella pivot il cui intervallo si sovrapponga con esse.
2. Per eliminare colonne vuote, utilizza il metodo [**Cells.DeleteBlankColumns()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/deleteblankcolumns/).

{{% /alert %}}

## Codice C++ per eliminare righe vuote

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Open an existing Excel file
    U16String inputFilePath = srcDir + u"SampleInput.xlsx";
    Workbook workbook(inputFilePath);

    // Create a Worksheets object with reference to the sheets of the Workbook
    WorksheetCollection sheets = workbook.GetWorksheets();

    // Get the first Worksheet from WorksheetCollection
    Worksheet sheet = sheets.Get(0);

    // Delete the Blank Rows from the worksheet
    sheet.GetCells().DeleteBlankRows();

    // Save the Excel file
    U16String outputFilePath = outDir + u"mybook.out.xlsx";
    workbook.Save(outputFilePath);

    std::cout << "Blank rows deleted and workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## Codice C++ per eliminare colonne vuote

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of input excel file
    U16String inputFilePath = srcDir + u"SampleInput.xlsx";

    // Create a smart pointer to a new Workbook instance
    std::unique_ptr<Workbook> wb = std::make_unique<Workbook>(inputFilePath);

    // Create a Worksheets object with reference to the sheets of the Workbook
    WorksheetCollection sheets = wb->GetWorksheets();

    // Get the first Worksheet from WorksheetCollection
    Worksheet sheet = sheets.Get(0);

    // Delete the blank columns from the worksheet
    sheet.GetCells().DeleteBlankColumns();

    // Save the excel file
    U16String outputFilePath = srcDir + u"mybook.out.xlsx";
    wb->Save(outputFilePath);

    std::cout << "Blank columns deleted successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
