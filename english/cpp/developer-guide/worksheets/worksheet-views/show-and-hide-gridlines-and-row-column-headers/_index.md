---
title: Show and Hide Gridlines and Row Column Headers with C++
linktitle: Show and Hide Gridlines and Row Column Headers
type: docs
weight: 30
url: /cpp/show-and-hide-gridlines-and-row-column-headers/
description: This article provides sample code for using the C++ API or Library to programmatically hide or show gridlines, row and column headers of an Excel worksheet.
---

{{% alert color="primary" %}}

Aspose.Cells supports hiding and showing Gridlines of the worksheet which are visible by default. It also provides controlling visibility of Row Column Headers of the worksheet.

{{% /alert %}}

## **Show and Hide Gridlines**

All Excel worksheets have gridlines by default. They help delineate cells so that it is easy to enter data into particular cells. Gridlines enable us to view a worksheet as a collection of cells, where each cell is easily identifiable.

### **Controlling the Visibility of the Gridlines**

Aspose.Cells provides a class, [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/), that represents a Microsoft Excel file. The [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) class contains a [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) collection that allows developers to access each worksheet in the Excel file. A worksheet is represented by the [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) class. The [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) class provides a wide range of properties and methods for managing a worksheet. To control the visibility of gridlines, use the [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) class [**IsGridlinesVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/isgridlinesvisible/) property. [**IsGridlinesVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/isgridlinesvisible/) is a Boolean property, which means that it can only store a **true** or **false** value.

#### **Making Gridlines Visible**

Make the gridlines visible by setting the [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) class [**IsGridlinesVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/isgridlinesvisible/) property to **true**.

#### **Hiding Gridlines**

Hide gridlines by setting the [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) class [**IsGridlinesVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/isgridlinesvisible/) property to **false**.

A complete example is given below that demonstrates the use of the [**IsGridlinesVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/isgridlinesvisible/) property by opening an excel file(book1.xls), hiding the gridlines on the first worksheet and saving the modified file as output.xls.

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
    U16String inputFilePath = srcDir + u"book1.xls";

    // Create workbook from file
    Workbook workbook(inputFilePath);

    // Access the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Hide the grid lines of the first worksheet
    worksheet.SetIsGridlinesVisible(false);

    // Save the modified Excel file
    U16String outputFilePath = srcDir + u"output.xls";
    workbook.Save(outputFilePath);

    std::cout << "Grid lines hidden successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Show and Hide Row Column Headers**

All worksheets in an Excel file are composed of cells that are arranged in rows and columns. All rows and columns have unique values that are used to identify them and to identify individual cells. For example, rows are numbered – 1, 2, 3, 4, etc. – and columns are ordered alphabetically – A, B, C, D, etc. The row and column values are displayed in the headers. Using Aspose.Cells, developers can control the visibility of these row and column headers.

### **Controlling the Visibility of the Worksheets**

Aspose.Cells provides a class, [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/), that represents a Microsoft Excel file. The [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) class contains a [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) collection that allows developers to access each worksheet in the Excel file. A worksheet is represented by the [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) class. The [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) class provides a wide range of properties and methods for managing a worksheet. To control the visibility of row and column headers, use the [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) class [**IsRowColumnHeadersVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/isrowcolumnheadersvisible/) property. [**IsRowColumnHeadersVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/isrowcolumnheadersvisible/) is a Boolean property, which means that it can only store a **true** or **false** value.

#### **Making Row/Column Headers Visible**

Make row and column headers visible by setting the [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) class [**IsRowColumnHeadersVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/isrowcolumnheadersvisible/) property to **true**.

#### **Hiding Row/Column Headers**

Hide row and column headers by setting the [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) class [**IsRowColumnHeadersVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/isrowcolumnheadersvisible/) property to **false**.

A complete example is given below that shows how to use the [**IsRowColumnHeadersVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/isrowcolumnheadersvisible/) property by opening an excel file(book1.xls), hiding the row and column headers on the first worksheet and saving the modified file as output.xls.

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
    U16String outputFilePath = outDir + u"output.xls";

    // Create workbook from the input file
    Workbook workbook(inputFilePath);

    // Access the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Hide the headers of rows and columns
    worksheet.SetIsRowColumnHeadersVisible(false);

    // Save the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "Headers hidden successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}}

It is also possible to use the [**UnhideRows**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/unhiderows/) and [**UnhideColumns**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/unhidecolumns/) methods of the [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) class to make multiple rows and columns visible.

{{% /alert %}}