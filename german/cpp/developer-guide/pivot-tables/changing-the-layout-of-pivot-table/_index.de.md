---
title: Ändern des Layouts der Pivot Tabelle mit C++
linktitle: Layout der Pivot Tabelle ändern
type: docs
weight: 10
url: /de/cpp/changing-the-layout-of-pivot-table/
description: Erfahren Sie, wie Sie das Layout einer Pivot Tabelle in Kompakt , Gliederungs und Tabellenform mit Aspose.Cells for C++ ändern.
---

{{% alert color="primary" %}}

Microsoft Excel ermöglicht es, das Layout der Pivot-Tabelle mit den Befehlen *PivotTable Tools > Design > Report Layout* zu ändern. Sie können das Layout in diesen drei Formen ändern:

- Im kompakten Formular anzeigen
- Im Gliederungsformular anzeigen
- Im tabellarischen Formular anzeigen

Aspose.Cells bietet auch die Methoden [**PivotTable.ShowInCompactForm()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/showincompactform/), [**PivotTable.ShowInOutlineForm()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/showinoutlineform/) und [**PivotTable.ShowInTabularForm()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/showintabularform/), um das Layout der Pivot-Tabelle in diesen drei Formen zu ändern.

{{% /alert %}}

Der folgende Beispielcode zeigt zunächst die Pivot-Tabelle in **Kompakter Form**, dann in **Gliederungsform**, und schließlich in **Tabellarischer Form**.

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
