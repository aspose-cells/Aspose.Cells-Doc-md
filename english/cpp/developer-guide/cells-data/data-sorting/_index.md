---
title: Data Sorting with C++
linktitle: Data Sorting
type: docs
weight: 130
url: /cpp/sort-data-of-excel/
description: Learn how to sort data by using the Aspose.Cells for C++ API.
keywords: Sort data in ascending or descending order, Sort data based on the background color
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Data sorting is one of Microsoft Excel's many useful features. It allows users to order data to make it easier to scan. Aspose.Cells lets developers sort worksheet data alphabetically or numerically which works in the same way as Microsoft Excel does to sort data.

{{% /alert %}}

## **Sorting Data in Microsoft Excel**

To sort data in Microsoft Excel:

1. Select **Data** from the **Sort** menu. The Sort dialog will be displayed.
1. Select a sorting option.

Generally, sorting is performed on a list - defined as a contiguous group of data where the data is displayed in columns.

## **Sorting Data with Aspose.Cells**

Aspose.Cells provides the [**DataSorter**](https://reference.aspose.com/cells/cpp/aspose.cells/datasorter/) class used to sort data in ascending or descending order. The class has some important members, for example, properties like Key1 ... Key3 and Order1 ... Order3. These members are used to define sorted keys and specify the key sort order.

You have to define keys and set the sort order before implementing data sorting. The class provides the [**Sort**](https://reference.aspose.com/cells/cpp/aspose.cells/datasorter/sort/) method used to perform data sorting based on the cell data in a worksheet.

The [**Sort**](https://reference.aspose.com/cells/cpp/aspose.cells/datasorter/sort/) method accepts the following parameters:

- [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/), the cells for the underlying worksheet.
- [**CellArea**](https://reference.aspose.com/cells/cpp/aspose.cells/cellarea/), the range of cells. Define the cell area before applying data sorting.

This example uses the template file "Book1.xls" created in Microsoft Excel. After executing the code below, data is sorted appropriately.

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

    // Path of input excel file
    U16String inputFilePath = srcDir + u"book1.xls";

    // Path of output excel file
    U16String outputFilePath = outDir + u"output.out.xls";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Get the workbook datasorter object
    DataSorter sorter = workbook.GetDataSorter();

    // Set the first order for datasorter object
    sorter.SetOrder1(SortOrder::Descending);

    // Define the first key
    sorter.SetKey1(0);

    // Set the second order for datasorter object
    sorter.SetOrder2(SortOrder::Ascending);

    // Define the second key
    sorter.SetKey2(1);

    // Create a cells area (range)
    CellArea ca = CellArea::CreateCellArea(0, 0, 13, 1);

    // Sort data in the specified data range (A1:B14)
    sorter.Sort(workbook.GetWorksheets().Get(0).GetCells(), ca);

    // Save the excel file
    workbook.Save(outputFilePath);

    std::cout << "Data sorted successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}}

If you want to sort *LeftToRight*, use the [**DataSorter.GetSortLeftToRight()**](https://reference.aspose.com/cells/cpp/aspose.cells/datasorter/getsortlefttoright/) attribute.

{{% /alert %}}

### **Sorting data with background color**

Excel provides features to sort data based on the background color. The same feature is provided using Aspose.Cells using DataSorter where [**SortOnType**](https://reference.aspose.com/cells/cpp/aspose.cells/sortontype/).CellColor can be used in [**AddKey()**](https://reference.aspose.com/cells/cpp/aspose.cells/datasorter/addkey/) to sort data based on the background color. All the cells which contain specified color in the [**AddKey()**](https://reference.aspose.com/cells/cpp/aspose.cells/datasorter/addkey/), function are placed on top or bottom according to the SortOrder setting and order of the rest of the cells is not changed at all.

Following are the sample files which can be downloaded for testing this feature:

[sampleBackGroundFile.xlsx](81920906.xlsx)

[outputsampleBackGroundFile.xlsx](81920907.xlsx)

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
    U16String inputFilePath = srcDir + u"CellsNet46500.xlsx";

    // Path of output excel file
    U16String outputFilePath = outDir + u"outputSortData_CustomSortList.xlsx";

    // Create a workbook object and load template file
    Workbook workbook(inputFilePath);

    // Instantiate data sorter object
    DataSorter sorter = workbook.GetDataSorter();

    // Add key for second column for red color
    sorter.AddColorKey(1, SortOnType::CellColor, SortOrder::Descending, Color::Red());

    // Sort the data based on the key
    sorter.Sort(workbook.GetWorksheets().Get(0).GetCells(), CellArea::CreateCellArea(u"A2", u"C6"));

    // Save the output file
    workbook.Save(outputFilePath);

    std::cout << "Data sorted successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Advance topics**
- [Sort Data in Column with Custom Sort List](/cells/cpp/sort-data-in-column-with-custom-sort-list/)
- [Specifying Sort Warning While Sorting Data](/cells/cpp/specifying-sort-warning-while-sorting-data/)
{{< app/cells/assistant language="cpp" >}}
