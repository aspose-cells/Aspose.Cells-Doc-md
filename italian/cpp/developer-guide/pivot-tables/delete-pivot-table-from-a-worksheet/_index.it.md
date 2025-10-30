---
title: Elimina una Pivot Table da un foglio di lavoro con C++
linktitle: Elimina Pivot Table
type: docs
weight: 60
url: /it/cpp/delete-pivot-table-from-a-worksheet/
description: Codice C++ per rimuovere PivotTable dai Fogli di Lavoro Excel usando Aspose.Cells.
keywords: c++ rimuovi pivot table dal foglio di lavoro, c++ rimuovi pivot table da excel, come eliminare pivot table con c++, elimina pivot table con c++, elimina pivot table da excel con c++, c++ cancella pivot table, c++ rimuovi pivot table, rimuovi pivot table, elimina pivot table, come eliminare pivot table
---

{{% alert color="primary" %}}

Aspose.Cells fornisce una funzionalità per eliminare o rimuovere la tabella pivot da un foglio di lavoro. Puoi eliminare la tabella pivot utilizzando l'oggetto tabella pivot o la posizione della tabella pivot. Si prega di utilizzare il metodo [**Worksheet.PivotTables.Remove()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottablecollection/remove/) per eliminare la tabella pivot utilizzando l'oggetto tabella pivot e il metodo [**Worksheet.PivotTables.RemoveAt()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottablecollection/removeat/) per eliminare l'oggetto tabella pivot utilizzando la sua posizione all'interno della collezione delle tabelle pivot.

{{% /alert %}}

Il seguente esempio di codice elimina due pivot table dal foglio di lavoro. Per primo elimina la pivot table usando il metodo [**Worksheet.PivotTables.Remove()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottablecollection/remove/) e poi utilizza il metodo [**Worksheet.PivotTables.RemoveAt()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottablecollection/removeat/).

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

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"source.xlsx";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"output_out.xlsx";

    // Create workbook object from source Excel file
    Workbook workbook(inputFilePath);

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access the first pivot table object
    PivotTable pivotTable = worksheet.GetPivotTables().Get(0);

    // Remove pivot table using pivot table object
    worksheet.GetPivotTables().Remove(pivotTable);

    // OR you can remove pivot table using pivot table position by uncommenting below line
    // worksheet.GetPivotTables().RemoveAt(0);

    // Save the workbook
    workbook.Save(outputFilePath);

    std::cout << "Pivot table removed successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
