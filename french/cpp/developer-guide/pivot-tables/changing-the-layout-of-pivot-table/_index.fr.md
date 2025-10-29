---
title: Changer la disposition du tableau croisé dynamique avec C++
linktitle: Modifier la disposition du tableau croisé dynamique
type: docs
weight: 10
url: /fr/cpp/changing-the-layout-of-pivot-table/
description: Apprenez comment changer la disposition d’un tableau croisé dynamique en formats Compact, Outline et Tabular en utilisant Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Microsoft Excel permet de changer la disposition du tableau croisé dynamique en utilisant les commandes *PivotTable Tools > Design > Report Layout*. Vous pouvez modifier la disposition dans ces trois formats :

- Afficher sous forme compacte
- Afficher sous forme de plan
- Afficher sous forme tabulaire

Aspose.Cells fournit également [**PivotTable.ShowInCompactForm()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/showincompactform/), [**PivotTable.ShowInOutlineForm()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/showinoutlineform/), et [**PivotTable.ShowInTabularForm()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/showintabularform/) méthodes pour changer la disposition du tableau croisé dynamique dans ces trois formats.

{{% /alert %}}

Le code d'exemple suivant montre d’abord le tableau croisé dynamique en **Forme compacte**, puis en **Forme Outline**, et enfin en **Forme tabulaire**.

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
{{< app/cells/assistant language="cpp" >}}
