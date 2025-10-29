---
title: 用C++显示和隐藏行、列和滚动条
linktitle: 显示和隐藏行、列及滚动条
type: docs
weight: 20
url: /zh/cpp/show-and-hide-rows-columns-and-scroll-bars/
description: 本文演示了如何使用C++语言和Aspose.Cells API以编程方式显示和隐藏Excel工作表的行和列。可以调整滚动条的可见性，并隐藏多行和多列。
---

{{% alert color="primary" %}}

Aspose.Cells 提供了控制工作表行、列和滚动条显示状态的方法。

{{% /alert %}}

## **显示和隐藏行和列**

Aspose.Cells 提供了一个类[**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)，表示一个Microsoft Excel文件。[**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)类包含一个[**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/)集合，允许开发者访问Excel文件中的每个工作表。工作表由[**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)类表示。[**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)类提供一个[**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)集合，表示工作表中的所有单元格。[**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)集合提供多种管理工作表中行或列的方法，这里简要介绍几种。

### **显示行和列**

开发者可以通过调用[**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)集合的[**UnhideRow**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/unhiderow/)和[**UnhideColumn**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/unhidecolumn/)方法，显示任何隐藏的行或列。两个方法都接受两个参数：

- 行或列索引 - 用于显示特定行或列的索引。
- 行高或列宽 - 在取消隐藏后分配给行或列的行高或列宽。

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
    U16String inputFilePath = srcDir + u"book1.xls";

    // Path of output excel file
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

在使隐藏的列显示时，如果需要恢复到之前设定的宽度或原始宽度，应使用宽度为负值的方式取消隐藏，例如：`worksheet->GetCells()->UnhideColumn(5, -1)`。

{{% /alert %}}

### **隐藏行和列**

开发者可以通过调用[**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)集合的[**HideRow**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/hiderow/)和[**HideColumn**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/hidecolumn/)方法，隐藏某一行或列。两个方法都接受行或列的索引作为参数以隐藏对应的行或列。

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

    // Path of input excel file
    U16String inputFilePath = srcDir + u"book1.xls";

    // Path of output excel file
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

还可以通过将行高或列宽设置为0来隐藏行或列。

{{% /alert %}}

### **隐藏多个行和列**

开发者还可以一次隐藏多行或多列，通过调用[**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)集合的[**HideRows**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/hiderows/)和[**HideColumns**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/hidecolumns/)方法，两个方法都接受起始行或列索引和隐藏的行或列数目作为参数。

```c++
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

    // Hide 3, 4, and 5 rows in the worksheet
    worksheet.GetCells().HideRows(2, 3);

    // Hide 2 and 3 columns in the worksheet
    worksheet.GetCells().HideColumns(1, 2);

    // Save the modified Excel file
    workbook.Save(outDir + u"outputxls");

    std::cout << "Rows and columns hidden successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **显示和隐藏滚动条**

滚动条用于浏览任何文件的内容。通常有两种类型的滚动条：

- 垂直滚动条
- 水平滚动条

Microsoft Excel还提供水平和垂直滚动条，以便用户可以滚动工作表内容。使用Aspose.Cells，开发人员可以控制Excel文件中两种类型滚动条的可见性。

### **控制滚动条的可见性**

Aspose.Cells 提供了一个表示Excel文件的类[**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)，[**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)类提供了管理Excel文件的丰富属性和方法。要控制滚动条的显示状态，可以使用[**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)类的[**WorkbookSettings.IsVScrollBarVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/isvscrollbarvisible/)和[**WorkbookSettings.IsHScrollBarVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/ishscrollbarvisible/)属性。[**WorkbookSettings.IsVScrollBarVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/isvscrollbarvisible/)和[**WorkbookSettings.IsHScrollBarVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/ishscrollbarvisible/)是布尔值属性，这意味着它们只能存储**true**或**false**。

#### **显示滚动条**

通过将[**WorkbookSettings.IsHScrollBarVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/ishscrollbarvisible/)类的[**WorkbookSettings.IsVScrollBarVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/isvscrollbarvisible/)或[**WorkbookSettings.IsHScrollBarVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/ishscrollbarvisible/)属性设置为**true**，使滚动条可见。

#### **隐藏滚动条**

通过将[**WorkbookSettings.IsHScrollBarVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/ishscrollbarvisible/)类的[**WorkbookSettings.IsVScrollBarVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/isvscrollbarvisible/)或[**WorkbookSettings.IsHScrollBarVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/ishscrollbarvisible/)属性设置为**false**，隐藏滚动条。

**示例代码**

以下是一个完整的示例代码，打开一个Excel文件`book1.xls`，隐藏两个滚动条，然后保存为`output.xls`。

```c++
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

    // Hide the vertical scroll bar of the Excel file
    workbook.GetSettings().SetIsVScrollBarVisible(false);

    // Hide the horizontal scroll bar of the Excel file
    workbook.GetSettings().SetIsHScrollBarVisible(false);

    // Save the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "Scroll bars hidden successfully and file saved!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
