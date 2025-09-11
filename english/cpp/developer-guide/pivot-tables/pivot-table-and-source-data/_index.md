---
title: Pivot Table and Source Data with C++
linktitle: Pivot Table and Source Data
type: docs
weight: 30
url: /cpp/pivot-table-and-source-data/
description: Learn how to dynamically change a pivot table's source data using Aspose.Cells with C++.
---

## **Pivot Table's Source Data**

There are times when you want to create Microsoft Excel reports with pivot tables that take data from different data sources (such as a database) that are not known at design time. This article provides an approach to dynamically change a pivot table's data source.

### **Changing a Pivot Table's Source Data**

1. Creating a new designer template.
   1. Create a new designer template file as in the screenshot below.
   1. Then define a named range, **DataSource**, which refers to this range of cells.

      **Creating a designer template & defining a named range, DataSource** 

![todo:image_alt_text](pivot-table-and-source-data_1.png)
   
1. Creating a Pivot Table Based on this named range.
   1. In Microsoft Excel, choose **Data**, then **PivotTable** and **PivotChart Report**.
   1. Create a pivot table based on the named range created in the first step.

      **Creating a pivot table based on the named range, DataSource** 

![todo:image_alt_text](pivot-table-and-source-data_2.png)

   
   1. Drag the corresponding field to pivot table row and column, then create the resulting pivot table as in the screenshot below.

   **Creating a pivot table based on a corresponding field** 

![todo:image_alt_text](pivot-table-and-source-data_3.png)

   
1. Right-click the pivot table and select **Table Options**.
   1. Check **Refresh on open** in **Data options** settings.

      **Setting the pivot table options** 

![todo:image_alt_text](pivot-table-and-source-data_4.png)


Now, you can save this file as your designer template file.

1. Populating new data and changing source data of a pivot table.
   1. Once the designer template is created, use the following code to change the source data of the pivot table.

Executing the example code below changes the source data of the pivot table.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"Book1.xlsx";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Accessing the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Populating new data to the worksheet cells
    worksheet.GetCells().Get(u"A9").PutValue(u"Golf");
    worksheet.GetCells().Get(u"B9").PutValue(u"Qtr4");
    worksheet.GetCells().Get(u"C9").PutValue(7000);

    // Changing named range "DataSource"
    Range range = worksheet.GetCells().CreateRange(0, 0, 9, 3);
    range.SetName(u"DataSource");

    // Saving the modified Excel file
    U16String outputFilePath = srcDir + u"output.xls";
    workbook.Save(outputFilePath);

    Aspose::Cells::Cleanup();

    std::cout << "File saved successfully!" << std::endl;

    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}