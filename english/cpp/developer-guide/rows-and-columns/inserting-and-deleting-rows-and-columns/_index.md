---
title: Inserting and Deleting Rows and Columns of an Excel File with C++
linktitle: Inserting and Deleting Rows and Columns
type: docs
weight: 70
url: /cpp/inserting-and-deleting-rows-and-columns/
description: This article shows how to insert and delete rows and columns using the Aspose.Cells for C++ API.
keywords: Aspose.Cells C++ manage rows and columns, insert rows and columns, delete rows and columns
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Introduction**

Whether creating a new worksheet from scratch or working on an existing worksheet, we may need to add extra rows or columns to accommodate more data. Conversely, we may also need to delete rows or columns from specified positions in the worksheet.  
To fulfill these requirements, Aspose.Cells provides a very simple set of classes and methods, discussed below.

### **Manage Rows and Columns**

Aspose.Cells provides a class [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) that represents a Microsoft Excel file. The [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) class contains a [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) collection that allows access to each worksheet in an Excel file. A worksheet is represented by the [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) class. The [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) class provides a **GetCells()** collection that represents all cells in the worksheet.

The **GetCells()** collection provides several methods for managing rows and columns in a worksheet. Some of these are discussed below.

{{% alert color="primary" %}}

When rows or columns are added, the content in the worksheet is shifted down or to the right, and if rows or columns are removed, the content is shifted up or to the left.

{{% /alert %}}

## **Insert Rows and Columns**

### **How to Insert a Row**

Insert a row into the worksheet at any location by calling the **InsertRow** method of the **GetCells()** collection. The **InsertRow** method takes the index of the row where the new row will be inserted.

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

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"book1.xls";

    // Instantiating a Workbook object
    Workbook workbook(inputFilePath);

    // Accessing the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Inserting a row into the worksheet at the 3rd position
    worksheet.GetCells().InsertRow(2);

    // Path of output Excel file
    U16String outputFilePath = outDir + u"output.out.xls";

    // Saving the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "Row inserted successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **How to Insert Multiple Rows**

To insert multiple rows into a worksheet, call the **InsertRows** method of the **GetCells()** collection. The **InsertRows** method takes two parameters:

- **Row index** – the index of the row from where the new rows will be inserted.  
- **Number of rows** – the total number of rows that need to be inserted.

```c++
#include <iostream>
#include <fstream>
#include <memory>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"book1.xls";

    // Create workbook from file
    Workbook workbook(inputFilePath);

    // Access the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Insert 10 rows into the worksheet starting from the 3rd row
    worksheet.GetCells().InsertRows(2, 10);

    // Path of output Excel file
    U16String outputFilePath = srcDir + u"output.out.xls";

    // Save the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "Rows inserted successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

### **How to Insert a Row with Formatting**

To insert a row with formatting options, use the **InsertRows** overload that takes **InsertOptions** as a parameter. Set the **CopyFormatType** property of the **InsertOptions** class using the **CopyFormatType** enumeration. The **CopyFormatType** enumeration has three members as listed below.

- **SameAsAbove** – Formats the row the same as the row above.  
- **SameAsBelow** – Formats the row the same as the row below.  
- **Clear** – Clears the formatting.

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

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"book1.xls";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"InsertingARowWithFormatting_out.xls";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Access the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Setting formatting options
    InsertOptions insertOptions;
    insertOptions.SetCopyFormatType(CopyFormatType::SameAsAbove);

    // Inserting a row into the worksheet at the 3rd position
    worksheet.GetCells().InsertRows(2, 1, insertOptions);

    // Save the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "Row inserted successfully with formatting!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **How to Insert a Column**

You can also insert a column into the worksheet at any location by calling the **InsertColumn** method of the **GetCells()** collection. The **InsertColumn** method takes the index of the column where the new column will be inserted.

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

    // Create workbook from the input file
    Workbook workbook(inputFilePath);

    // Access the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Insert a column into the worksheet at the 2nd position
    worksheet.GetCells().InsertColumn(1);

    // Save the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "Column inserted successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Delete Rows and Columns**

### **How to Delete Multiple Rows**

To delete multiple rows from a worksheet, call the **DeleteRows** method of the **GetCells()** collection. The **DeleteRows** method takes two parameters:

- **Row index** – the index of the row from where the rows will be deleted.  
- **Number of rows** – the total number of rows that need to be deleted.

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

    // Create workbook from the input file
    Workbook workbook(inputFilePath);

    // Access the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Delete 10 rows from the worksheet starting from the 3rd row
    worksheet.GetCells().DeleteRows(2, 10);

    // Save the modified Excel file
    U16String outputFilePath = srcDir + u"output.xlsx";
    workbook.Save(outputFilePath);

    std::cout << "Rows deleted successfully and file saved!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **How to Delete a Column**

To delete a column from the worksheet at any location, call the **DeleteColumn** method of the **GetCells()** collection. The **DeleteColumn** method takes the index of the column to delete.

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

    // Create workbook from file
    Workbook workbook(inputFilePath);

    // Access the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Delete a column from the worksheet at the 5th position (index 4)
    worksheet.GetCells().DeleteColumn(4);

    // Save the modified Excel file
    U16String outputFilePath = srcDir + u"output.xlsx";
    workbook.Save(outputFilePath);

    std::cout << "Column deleted successfully and file saved!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
