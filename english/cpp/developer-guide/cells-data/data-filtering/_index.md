---
title: Data Filtering with C++
linktitle: Data Filtering
type: docs
weight: 85
url: /cpp/data-filtering/
description: Learn how to add a data filter by using the Aspose.Cells for C++ API.
keywords: Add Filter by Color, Add Date Filters, Add Number Filters, Add Dynamic Filter, Add Text Filters, Add custom filter with Contains, Add custom filter with NotContains, Add custom filter with BeginsWith, Add custom filter with EndsWith
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Microsoft Excel provides several useful features to autofilter worksheet data. Aspose.Cells fully supports Microsoft Excel's autofilter features. This article explains how to use the features in Microsoft Excel, and how to code them using Aspose.Cells.

{{% /alert %}}

## **AutoFilter Data**

AutoFiltering is the quickest way to select only those items from the worksheet that you want to display in a list. The AutoFilter feature allows users to filter items in a list according to a set of criteria. Filters can be based on text, numbers, or dates.

### **AutoFilter in Microsoft Excel**

To activate the AutoFilter feature in Microsoft Excel:

1. Click a heading row in a worksheet.  
2. From the **Data** menu, select **Filter** and then **AutoFilter**.

When you apply an AutoFilter to a worksheet, filter switches (black arrows) appear to the right of the column headings.

1. Click a filter arrow to see a list of filter options.

Some of the AutoFilter options are:

|**Options**|**Description**|
| :- | :- |
|All|Show all items in the list once.|
|Custom|Customize filter criteria like contains/not contains|
|Filter by Color|Filters based on filled color|
|Date Filters|Filters rows based on different date criteria|
|Number Filters|Different types of filters on numbers, such as comparisons, averages, and Top 10, etc.|
|Text Filters|Different filters like begins with, ends with, contains, etc.|
|Blanks/Non Blanks|These filters can be implemented through the Text Filter Blank option|

Users manually filter their worksheet data in Microsoft Excel using these options.

### **AutoFilter with Aspose.Cells**

Aspose.Cells provides a class `Workbook` that represents an Excel file. The `Workbook` class contains a `Worksheets` collection that allows access to each worksheet in the Excel file.

A worksheet is represented by the `Worksheet` class. The `Worksheet` class provides a wide range of properties and methods to manage worksheets. To create an AutoFilter, use the `AutoFilter` property of the `Worksheet` class. The `AutoFilter` property is an object of the `AutoFilter` class, which provides the `Range` property for specifying the range of cells that make up a heading row. An AutoFilter is applied to the range of cells that is the heading row.

In each worksheet, you can specify only one filter range. This limitation is imposed by Microsoft Excel. For custom data filtering, use the `AutoFilter.Custom` method.

In the example given below, we have created the same AutoFilter using Aspose.Cells as we created using Microsoft Excel in the above section.

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
    U16String inputFilePath = srcDir + u"book1.xls";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"output.out.xls";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Access the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Create AutoFilter by specifying the cells range of the heading row
    worksheet.GetAutoFilter().SetRange(u"A1:B1");

    // Save the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "AutoFilter applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

#### **Different Types of Filters**

Aspose.Cells provides multiple options to apply different types of filters, such as Color Filter, Date Filter, Number Filter, Text Filter, Blank Filters, and Non‑Blank Filters.

##### **Fill Color**

Aspose.Cells provides a function `AddFillColorFilter` to filter data based upon the fill‑color property of the cells. In the example given below, a template file having different fill colors in the first column of the sheet is used to test the color‑filtering function. Sample files can be downloaded from the following links.

1. [ColouredCells.xlsx](72417315.xlsx)  
2. [FilteredColouredCells.xlsx](72417316.xlsx)

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

    // Instantiating a Workbook object
    Workbook workbook(srcDir + u"ColouredCells.xlsx");

    // Instantiating a CellsColor object for foreground color
    CellsColor clrForeground = workbook.CreateCellsColor();
    clrForeground.SetColor(Color::Red());

    // Instantiating a CellsColor object for background color
    CellsColor clrBackground = workbook.CreateCellsColor();
    clrBackground.SetColor(Color::White());

    // Access the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Apply the fill‑color filter
    worksheet.GetAutoFilter().AddFillColorFilter(0, BackgroundType::Solid, clrForeground, clrBackground);

    // Refresh the worksheet
    worksheet.GetAutoFilter().Refresh();

    // Save the modified Excel file
    workbook.Save(outDir + u"FilteredColouredCells.xlsx");

    std::cout << "Filter applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

##### **Date**

Different types of date filters can be implemented, such as filtering all rows that have dates in January 2018. The following sample code demonstrates this filter using the `AddDateFilter` function. Sample files are given below.

1. [Date.xlsx](72417317.xlsx)  
2. [FilteredDate.xlsx](72417318.xlsx)

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
    U16String inputFilePath = srcDir + u"Date.xlsx";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"FilteredDate.xlsx";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Access the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Apply the date filter (January 2018)
    worksheet.GetAutoFilter().AddDateFilter(0, DateTimeGroupingType::Month, 2018, 1, 0, 0, 0, 0);

    // Refresh the worksheet
    worksheet.GetAutoFilter().Refresh();

    // Save the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "Date filter applied and file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

##### **Dynamic Date**

Sometimes dynamic filters are required based on date, such as all cells having dates in January irrespective of the year. In this case the `DynamicFilter` function is used, as shown in the following sample code. Sample files are given below.

1. [Date.xlsx](72417317.xlsx)  
2. [FilteredDynamicDate.xlsx](72417319.xlsx)

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
    U16String inputFilePath = srcDir + u"Date.xlsx";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"FilteredDynamicDate.xlsx";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Access the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Apply the dynamic date filter (January, any year)
    worksheet.GetAutoFilter().Dynamic_Filter(0, DynamicFilterType::January);

    // Refresh the worksheet
    worksheet.GetAutoFilter().Refresh();

    // Save the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "Dynamic filter applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

##### **Number**

Custom filters can be applied using Aspose.Cells, such as selecting cells that have numbers between a given range. The following example demonstrates the usage of the `Custom()` function to filter numbers. Sample files are given below.

1. [Number.xlsx](72417320.xlsx)  
2. [FilteredNumber.xlsx](72417321.xlsx)

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
    U16String inputFilePath = srcDir + u"Number.xlsx";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"FilteredNumber.xlsx";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Access the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Apply the custom number filter (5 ≤ value ≤ 10)
    worksheet.GetAutoFilter().Custom(0, FilterOperatorType::GreaterOrEqual, 5, true, FilterOperatorType::LessOrEqual, 10);

    // Refresh the worksheet
    worksheet.GetAutoFilter().Refresh();

    // Save the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "Filter applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

##### **Text**

If a column contains text and you want to select cells containing particular text, the `Filter()` function can be used. In the following example, the template file contains a list of countries, and rows are selected that contain a particular country name. Sample files are given below.

1. [Text.xlsx](72417322.xlsx)  
2. [FilteredText.xlsx](72417323.xlsx)

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
    U16String inputFilePath = srcDir + u"Text.xlsx";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"FilteredText.xlsx";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Access the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Apply the text filter (e.g., "Angola")
    worksheet.GetAutoFilter().Filter(0, u"Angola");

    // Refresh the worksheet
    worksheet.GetAutoFilter().Refresh();

    // Save the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "Filter applied and file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

##### **Blanks**

If a column contains text but some cells are blank, and you need to filter to select only rows where the cells are blank, the `MatchBlanks()` function can be used as demonstrated below. Sample files are given below.

1. [Blank.xlsx](72417324.xlsx)  
2. [FilteredBlank.xlsx](72417325.xlsx)

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

    // Instantiating a Workbook object
    Workbook workbook(srcDir + u"Blank.xlsx");

    // Access the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Apply the blanks filter
    worksheet.GetAutoFilter().MatchBlanks(0);

    // Refresh the worksheet
    worksheet.GetAutoFilter().Refresh();

    // Save the modified Excel file
    workbook.Save(outDir + u"FilteredBlank.xlsx");

    std::cout << "Filter applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

##### **Non‑Blank**

When cells containing any text are to be filtered, use the `MatchNonBlanks()` filter function as demonstrated below. Sample files are given below.

1. [Blank.xlsx](72417324.xlsx)  
2. [FilteredNonBlank.xlsx](72417326.xlsx)

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

    // Create workbook object and open the Excel file
    Workbook workbook(srcDir + u"Blank.xlsx");

    // Access the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Apply the non‑blank filter
    worksheet.GetAutoFilter().MatchNonBlanks(0);

    // Refresh the worksheet
    worksheet.GetAutoFilter().Refresh();

    // Save the modified Excel file
    workbook.Save(outDir + u"FilteredNonBlank.xlsx");

    std::cout << "Non‑blank filter applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

##### **Custom filter with Contains**

Excel provides custom filters, such as filtering rows that contain a specific string. This feature is available in Aspose.Cells and is demonstrated below by filtering the names in the sample file. Sample files are given below.

1. [sourceSampleCountryNames.xlsx](sourceSampleCountryNames.xlsx)  
2. [outSourceSampleCountryNames.xlsx](outSourceSampleCountryNames.xlsx)

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
    U16String inputFilePath = srcDir + u"sourceSampleCountryNames.xlsx";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"outSourceSampleCountryNames.xlsx";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Access the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Set the range for AutoFilter
    worksheet.GetAutoFilter().SetRange(u"A1:A18");

    // Apply custom filter for rows containing the string "Ba"
    worksheet.GetAutoFilter().Custom(0, FilterOperatorType::Contains, u"Ba");

    // Refresh the filter to show/hide filtered rows
    worksheet.GetAutoFilter().Refresh();

    // Save the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "AutoFilter applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

##### **Custom filter with NotContains**

Excel provides custom filters, such as filtering rows that do **not** contain a specific string. This feature is available in Aspose.Cells and is demonstrated below by filtering the names in the sample file. Sample file is given below.

1. [sourceSampleCountryNames.xlsx](sourceSampleCountryNames.xlsx)

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
    U16String inputFilePath = srcDir + u"sourceSampleCountryNames.xlsx";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"outSourceSampleCountryNames.xlsx";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Access the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Set the range for AutoFilter
    worksheet.GetAutoFilter().SetRange(u"A1:A18");

    // Apply custom filter for rows not containing the string "Be"
    worksheet.GetAutoFilter().Custom(0, FilterOperatorType::NotContains, u"Be");

    // Refresh the filter to show/hide filtered rows
    worksheet.GetAutoFilter().Refresh();

    // Save the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "File filtered and saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

##### **Custom filter with BeginsWith**

Excel provides custom filters, such as filtering rows that begin with a specific string. This feature is available in Aspose.Cells and is demonstrated below by filtering the names in the sample file. Sample file is given below.

1. [sourceSampleCountryNames.xlsx](sourceSampleCountryNames.xlsx)

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
    U16String inputFilePath = srcDir + u"sourceSampleCountryNames.xlsx";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"outSourceSampleCountryNames.xlsx";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Access the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Set the range for AutoFilter
    worksheet.GetAutoFilter().SetRange(u"A1:A18");

    // Apply custom filter for rows beginning with the string "Ba"
    worksheet.GetAutoFilter().Custom(0, FilterOperatorType::BeginsWith, u"Ba");

    // Refresh the filter to show/hide filtered rows
    worksheet.GetAutoFilter().Refresh();

    // Save the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "File saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

##### **Custom filter with EndsWith**

Excel provides custom filters, such as filtering rows that end with a specific string. This feature is available in Aspose.Cells and is demonstrated below by filtering the names in the sample file. Sample file is given below.

1. [sourceSampleCountryNames.xlsx](sourceSampleCountryNames.xlsx)

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
    U16String inputFilePath = srcDir + u"sourceSampleCountryNames.xlsx";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"outSourceSampleCountryNames.xlsx";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Access the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Set the range for AutoFilter
    worksheet.GetAutoFilter().SetRange(u"A1:A18");

    // Apply custom filter for rows ending with the string "ia"
    worksheet.GetAutoFilter().Custom(0, FilterOperatorType::EndsWith, u"ia");

    // Refresh the filter to show/hide filtered rows
    worksheet.GetAutoFilter().Refresh();

    // Save the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "File saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Advanced Topics**
- [Apply Advanced Filter of Microsoft Excel to Display Records Meeting Complex Criteria](/cells/cpp/apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria/)
- [Get All Hidden Rows Indices after Refreshing AutoFilter](/cells/cpp/get-all-hidden-rows-indices-after-refreshing-autofilter/)
{{< app/cells/assistant language="cpp" >}}
