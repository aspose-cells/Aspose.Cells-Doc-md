---
title: Show and Hide Rows, Columns, and Scroll Bars with C++
linktitle: Show and Hide Rows, Columns, and Scroll Bars
type: docs
weight: 20
url: /cpp/show-and-hide-rows-columns-and-scroll-bars/
description: This article demonstrates how to programmatically display and hide Excel worksheet rows and columns using the C++ language and the Aspose.Cells API. The visibility of scroll bars can be adjusted, and several rows and columns can be hidden.
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells provides ways to control the visibility of rows, columns, and scroll bars of a worksheet.

{{% /alert %}}

## **Show and Hide Rows and Columns**

Aspose.Cells provides a class, [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/), that represents a Microsoft Excel file. The [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) class contains a [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) collection that allows developers to access each worksheet in the Excel file. A worksheet is represented by the [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) class. The [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) class provides a [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) collection that represents all cells in the worksheet. The [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) collection provides several methods for managing rows or columns in a worksheet. A few of these are discussed below.

### **Show Rows and Columns**

Developers can show any hidden row or column by calling the [**UnhideRow**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/unhiderow/) and [**UnhideColumn**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/unhidecolumn/) methods of the [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) collection respectively. Both methods take two parameters:

- **Row or column index** – the index of a row or column that is used to show the specific row or column.  
- **Row height or column width** – the row height or column width assigned to the row or column after unhiding.

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
    U16String outputFilePath = outDir + u"output.xls";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Accessing the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Unhiding the 3rd row and setting its height to 13.5
    worksheet.GetCells().UnhideRow(2, 13.5);

    // Unhiding the 2nd column and setting its width to 8.5
    worksheet.GetCells().UnhideColumn(1, 8.5);

    // Save the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "Excel file modified and saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}}

While making a hidden column visible, if you need to restore it to its previously assigned width or to its original width, you should unhide the column with a negative width. For example: `worksheet.GetCells().UnhideColumn(5, -1)`.

{{% /alert %}}

### **Hide Rows and Columns**

Developers can hide a row or column by calling the [**HideRow**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/hiderow/) and [**HideColumn**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/hidecolumn/) methods of the [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) collection respectively. Both methods take the row or column index as a parameter to hide the specific row or column.

```cpp
#include <iostream>
#include <memory>
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

    // Hide the 3rd row of the worksheet
    worksheet.GetCells().HideRow(2);

    // Hide the 2nd column of the worksheet
    worksheet.GetCells().HideColumn(1);

    // Save the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "Rows and columns hidden successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}}

It is also possible to hide a row or column by setting the row height or column width to 0, respectively.

{{% /alert %}}

### **Hide Multiple Rows and Columns**

Developers can hide multiple rows or columns at once by calling the [**HideRows**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/hiderows/) and [**HideColumns**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/hidecolumns/) methods of the [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) collection respectively. Both methods take the starting row or column index and the number of rows or columns that should be hidden as parameters.

```cpp
#include <iostream>
#include <memory>
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

    // Create workbook
    Workbook workbook(inputFilePath);

    // Access the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Hide rows 3, 4, and 5 in the worksheet
    worksheet.GetCells().HideRows(2, 3);

    // Hide columns 2 and 3 in the worksheet
    worksheet.GetCells().HideColumns(1, 2);

    // Save the modified Excel file
    workbook.Save(outDir + u"output.xls");

    std::cout << "Rows and columns hidden successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Show and Hide Scroll Bars**

Scroll bars are used to navigate the contents of a worksheet. Normally, there are two kinds of scroll bars:

- Vertical scroll bars  
- Horizontal scroll bars

Microsoft Excel provides both horizontal and vertical scroll bars so that users can scroll through worksheet contents. Using Aspose.Cells, developers can control the visibility of both types of scroll bars in Excel files.

### **Controlling the Visibility of Scroll Bars**

Aspose.Cells provides a class, [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/), that represents an Excel file. The [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) class provides a wide range of properties and methods for managing an Excel file. To control the visibility of scroll bars, use the [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) class's [**WorkbookSettings.IsVScrollBarVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/isvscrollbarvisible/) and [**WorkbookSettings.IsHScrollBarVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/ishscrollbarvisible/) properties. Both are Boolean properties, which means they can store only **true** or **false** values.

#### **Making Scroll Bars Visible**

Make scroll bars visible by setting the [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) class's [**WorkbookSettings.IsVScrollBarVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/isvscrollbarvisible/) or [**WorkbookSettings.IsHScrollBarVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/ishscrollbarvisible/) property to **true**.

#### **Hiding Scroll Bars**

Hide scroll bars by setting the [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) class's [**WorkbookSettings.IsVScrollBarVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/isvscrollbarvisible/) or [**WorkbookSettings.IsHScrollBarVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/ishscrollbarvisible/) property to **false**.

**Sample Code**

Below is a complete code example that opens an Excel file (`book1.xls`), hides both scroll bars, and then saves the modified file as `output.xls`.

```cpp
#include <iostream>
#include <fstream>
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
    U16String outputFilePath = outDir + u"output.xls";

    // Create workbook from the input file
    Workbook workbook(inputFilePath);

    // Hide the vertical scroll bar of the workbook
    workbook.GetSettings().SetIsVScrollBarVisible(false);

    // Hide the horizontal scroll bar of the workbook
    workbook.GetSettings().SetIsHScrollBarVisible(false);

    // Save the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "Scroll bars hidden successfully and file saved!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
