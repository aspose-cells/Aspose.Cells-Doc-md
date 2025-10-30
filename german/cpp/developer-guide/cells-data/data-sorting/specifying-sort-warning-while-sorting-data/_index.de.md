---
title: Angabe von Sortierwarnungen beim Sortieren von Daten mit C++
linktitle: Angabe von Sortierwarnungen beim Sortieren von Daten.
type: docs
weight: 140
url: /de/cpp/specifying-sort-warning-while-sorting-data/
description: Erfahren Sie, wie Sie beim Sortieren von Daten mithilfe der API Aspose.Cells for C++ Warnungen bei der Sortierung angeben.
keywords: Sortierwarnung hinzufügen beim Sortieren von Daten, Sortierwarnung beim Sortieren von Daten festlegen, Sortierwarnung beim Sortieren von Daten auswählen.
---

## **Mögliche Verwendungsszenarien**

Bitte beachten Sie diese Textdaten, d.h. {11, 111, 22}. Diese Textdaten werden sortiert, weil hinsichtlich des Textes 111 vor 22 kommt. Wenn Sie jedoch diese Daten nicht als Text, sondern als Zahlen sortieren möchten, werden sie zu {11, 22, 111}, da numerisch 111 nach 22 kommt. Aspose.Cells bietet die {0}-Eigenschaft, um dieses Problem zu beheben. Bitte setzen Sie diese Eigenschaft auf **true** und Ihre Textdaten werden als numerische Daten sortiert. Der folgende Screenshot zeigt die Sortierwarnung, die von Microsoft Excel angezeigt wird, wenn Textdaten, die wie numerische Daten aussehen, sortiert werden.

![todo:image_alt_text](specifying-sort-warning-while-sorting-data_1.png)

## **Beispielcode**

Der folgende Beispielscode veranschaulicht die Verwendung der [**DataSorter.GetSortAsNumber()**](https://reference.aspose.com/cells/cpp/aspose.cells/datasorter/getsortasnumber/)-Eigenschaft wie zuvor erläutert. Bitte überprüfen Sie die [Beispieldatei Excel](43352075.xlsx) und die [Ausgabedatei Excel](43352076.xlsx) für mehr Hilfe.

```c++
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

    // Create workbook
    Workbook workbook(srcDir + u"sampleSortAsNumber.xlsx");

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Create cell area
    CellArea ca = CellArea::CreateCellArea(u"A1", u"A20");

    // Create data sorter
    DataSorter sorter = workbook.GetDataSorter();

    // Find the index of column A
    int idx = CellsHelper::ColumnNameToIndex(u"A");

    // Add key in sorter for sorting in ascending order
    sorter.AddKey(idx, SortOrder::Ascending);
    sorter.SetSortAsNumber(true);

    // Perform sort
    sorter.Sort(worksheet.GetCells(), ca);

    // Save the output workbook
    workbook.Save(outDir + u"outputSortAsNumber.xlsx");

    std::cout << "Sorting completed successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
