---
title: 用C++显示和隐藏网格线及行列标题
linktitle: 显示和隐藏网格线以及行列标题
type: docs
weight: 30
url: /zh/cpp/show-and-hide-gridlines-and-row-column-headers/
description: 本文提供使用C++ API或库通过编程隐藏或显示Excel工作表的网格线、行和列标题的示例代码。
---

{{% alert color="primary" %}}

Aspose.Cells支持隐藏和显示工作表中默认情况下可见的网格线。它还提供了控制工作表的行列标题的可见性。

{{% /alert %}}

## **显示和隐藏网格线**

所有Excel工作表默认情况下都有网格线。它们有助于划分单元格，便于将数据输入特定的单元格。网格线使我们能够将工作表视为单元格的集合，其中每个单元格都易于识别。

### **控制网格线的可见性**

Aspose.Cells提供一个类[**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)，代表一个Microsoft Excel文件。[**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)类包含一个[**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/)集合，允许开发者访问Excel文件中的每个工作表。工作表由[**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)类表示。[**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)类提供了管理工作表的各种属性和方法。要控制网格线是否可见，使用[**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)类的[**IsGridlinesVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/isgridlinesvisible/)属性。[**IsGridlinesVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/isgridlinesvisible/)是一个布尔属性，意味着它只能存储**true**或**false**值。

#### **使网格线可见**

通过将[**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)类的[**IsGridlinesVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/isgridlinesvisible/)属性设置为**true**，使网格线可见。

#### **隐藏网格线**

通过将[**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)类的[**IsGridlinesVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/isgridlinesvisible/)属性设置为**false**，隐藏网格线。

下面提供一个完整示例，演示如何通过打开excel文件（book1.xls），隐藏第一个工作表的网格线，并将修改后的文件另存为output.xls。

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

## **显示和隐藏行列标题**

Excel文件中的所有工作表都由排列在行和列中的单元格组成。所有行和列都有用于标识它们和单个单元格的唯一值。例如，行编号为1、2、3、4等，列按字母顺序排列为A、B、C、D等。行和列值显示在标题中。使用Aspose.Cells，开发人员可以控制这些行和列标题的可见性。

### **控制工作表的可见性**

Aspose.Cells提供一个类[**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)，代表Microsoft Excel文件。[**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)类包含一个[**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/)集合，允许开发者访问每个工作表。工作表由[**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)类表示。[**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)类提供了管理工作表的各种属性和方法。要控制行和列标题的可见性，使用[**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)类的[**IsRowColumnHeadersVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/isrowcolumnheadersvisible/)属性。[**IsRowColumnHeadersVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/isrowcolumnheadersvisible/)是一个布尔属性，只能存储**true**或**false**值。

#### **使行/列标头可见**

通过将[**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)类的[**IsRowColumnHeadersVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/isrowcolumnheadersvisible/)属性设置为**true**，使行和列标题可见。

#### **隐藏行/列标头**

通过将[**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)类的[**IsRowColumnHeadersVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/isrowcolumnheadersvisible/)属性设置为**false**，隐藏行和列标题。

下面提供一个完整示例，演示如何通过打开excel文件（book1.xls），隐藏第一个工作表的行和列标题，并将修改后的文件另存为output.xls。

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

也可以使用[**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)类的[**UnhideRows**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/unhiderows/)和[**UnhideColumns**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/unhidecolumns/)方法，使多行或多列变得可见。

{{% /alert %}}
