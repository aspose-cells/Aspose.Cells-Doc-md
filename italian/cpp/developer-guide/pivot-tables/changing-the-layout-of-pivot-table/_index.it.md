---
title: Modifica il layout della Pivot Table con C++
linktitle: Cambiare il Layout della Tabella Pivot
type: docs
weight: 10
url: /it/cpp/changing-the-layout-of-pivot-table/
description: Scopri come modificare il layout di una Pivot Table in forme compatte, outline e tabellare usando Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Microsoft Excel consente di modificare il layout della Pivot Table utilizzando i comandi di menu *PivotTable Tools > Design > Report Layout*. Puoi cambiare il layout in queste tre forme:

- Mostra in forma compatta
- Mostra in forma di contorno
- Mostra in forma tabellare

Aspose.Cells fornisce anche i metodi [**PivotTable.ShowInCompactForm()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/showincompactform/), [**PivotTable.ShowInOutlineForm()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/showinoutlineform/) e [**PivotTable.ShowInTabularForm()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/showintabularform/) per cambiare il layout della tabella pivot in queste tre forme.

{{% /alert %}}

Il seguente esempio di codice mostra prima la Pivot Table in **Forma Compatta**, poi in **Forma Outline** e infine in **Forma Tabellare**.

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

    // Path of input excel file
    U16String inputFilePath = srcDir + u"pivotTable_sample.xlsx";

    // Create workbook object from source excel file
    Workbook workbook(inputFilePath);

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access first pivot table
    PivotTable pivotTable = worksheet.GetPivotTables().Get(0);

    // 1 - Show the pivot table in compact form
    pivotTable.ShowInCompactForm();

    // Refresh the pivot table
    pivotTable.RefreshData();
    pivotTable.CalculateData();

    // Save the output
    workbook.Save(outDir + u"CompactForm_out.xlsx");

    // 2 - Show the pivot table in outline form
    pivotTable.ShowInOutlineForm();

    // Refresh the pivot table
    pivotTable.RefreshData();
    pivotTable.CalculateData();

    // Save the output
    workbook.Save(outDir + u"OutlineForm_out.xlsx");

    // 3 - Show the pivot table in tabular form
    pivotTable.ShowInTabularForm();

    // Refresh the pivot table
    pivotTable.RefreshData();
    pivotTable.CalculateData();

    // Save the output
    workbook.Save(outDir + u"TabularForm_out.xlsx");

    std::cout << "Pivot table forms saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
