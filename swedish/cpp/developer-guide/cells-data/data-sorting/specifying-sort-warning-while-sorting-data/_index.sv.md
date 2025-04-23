---
title: Specifikation av sortvarning vid sortering av data med C++
linktitle: Specificera sorteringsvarning vid sortering av data
type: docs
weight: 140
url: /sv/cpp/specifying-sort-warning-while-sorting-data/
description: Lär dig hur du anger sortvarning vid sortering av data med API et Aspose.Cells for C++.
keywords: Lägg till sorteringsvarning vid sortering av data, ställ in sorteringsvarning vid sortering av data, välj sorteringsvarning vid sortering av data.
---

## **Möjliga användningsscenario**

Överväg denna textdata dvs. {11, 111, 22}. Denna textdata sorteras eftersom, i termer av text, kommer 111 före 22. Men om du vill sortera denna data inte som text utan som nummer, kommer det att bli {11, 22, 111} eftersom 111 numeriskt kommer efter 22. Aspose.Cells tillhandahåller {0} egenskapen för att hantera detta problem. Ställ in denna egenskap **true** och din textdata kommer att sorteras som numerisk data. Följande skärmdump visar sorteringsvarningen som visas av Microsoft Excel när textdata som ser ut som numerisk data sorteras.

![todo:image_alt_text](specifying-sort-warning-while-sorting-data_1.png)

## **Exempelkod**

Den följande exemplarkoden illustrerar användningen av [**DataSorter.GetSortAsNumber()**](https://reference.aspose.com/cells/cpp/aspose.cells/datasorter/getsortasnumber/)-egenskapen enligt tidigare förklaring. Kontrollera dess [exempelfil för Excel](43352075.xlsx) och [utdatafil för Excel](43352076.xlsx) för mer hjälp.

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
