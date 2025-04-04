---
title: How to Filter Blanks or Non-Blanks with C++
linktitle: How to Filter Blanks or Non-Blanks
type: docs
weight: 85
url: /cpp/how-to-filter-blanks-and-non-blanks/
description: Learn how to filter Blanks and non-blanks by using the Aspose.Cells for C++ API.
keywords: Filter Blanks, Filter Non-Blanks, Filter Blanks in worksheet, Filter Non-Blanks in worksheet, Filter Blanks in excel, Filter Non-Blanks in excel, Filter Blanks and Non-Blanks in excel
---

## **Possible Usage Scenarios**
Filtering data in Excel is a valuable tool that enhances data analysis, exploration, and presentation by enabling users to focus on specific subsets of data based on their criteria, making the overall data manipulation and interpretation process more efficient and effective.

## **How to Filter Blanks or Non-Blanks in Excel**
In Excel, you can easily filter blanks or non-blanks using the filtering options. Here's how you can do it:

### **How to Filter Blanks in Excel**
1. Select the Range: Click on the letter of the column header to select the entire column or select the range where you want to filter blanks.
1. Open the Filter Menu: Go to the "Data" tab in the ribbon.
<br>
<image src="1.png" width="70%" />
1. Filter Options: Click on the "Filter" button. This will add filter arrows to the selected range.
1. Filter Blanks: Click on the filter arrow in the column you want to filter blanks. Unselect all options except "Blanks" and click OK. This will display only the blank cells in that column.
<br>
<image src="2.png" width="70%" />
1. The result as follows:
<br>
<image src="3.png" width="70%" />

### **How to Filter Non-Blanks in Excel**
1. Select the Range: Click on the letter of the column header to select the entire column or select the range where you want to filter non-blanks.
1. Open the Filter Menu: Go to the "Data" tab in the ribbon.
<br>
<image src="1.png" width="70%" />
1. Filter Options: Click on the "Filter" button. This will add filter arrows to the selected range.
1. Filter Non-Blanks: Click on the filter arrow in the column you want to filter non-blanks. Unselect all options except "Non-blanks" or "Custom" and set the conditions accordingly. Click OK. This will display only the cells that are not blank in that column.
<br>
<image src="4.png" width="70%" />
1. The result as follows:
<br>
<image src="5.png" width="70%" />

## **How to Filter Blanks using Aspose.Cells**
If a column contains text such that few cells are blank, and filter is required to select those rows only where blank cells are present, [AutoFilter.MatchBlanks(int fieldIndex)](https://reference.aspose.com/cells/cpp/aspose.cells/autofilter/matchblanks/) and [AutoFilter.AddFilter(int fieldIndex, string criteria)](https://reference.aspose.com/cells/cpp/aspose.cells/autofilter/addfilter/) functions can be used as demonstrated below. 

Please see the following sample code that loads the [sample Excel file](sample.xlsx) which contains some dummy data. The sample code uses three methods to filter blanks. It then saves the workbook as [output Excel file](FilteredBlanks.xlsx). 

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Open the Excel file
    Workbook workbook(u"sample.xlsx");

    // Access the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Method 1: Call MatchBlanks function to apply the filter
    // worksheet.GetAutoFilter().MatchBlanks(1);

    // Method 2: Call AddFilter function and set criteria to ""
    // worksheet.GetAutoFilter().AddFilter(1, u"");

    // Method 3: Call AddFilter function and set criteria to nullptr
    worksheet.GetAutoFilter().AddFilter(1, nullptr);

    // Call refresh function to update the worksheet
    worksheet.GetAutoFilter().Refresh();

    // Saving the modified Excel file
    workbook.Save(u"FilteredBlanks.xlsx");

    std::cout << "Excel file modified and saved successfully!" << std::endl;
    
    Aspose::Cells::Cleanup();
}
```

## **How to Filter Non-Blanks using Aspose.Cells**

Please see the following sample code that loads the [sample Excel file](sample.xlsx) which contains some dummy data. After loading the file, call the [AutoFilter.MatchNonBlanks(int fieldIndex)](https://reference.aspose.com/cells/cpp/aspose.cells/autofilter/matchnonblanks/) function to filter non-blanks data, and finally save the workbook as [output Excel file](FilteredNonBlanks.xlsx). 

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a workbook by opening an existing Excel file
    Workbook workbook(u"sample.xlsx");

    // Access the first worksheet in the workbook
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Call MatchNonBlanks function to apply the filter on the second column (index 1)
    worksheet.GetAutoFilter().MatchNonBlanks(1);

    // Call refresh function to update the worksheet
    worksheet.GetAutoFilter().Refresh();

    // Save the modified Excel file
    workbook.Save(u"FilteredNonBlanks.xlsx");

    std::cout << "Filtered non-blanks saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```


