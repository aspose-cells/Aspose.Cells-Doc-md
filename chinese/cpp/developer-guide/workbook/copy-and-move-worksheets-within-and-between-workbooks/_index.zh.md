---
title: 在Excel工作簿内复制和移动工作表
linktitle: 复制和移动工作表
type: docs
weight: 80
url: /zh/cpp/copy-and-move-worksheets-within-and-between-workbooks/
description: 学习如何使用Aspose.Cells for C++在Excel工作簿中复制和移动工作表。
---

{{% alert color="primary" %}}

有时，您需要多个具有相同格式和数据输入的工作表。例如，制作季度预算时，可能需要创建包含相同列标题、行标题和公式的工作簿。这可以通过创建一个工作表，然后多次复制实现。

Aspose.Cells支持在工作簿内或工作簿之间复制或移动工作表。包括数据、格式、表、矩阵、图表、图像和其他对象的工作表都可以以最高精度复制。

{{% /alert %}}

## **复制和移动工作表**

### **在工作簿内复制工作表**

所有示例的初始步骤相同：

1. 在Microsoft Excel中创建两个带有一些数据的工作簿。本示例中，我们创建了两个新工作簿并在工作表中输入了一些数据：
   - FirstWorkbook.xlsx（3个工作表）
   - SecondWorkbook.xlsx（1个工作表）

1. 下载并安装 Aspose.Cells：
   1. [下载Aspose.Cells for C++](https://downloads.aspose.com/cells/cpp)
   1. 在您的开发计算机上安装

1. 创建一个项目：
   1. 在你偏好的IDE中创建一个新的C++项目

1. 添加引用：
   1. 添加Aspose.Cells for C++库到你的项目

1. 在工作簿内复制工作表
   第一个示例将 FirstWorkbook.xlsx 内的第一个工作表（Copy）复制。

执行代码后，名为 Copy 的工作表将在 FirstWorkbook.xlsx 中复制并命名为 Last Sheet。

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source and output directory paths
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create workbook from input file
    Workbook excelWorkbook1(srcDir + u"FirstWorkbook.xlsx");

    // Get worksheet collection reference
    WorksheetCollection worksheets = excelWorkbook1.GetWorksheets();

    // Copy third worksheet (index 2) within the workbook
    worksheets.AddCopy(worksheets.Get(2).GetName());

    // Save modified workbook
    excelWorkbook1.Save(outDir + u"FirstWorkbookCopied_out.xlsx");

    std::cout << "Worksheet copied successfully." << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **工作簿内移动工作表**

以下代码显示了如何将工作簿内的工作表从一个位置移动到另一个位置。执行代码后，Move 工作表从 FirstWorkbook.xlsx 的索引 1 移动到索引 2。

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source and output directory paths
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create input and output file paths
    U16String inputFilePath = srcDir + u"FirstWorkbook.xlsx";
    U16String outputFilePath = outDir + u"FirstWorkbookMoved_out.xlsx";

    // Load source workbook
    Workbook excelWorkbook2(inputFilePath);

    // Access worksheet collection and move target sheet
    WorksheetCollection sheets = excelWorkbook2.GetWorksheets();
    sheets.Get(u"Move").MoveTo(2);

    // Save modified workbook
    excelWorkbook2.Save(outputFilePath);

    std::cout << "Worksheet moved successfully." << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **在工作簿之间复制工作表**

执行代码时，将名为Copy的工作表复制到SecondWorkbook.xlsx，并命名为Sheet2。

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source and output directories
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Open source workbooks
    Workbook excelWorkbook3(srcDir + u"FirstWorkbook.xlsx");
    Workbook excelWorkbook4(srcDir + u"SecondWorkbook.xlsx");

    // Access worksheets collection from second workbook
    WorksheetCollection sheets4 = excelWorkbook4.GetWorksheets();

    // Add new worksheet to destination workbook
    sheets4.Add();

    // Copy specified worksheet from source to destination
    Worksheet sourceSheet = excelWorkbook3.GetWorksheets().Get(u"Copy");
    sheets4.Get(1).Copy(sourceSheet);

    // Save modified workbook
    excelWorkbook4.Save(outDir + u"CopyWorksheetsBetweenWorkbooks_out.xlsx");

    std::cout << "Worksheets copied successfully between workbooks." << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **在工作簿之间移动工作表**

执行代码后，工作表名为 Move 从 FirstWorkbook.xlsx 移动到 SecondWorkbook.xlsx，并命名为 Sheet3。

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source and output directories
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Open first workbook
    Workbook excelWorkbook5(srcDir + u"FirstWorkbook.xlsx");

    // Open second workbook and add new worksheet
    Workbook excelWorkbook6(srcDir + u"SecondWorkbook.xlsx");
    excelWorkbook6.GetWorksheets().Add();

    // Copy third worksheet from first workbook to third position in second workbook
    WorksheetCollection sheets5 = excelWorkbook5.GetWorksheets();
    WorksheetCollection sheets6 = excelWorkbook6.GetWorksheets();
    sheets6.Get(2).Copy(sheets5.Get(2));

    // Remove copied worksheet from source workbook
    sheets5.RemoveAt(2);

    // Save modified workbooks
    excelWorkbook5.Save(outDir + u"FirstWorkbookWithMove_out.xlsx");
    excelWorkbook6.Save(outDir + u"SecondWorkbookWithMove_out.xlsx");

    std::cout << "Worksheets moved successfully between workbooks." << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
