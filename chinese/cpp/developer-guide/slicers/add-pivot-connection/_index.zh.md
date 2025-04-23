---
title: 添加数据透视连接用C++
linktitle: 添加数据透视连接
type: docs
weight: 30
url: /zh/cpp/add-pivot-connection/
description: 学习如何使用C++通过Aspose.Cells库添加透视连接。
keywords: 在无Office 2013、Office 2016、Office 2019和Office 365的情况下添加数据透视连接
---

## **可能的使用场景**

如果你想在Excel中关联切片器和数据透视表，你需要右键单击切片器，然后选择"报表连接..."项目。在选项列表中，你可以操作复选框。 类似地，如果你想使用Aspose.Cells API以编程方式关联切片器和数据透视表，请使用[**Slicer.AddPivotConnection(PivotTable pivot)**](https://reference.aspose.com/cells/cpp/aspose.cells.slicers/slicer/addpivotconnection/) 方法。 它将关联切片器和数据透视表。

## **关联切片器和数据透视表**

以下示例代码加载包含现有切片器的[sample Excel file](add-pivot-connection.xlsx)。它访问切片器然后将切片器与数据透视表关联。最后，将工作簿另存为[output Excel file](add-pivot-connection-out.xlsx)。 

## **示例代码**

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
    U16String inputFilePath = srcDir + u"add-pivot-connection.xlsx";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"add-pivot-connection-out.xlsx";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Access first worksheet
    WorksheetCollection worksheets = workbook.GetWorksheets();
    Worksheet worksheet = worksheets.Get(0);

    // Access the first PivotTable inside the PivotTable collection
    PivotTableCollection pivotTables = worksheet.GetPivotTables();
    PivotTable pivotTable = pivotTables.Get(0);

    // Access the first slicer inside the slicer collection
    SlicerCollection slicers = worksheet.GetSlicers();
    Slicer slicer = slicers.Get(0);

    // Add PivotTable connection
    slicer.AddPivotConnection(pivotTable);

    // Save the workbook
    workbook.Save(outputFilePath);

    std::cout << "PivotTable connection added successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
