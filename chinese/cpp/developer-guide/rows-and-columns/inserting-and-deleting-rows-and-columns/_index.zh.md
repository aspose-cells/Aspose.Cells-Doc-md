---
title: 用C++插入和删除Excel文件的行和列
linktitle: 插入和删除行和列
type: docs
weight: 70
url: /zh/cpp/inserting-and-deleting-rows-and-columns/
description: 本文展示了如何使用Aspose.Cells for C++ API插入和删除行列。
keywords: Aspose.Cells C++管理行列，插入行列，删除行列
---

## **介绍**

无论是从头开始创建新工作表还是在现有工作表上操作，我们可能需要添加额外的行或列来容纳更多数据。反之，我们可能还需要从工作表中的指定位置删除行或列。
为了满足这些需求，Aspose.Cells提供了一组非常简单的类和方法，详述如下。

### **管理行和列**

Aspose.Cells提供了类 [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)，代表一个微软Excel文件。[**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) 类包含一个 [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) 集合，允许访问Excel文件中的每个工作表。工作表由 [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) 类表示。[**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) 类提供了一个 [**GetCells()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getcells/) 集合，代表工作表中的所有单元格。

[**GetCells()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getcells/) 集合提供了多种管理工作表中行和列的方法，下面将介绍一些。

{{% alert color="primary" %}}

当添加行或列时，工作表中的内容会向下或向右移动；删除行或列时，内容会向上或向左移动。

{{% /alert %}}

## **插入行和列**

### **如何插入行**

通过调用 [**InsertRow**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertrow/) 方法，您可以在任何位置插入一行到工作表中。[**GetCells()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getcells/) 方法接受将插入新行的行索引。

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

    // Instantiating a Workbook object
    Workbook workbook(inputFilePath);

    // Accessing the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Inserting a row into the worksheet at 3rd position
    worksheet.GetCells().InsertRow(2);

    // Path of output excel file
    U16String outputFilePath = outDir + u"output.out.xls";

    // Saving the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "Row inserted successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **如何插入多行**

要在工作表中插入多行，请调用 [**InsertRows**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertrows/) 方法。此方法需要两个参数：

- 行索引，新行将从该行插入。
- 行数，需要插入的总行数。

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

    // Path of input excel file
    U16String inputFilePath = srcDir + u"book1.xls";

    // Create workbook from file
    Workbook workbook(inputFilePath);

    // Access the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Insert 10 rows into the worksheet starting from 3rd row
    worksheet.GetCells().InsertRows(2, 10);

    // Path of output excel file
    U16String outputFilePath = srcDir + u"output.out.xls";

    // Save the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "Rows inserted successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

### **如何插入带有格式的行**

若要插入带有格式选项的行，请使用接受 [**InsertOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/insertoptions/) 作为参数的 [**InsertRows**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertrows/) 重载。将 [**CopyFormatType**](https://reference.aspose.com/cells/cpp/aspose.cells/insertoptions/getcopyformattype/) 属性设置为 [**CopyFormatType**](https://reference.aspose.com/cells/cpp/aspose.cells/insertoptions/getcopyformattype/) 枚举。[**InsertOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/insertoptions/) 类的 [**CopyFormatType**](https://reference.aspose.com/cells/cpp/aspose.cells/insertoptions/getcopyformattype/) 属性被赋予值。枚举 [**CopyFormatType**](https://reference.aspose.com/cells/cpp/aspose.cells/insertoptions/getcopyformattype/) 中，包括以下三个成员：

开发者还可以调用 {0} 方法，插入列，参数为列索引。
要删除多行，请调用 {0} 方法，参数为起始和结束行索引。
- Clear: 清除格式。

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

    // Setting Formatting options
    InsertOptions insertOptions;
    insertOptions.SetCopyFormatType(CopyFormatType::SameAsAbove);

    // Inserting a row into the worksheet at 3rd position
    worksheet.GetCells().InsertRows(2, 1, insertOptions);

    // Save the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "Row inserted successfully with formatting!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **如何插入列**

用C++从工作表中删除列

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

    // Insert a column into the worksheet at 2nd position
    worksheet.GetCells().InsertColumn(1);

    // Save the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "Column inserted successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **删除行和列**

### **如何删除多行**

调用 [**DeleteRows**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/deleterows/) 方法，从工作表中删除列，参数为列索引。

- 行索引，要删除行的索引。
- 行数，需要删除的总行数。

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

    // Delete 10 rows from the worksheet starting from 3rd row
    worksheet.GetCells().DeleteRows(2, 10);

    // Save the modified Excel file
    U16String outputFilePath = srcDir + u"output.xlsx";
    workbook.Save(outputFilePath);

    std::cout << "Rows deleted successfully and file saved!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **如何删除列**

用C++删除工作表中的重复行

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

    // Delete a column from the worksheet at 5th position (index 4)
    worksheet.GetCells().DeleteColumn(4);

    // Save the modified Excel file
    U16String outputFilePath = srcDir + u"output.xlsx";
    workbook.Save(outputFilePath);

    std::cout << "Column deleted successfully and file saved!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
