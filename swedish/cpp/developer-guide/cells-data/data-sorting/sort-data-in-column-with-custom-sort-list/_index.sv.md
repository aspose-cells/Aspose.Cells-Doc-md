---
title: Sortera data i kolumn med anpassad sorteringslista med C++
linktitle: Sortera data i kolumn med anpassad sorteringslista
type: docs
weight: 290
url: /sv/cpp/sort-data-in-column-with-custom-sort-list/
description: Lär dig hur du sorterar data i en kolumn med en anpassad lista med API et Aspose.Cells for C++.
keywords: Sortera Data i Kolumn med Anpassad Sorteringslista, Sortera data med anpassad lista.
---

## **Möjliga användningsscenario**

Du kan sortera data i en kolumn med en anpassad lista. Detta kan göras med [**DataSorter::AddKey(int key, SortOrder order, String customList)**](https://reference.aspose.com/cells/cpp/aspose.cells/datasorter/addkey/)-metoden. Men, denna metod fungerar endast om objekten i den anpassade listan inte innehåller kommatecken. Om de har kommatecken som "USA,US", "China,CN" etc., måste du använda [**DataSorter::AddKey Method (Int32, SortOrder, String[])**](https://reference.aspose.com/cells/cpp/aspose.cells/datasorter/addkey/)-metoden. Här är det sista parametern inte en String, utan en array av strängar.

## **Sortera Data i Kolumn med Anpassad Sorteringslista**

Följande exempel på kod förklarar hur man använder [**DataSorter::AddKey Method (Int32, SortOrder, String[])**](https://reference.aspose.com/cells/cpp/aspose.cells/datasorter/addkey/)-metoden för att sortera data med en anpassad sorteringslista. Se [exempel-Excel fil](50528327.xlsx) som används i denna kod och [utdata Excel-fil](50528328.xlsx) som genereras av den. Följande skärmbild visar effekten av koden på exempel-Excel-filen vid körning.

![todo:image_alt_text](sort-data-in-column-with-custom-sort-list_1.png)

## **Exempelkod**

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

    // Load the source Excel file
    Workbook wb(srcDir + u"sampleSortData_CustomSortList.xlsx");

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Specify cell area - sort from A1 to A40
    CellArea ca = CellArea::CreateCellArea(u"A1", u"A40");

    // Create Custom Sort list
    Vector<U16String> customSortList = { u"USA,US", u"Brazil,BR", u"China,CN", u"Russia,RU", u"Canada,CA" };

    // Add Key for Column A, Sort it in Ascending Order with Custom Sort List
    wb.GetDataSorter().AddKey(0, SortOrder::Ascending, customSortList);
    wb.GetDataSorter().Sort(ws.GetCells(), ca);

    // Save the output Excel file
    wb.Save(outDir + u"outputSortData_CustomSortList.xlsx");

    std::cout << "Data sorted successfully with custom sort list!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
