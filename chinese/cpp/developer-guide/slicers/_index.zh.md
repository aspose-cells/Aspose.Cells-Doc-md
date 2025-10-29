---
title: 用C++插入切片器
linktitle: 切片器
type: docs
weight: 170
url: /zh/cpp/create-slicer/
description: 使用Aspose.Cells结合C++管理Excel文件中的切片器。
---

## **可能的使用场景**

切片器用于快速筛选数据。它可以用于筛选表格或数据透视表中的数据。Microsoft Excel允许通过选择表格或数据透视表，然后点击*插入 > 切片器*来创建切片器。Aspose.Cells也允许使用[**Worksheet.Slicers.Add()**](https://reference.aspose.com/cells/cpp/aspose.cells.slicers/slicercollection/add/)方法创建切片器。

## **为数据透视表创建切片器**

请参阅以下示例代码。它加载包含数据透视表的 [示例 Excel 文件](67338470.xlsx)。然后基于第一个基本数据透视表字段创建切片器。最后，它以 [输出 XLSX](67338471.xlsx) 和 [输出 XLSB](67338472.xlsb) 格式保存工作簿。以下屏幕截图显示了由 Aspose.Cells 在输出 Excel 文件中创建的切片器。

![todo:image_alt_text](create-slicer-to-a-pivot-table_1.png)

### **示例代码**

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
using namespace Aspose::Cells::Slicers;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"sampleCreateSlicerToPivotTable.xlsx";

    // Path of output Excel files
    U16String outputFilePathXlsx = outDir + u"outputCreateSlicerToPivotTable.xlsx";
    U16String outputFilePathXlsb = outDir + u"outputCreateSlicerToPivotTable.xlsb";

    // Load sample Excel file containing pivot table
    Workbook wb(inputFilePath);

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access first pivot table inside the worksheet
    PivotTable pt = ws.GetPivotTables().Get(0);

    // Add slicer relating to pivot table with first base field at cell B22
    int idx = ws.GetSlicers().Add(pt, u"B22", pt.GetBaseFields().Get(0));

    // Access the newly added slicer from slicer collection
    Slicer slicer = ws.GetSlicers().Get(idx);

    // Save the workbook in output XLSX format
    wb.Save(outputFilePathXlsx, SaveFormat::Xlsx);

    // Save the workbook in output XLSB format
    wb.Save(outputFilePathXlsb, SaveFormat::Xlsb);

    std::cout << "Slicer created and workbooks saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **为Excel表创建切片器**

请查看以下示例代码。它加载包含数据表的[sample Excel file](sampleCreateSlicerToExcelTable.xlsx)，然后基于第一列创建切片器。最后，将工作簿保存为[output XLSX](outputCreateSlicerToExcelTable.xlsx)格式。

### **示例代码**

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

    // Load sample Excel file containing a table
    Workbook workbook(srcDir + u"sampleCreateSlicerToExcelTable.xlsx");

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access first table inside the worksheet
    ListObject table = worksheet.GetListObjects().Get(0);

    // Add slicer
    int idx = worksheet.GetSlicers().Add(table, 0, u"H5");

    // Save the workbook in output XLSX format
    workbook.Save(outDir + u"outputCreateSlicerToExcelTable.xlsx", SaveFormat::Xlsx);

    std::cout << "Slicer added successfully to the Excel table!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **高级主题**
- [更改切片器属性](/cells/zh/cpp/change-slicer-properties/)
- [在将 Excel 渲染为 PDF 时绘制分析器](/cells/zh/cpp/draw-slicer-while-rendering-excel-to-pdf/)
- [格式化切片器](/cells/zh/cpp/formatting-slicer/)
- [移除切片器](/cells/zh/cpp/removing-slicer/)
- [呈现切片器](/cells/zh/cpp/rendering-slicer/)
- [更新分析器](/cells/zh/cpp/updating-slicer/)
{{< app/cells/assistant language="cpp" >}}
